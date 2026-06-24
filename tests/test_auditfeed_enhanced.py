import argparse
import json
from types import SimpleNamespace

from catocli.parsers.query_auditFeed import auditFeed_dispatcher, query_auditFeed_parse
from catocli.parsers.custom import auditFeedEnhanced


def make_args(**overrides):
    args = {
        "json": "{}",
        "json_file": None,
        "marker": None,
        "marker_file": None,
        "field_names": None,
        "filter_field": None,
        "filter_operator": "is",
        "filter_values": None,
        "fetch_limit": 1,
        "runtime_limit": None,
        "run": False,
        "print_events": False,
        "prettify": False,
        "stream_events": None,
        "sentinel": None,
        "append_new_line": False,
        "v": False,
        "very_verbose": False,
    }
    args.update(overrides)
    return SimpleNamespace(**args)


def test_auditfeed_parser_uses_standard_dispatcher_without_enhanced_flags(monkeypatch):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    query_auditFeed_parse(subparsers)
    args = parser.parse_args(["auditFeed"])

    def fake_create_request(received_args, configuration):
        assert received_args is args
        assert configuration.accountID == "12345"
        return [{"standard": True}]

    def fail_enhanced_handler(received_args, configuration):
        raise AssertionError("enhanced handler should not be used by default")

    monkeypatch.setattr("catocli.parsers.query_auditFeed.createRequest", fake_create_request)
    monkeypatch.setattr("catocli.parsers.query_auditFeed.enhanced_audit_feed_handler", fail_enhanced_handler)

    assert args.func == auditFeed_dispatcher
    assert args.json == "{}"
    assert args.run is False
    assert args.fetch_limit == 1
    assert auditFeed_dispatcher(args, SimpleNamespace(accountID="12345")) == [{"standard": True}]


def test_auditfeed_parser_routes_enhanced_flags_to_dispatcher():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    query_auditFeed_parse(subparsers)

    args = parser.parse_args([
        "auditFeed",
        "--run",
        "--marker-file",
        "audit-marker.txt",
        "--field-names",
        "admin,change_type",
        "--filter-field",
        "change_type",
        "--filter-values",
        "MODIFIED",
        "--append-new-line",
    ])

    assert args.func == auditFeed_dispatcher
    assert args.operation_name == "query.auditFeed"
    assert args.run is True
    assert args.field_names == "admin,change_type"
    assert args.filter_field == "change_type"
    assert args.filter_values == "MODIFIED"
    assert args.append_new_line is True


def test_enhanced_auditfeed_persists_marker_and_builds_request(monkeypatch, tmp_path):
    captured_requests = []
    streamed_records = []
    marker_file = tmp_path / "audit-marker.txt"

    def fake_create_request(args, configuration):
        assert args.stream_events is None
        assert args.sentinel is None
        captured_requests.append(json.loads(args.json))
        return {
            "data": {
                "auditFeed": {
                    "marker": "next-marker",
                    "fetchedCount": 1,
                    "accounts": [
                        {
                            "id": "12345",
                            "records": [
                                {
                                    "time": "2026-05-22T10:00:00Z",
                                    "fieldsMap": {
                                        "admin": "admin@example.com",
                                        "change_type": "MODIFIED",
                                    },
                                }
                            ],
                        }
                    ],
                }
            }
        }

    monkeypatch.setattr(auditFeedEnhanced, "createRequest", fake_create_request)
    monkeypatch.setattr(
        auditFeedEnhanced,
        "send_audit_records_to_outputs",
        lambda records, network, sentinel, args: streamed_records.extend(records),
    )

    args = make_args(
        marker_file=str(marker_file),
        field_names="admin,change_type",
        filter_field="change_type",
        filter_values="MODIFIED",
        fetch_limit=2,
        stream_events="127.0.0.1:9999",
        append_new_line=True,
    )

    result = auditFeedEnhanced.enhanced_audit_feed_handler(args, SimpleNamespace(accountID="12345"))

    assert result[0]["success"] is True
    assert result[0]["total_audit_records"] == 1
    assert marker_file.read_text() == "next-marker"
    assert args.stream_events == "127.0.0.1:9999"

    request = captured_requests[0]
    assert request["timeFrame"] == auditFeedEnhanced.DEFAULT_AUDIT_TIME_FRAME
    assert request["marker"] == ""
    assert request["fieldNames"] == ["admin", "change_type"]
    assert request["auditFieldFilterInput"] == [
        {
            "fieldNameInput": {"AuditFieldName": "change_type"},
            "operator": "is",
            "values": ["MODIFIED"],
        }
    ]

    assert streamed_records[0]["audit_timestamp"] == "2026-05-22T10:00:00Z"
    assert streamed_records[0]["event_timestamp"] == "2026-05-22T10:00:00Z"
    assert streamed_records[0]["account_id"] == "12345"


def test_enhanced_auditfeed_advances_marker_until_fetch_threshold(monkeypatch, tmp_path):
    captured_requests = []
    marker_file = tmp_path / "audit-marker.txt"
    responses = [
        {
            "data": {
                "auditFeed": {
                    "marker": "marker-1",
                    "fetchedCount": 1,
                    "accounts": [
                        {
                            "id": "12345",
                            "records": [
                                {
                                    "time": "2026-05-22T10:00:00Z",
                                    "fieldsMap": {"admin": "first@example.com"},
                                }
                            ],
                        }
                    ],
                }
            }
        },
        {
            "data": {
                "auditFeed": {
                    "marker": "marker-2",
                    "fetchedCount": 0,
                    "accounts": [],
                }
            }
        },
    ]

    def fake_create_request(args, configuration):
        captured_requests.append(json.loads(args.json))
        return responses.pop(0)

    monkeypatch.setattr(auditFeedEnhanced, "createRequest", fake_create_request)

    args = make_args(marker="initial-marker", marker_file=str(marker_file), fetch_limit=1)

    result = auditFeedEnhanced.enhanced_audit_feed_handler(args, SimpleNamespace(accountID="12345"))

    assert result[0]["total_audit_records"] == 1
    assert result[0]["final_marker"] == "marker-2"
    assert result[0]["iterations"] == 2
    assert marker_file.read_text() == "marker-2"
    assert [request["marker"] for request in captured_requests] == ["initial-marker", "marker-1"]


def test_print_events_prettifies_audit_records(monkeypatch, capsys, tmp_path):
    def fake_create_request(args, configuration):
        return {
            "data": {
                "auditFeed": {
                    "marker": "next-marker",
                    "fetchedCount": 1,
                    "accounts": [
                        {
                            "id": "12345",
                            "records": [
                                {
                                    "time": "2026-05-22T10:00:00Z",
                                    "fields": [
                                        {"name": "admin", "value": {"string": "admin@example.com"}},
                                        {"name": "change_type", "value": {"string": "CREATED"}},
                                    ],
                                }
                            ],
                        }
                    ],
                }
            }
        }

    monkeypatch.setattr(auditFeedEnhanced, "createRequest", fake_create_request)

    args = make_args(
        fetch_limit=2,
        marker_file=str(tmp_path / "audit-marker.txt"),
        print_events=True,
        prettify=True,
    )

    auditFeedEnhanced.enhanced_audit_feed_handler(args, SimpleNamespace(accountID="12345"))

    stdout = capsys.readouterr().out
    assert '"audit_timestamp": "2026-05-22T10:00:00Z"' in stdout
    assert '  "admin": "admin@example.com"' in stdout
    assert '  "change_type": "CREATED"' in stdout


class FakeSocket:
    """Minimal socket stub that records connect/sendall calls.

    Shared across tests to assert one connection is opened per batch."""

    instances = []

    def __init__(self, *args, **kwargs):
        self.connected_to = None
        self.sent = []
        self.timeout = None
        FakeSocket.instances.append(self)

    def settimeout(self, timeout):
        self.timeout = timeout

    def connect(self, address):
        self.connected_to = address

    def sendall(self, data):
        self.sent.append(data)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_network_output_appends_newline(monkeypatch):
    FakeSocket.instances = []
    monkeypatch.setattr(auditFeedEnhanced.socket, "socket", FakeSocket)

    args = SimpleNamespace(append_new_line=True, v=False, very_verbose=False)
    auditFeedEnhanced.send_audit_records_to_outputs(
        [{"audit_timestamp": "2026-05-22T10:00:00Z", "admin": "admin@example.com"}],
        {"host": "rapid7-collector.local", "port": 10000},
        None,
        args,
    )

    assert len(FakeSocket.instances) == 1
    sock = FakeSocket.instances[0]
    assert sock.connected_to == ("rapid7-collector.local", 10000)
    assert len(sock.sent) == 1
    payload = sock.sent[0].decode("utf-8")
    assert payload.endswith("\n")
    assert json.loads(payload)["admin"] == "admin@example.com"


def test_network_output_uses_single_connection_per_batch(monkeypatch):
    FakeSocket.instances = []
    monkeypatch.setattr(auditFeedEnhanced.socket, "socket", FakeSocket)

    records = [
        {"audit_timestamp": "2026-05-22T10:00:00Z", "admin": "a@example.com"},
        {"audit_timestamp": "2026-05-22T10:00:01Z", "admin": "b@example.com"},
        {"audit_timestamp": "2026-05-22T10:00:02Z", "admin": "c@example.com"},
    ]
    args = SimpleNamespace(append_new_line=True, v=False, very_verbose=False)
    auditFeedEnhanced.send_audit_records_to_outputs(
        records,
        {"host": "collector.local", "port": 514},
        None,
        args,
    )

    # One connection opened for the whole batch, not one per record
    assert len(FakeSocket.instances) == 1
    sock = FakeSocket.instances[0]
    assert sock.connected_to == ("collector.local", 514)
    # Each record was sent over that single connection
    assert len(sock.sent) == 3
    admins = [json.loads(p.decode("utf-8"))["admin"] for p in sock.sent]
    assert admins == ["a@example.com", "b@example.com", "c@example.com"]


def test_network_output_no_connection_when_batch_empty(monkeypatch):
    FakeSocket.instances = []
    monkeypatch.setattr(auditFeedEnhanced.socket, "socket", FakeSocket)

    args = SimpleNamespace(append_new_line=False, v=False, very_verbose=False)
    auditFeedEnhanced.send_audit_records_to_outputs(
        [],
        {"host": "collector.local", "port": 514},
        None,
        args,
    )

    assert FakeSocket.instances == []


def test_streaming_handler_does_not_print_records_to_stdout(monkeypatch, capsys, tmp_path):
    streamed_records = []

    def fake_create_request(args, configuration):
        return {
            "data": {
                "auditFeed": {
                    "marker": "next-marker",
                    "fetchedCount": 1,
                    "accounts": [
                        {
                            "id": "12345",
                            "records": [
                                {
                                    "time": "2026-05-22T10:00:00Z",
                                    "fieldsMap": {"admin": "admin@example.com"},
                                }
                            ],
                        }
                    ],
                }
            }
        }

    monkeypatch.setattr(auditFeedEnhanced, "createRequest", fake_create_request)
    monkeypatch.setattr(
        auditFeedEnhanced,
        "send_audit_records_to_outputs",
        lambda records, network, sentinel, args: streamed_records.extend(records),
    )

    args = make_args(
        fetch_limit=2,
        marker_file=str(tmp_path / "audit-marker.txt"),
        stream_events="127.0.0.1:9999",
        print_events=False,
    )

    auditFeedEnhanced.enhanced_audit_feed_handler(args, SimpleNamespace(accountID="12345"))

    assert capsys.readouterr().out == ""
    assert streamed_records[0]["admin"] == "admin@example.com"
