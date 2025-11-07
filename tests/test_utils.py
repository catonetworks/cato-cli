#!/usr/bin/env python3
"""
Shared Test Utilities

Common functions and classes used across test scripts.
"""

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# ANSI color codes
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    BOLD = '\033[1m'
    NC = '\033[0m'  # No Color

# Get project paths
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TESTS_DIR = Path(__file__).parent.absolute()
TEST_PAYLOADS_FILE = TESTS_DIR / "payloads_generated.json"
PAYLOADS_CUSTOM_FILE = TESTS_DIR / "payloads_custom.json"
TEST_SETTINGS_FILE = TESTS_DIR / "payloads_settings.json"
PYTHON_CMD = "python3" if sys.platform != "win32" else "python"


def load_json_with_comments(file_path: Path) -> Any:
    """
    Load a JSON file that may contain JavaScript-style // comments.
    Returns the parsed JSON data.
    
    Args:
        file_path: Path to the JSON file
    
    Returns:
        Parsed JSON data (dict, list, etc.)
    
    Raises:
        json.JSONDecodeError: If the JSON is invalid after comment removal
        FileNotFoundError: If the file doesn't exist
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove JavaScript-style single-line comments
    # This regex removes // comments but preserves URLs (http://)
    lines = []
    for line in content.split('\n'):
        # Remove // comments, but not if part of a URL (preceded by :)
        # Also handle comments at the start of lines or after whitespace
        line = re.sub(r'(?<!:)//.*$', '', line)
        lines.append(line)
    
    cleaned_content = '\n'.join(lines)
    
    # Parse the cleaned JSON
    return json.loads(cleaned_content)


def load_test_settings(verbose: bool = False) -> Dict:
    """
    Load test_settings.json which contains ignoreOperations, overrideOperationPayload, etc.
    Supports JavaScript-style // comments in the JSON file.
    Returns the settings dict.
    """
    if not TEST_SETTINGS_FILE.exists():
        return {}
    
    try:
        settings = load_json_with_comments(TEST_SETTINGS_FILE)
        
        ignore_ops = settings.get('ignoreOperations', {})
        override_ops = settings.get('overrideOperationPayload', {})
        
        if verbose:
            if ignore_ops:
                print(f"{Colors.CYAN}Loaded {len(ignore_ops)} operation(s) to ignore from test_settings.json{Colors.NC}")
            if override_ops:
                print(f"{Colors.CYAN}Loaded {len(override_ops)} payload override(s) from test_settings.json{Colors.NC}")
        
        return settings
    except json.JSONDecodeError as e:
        print(f"{Colors.YELLOW}Warning: Invalid JSON in test_settings.json: {str(e)}{Colors.NC}")
        return {}
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: Failed to load test_settings.json: {str(e)}{Colors.NC}")
        return {}


def get_nested_value(data: Any, path: str) -> Tuple[bool, Any]:
    """
    Extract value from nested JSON using dot notation path.
    Returns (found, value) tuple.
    
    Examples:
        accountSnapshot.id
        sites[0].name
        data.result
        .data.result (leading dot is optional and will be stripped)
    """
    # Remove leading dot if present (for backwards compatibility)
    if path.startswith('.'):
        path = path[1:]
    
    # Return original data if path is empty
    if not path:
        return True, data
    
    current = data
    parts = path.replace('[', '.').replace(']', '').split('.')
    
    try:
        for part in parts:
            if not part:
                continue
                
            if part.isdigit():
                # Array index
                current = current[int(part)]
            else:
                # Object key
                current = current[part]
                
        return True, current
    except (KeyError, IndexError, TypeError):
        return False, None


def evaluate_assertion(data: Dict, assertion) -> Tuple[bool, str]:
    """
    Evaluate a single assertion against response data.
    Returns (passed, message) tuple.
    
    Assertion can be:
    - A string: path to check for existence (e.g., "data.appStats")
    - A dict with 'path', 'operator', and optionally 'value' fields
    
    Supported operators:
        - exists: Check if path exists (default)
        - exists_flexible: Check both data.{path} and {path}
        - not_exists: Check if path does not exist
        - ==: Check equality
        - !=: Check inequality
        - contains: Check if value contains element
        - type: Check value type (string, number, boolean, array, object, null)
        - length: Check exact length
        - length_gt: Check length greater than
    """
    # Handle simple string assertion (just check existence)
    if isinstance(assertion, str):
        path = assertion
        operator = 'exists_flexible'
        expected = None
    else:
        # Handle dict assertion
        path = assertion.get('path', '')
        operator = assertion.get('operator', 'exists')
        expected = assertion.get('value')
    
    # Special operator that checks both data.{path} and {path}
    if operator == 'exists_flexible':
        # Try data.{path} first
        found_data, actual_data = get_nested_value(data, f"data.{path}")
        if found_data:
            return True, f"Path data.{path} exists"
        
        # Try {path} as fallback
        found_direct, actual_direct = get_nested_value(data, path)
        if found_direct:
            return True, f"Path {path} exists"
        
        return False, f"Path not found (tried data.{path} and {path})"
    
    found, actual = get_nested_value(data, path)
    
    # Evaluate based on operator
    if operator == 'exists':
        if found:
            return True, f"Path {path} exists"
        return False, f"Path {path} does not exist"
        
    elif operator == 'not_exists':
        if not found:
            return True, f"Path {path} does not exist (as expected)"
        return False, f"Path {path} exists (expected not to exist)"
        
    elif operator == '==':
        if not found:
            return False, f"Path {path} not found"
        if actual == expected:
            return True, f"Path {path} equals {expected}"
        return False, f"Path {path} is {actual}, expected {expected}"
        
    elif operator == '!=':
        if not found:
            return False, f"Path {path} not found"
        if actual != expected:
            return True, f"Path {path} is {actual} (not equal to {expected})"
        return False, f"Path {path} equals {expected} (expected different value)"
        
    elif operator == 'contains':
        if not found:
            return False, f"Path {path} not found"
        if isinstance(actual, (list, str)) and expected in actual:
            return True, f"Path {path} contains {expected}"
        return False, f"Path {path} does not contain {expected}"
        
    elif operator == 'type':
        if not found:
            return False, f"Path {path} not found"
        type_map = {
            'string': str,
            'number': (int, float),
            'boolean': bool,
            'array': list,
            'object': dict,
            'null': type(None)
        }
        expected_type = type_map.get(expected)
        if isinstance(actual, expected_type):
            return True, f"Path {path} is type {expected}"
        return False, f"Path {path} is {type(actual).__name__}, expected {expected}"
        
    elif operator == 'length':
        if not found:
            return False, f"Path {path} not found"
        if isinstance(actual, (list, str, dict)) and len(actual) == expected:
            return True, f"Path {path} has length {expected}"
        actual_len = len(actual) if isinstance(actual, (list, str, dict)) else None
        return False, f"Path {path} has length {actual_len}, expected {expected}"
        
    elif operator == 'length_gt':
        if not found:
            return False, f"Path {path} not found"
        if isinstance(actual, (list, str, dict)) and len(actual) > expected:
            return True, f"Path {path} length {len(actual)} > {expected}"
        actual_len = len(actual) if isinstance(actual, (list, str, dict)) else None
        return False, f"Path {path} length {actual_len} not > {expected}"
        
    else:
        return False, f"Unknown operator: {operator}"


def run_cli_command(operation: str, payload: Dict, timeout: int = 30, verbose: bool = False) -> Tuple[bool, Optional[Dict], str, str]:
    """
    Execute CLI command using payload dict and return (success, json_response, error_message, command_str).
    operation is in the form 'query.appStats' (operationType.operationName).
    """
    # Parse operation (e.g., "query.appStats" -> "query", "appStats")
    try:
        op_type, *cli_op_parts = operation.split('.')
    except ValueError:
        return False, None, f"Invalid operation format: {operation}. Expected format: <type>.<name>", ""
    
    # Convert payload dict to JSON string
    json_payload = json.dumps(payload)
    
    cmd = [PYTHON_CMD, '-m', 'catocli', op_type] + cli_op_parts + [json_payload]
    
    # Build readable command string for display
    payload_str = json.dumps(payload, indent=2) if payload else '{}'
    cmd_display = f"catocli {op_type} {' '.join(cli_op_parts)} '{payload_str}'"
    
    if verbose:
        print(f"{Colors.CYAN}Executing: {' '.join(cmd[:5])} <payload> ...{Colors.NC}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(PROJECT_ROOT)
        )
        
        # Try to parse JSON first, regardless of exit code
        # (CLI might return non-zero for warnings but still have valid output)
        try:
            response = json.loads(result.stdout)
            return True, response, "", cmd_display
        except json.JSONDecodeError:
            # If we can't parse JSON and command failed, report error
            if result.returncode != 0:
                return False, None, f"Command failed with code {result.returncode}: {result.stderr or result.stdout[:500]}", cmd_display
            
            # Non-JSON output (e.g., CSV); wrap minimal structure
            response = {
                'raw_output': result.stdout,
                'lines': result.stdout.strip().split('\n'),
                'line_count': len(result.stdout.strip().split('\n'))
            }
            return True, response, "", cmd_display
        
    except subprocess.TimeoutExpired:
        return False, None, f"Command timed out after {timeout}s", cmd_display
    except Exception as e:
        return False, None, f"Unexpected error: {str(e)}", cmd_display


def run_test(test_file: Path, verbose: bool = False, test_label: str = "Test") -> Dict[str, Any]:
    """
    Run a single test from JSON file and return results.
    test_label is used to distinguish between generated/custom tests in output.
    """
    test_name = test_file.stem
    
    # Load test configuration
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            test_config = json.load(f)
    except json.JSONDecodeError as e:
        return {
            'name': test_name,
            'status': 'error',
            'error': f"Invalid JSON in test file: {str(e)}"
        }
    except Exception as e:
        return {
            'name': test_name,
            'status': 'error',
            'error': f"Failed to load test file: {str(e)}"
        }
    
    name = test_config.get('name', test_name)
    description = test_config.get('description', '')
    timeout = test_config.get('timeout', 30)
    operation = test_config.get('operation', '')
    payload = test_config.get('payload', {})
    
    # Validate required fields
    if not operation:
        return {
            'name': name,
            'description': description,
            'status': 'error',
            'error': 'Missing "operation" field in test config'
        }
    
    if payload is None or 'payload' not in test_config:
        return {
            'name': name,
            'description': description,
            'status': 'error',
            'error': 'Missing "payload" field in test config'
        }
    
    print(f"\n{Colors.BOLD}Running {test_label}: {name}{Colors.NC}")
    if description and verbose:
        print(f"{Colors.CYAN}Description: {description}{Colors.NC}")
    if verbose:
        print(f"{Colors.CYAN}Test file: {test_file.name}{Colors.NC}")
        print(f"{Colors.CYAN}Operation: {operation}{Colors.NC}")
    
    # Run CLI command
    success, response, error, command = run_cli_command(operation, payload, timeout, verbose)
    
    if not success:
        return {
            'name': name,
            'description': description,
            'status': 'failed',
            'error': error,
            'command': command
        }
    
    # Run assertions
    assertions = test_config.get('assertions', [])
    passed_assertions = []
    failed_assertions = []
    
    for i, assertion in enumerate(assertions):
        passed, message = evaluate_assertion(response, assertion)
        
        if passed:
            passed_assertions.append(message)
            if verbose:
                print(f"{Colors.CYAN}  ✓ Assertion {i+1}: {message}{Colors.NC}")
        else:
            failed_assertions.append(message)
            print(f"{Colors.RED}  ✗ Assertion {i+1}: {message}{Colors.NC}")
    
    # Determine overall test status
    if failed_assertions:
        status = 'failed'
    else:
        status = 'passed'
    
    result = {
        'name': test_name,
        'description': description,
        'status': status,
        'passed_assertions': len(passed_assertions),
        'failed_assertions': len(failed_assertions),
        'failures': failed_assertions,
        'response_sample': str(response)[:200] if verbose else None,
        'command': command
    }
    
    return result


def run_test_from_config(test_key: str, test_config: Dict, verbose: bool = False, test_label: str = "Test") -> Dict[str, Any]:
    """
    Run a single test from config dict and return results.
    test_label is used to distinguish between generated/custom tests in output.
    """
    name = test_config.get('name', test_key)
    description = test_config.get('description', '')
    timeout = test_config.get('timeout', 30)
    operation = test_config.get('operation', '')
    payload = test_config.get('payload', {})
    
    # Validate required fields
    if not operation:
        return {
            'name': name,
            'description': description,
            'status': 'error',
            'error': 'Missing "operation" field in test config'
        }
    
    if payload is None or 'payload' not in test_config:
        return {
            'name': name,
            'description': description,
            'status': 'error',
            'error': 'Missing "payload" field in test config'
        }
    
    print(f"\n{Colors.BOLD}Running {test_label}: {name}{Colors.NC}")
    if description and verbose:
        print(f"{Colors.CYAN}Description: {description}{Colors.NC}")
    if verbose:
        print(f"{Colors.CYAN}Test key: {test_key}{Colors.NC}")
        print(f"{Colors.CYAN}Operation: {operation}{Colors.NC}")
    
    # Run CLI command
    success, response, error, command = run_cli_command(operation, payload, timeout, verbose)
    
    if not success:
        return {
            'name': name,
            'description': description,
            'status': 'failed',
            'error': error,
            'command': command
        }
    
    # Run assertions
    assertions = test_config.get('assertions', [])
    passed_assertions = []
    failed_assertions = []
    
    for i, assertion in enumerate(assertions):
        passed, message = evaluate_assertion(response, assertion)
        
        if passed:
            passed_assertions.append(message)
            if verbose:
                print(f"{Colors.CYAN}  ✓ Assertion {i+1}: {message}{Colors.NC}")
        else:
            failed_assertions.append(message)
            print(f"{Colors.RED}  ✗ Assertion {i+1}: {message}{Colors.NC}")
    
    # Determine overall test status
    if failed_assertions:
        status = 'failed'
    else:
        status = 'passed'
    
    result = {
        'name': test_key,
        'description': description,
        'status': status,
        'passed_assertions': len(passed_assertions),
        'failed_assertions': len(failed_assertions),
        'failures': failed_assertions,
        'response_sample': str(response)[:200] if verbose else None,
        'command': command
    }
    
    return result


def load_test_payloads_tests(ignore_operations: set, override_payloads: Dict, verbose: bool = False) -> Dict[str, Dict]:
    """
    Load tests from payloads_generated.json and return test configs.
    Supports JavaScript-style // comments in the JSON file.
    Returns dict of test configs indexed by operation name.
    """
    if not TEST_PAYLOADS_FILE.exists():
        return {}
    
    try:
        test_payloads = load_json_with_comments(TEST_PAYLOADS_FILE)
    except Exception as e:
        print(f"{Colors.YELLOW}Error loading {TEST_PAYLOADS_FILE.name}: {str(e)}{Colors.NC}")
        return {}
    
    generated_tests = {}
    
    for operation, args in test_payloads.items():
        # Skip if operation is in ignoreOperations
        if operation in ignore_operations:
            if verbose:
                print(f"{Colors.CYAN}Skipping {operation} (in ignoreOperations){Colors.NC}")
            continue
        
        # Check if there's an override config for this operation
        payload = args
        custom_assertions = []
        if operation in override_payloads:
            override_config = override_payloads[operation]
            # Handle new structure: {"payload": {...}, "assertions": [...]}
            if isinstance(override_config, dict) and 'payload' in override_config:
                payload = override_config.get('payload', {})
                custom_assertions = override_config.get('assertions', [])
                if verbose:
                    print(f"{Colors.CYAN}Using override payload for {operation}{Colors.NC}")
            else:
                # Legacy structure: just the payload dict
                payload = override_config
                if verbose:
                    print(f"{Colors.CYAN}Using override payload for {operation} (legacy format){Colors.NC}")
        
        # Extract the operation name (last part after dots)
        # The data key in the GraphQL response usually mirrors the operation name after "query."
        # e.g., "query.appStats" -> ".data.appStats" or ".appStats"
        # e.g., "query.site.siteGeneralDetails" -> ".data.site.siteGeneralDetails" or ".site.siteGeneralDetails"
        data_key = operation.split('.', 1)[1] if '.' in operation else operation
        
        # Build assertions list
        assertion_list = []
        if custom_assertions:
            # Use custom assertions from settings file (simple strings)
            assertion_list = custom_assertions if isinstance(custom_assertions, list) else [custom_assertions]
        else:
            # Default: check data.{operation} or {operation} (flexible check)
            assertion_list = [data_key]
        
        # Build test config
        test_config = {
            "name": f"{operation} - Generated Test",
            "description": f"Auto-generated test for {operation}",
            "operation": operation,
            "payload": payload if payload else {},
            "timeout": 30,
            "assertions": assertion_list
        }
        
        generated_tests[operation] = test_config
    
    return generated_tests


def load_custom_tests(verbose: bool = False) -> Dict[str, Dict]:
    """
    Load custom tests from payloads_custom.json.
    Supports JavaScript-style // comments in the JSON file.
    Returns a dict of test configs indexed by test key.
    """
    if not PAYLOADS_CUSTOM_FILE.exists():
        return {}
    
    try:
        custom_tests = load_json_with_comments(PAYLOADS_CUSTOM_FILE)
        if verbose:
            print(f"{Colors.CYAN}Loaded {len(custom_tests)} custom test(s) from {PAYLOADS_CUSTOM_FILE.name}{Colors.NC}")
        return custom_tests
    except Exception as e:
        print(f"{Colors.YELLOW}Error loading {PAYLOADS_CUSTOM_FILE.name}: {str(e)}{Colors.NC}")
        return {}


def cleanup_generated_tests(generated_tests: Dict[str, Dict]):
    """
    Cleanup function - no longer needed as tests run in-memory.
    Kept for backwards compatibility.
    """
    pass


def print_test_summary(passed: int, failed: int, skipped: int):
    """Print test run summary"""
    total = passed + failed + skipped
    
    print(f"\n{Colors.BOLD}{'='*60}", Colors.CYAN)
    print("Test Summary", Colors.CYAN)
    print(f"{'='*60}{Colors.NC}", Colors.CYAN)
    print(f"Total:   {total}")
    print(f"{Colors.GREEN if passed else Colors.NC}Passed:  {passed}{Colors.NC}")
    print(f"{Colors.RED if failed else Colors.NC}Failed:  {failed}{Colors.NC}")
    print(f"{Colors.YELLOW if skipped else Colors.NC}Skipped: {skipped}{Colors.NC}")
    
    if failed == 0:
        print(f"\n{Colors.GREEN}✓ All tests passed!{Colors.NC}")
    else:
        print(f"\n{Colors.RED}✗ {failed} test(s) failed{Colors.NC}")
