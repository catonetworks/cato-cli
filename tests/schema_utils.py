"""Load the vendor schema for strict operation and variable validation."""

import copy
import json
from pathlib import Path

from graphql import DirectiveLocation, build_client_schema, parse_value, print_ast
from graphql.language import ListValueNode, ObjectValueNode


def normalize_test_introspection(data):
    """Normalize known vendor metadata defects without disabling validation."""
    data = copy.deepcopy(data)
    types = {item["name"]: item for item in data["__schema"]["types"]}
    for directive in data["__schema"]["directives"]:
        directive["locations"] = [
            location for location in directive["locations"]
            if location in DirectiveLocation.__members__
        ]

    for type_data in types.values():
        for field in type_data.get("inputFields") or ():
            if field.get("defaultValue") is None:
                continue
            field_type = field["type"]
            while field_type["kind"] == "NON_NULL":
                field_type = field_type["ofType"]
            if field_type["kind"] != "INPUT_OBJECT":
                continue
            fields = {item["name"] for item in types[field_type["name"]]["inputFields"]}
            if "customCategory" in fields:
                continue
            default = parse_value(field["defaultValue"])
            if not isinstance(default, ObjectValueNode):
                continue
            # The API removed customCategory but retained customCategory: [] in
            # several firewall defaults. Only remove this known empty field;
            # all other invalid metadata must still fail schema validation.
            retained = tuple(item for item in default.fields if not (
                item.name.value == "customCategory"
                and isinstance(item.value, ListValueNode)
                and not item.value.values
            ))
            if len(retained) != len(default.fields):
                field["defaultValue"] = print_ast(ObjectValueNode(fields=retained))
    return data


def build_test_schema(data):
    return build_client_schema(normalize_test_introspection(data))


def load_test_schema():
    path = Path(__file__).resolve().parents[1] / "schema/introspection.json"
    return build_test_schema(json.loads(path.read_text(encoding="utf-8"))["data"])
