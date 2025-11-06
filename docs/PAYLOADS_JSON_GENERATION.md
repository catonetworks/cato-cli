# Payloads.json Generation Feature

## Overview

During the build process, `catolib.py` now automatically generates a `tests/payloads.json` file that contains all query operation names mapped to their required arguments with example values.

## Purpose

This file is used for:
- Testing: Provides example payloads for all query operations
- Documentation: Shows what required arguments each operation needs
- Validation: Helps ensure operations have proper required argument examples

## Implementation

### Files Modified

1. **schema/catolib.py**
   - Added `writePayloadsJson(schema)` function (lines 1678-1745)
   - Extracts required arguments (excluding `accountID`) from model files
   - Loads `tests/test_settings.json` for default values and operation exclusions
   - Generates JSON mapping of operation names to required argument payloads

2. **schema/importSchema.py**
   - Added call to `catolib.writePayloadsJson()` in build process (line 40)
   - Executes after operation parsers are generated but before README files

3. **tests/test_settings.json**
   - Configuration file for payload generation
   - `defaultValues`: Map of argument names to replacement values
   - `ignoreOperations`: Operations to exclude from payloads.json

### How It Works

1. **During Build**: After all model files are generated in `models/`, the `writePayloadsJson()` function is called

2. **Processing**: For each query operation:
   - Checks if operation is in `ignoreOperations` list in `test_settings.json` - if so, skips it
   - Loads the corresponding model file from `models/query.*.json`
   - Extracts `operationArgs` and `variablesPayload` from the model
   - Filters to include only required arguments (where `required == true`)
   - Excludes `accountID` as it's automatically provided by the CLI
   - Maps the argument name to its example value from `variablesPayload`
   - Applies default value replacements from `test_settings.json` `defaultValues`

3. **Output**: Writes all mappings to `tests/payloads.json` sorted by operation name

## Output Format

```json
{
    "query.accountBySubdomain": {
        "subdomains": [
            "string1",
            "string2"
        ]
    },
    "query.accountSnapshot": {},
    "query.appStats": {
        "timeFrame": "last.P1D"
    }
}
```

### Key Features

- **Required Only**: Only includes arguments where `required: true` in the model
- **AccountID Excluded**: `accountID` is automatically excluded as it's provided by the CLI configuration
- **Empty Objects**: Operations with no required arguments (other than accountID) get an empty object `{}`
- **Sorted**: Operations are sorted alphabetically for consistent output
- **Example Values**: Values are taken from the `variablesPayload` field in each model
- **Default Value Replacements**: Configured in `tests/test_settings.json` under `defaultValues`
  - `timeFrame` arguments are replaced with `"last.P1D"` (last 1 day)
  - `adminID` arguments are replaced with `"0"`
- **Operation Exclusions**: Configured in `tests/test_settings.json` under `ignoreOperations`
  - Operations like `query.accountBySubdomain` and `query.devices` can be excluded

## Build Process Integration

The generation happens during the schema build process:

```
1. Download GraphQL schema
2. Parse schema
3. Generate CLI driver
4. Generate operation parsers
5. Generate payloads.json ← NEW STEP
6. Generate README files
```

## Configuration File (test_settings.json)

The `tests/test_settings.json` file controls how payloads are generated:

```json
{
    "ignoreOperations": {
        "query.accountBySubdomain": {},
        "query.devices": {}
    },
    "defaultValues": {
        "timeFrame": "last.P1D",
        "adminID": "0"
    }
}
```

### Configuration Options

**ignoreOperations**: Object containing operation names to exclude from `payloads.json`
- Keys are operation names (e.g., `"query.accountBySubdomain"`)
- Values are empty objects `{}`
- Operations in this list will not appear in the generated `payloads.json`

**defaultValues**: Object mapping argument names to replacement values
- Keys are argument names (e.g., `"timeFrame"`)
- Values are the default values to use (e.g., `"last.P1D"`)
- When an argument matches a key, its value is replaced with the configured default
- Applies to all operations that have these required arguments

## Usage Example

The generated file can be used in tests:

```python
import json

# Load payloads
with open('tests/payloads.json', 'r') as f:
    payloads = json.load(f)

# Get required payload for an operation
required_args = payloads.get('query.accountBySubdomain', {})
# Returns: {"subdomains": ["string1", "string2"]}
```

## Error Handling

- If a model file is missing or invalid, the operation is still included with an empty payload `{}`
- A warning is printed to the console during build
- Build continues without failing

## Maintenance

The `payloads.json` file is automatically regenerated each time the schema is rebuilt using:

```bash
cd schema
python3 importSchema.py
```

Or:

```bash
cd schema  
python3 catolib.py
```

No manual intervention is required - the file stays in sync with the current schema and model files.
