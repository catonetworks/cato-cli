# eventsFeedEnhanced.py - Enhanced eventsFeed for catocli with advanced features
#
# This module provides an enhanced eventsFeed implementation that integrates with catocli
# while providing the advanced features from the original cato-toolbox eventsFeed.py.
# It leverages catocli's native authentication, API client, and compression features.
#

import datetime
import json
import os
import signal
import socket
import ssl
import sys
import time
import urllib.request
import base64
import hmac
import hashlib
from ..customParserApiClient import createRequest


def enhanced_events_feed_handler(args, configuration):
    """Enhanced eventsFeed handler with advanced features like marker persistence, 
    continuous polling, and filtering."""
    
    # Store original function to restore later
    original_args = vars(args).copy()
    
    # Setup marker and config file handling
    marker, marker_file = setup_marker_and_config(args)
    
    # Setup filters
    filter_obj = setup_filters(args)
    
    # Setup network streaming and Sentinel options
    network_config, sentinel_config = setup_output_options(args)
    
    # Setup thresholds
    fetch_threshold = getattr(args, 'fetch_limit', 1)
    runtime_limit = getattr(args, 'runtime_limit', None)
    if runtime_limit is None:
        runtime_limit = sys.maxsize
    
    # Statistics tracking
    iteration = 1
    total_count = 0
    all_events = []
    start = datetime.datetime.now()
    
    log(f"Starting enhanced eventsFeed with marker: {marker}", args)
    log(f"Marker file: {marker_file}, fetch_limit: {fetch_threshold}, runtime_limit: {runtime_limit}", args)
    
    # Setup signal handling for graceful shutdown in enhanced mode
    interrupted = False
    def signal_handler(signum, frame):
        nonlocal interrupted
        interrupted = True
        log("Received interrupt signal, finishing current iteration...", args)
    
    if getattr(args, 'run', False):
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        log("Run continuous mode enabled. Press Ctrl+C to stop gracefully.", args)
    
    while True:
        # Build the JSON request for this iteration
        request_json = {
            "marker": marker
        }
        
        # Add account ID handling (catocli will handle this automatically)
        # Add filters if specified
        if filter_obj:
            request_json["filters"] = [filter_obj]
        
        # Set the JSON argument for the native catocli handler
        args.json = json.dumps(request_json)
        
        log(f"Iteration {iteration}: Requesting events with marker: {marker}", args)
        logd(f"Request JSON: {args.json}", args)
        
        # Use native catocli createRequest function 
        response = createRequest(args, configuration)
        
        if not response:
            log("No response received from API", args)
            break
        
        # Handle response format - catocli createRequest can return different formats
        response_data = None
        if isinstance(response, tuple):
            # If it's a tuple, the actual data is usually in the first element
            response_data = response[0] if len(response) > 0 else None
        elif isinstance(response, list):
            response_data = response[0] if len(response) > 0 else None
        else:
            response_data = response
        
        if not response_data or not isinstance(response_data, dict) or "data" not in response_data:
            log(f"Invalid response format: {type(response_data)} - {response_data}", args)
            break
            
        # Extract eventsFeed data
        try:
            events_feed_data = response_data["data"]["eventsFeed"]
            marker = events_feed_data.get("marker", "")
            fetched_count = int(events_feed_data.get("fetchedCount", 0))
            total_count += fetched_count
            
            # Process accounts and records
            events_list = []
            accounts = events_feed_data.get("accounts", [])
            if accounts and len(accounts) > 0:
                # Try different possible field names for records
                records = accounts[0].get("records", accounts[0].get("recordsEventsFeedAccountRecords", []))
                for record in records:
                    # Process fieldsMap format like original script
                    if "fieldsMap" in record:
                        event_data = record["fieldsMap"].copy()
                        event_data["event_timestamp"] = record.get("time", "")
                        # Reorder with timestamp first (for Splunk compatibility)
                        event_reorder = dict(sorted(event_data.items(), 
                                                   key=lambda i: i[0] == 'event_timestamp', reverse=True))
                        events_list.append(event_reorder)
                        all_events.append(event_reorder)
            
            # Build log line
            line = f"iteration:{iteration} fetched:{fetched_count} total_count:{total_count} marker:{marker}"
            if events_list:
                line += f" first_event:{events_list[0].get('event_timestamp', 'N/A')}"
                line += f" last_event:{events_list[-1].get('event_timestamp', 'N/A')}"
            log(line, args)
            
            # Print events if requested (use native catocli format)
            if getattr(args, 'print_events', False):
                for event in events_list:
                    if getattr(args, 'prettify', False):
                        print(json.dumps(event, indent=2, ensure_ascii=False))
                    else:
                        try:
                            print(json.dumps(event, ensure_ascii=False))
                        except Exception:
                            print(json.dumps(event))
            
            # Send events to network or Sentinel if configured
            if (network_config or sentinel_config) and events_list:
                send_events_to_outputs(events_list, network_config, sentinel_config, args)
            
            # Write marker back to marker file
            if marker:
                try:
                    with open(marker_file, "w") as f:
                        f.write(marker)
                    logd(f"Written marker to {marker_file}: {marker}", args)
                except IOError as e:
                    log(f"Warning: Could not write marker to marker file: {e}", args)
            
        except (KeyError, TypeError, ValueError) as e:
            log(f"Error processing response: {e}", args)
            break
        
        # Check stopping conditions
        iteration += 1
        
        # Check for interrupt signal
        if interrupted:
            log("Gracefully stopping due to interrupt signal", args)
            break
        
        # Only stop on fetch_limit if NOT in run continuous mode
        if not getattr(args, 'run', False) and fetched_count < fetch_threshold:
            log(f"Fetched count {fetched_count} less than threshold {fetch_threshold}, stopping", args)
            break
        
        # In run mode, continue polling even if no events, but respect runtime limit
        elapsed = datetime.datetime.now() - start
        if elapsed.total_seconds() > runtime_limit:
            log(f"Elapsed time {elapsed.total_seconds()} exceeds runtime limit {runtime_limit}, stopping", args)
            break
        
        # In run mode, add a small delay between iterations to avoid hammering the API
        if getattr(args, 'run', False):
            if fetched_count == 0:
                log("No events in this iteration, waiting 2 seconds before next poll...", args)
                time.sleep(2)  # Wait 2 seconds when no events
            else:
                time.sleep(0.1)  # Small delay when events are flowing
    
    # Final statistics
    end = datetime.datetime.now()
    log(f"Enhanced eventsFeed completed: {total_count} events in {end-start}", args)
    
    # Return in standard catocli format (the network streaming and sentinel 
    # integration are handled automatically by the native createRequest function)
    return [{
        "success": True,
        "total_events": total_count,
        "duration": str(end - start),
        "final_marker": marker,
        "iterations": iteration - 1
    }]


def setup_marker_and_config(args):
    """Setup marker and marker file handling (similar to original eventsFeed.py)"""
    marker_file = "./events-marker.txt"  # Default from argument parser help text
    
    if getattr(args, 'marker_file', None):
        marker_file = args.marker_file
        log(f"Using marker file from argument: {marker_file}", args)
    else:
        log(f"Using default marker file: {marker_file}", args)
    
    marker = ""
    if getattr(args, 'marker', None):
        marker = args.marker
        log(f"Using marker from argument: {marker}", args)
    else:
        # Try to load marker from marker file
        if os.path.isfile(marker_file):
            try:
                with open(marker_file, "r") as f:
                    marker = f.readlines()[0].strip()
                log(f"Read marker from marker file: {marker}", args)
            except (IndexError, IOError) as e:
                log(f"Could not read marker from marker file: {e}", args)
        else:
            log("Marker file does not exist, starting with empty marker", args)
    
    return marker, marker_file


def setup_filters(args):
    """Setup event filtering based on type and subtype"""
    filters = []
    
    # Process event_types filter
    if getattr(args, 'event_types', None):
        event_types = [t.strip() for t in args.event_types.split(',')]
        filters.append({
            "fieldName": "event_type",
            "operator": "in",
            "values": event_types
        })
        log(f"Added event_type filter: {event_types}", args)
    
    # Process event_sub_types filter
    if getattr(args, 'event_sub_types', None):
        event_sub_types = [t.strip() for t in args.event_sub_types.split(',')]
        filters.append({
            "fieldName": "event_sub_type", 
            "operator": "in",
            "values": event_sub_types
        })
        log(f"Added event_sub_type filter: {event_sub_types}", args)
    
    # Return single filter object if only one, None if none
    if len(filters) == 1:
        return filters[0]
    elif len(filters) > 1:
        # For multiple filters, we'd need to handle this differently
        # For now, just return the first one and warn
        log(f"Warning: Multiple filters specified, using first one only: {filters[0]}", args)
        return filters[0]
    
    return None


def log(text, args):
    """Log debug output"""
    # Handle catocli's -v argument which can be True or a string
    verbose = getattr(args, 'v', False)
    if verbose is True or (isinstance(verbose, str) and verbose.lower() in ['true', '1', 'yes']):
        print(f"LOG {datetime.datetime.now(datetime.UTC)}> {text}")


def logd(text, args):
    """Log detailed debug output"""
    if getattr(args, 'very_verbose', False):
        log(text, args)


def setup_output_options(args):
    """Setup network streaming and Sentinel output options"""
    network_config = None
    sentinel_config = None
    
    # Process network options (-n)
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
    
    # Process Sentinel options (-z)
    if getattr(args, 'sentinel', None):
        sentinel_elements = args.sentinel.split(":")
        if len(sentinel_elements) != 2:
            log("Error: -z value must be in the form of customerid:sharedkey", args)
            sys.exit(1)
        
        customer_id = sentinel_elements[0]
        shared_key = sentinel_elements[1]
        sentinel_config = {'customer_id': customer_id, 'shared_key': shared_key}
        log(f"Sentinel streaming enabled to workspace {customer_id}", args)
    
    return network_config, sentinel_config


def send_events_to_outputs(events_list, network_config, sentinel_config, args):
    """Send events to network and/or Sentinel outputs with optional newline appending"""
    append_newline = getattr(args, 'append_new_line', False)
    
    for event in events_list:
        try:
            # Convert event to JSON string
            event_json = json.dumps(event, ensure_ascii=False)
            
            # Add newline if requested
            if append_newline:
                event_json += "\n"
            
            # Send to network if configured
            if network_config:
                send_event_to_network(event_json, network_config['host'], network_config['port'], args)
            
            # Send to Sentinel if configured
            if sentinel_config:
                send_event_to_sentinel(event, sentinel_config['customer_id'], sentinel_config['shared_key'], args)
            
        except Exception as e:
            log(f"Error processing event for output: {e}", args)


def send_event_to_network(event_json, host, port, args):
    """Send a single event over network to host:port TCP"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)  # 10 second timeout
            sock.connect((host, port))
            sock.sendall(event_json.encode('utf-8'))
        logd(f"Sent event to {host}:{port}", args)
    except socket.error as e:
        log(f"Network error sending to {host}:{port}: {e}", args)
    except Exception as e:
        log(f"Error sending event to network: {e}", args)


def build_sentinel_signature(customer_id, shared_key, date, content_length):
    """Build the API signature for Sentinel"""
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"POST\n{content_length}\napplication/json\n{x_headers}\n/api/logs"
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    authorization = "SharedKey {}:{}".format(customer_id, encoded_hash)
    return authorization


def send_event_to_sentinel(event, customer_id, shared_key, args):
    """Send a single event to Microsoft Sentinel"""
    try:
        # Convert event to JSON bytes
        event_data = [event]  # Sentinel expects an array
        json_data = json.dumps(event_data).encode('utf-8')
        
        # Build request
        rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        content_length = len(json_data)
        signature = build_sentinel_signature(customer_id, shared_key, rfc1123date, content_length)
        
        headers = {
            'content-type': 'application/json',
            'Authorization': signature,
            'Log-Type': 'CatoEvents',
            'Time-generated-field': 'event_timestamp',
            'x-ms-date': rfc1123date
        }
        
        # Send request
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
            logd(f"Sent event to Sentinel workspace {customer_id}", args)
            
    except urllib.error.URLError as e:
        log(f"Sentinel API error: {e}", args)
    except Exception as e:
        log(f"Error sending event to Sentinel: {e}", args)
