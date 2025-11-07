# Cato CLI Test Suite

Comprehensive test suite for the catocli tool with three types of tests: validation tests, auto-generated tests, and custom tests.

## Test Structure

### 1. Validation Tests (Pytest)
Structural validation and regression tests that verify:
- CLI entry points and command structure
- Model file validity and structure
- Query payload file validity
- Data integrity between models and payloads
- Error handling and packaging

### 2. Generated Tests
Auto-generated from `payloads_generated.json` to test all query operations with default payloads.

### 3. Custom Tests
Manual test cases from `payloads_custom.json` for complex scenarios, edge cases, and specific use cases.

## Installation

Install test dependencies:

```bash
pip install -r requirements.txt
```

Install catocli in development mode:

```bash
pip install -e .
```

## Rebuild the CLI from the latest schema introspection query"
```bash
cd schema
python3 importSchema.py
```

## Running Tests

### Run all test suites
```bash
cd tests
python3 run_all_tests.py
```

### Run with options
```bash
# Skip validation tests (pytest)
python3 run_all_tests.py --skip-validation

# Skip auto-generated tests
python3 run_all_tests.py --skip-generated

# Skip custom tests
python3 run_all_tests.py --skip-custom

# Verbose output
python3 run_all_tests.py --verbose

# Stop on first failure
python3 run_all_tests.py --stop-on-fail
```

### Filter tests
```bash
# Run only generated tests matching operation name
python3 run_all_tests.py --operation accountMetrics

# Run only custom tests matching test name
python3 run_all_tests.py --test "SCIM"

# Combine filters and options
python3 run_all_tests.py --skip-validation --operation appStats --verbose
```

## Test Configuration

### `payloads_settings.json`
Central configuration for test behavior:

```json
{
    "ignoreOperations": {
        "query.devices": {},
        "query.catalogs.catalogApplication": {}
    },
    "defaultValues": {
        "timeFrame": "last.P1D",
        "adminID": "0"
    },
    "overrideOperationPayload": {
        "query.accountMetrics": {
            "payload": {...},
            "assertions": [...]
        }
    }
}
```

**Configuration options:**
- `ignoreOperations`: Tests are generated but skipped during execution (marked as ignored)
- `defaultValues`: Default values to use when generating test payloads
- `overrideOperationPayload`: Custom payloads and assertions for specific operations

### `payloads_custom.json`
Custom test cases with advanced scenarios:

```json
{
    "test.key": {
        "name": "Test Name",
        "description": "Test description",
        "operation": "query.appStats",
        "payload": {...},
        "timeout": 30,
        "assertions": [...]
    }
}
```

## Assertion System

Tests support powerful assertion syntax for validating API responses:

### String Assertions (Simple Existence Check)
```json
"assertions": [
    "data.appStats",           // Check if path exists
    "accountMetrics.sites"     // Supports dot notation
]
```

### Object Assertions (Advanced Validation)

#### Type Checking
```json
{
    "path": "data.sites",
    "operator": "type",
    "value": "array"  // Options: string, number, boolean, array, object, null
}
```

#### Value Comparison
```json
{
    "path": "data.status",
    "operator": "==",
    "value": "active"
},
{
    "path": "data.count",
    "operator": "!=",
    "value": 0
}
```

#### Array Operations
```json
{
    "path": "data.items",
    "operator": "length",
    "value": 5              // Exact length
},
{
    "path": "data.results",
    "operator": "length_gt",
    "value": 0              // Length greater than
},
{
    "path": "data.tags",
    "operator": "contains",
    "value": "production"   // Array/string contains
}
```

#### Array Element Access
```json
"assertions": [
    "[0].id",                   // First element has id field
    "[0].site.name",            // Nested field in first element
    "data.sites[2].status"      // Third element status
]
```

#### Existence Checks
```json
{
    "path": "data.metadata",
    "operator": "exists"        // Path must exist
},
{
    "path": "data.error",
    "operator": "not_exists"    // Path must NOT exist
}
```

## Example Custom Test

```json
{
    "query.accountMetrics.detailed": {
        "name": "Account Metrics - Detailed Analysis",
        "description": "Monitor bandwidth with multiple dimensions",
        "operation": "query.accountMetrics",
        "payload": {
            "buckets": 24,
            "labels": ["bytesDownstream", "bytesUpstream", "health"],
            "siteIDs": ["144905"],
            "timeFrame": "last.P1D"
        },
        "timeout": 30,
        "assertions": [
            // Check response structure
            "accountMetrics.metadata",
            "accountMetrics.sites",
            
            // Validate array has data
            {
                "path": "accountMetrics.sites",
                "operator": "length_gt",
                "value": 0
            },
            
            // Check first site has expected fields
            "accountMetrics.sites[0].id",
            "accountMetrics.sites[0].name",
            "accountMetrics.sites[0].timeSeries"
        ]
    }
}
```

## Test Output

### Success Output
```
======================================================================
CLI Test Suite Runner - 2025-11-07 10:56:12
======================================================================

Running Validation Tests (pytest) - 2025-11-07 10:56:12
======================================================================
...
======================================================================

Running Generated Tests - 2025-11-07 10:56:15
======================================================================
Found 250 auto-generated test(s)

✓ query.appStats - Generated Test
✓ query.accountMetrics - Generated Test
⊘ query.devices - Generated Test (ignored)
...

Generated Tests Summary:
Passed: 245, Failed: 0, Ignored: 5

Running Custom Tests - 2025-11-07 10:56:45
======================================================================
Found 15 custom test(s)

✓ Account Metrics - Site Health Check
✓ SCIM Get Users
...

Custom Tests Summary:
Passed: 15, Failed: 0, Ignored: 0

======================================================================
Overall Test Summary
======================================================================

Total Payload Tests:
Passed:  260
Failed:  0
Skipped: 5

Suite Status:
  Validation Tests: ✓ PASSED
  Generated Tests:  ✓ PASSED
  Custom Tests:     ✓ PASSED

✓ All tests passed!
```

### Failure Output
```
✗ query.appStats - Generated Test
    Command: 
catocli query appStats '{"timeFrame": "last.P1D"}'
    Error: Command failed with code 1: ERROR! Status code: 422
    Path data.appStats.metadata does not exist
```

## Test Development Workflow

### Adding a New Custom Test

1. Add entry to `payloads_custom.json`:
```json
{
    "my.new.test": {
        "name": "My New Test",
        "description": "Test description",
        "operation": "query.myOperation",
        "payload": {...},
        "assertions": [...]
    }
}
```

2. Run the test:
```bash
python3 run_all_tests.py --test "My New Test"
```

### Ignoring a Flaky Operation

Add to `payloads_settings.json`:
```json
{
    "ignoreOperations": {
        "query.flakyOperation": {}
    }
}
```

The operation test will still be generated but marked as ignored during execution.

### Overriding an Operation Payload

Add to `payloads_settings.json`:
```json
{
    "overrideOperationPayload": {
        "query.myOperation": {
            "payload": {
                "customParam": "value"
            },
            "assertions": [
                "data.result"
            ]
        }
    }
}
```

## Continuous Integration

The test suite is configured in `.github/workflows/test.yml`:

```yaml
- name: Run all test suites
  run: |
    python3 tests/run_all_tests.py --verbose
```

## Test Files

- `run_all_tests.py` - Main test orchestrator that runs all test suites
- `test_utils.py` - Shared utilities for test execution and assertions
- `payloads_generated.json` - Auto-generated test payloads (do not edit manually)
- `payloads_custom.json` - Custom test cases (edit to add tests)
- `payloads_settings.json` - Test configuration and overrides

## Troubleshooting

### "Module not found" errors
Ensure catocli is installed in development mode:
```bash
pip install -e .
```

### "Configuration not found" errors
Some tests require a configured profile:
```bash
catocli configure set --profile test
```

### Tests timeout
Increase timeout in test configuration:
```json
{
    "my.test": {
        "timeout": 60,
        ...
    }
}
```

### Empty payload issue
For operations that don't require arguments, use empty payload:
```json
{
    "operation": "entity.site.list",
    "payload": {},    // Will not add '{}' as command argument
    ...
}
```

## Performance

Typical execution times:
- **Validation Tests**: ~10-20 seconds
- **Generated Tests**: ~2-5 minutes (250+ operations)
- **Custom Tests**: ~30-60 seconds (15-20 tests)
- **Total**: ~3-6 minutes for full suite
