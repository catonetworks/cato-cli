"""Build GraphQL multipart uploads from explicitly typed CLI input paths."""

import copy
import json
import os
import stat

from urllib3.filepost import encode_multipart_formdata


MAX_UPLOAD_BYTES = 32 * 1024 * 1024


def encode_uploads(body, model):
    """Return (encoded body, content type), or None for ordinary JSON requests.

    Only values whose model type is Upload are interpreted as local file paths.
    Leave the caller's variables intact, including for repeated invocations.
    """
    operations = copy.deepcopy(body)
    files = []
    file_map = {}
    total_bytes = 0

    def visit(value, type_info, path, parent, key, list_depth=0):
        nonlocal total_bytes
        if value is None:
            return
        list_count = type_info.get("kind", []).count("LIST")
        if list_depth < list_count:
            if not isinstance(value, list):
                # GraphQL permits a single value for a list input.
                value = [value]
                parent[key] = value
            for index, item in enumerate(value):
                visit(item, type_info, f"{path}.{index}", value, index, list_depth + 1)
        elif type_info.get("name") == "Upload":
            if not isinstance(value, str) or not value:
                raise ValueError(f"{path} must be a local file path")
            # Avoid blocking on FIFOs or devices; bound memory for multipart encoding.
            if not stat.S_ISREG(os.stat(value).st_mode):
                raise ValueError(f"{path} must reference a regular file")
            with open(value, "rb") as handle:
                content = handle.read(MAX_UPLOAD_BYTES - total_bytes + 1)
            total_bytes += len(content)
            if total_bytes > MAX_UPLOAD_BYTES:
                raise ValueError("GraphQL uploads exceed the 32 MiB request limit")
            file_index = str(len(files))
            files.append((file_index, (os.path.basename(value), content, "application/octet-stream")))
            file_map[file_index] = [path]
            parent[key] = None
        elif isinstance(value, dict):
            fields = type_info.get("definition", {}).get("inputFields") or {}
            for name, field in fields.items():
                if name in value:
                    visit(value[name], field["type"], f"{path}.{name}", value, name)

    variables = operations.get("variables", {})
    for name, argument in model.get("operationArgs", {}).items():
        name = argument.get("varName", name)
        if name in variables:
            visit(variables[name], argument["type"], f"variables.{name}", variables, name)
    if not files:
        return None
    fields = [("operations", json.dumps(operations)), ("map", json.dumps(file_map))]
    return encode_multipart_formdata(fields + files)
