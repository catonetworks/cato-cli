# Cato CLI Regression Test Suite

Comprehensive regression tests for the catocli tool. These tests validate all CLI commands, data integrity, and proper packaging.

## Installation

Install test dependencies:

```bash
pip install -r tests/requirements.txt
```

## Running Tests

### Run all tests
```bash
pytest tests/test_cli_regression.py -v
```

### Run specific test class
```bash
# Test CLI structure only
pytest tests/test_cli_regression.py::TestCLIStructure -v

# Test model files only
pytest tests/test_cli_regression.py::TestModelFiles -v

# Test query payloads only
pytest tests/test_cli_regression.py::TestQueryPayloads -v

# Test query operations
pytest tests/test_cli_regression.py::TestQueryOperations -v

# Test mutation operations
pytest tests/test_cli_regression.py::TestMutationOperations -v

# Test data integrity
pytest tests/test_cli_regression.py::TestDataIntegrity -v

# Test error handling
pytest tests/test_cli_regression.py::TestErrorHandling -v

# Test packaging
pytest tests/test_cli_regression.py::TestPackaging -v
```

### Run specific test
```bash
pytest tests/test_cli_regression.py::TestCLIStructure::test_cli_entry_point_exists -v
```

### Run with coverage
```bash
pytest tests/test_cli_regression.py --cov=catocli --cov-report=html
```

### Run with detailed output
```bash
pytest tests/test_cli_regression.py -vv -s
```

### Run and stop on first failure
```bash
pytest tests/test_cli_regression.py -x
```

## Test Categories

### 1. CLI Structure Tests (`TestCLIStructure`)
- Validates entry point exists
- Verifies help text is available
- Tests query, mutation, and raw subcommands

### 2. Model Files Tests (`TestModelFiles`)
- Checks models directory exists
- Validates all model files contain valid JSON
- Ensures required fields are present

### 3. Query Payloads Tests (`TestQueryPayloads`)
- Checks query payloads directory exists
- Validates all payload files contain valid JSON
- Ensures required GraphQL fields are present
- Validates payloads match corresponding model files

### 4. Query Operations Tests (`TestQueryOperations`)
- Tests that all query operations have help text
- Validates command parsing for all query operations

### 5. Mutation Operations Tests (`TestMutationOperations`)
- Tests that all mutation operations have help text
- Validates command parsing for all mutation operations

### 6. Data Integrity Tests (`TestDataIntegrity`)
- Validates payload variables match model operation args
- Ensures consistency between models and payloads

### 7. Error Handling Tests (`TestErrorHandling`)
- Tests invalid JSON input handling
- Validates missing required arguments handling

### 8. Packaging Tests (`TestPackaging`)
- Verifies MANIFEST.in includes all required files
- Ensures setup.py exists

## Test Statistics

The test suite validates:
- ✓ 299 operation payload files
- ✓ 299 operation model files
- ✓ All CLI command structures
- ✓ Help text for all operations
- ✓ JSON validity for all data files
- ✓ Data integrity between models and payloads

## Continuous Integration

### Add to GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11', '3.12']
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r tests/requirements.txt
        pip install -e .
    
    - name: Run regression tests
      run: |
        pytest tests/test_cli_regression.py -v --tb=short
```

## Troubleshooting

### Test fails with "Models directory not found"
Ensure you're running tests from the project root directory.

### Test fails with "CLI entry point failed"
Make sure catocli is installed in development mode:
```bash
pip install -e .
```

### Tests timeout
Some tests have a 10-second timeout. If your system is slow, you can increase it by modifying the `timeout` parameter in the test file.

### Configuration not found errors
Some tests that actually call CLI commands may fail if no catocli profile is configured. These tests handle this gracefully, but you can configure a profile with:
```bash
catocli configure set
```

## Adding New Tests

To add tests for new operations:

1. The test suite automatically discovers new operations from the `queryPayloads/` directory
2. Ensure your new operation has:
   - A model file in `models/`
   - A payload file in `queryPayloads/`
   - Matching operation name between model and payload files

Then run the tests to validate the new operation.

## Performance

The full test suite typically runs in:
- **~30-60 seconds** on a modern machine
- **~2-3 minutes** on slower systems or CI

Individual test classes run much faster (~5-10 seconds each).
