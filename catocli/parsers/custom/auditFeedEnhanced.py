# auditFeedEnhanced.py - Enhanced auditFeed for catocli with SIEM-friendly run mode

import base64
import copy
import datetime
import hashlib
import hmac
import json
import os
import signal
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request

from ..customParserApiClient import createRequest, preprocess_json_input


DEFAULT_AUDIT_TIME_FRAME = "last.P1D"


def enhanced_audit_feed_handler(args, configuration):
    """Enhanced auditFeed handler with marker persistence and continuous polling."""
    original_args = vars(args).copy()
    marker, marker_file = setup_marker_and_config(args)
    initial_variables = load_initial_variables(args)
    field_names = setup_field_names(args)
    filter_obj = setup_filter(args)
    network_config, sentinel_config = setup_output_options(args)

    fetch_threshold = getattr(args, 'fetch_limit', 1)
    runtime_limit = getattr(args, 'runtime_limit', None)
    if runtime_limit is None:
        runtime_limit = sys.maxsize

    iteration = 1
    total_count = 0
    start = datetime.datetime.now()
    interrupted = False

    log(f"Starting enhanced auditFeed with marker: {marker}", args)
    log(f"Marker file: {marker_file}, fetch_limit: {fetch_threshold}, runtime_limit: {runtime_limit}", args)

    def signal_handler(signum, frame):
        nonlocal interrupted
        interrupted = True
        log("Received interrupt signal, finishing current iteration...", args)

    if getattr(args, 'run', False):
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        log("Run continuous mode enabled. Press Ctrl+C to stop gracefully.", args)

    try:
        while True:
            request_json = build_request_json(initial_variables, marker, field_names, filter_obj)
            args.json = json.dumps(request_json)

            log(f"Iteration {iteration}: Requesting audit records with marker: {marker}", args)
            logd(f"Request JSON: {args.json}", args)

            response = call_create_request_without_output_routing(args, configuration)
            if not response:
                log("No response received from API", args)
                break

            response_data = normalize_response(response)
            if not response_data or not isinstance(response_data, dict) or "data" not in response_data:
                log(f"Invalid response format: {type(response_data)} - {response_data}", args)
                break

            try:
                audit_feed_data = response_data["data"]["auditFeed"]
                marker = audit_feed_data.get("marker", "")
                fetched_count = int(audit_feed_data.get("fetchedCount", 0))
                total_count += fetched_count

                audit_records = extract_audit_records(audit_feed_data)
                line = f"iteration:{iteration} fetched:{fetched_count} total_count:{total_count} marker:{marker}"
                if audit_records:
                    line += f" first_audit:{audit_records[0].get('audit_timestamp', 'N/A')}"
                    line += f" last_audit:{audit_records[-1].get('audit_timestamp', 'N/A')}"
                log(line, args)

                if getattr(args, 'print_events', False):
                    print_audit_records(audit_records, args)

                if (network_config or sentinel_config) and audit_records:
                    send_audit_records_to_outputs(audit_records, network_config, sentinel_config, args)

                if marker:
                    write_marker(marker_file, marker, args)

            except (KeyError, TypeError, ValueError) as e:
                log(f"Error processing response: {e}", args)
                break

            iteration += 1

            if interrupted:
                log("Gracefully stopping due to interrupt signal", args)
                break

            if not getattr(args, 'run', False) and fetched_count < fetch_threshold:
                log(f"Fetched count {fetched_count} less than threshold {fetch_threshold}, stopping", args)
                break

            elapsed = datetime.datetime.now() - start
            if elapsed.total_seconds() > runtime_limit:
                log(f"Elapsed time {elapsed.total_seconds()} exceeds runtime limit {runtime_limit}, stopping", args)
                break

            if getattr(args, 'run', False):
                if fetched_count == 0:
                    log("No audit records in this iteration, waiting 2 seconds before next poll...", args)
                    time.sleep(2)
                else:
                    time.sleep(0.1)
    finally:
        for key, value in original_args.items():
            setattr(args, key, value)

    end = datetime.datetime.now()
    log(f"Enhanced auditFeed completed: {total_count} audit records in {end-start}", args)

    return [{
        "success": True,
        "total_events": total_count,
        "total_audit_records": total_count,
        "duration": str(end - start),
        "final_marker": marker,
        "iterations": iteration - 1
    }]


def load_initial_variables(args):
    """Load the initial JSON variables from command line or --json-file."""
    json_input = getattr(args, 'json', '{}') or '{}'
    json_file = getattr(args, 'json_file', None)

    if json_file:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_input = f.read()
        except Exception as e:
            print(f"ERROR: Failed to read JSON file '{json_file}': {e}")
            return {}

    try:
        variables = json.loads(preprocess_json_input(json_input))
        if not isinstance(variables, dict):
            print("ERROR: JSON input must be an object/dictionary")
            return {}
    except ValueError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        return {}

    if "timeFrame" not in variables:
        variables["timeFrame"] = DEFAULT_AUDIT_TIME_FRAME

    return variables


def build_request_json(initial_variables, marker, field_names, filter_obj):
    request_json = copy.deepcopy(initial_variables)
    request_json["marker"] = marker

    if field_names:
        request_json["fieldNames"] = field_names

    if filter_obj:
        existing_filters = (
            request_json.get("auditFieldFilterInput")
            or request_json.get("filters")
            or []
        )
        if isinstance(existing_filters, dict):
            existing_filters = [existing_filters]
        request_json["auditFieldFilterInput"] = existing_filters + [filter_obj]
        request_json.pop("filters", None)

    return request_json


def call_create_request_without_output_routing(args, configuration):
    """Let enhanced mode stream individual records instead of whole API responses."""
    original_stream_events = getattr(args, 'stream_events', None)
    original_sentinel = getattr(args, 'sentinel', None)
    args.stream_events = None
    args.sentinel = None
    try:
        return createRequest(args, configuration)
    finally:
        args.stream_events = original_stream_events
        args.sentinel = original_sentinel


def normalize_response(response):
    if isinstance(response, tuple):
        return response[0] if len(response) > 0 else None
    if isinstance(response, list):
        return response[0] if len(response) > 0 else None
    return response


def extract_audit_records(audit_feed_data):
    audit_records = []

    for account in audit_feed_data.get("accounts", []) or []:
        account_id = account.get("id")
        records = (
            account.get("records")
            or account.get("recordsAuditFeedAccountRecords")
            or account.get("auditFeedAccountRecords")
            or []
        )

        for record in records:
            audit_record = normalize_audit_record(record, account_id)
            audit_records.append(audit_record)

    return audit_records


def normalize_audit_record(record, account_id=None):
    if not isinstance(record, dict):
        return {"raw_record": record}

    audit_data = {}
    fields_map = record.get("fieldsMap")
    flat_fields = record.get("flatFields")

    if isinstance(fields_map, dict):
        audit_data.update(fields_map)
    elif isinstance(flat_fields, dict):
        audit_data.update(flat_fields)
    elif isinstance(flat_fields, str):
        audit_data["flatFields"] = flat_fields

    for field in record.get("fields", []) or []:
        if not isinstance(field, dict):
            continue
        name = field.get("name")
        if name and name not in audit_data:
            audit_data[name] = extract_field_value(field.get("value"))

    audit_time = record.get("time")
    if audit_time:
        audit_data["audit_timestamp"] = audit_time
        audit_data["event_timestamp"] = audit_time

    if account_id and "account_id" not in audit_data:
        audit_data["account_id"] = account_id

    for key in ("admin", "apiKey", "object", "account"):
        if key in record and key not in audit_data:
            audit_data[key] = record[key]

    return reorder_timestamp_first(audit_data)


def extract_field_value(value):
    if isinstance(value, dict):
        if "string" in value:
            return value["string"]
        if "date" in value:
            return value["date"]
        entity_keys = {"id", "name", "type"}
        if entity_keys.intersection(value.keys()):
            return {key: value.get(key) for key in ("id", "name", "type") if key in value}
    return value


def reorder_timestamp_first(audit_data):
    timestamp_keys = {"audit_timestamp", "event_timestamp"}
    return dict(sorted(audit_data.items(), key=lambda item: item[0] in timestamp_keys, reverse=True))


def print_audit_records(audit_records, args):
    for audit_record in audit_records:
        if getattr(args, 'prettify', False):
            print(json.dumps(audit_record, indent=2, ensure_ascii=False))
        else:
            try:
                print(json.dumps(audit_record, ensure_ascii=False))
            except Exception:
                print(json.dumps(audit_record))


def setup_marker_and_config(args):
    marker_file = "./audit-marker.txt"

    if getattr(args, 'marker_file', None):
        marker_file = args.marker_file
        log(f"Using marker file from argument: {marker_file}", args)
    else:
        log(f"Using default marker file: {marker_file}", args)

    marker = ""
    if getattr(args, 'marker', None):
        marker = args.marker
        log(f"Using marker from argument: {marker}", args)
    elif os.path.isfile(marker_file):
        try:
            with open(marker_file, "r") as f:
                marker = f.readlines()[0].strip()
            log(f"Read marker from marker file: {marker}", args)
        except (IndexError, IOError) as e:
            log(f"Could not read marker from marker file: {e}", args)
    else:
        log("Marker file does not exist, starting with empty marker", args)

    return marker, marker_file


def setup_field_names(args):
    if not getattr(args, 'field_names', None):
        return None

    field_names = [field.strip() for field in args.field_names.split(',') if field.strip()]
    log(f"Using audit field names: {field_names}", args)
    return field_names or None


def setup_filter(args):
    filter_field = getattr(args, 'filter_field', None)
    filter_values = getattr(args, 'filter_values', None)

    if not filter_field and not filter_values:
        return None
    if not filter_field or not filter_values:
        print("ERROR: --filter-field and --filter-values must be used together")
        sys.exit(1)

    values = [value.strip() for value in filter_values.split(',') if value.strip()]
    filter_obj = {
        "fieldNameInput": {"AuditFieldName": filter_field},
        "operator": getattr(args, 'filter_operator', 'is'),
        "values": values
    }
    log(f"Added audit filter: {filter_obj}", args)
    return filter_obj


def setup_output_options(args):
    network_config = None
    sentinel_config = None

    if getattr(args, 'stream_events', None):
        network_elements = args.stream_events.split(":")
        if len(network_elements) != 2:
            log("Error: -n value must be in the form of host:port", args)
            sys.exit(1)

        try:
            host = network_elements[0]
            port = int(network_elements[1])
            network_config = {'host': host, 'port': port}
            log(f"Network streaming enabled to {host}:{port}", args)
        except ValueError:
            log("Error: -n port must be a valid integer", args)
            sys.exit(1)

    if getattr(args, 'sentinel', None):
        sentinel_elements = args.sentinel.split(":")
        if len(sentinel_elements) != 2:
            log("Error: -z value must be in the form of customerid:sharedkey", args)
            sys.exit(1)

        sentinel_config = {
            'customer_id': sentinel_elements[0],
            'shared_key': sentinel_elements[1]
        }
        log(f"Sentinel streaming enabled to workspace {sentinel_config['customer_id']}", args)

    return network_config, sentinel_config


def send_audit_records_to_outputs(audit_records, network_config, sentinel_config, args):
    append_newline = getattr(args, 'append_new_line', False)

    for audit_record in audit_records:
        try:
            audit_json = json.dumps(audit_record, ensure_ascii=False)
            if append_newline:
                audit_json += "\n"

            if network_config:
                send_record_to_network(audit_json, network_config['host'], network_config['port'], args)

            if sentinel_config:
                send_record_to_sentinel(audit_record, sentinel_config['customer_id'], sentinel_config['shared_key'], args)
        except Exception as e:
            log(f"Error processing audit record for output: {e}", args)


def send_record_to_network(record_json, host, port, args):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            sock.connect((host, port))
            sock.sendall(record_json.encode('utf-8'))
        logd(f"Sent audit record to {host}:{port}", args)
    except socket.error as e:
        log(f"Network error sending to {host}:{port}: {e}", args)
    except Exception as e:
        log(f"Error sending audit record to network: {e}", args)


def build_sentinel_signature(customer_id, shared_key, date, content_length):
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"POST\n{content_length}\napplication/json\n{x_headers}\n/api/logs"
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    return "SharedKey {}:{}".format(customer_id, encoded_hash)


def send_record_to_sentinel(audit_record, customer_id, shared_key, args):
    try:
        json_data = json.dumps([audit_record]).encode('utf-8')
        rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        content_length = len(json_data)
        signature = build_sentinel_signature(customer_id, shared_key, rfc1123date, content_length)

        headers = {
            'content-type': 'application/json',
            'Authorization': signature,
            'Log-Type': 'CatoAudit',
            'Time-generated-field': 'audit_timestamp',
            'x-ms-date': rfc1123date
        }

        no_verify = ssl._create_unverified_context()
        request = urllib.request.Request(
            url='https://' + customer_id + '.ods.opinsights.azure.com/api/logs?api-version=2016-04-01',
            data=json_data,
            headers=headers
        )
        response = urllib.request.urlopen(request, context=no_verify, timeout=30)

        if response.code < 200 or response.code >= 300:
            log(f"Sentinel API returned {response.code}", args)
        else:
            logd(f"Sent audit record to Sentinel workspace {customer_id}", args)
    except urllib.error.URLError as e:
        log(f"Sentinel API error: {e}", args)
    except Exception as e:
        log(f"Error sending audit record to Sentinel: {e}", args)


def write_marker(marker_file, marker, args):
    try:
        with open(marker_file, "w") as f:
            f.write(marker)
        logd(f"Written marker to {marker_file}: {marker}", args)
    except IOError as e:
        log(f"Warning: Could not write marker to marker file: {e}", args)


def log(text, args):
    verbose = getattr(args, 'v', False)
    if verbose is True or (isinstance(verbose, str) and verbose.lower() in ['true', '1', 'yes']):
        print(f"LOG {datetime.datetime.now(datetime.UTC)}> {text}")


def logd(text, args):
    if getattr(args, 'very_verbose', False):
        log(text, args)
