#!/usr/bin/env python3
"""
CLI All Tests Runner

Runs all test suites for the catocli project:
1. Validation tests (pytest-based regression tests)
2. Generated tests (from payloads_generated.json)
3. Custom tests (from payloads_custom.json)

Usage:
    python3 run_all_tests.py                    # Run all test suites
    python3 run_all_tests.py --skip-generated   # Skip auto-generated tests
    python3 run_all_tests.py --skip-custom      # Skip custom tests
    python3 run_all_tests.py --skip-validation  # Skip validation tests
    python3 run_all_tests.py --verbose          # Verbose output
    python3 run_all_tests.py --stop-on-fail     # Stop on first failure
"""

import subprocess
import sys
import argparse
import json
import re
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

from test_utils import (
    Colors,
    TestStatus,
    DictKeys,
    SuiteName,
    Defaults,
    load_test_settings,
    load_test_payloads_tests,
    load_custom_tests,
    cleanup_generated_tests,
    run_test_from_config,
    print_test_summary,
    convert_test_result_to_json_format
)

# Get project paths (can be overridden via --dir)
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TESTS_DIR = Path(__file__).parent.absolute()
PYTHON_CMD = "python3" if sys.platform != "win32" else "python"


def set_tests_directory(directory: Path):
    """Update global paths to use specified test directory"""
    global PROJECT_ROOT, TESTS_DIR
    TESTS_DIR = directory.absolute()
    PROJECT_ROOT = TESTS_DIR.parent.absolute()
    
    # Also update test_utils module paths
    import test_utils
    test_utils.PROJECT_ROOT = PROJECT_ROOT
    test_utils.TESTS_DIR = TESTS_DIR


class AllTestsRunner:
    """Orchestrates running all test suites"""
    
    def __init__(self, verbose: bool = False, stop_on_fail: bool = False, json_output: str = None, 
                 external_test_report_link: str = None, s3_config: Dict = None, s3_verify_ssl: bool = False):
        self.verbose = verbose
        self.stop_on_fail = stop_on_fail
        self.json_output = json_output
        self.external_test_report_link = external_test_report_link
        self.s3_config = s3_config
        self.s3_verify_ssl = s3_verify_ssl
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.validation_passed = False
        self.generated_passed = False
        self.custom_passed = False
        self.test_results = []  # Store all test results for JSON export
        self.test_file_mapping = {}  # Map test results to their file paths and suite names
    
    def run_validation_tests(self):
        """Run pytest-based validation tests"""
        print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"Running Validation Tests (pytest) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        
        # Run tests from this module - pytest will discover the test classes
        pytest_args = ['-v', '--tb=short', __file__]
        
        if self.verbose:
            pytest_args.append('-vv')
        if self.stop_on_fail:
            pytest_args.append('-x')
        
        try:
            import pytest as pytest_module
            exit_code = pytest_module.main(pytest_args)
            self.validation_passed = (exit_code == 0)
            return exit_code == 0
        except ImportError:
            print(f"{Colors.YELLOW}Warning: pytest not installed, skipping validation tests{Colors.NC}")
            return True
    
    def run_generated_tests(self, operation_filter: str = None):
        """Run auto-generated tests from payloads_generated.json"""
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"Running Generated Tests - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        
        # Load test settings
        test_settings = load_test_settings(self.verbose)
        override_payloads = test_settings.get('overrideOperationPayload', {})
        ignore_operations = set(test_settings.get('ignoreOperations', {}).keys())
        enable_trace_id = test_settings.get('enableTraceId', False)
        
        # Load test configs (in-memory)
        generated_tests = load_test_payloads_tests(
            ignore_operations,
            override_payloads,
            self.verbose
        )
        
        if not generated_tests:
            print(f"{Colors.YELLOW}No generated tests found{Colors.NC}")
            return True
        
        # Filter tests
        filtered_generated = {}
        for operation, test_config in generated_tests.items():
            if operation_filter:
                if operation_filter.lower() not in operation.lower():
                    continue
            
            filtered_generated[operation] = test_config
        
        if not filtered_generated:
            print(f"{Colors.YELLOW}No tests found matching filters{Colors.NC}")
            return True
        
        print(f"Found {len(filtered_generated)} auto-generated test(s)\n")
        
        suite_passed = 0
        suite_failed = 0
        suite_ignored = 0
        
        for operation, test_config in filtered_generated.items():
            # Check if test is marked as ignored
            if test_config.get('ignored', False):
                suite_ignored += 1
                print(f"{Colors.YELLOW}⊘ {test_config.get(DictKeys.NAME, operation)} (ignored){Colors.NC}")
                continue
            
            result = run_test_from_config(operation, test_config, self.verbose, "Generated Test", enable_trace_id)
            
            # Store result for JSON export with suite name
            if self.json_output:
                result[DictKeys.SUITE_NAME] = SuiteName.GENERATED  # Track suite name
                self.test_results.append(result)
            
            status = result[DictKeys.STATUS]
            if status == TestStatus.PASSED:
                suite_passed += 1
                print(f"{Colors.GREEN}✓ {test_config.get(DictKeys.NAME, operation)}{Colors.NC}")
            elif status == TestStatus.FAILED:
                suite_failed += 1
                print(f"{Colors.RED}✗ {test_config.get(DictKeys.NAME, operation)}{Colors.NC}")
                if result.get(DictKeys.COMMAND):
                    print(f"{Colors.YELLOW}Command: \n{result[DictKeys.COMMAND]}{Colors.NC}")
                if result.get(DictKeys.ERROR):
                    print(f"{Colors.RED}    Error: {result[DictKeys.ERROR]}{Colors.NC}")
                if result.get(DictKeys.TRACE_ID):
                    print(f"{Colors.CYAN}    Trace ID: {result[DictKeys.TRACE_ID]}{Colors.NC}")
                if result.get('query'):
                    print(f"{Colors.CYAN}    GraphQL Query:\n{result['query']}{Colors.NC}")
                if result.get(DictKeys.FAILURES):
                    for failure in result[DictKeys.FAILURES]:
                        print(f"{Colors.RED}    {failure}{Colors.NC}")
                if self.stop_on_fail:
                    print(f"{Colors.YELLOW}\nStopping on first failure (--stop-on-fail){Colors.NC}")
                    break
            else:  # error
                suite_failed += 1
                print(f"{Colors.RED}✗ {test_config.get(DictKeys.NAME, operation)} (error){Colors.NC}")
                if result.get(DictKeys.COMMAND):
                    print(f"{Colors.YELLOW}Command: \n{result[DictKeys.COMMAND]}{Colors.NC}")
                if result.get(DictKeys.ERROR):
                    print(f"{Colors.RED}    {result[DictKeys.ERROR]}{Colors.NC}")
                if result.get(DictKeys.TRACE_ID):
                    print(f"{Colors.CYAN}    Trace ID: {result[DictKeys.TRACE_ID]}{Colors.NC}")
                if result.get('query'):
                    print(f"{Colors.CYAN}    GraphQL Query:\n{result['query']}{Colors.NC}")
        
        # Print suite summary
        print(f"\n{Colors.BOLD}Generated Tests Summary:{Colors.NC}")
        print(f"Passed: {suite_passed}, Failed: {suite_failed}, Ignored: {suite_ignored}")
        
        self.passed += suite_passed
        self.failed += suite_failed
        self.skipped += suite_ignored
        self.generated_passed = (suite_failed == 0)
        
        return suite_failed == 0
    
    def run_custom_tests(self, test_filter: str = None):
        """Run custom tests from payloads_custom.json"""
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"Running Custom Tests - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        
        # Load test settings to get trace-id setting
        test_settings = load_test_settings(self.verbose)
        enable_trace_id = test_settings.get('enableTraceId', False)
        
        custom_tests_dict = load_custom_tests(self.verbose)
        
        if not custom_tests_dict:
            print(f"{Colors.YELLOW}No custom tests found{Colors.NC}")
            return True
        
        # Filter custom tests
        filtered_custom = {}
        for test_key, test_config in custom_tests_dict.items():
            if test_filter:
                test_name = test_config.get(DictKeys.NAME, '')
                if test_filter.lower() not in test_name.lower():
                    continue
            
            filtered_custom[test_key] = test_config
        
        if not filtered_custom:
            print(f"{Colors.YELLOW}No tests found matching filters{Colors.NC}")
            return True
        
        print(f"Found {len(filtered_custom)} custom test(s)\n")
        
        suite_passed = 0
        suite_failed = 0
        suite_ignored = 0
        
        for test_key, test_config in filtered_custom.items():
            # Check if test is marked as ignored
            if test_config.get('ignored', False):
                suite_ignored += 1
                print(f"{Colors.YELLOW}⊘ {test_config.get(DictKeys.NAME, test_key)} (ignored){Colors.NC}")
                continue
            
            result = run_test_from_config(test_key, test_config, self.verbose, "Custom Test", enable_trace_id)
            
            # Store result for JSON export with suite name
            if self.json_output:
                result[DictKeys.SUITE_NAME] = SuiteName.CUSTOM  # Track suite name
                self.test_results.append(result)
            
            status = result[DictKeys.STATUS]
            if status == TestStatus.PASSED:
                suite_passed += 1
                print(f"{Colors.GREEN}✓ {test_config.get(DictKeys.NAME, test_key)}{Colors.NC}")
            elif status == TestStatus.FAILED:
                suite_failed += 1
                print(f"{Colors.RED}✗ {test_config.get(DictKeys.NAME, test_key)}{Colors.NC}")
                if result.get(DictKeys.COMMAND):
                    print(f"{Colors.YELLOW}    Command: \n{result[DictKeys.COMMAND]}{Colors.NC}")
                if result.get(DictKeys.ERROR):
                    print(f"{Colors.RED}    Error: {result[DictKeys.ERROR]}{Colors.NC}")
                if result.get(DictKeys.TRACE_ID):
                    print(f"{Colors.CYAN}    Trace ID: {result[DictKeys.TRACE_ID]}{Colors.NC}")
                if result.get('query'):
                    print(f"{Colors.CYAN}    GraphQL Query:\n{result['query']}{Colors.NC}")
                if result.get(DictKeys.FAILURES):
                    for failure in result[DictKeys.FAILURES]:
                        print(f"{Colors.RED}    {failure}{Colors.NC}")
                if self.stop_on_fail:
                    print(f"{Colors.YELLOW}\nStopping on first failure (--stop-on-fail){Colors.NC}")
                    break
            else:  # error
                suite_failed += 1
                print(f"{Colors.RED}✗ {test_config.get(DictKeys.NAME, test_key)} (error){Colors.NC}")
                if result.get(DictKeys.COMMAND):
                    print(f"{Colors.YELLOW}    Command: \n{result[DictKeys.COMMAND]}{Colors.NC}")
                if result.get(DictKeys.ERROR):
                    print(f"{Colors.RED}    {result[DictKeys.ERROR]}{Colors.NC}")
                if result.get(DictKeys.TRACE_ID):
                    print(f"{Colors.CYAN}    Trace ID: {result[DictKeys.TRACE_ID]}{Colors.NC}")
                if result.get('query'):
                    print(f"{Colors.CYAN}    GraphQL Query:\n{result['query']}{Colors.NC}")
        
        # Print suite summary
        print(f"\n{Colors.BOLD}Custom Tests Summary:{Colors.NC}")
        print(f"Passed: {suite_passed}, Failed: {suite_failed}, Ignored: {suite_ignored}")
        
        self.passed += suite_passed
        self.failed += suite_failed
        self.skipped += suite_ignored
        self.custom_passed = (suite_failed == 0)
        
        return suite_failed == 0
    
    def run_all_suites(self, skip_validation: bool = False, skip_generated: bool = False, 
                      skip_custom: bool = False, operation_filter: str = None, test_filter: str = None):
        """Run all test suites in order: validation, generated, custom"""
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"CLI Test Suite Runner - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        
        all_passed = True
        
        # 1. Run validation tests
        if not skip_validation:
            validation_result = self.run_validation_tests()
            if not validation_result:
                all_passed = False
                if self.stop_on_fail:
                    print(f"{Colors.YELLOW}\nStopping test execution (--stop-on-fail){Colors.NC}")
                    self.print_overall_summary()
                    return
        
        # 2. Run generated tests
        if not skip_generated:
            generated_result = self.run_generated_tests(operation_filter)
            if not generated_result:
                all_passed = False
                if self.stop_on_fail:
                    print(f"{Colors.YELLOW}\nStopping test execution (--stop-on-fail){Colors.NC}")
                    self.print_overall_summary()
                    return
        
        # 3. Run custom tests
        if not skip_custom:
            custom_result = self.run_custom_tests(test_filter)
            if not custom_result:
                all_passed = False
        
        self.print_overall_summary()
        
        # Export JSON if requested
        if self.json_output:
            self.export_json_results()
    
    def export_json_results(self):
        """Export test results to individual JSON files in the requested format"""
        if not self.test_results:
            print(f"{Colors.YELLOW}No test results to export{Colors.NC}")
            return
        
        # Determine output directory
        output_path = Path(self.json_output)
        
        # If it's a file path (not ending with /), use its parent directory
        # If it's a directory path, use it directly
        if output_path.suffix == '.json':
            # It's a file path, use parent directory
            output_dir = output_path.parent
            # Create directory if it doesn't exist
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            # It's a directory path
            output_dir = output_path
            output_dir.mkdir(parents=True, exist_ok=True)
        
        # Clean up old JSON files in the directory
        if output_dir.exists():
            json_files = list(output_dir.glob('*.json'))
            if json_files:
                removed_count = 0
                for json_file in json_files:
                    try:
                        json_file.unlink()
                        removed_count += 1
                    except Exception as e:
                        if self.verbose:
                            print(f"{Colors.YELLOW}Warning: Could not remove {json_file}: {str(e)}{Colors.NC}")
                if removed_count > 0:
                    print(f"{Colors.CYAN}Removed {removed_count} previous JSON file(s) from {output_dir}{Colors.NC}")
        
        exported_count = 0
        
        try:
            # Export each test result to its own file
            for test_result in self.test_results:
                # Convert to JSON format
                json_result = convert_test_result_to_json_format(
                    test_result,
                    self.external_test_report_link
                )
                
                # Generate safe filename from test name
                test_name = test_result.get(DictKeys.NAME, Defaults.UNKNOWN)
                # Replace invalid filename characters
                safe_name = re.sub(r'[<>:"/\\|?*]', '_', test_name)
                safe_name = re.sub(r'\s+', '_', safe_name)
                safe_name = safe_name[:200]  # Limit length
                
                # Create filename
                filename = f"{safe_name}.json"
                file_path = output_dir / filename
                
                # Handle duplicate filenames
                counter = 1
                while file_path.exists():
                    filename = f"{safe_name}_{counter}.json"
                    file_path = output_dir / filename
                    counter += 1
                
                # Write individual JSON file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(json_result, f, indent=2, ensure_ascii=False)
                
                # Store mapping for S3 upload
                suite_name = test_result.get(DictKeys.SUITE_NAME, SuiteName.UNKNOWN)
                self.test_file_mapping[str(file_path)] = {
                    DictKeys.TEST_RESULT: test_result,
                    DictKeys.SUITE_NAME: suite_name
                }
                
                exported_count += 1
            
            print(f"\n{Colors.GREEN}✓ Exported {exported_count} test result(s) to individual JSON files in {output_dir}{Colors.NC}")
            
            # Upload to S3 if configured
            if self.s3_config:
                self.upload_to_s3()
        except Exception as e:
            print(f"{Colors.RED}Error exporting JSON results: {str(e)}{Colors.NC}")
    
    def upload_to_s3(self):
        """Upload test result JSON files to S3"""
        if not self.test_file_mapping:
            print(f"{Colors.YELLOW}No files to upload to S3{Colors.NC}")
            return
        
        try:
            import boto3
            from botocore.exceptions import ClientError, NoCredentialsError
        except ImportError:
            print(f"{Colors.RED}Error: boto3 is required for S3 upload. Install with: pip install boto3{Colors.NC}")
            return
        
        s3_config = self.s3_config
        region = s3_config.get('region', 'eu-central-1')
        bucket = s3_config.get('bucket', 'external-test-results')
        test_framework_repo_name = s3_config.get('testFrameworkRepoName', '')
        catomatic_cycle = s3_config.get('catomaticCycle', '')
        catomatic_run_id = s3_config.get('catomaticRunId', '')
        catomatic_suite_name = s3_config.get('catomaticSuiteName', '')
        catomatic_timestamp = s3_config.get('catomaticTimestamp', '')
        
        # Generate timestamp if not provided
        if not catomatic_timestamp:
            catomatic_timestamp = int(time.time() * 1000)  # milliseconds
        else:
            # Convert to int if provided as string
            try:
                catomatic_timestamp = int(catomatic_timestamp)
            except (ValueError, TypeError):
                if self.verbose:
                    print(f"{Colors.YELLOW}Warning: Invalid timestamp format, generating new timestamp{Colors.NC}")
                catomatic_timestamp = int(time.time() * 1000)
        
        try:
            # Configure SSL verification (disabled by default)
            if not self.s3_verify_ssl:
                import urllib3
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                # Monkey patch botocore's URLLib3Session to disable SSL verification
                import botocore.httpsession
                original_init = botocore.httpsession.URLLib3Session.__init__
                
                def patched_init(self, *args, **kwargs):
                    kwargs['verify'] = False
                    return original_init(self, *args, **kwargs)
                
                botocore.httpsession.URLLib3Session.__init__ = patched_init
            
            # Create S3 client
            s3_client = boto3.client('s3', region_name=region)
            
            uploaded_count = 0
            failed_count = 0
            
            for file_path_str, mapping in self.test_file_mapping.items():
                file_path = Path(file_path_str)
                # Use provided suite name or fall back to detected suite name
                suite_name = catomatic_suite_name if catomatic_suite_name else mapping[DictKeys.SUITE_NAME]
                test_result = mapping[DictKeys.TEST_RESULT]
                
                # Get test name from result
                test_name = test_result.get(DictKeys.NAME, Defaults.UNKNOWN)
                # Sanitize test name for S3 key
                safe_test_name = re.sub(r'[<>:"/\\|?*]', '_', test_name)
                safe_test_name = re.sub(r'\s+', '_', safe_test_name)
                safe_test_name = safe_test_name[:200]  # Limit length
                
                # Build S3 key path
                s3_key = f"{test_framework_repo_name}/{catomatic_cycle}/{catomatic_run_id}/{suite_name}/{safe_test_name}_{catomatic_timestamp}.json"
                
                try:
                    # Upload file to S3
                    s3_client.upload_file(
                        str(file_path),
                        bucket,
                        s3_key,
                        ExtraArgs={'ContentType': 'application/json'}
                    )
                    
                    if self.verbose:
                        print(f"{Colors.CYAN}  Uploaded: s3://{bucket}/{s3_key}{Colors.NC}")
                    uploaded_count += 1
                except Exception as e:
                    print(f"{Colors.RED}  Failed to upload {file_path.name}: {str(e)}{Colors.NC}")
                    failed_count += 1
            
            if uploaded_count > 0:
                print(f"\n{Colors.GREEN}✓ Uploaded {uploaded_count} file(s) to S3 bucket '{bucket}'{Colors.NC}")
            if failed_count > 0:
                print(f"{Colors.RED}✗ Failed to upload {failed_count} file(s){Colors.NC}")
                
        except NoCredentialsError:
            print(f"{Colors.RED}Error: AWS credentials not found. Please configure AWS credentials.{Colors.NC}")
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')
            print(f"{Colors.RED}Error uploading to S3 ({error_code}): {str(e)}{Colors.NC}")
        except Exception as e:
            print(f"{Colors.RED}Error uploading to S3: {str(e)}{Colors.NC}")
    
    def print_overall_summary(self):
        """Print overall test summary"""
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        print("Overall Test Summary")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        
        print(f"\nTotal Payload Tests:")
        print(f"{Colors.GREEN if self.passed else Colors.NC}Passed:  {self.passed}{Colors.NC}")
        print(f"{Colors.RED if self.failed else Colors.NC}Failed:  {self.failed}{Colors.NC}")
        print(f"{Colors.YELLOW if self.skipped else Colors.NC}Skipped: {self.skipped}{Colors.NC}")
        
        print(f"\nSuite Status:")
        if hasattr(self, 'validation_passed'):
            status = "✓ PASSED" if self.validation_passed else "✗ FAILED"
            color = Colors.GREEN if self.validation_passed else Colors.RED
            print(f"{color}  Validation Tests: {status}{Colors.NC}")
        
        if hasattr(self, 'generated_passed'):
            status = "✓ PASSED" if self.generated_passed else "✗ FAILED"
            color = Colors.GREEN if self.generated_passed else Colors.RED
            print(f"{color}  Generated Tests:  {status}{Colors.NC}")
        
        if hasattr(self, 'custom_passed'):
            status = "✓ PASSED" if self.custom_passed else "✗ FAILED"
            color = Colors.GREEN if self.custom_passed else Colors.RED
            print(f"{color}  Custom Tests:     {status}{Colors.NC}")
        
        all_passed = (self.failed == 0 and 
                     getattr(self, 'validation_passed', True) and
                     getattr(self, 'generated_passed', True) and
                     getattr(self, 'custom_passed', True))
        
        if all_passed:
            print(f"\n{Colors.GREEN}✓ All tests passed!{Colors.NC}")
        else:
            print(f"\n{Colors.RED}✗ Some tests failed{Colors.NC}")


# Import pytest test classes for validation tests
try:
    import pytest
    
    # Test classes from old run_validation_tests.py
    MODELS_DIR = PROJECT_ROOT / "models"
    QUERY_PAYLOADS_DIR = PROJECT_ROOT / "queryPayloads"
    
    class TestCLIStructure:
        """Test the overall CLI structure and parsing"""
        
        def test_cli_entry_point_exists(self):
            """Test that catocli entry point exists"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "--version"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT)
            )
            assert result.returncode == 0, f"CLI entry point failed: {result.stderr}"
            assert len(result.stdout.strip()) > 0, "Version output should not be empty"
        
        def test_cli_help_available(self):
            """Test that CLI help text is available"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "-h"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT)
            )
            assert result.returncode == 0, f"Help command failed: {result.stderr}"
            assert "usage:" in result.stdout.lower()
        
        def test_query_subcommand_exists(self):
            """Test that query subcommand exists"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "query", "-h"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT)
            )
            assert result.returncode == 0, f"Query subcommand failed: {result.stderr}"
            assert "query" in result.stdout.lower()
        
        def test_mutation_subcommand_exists(self):
            """Test that mutation subcommand exists"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "mutation", "-h"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT)
            )
            assert result.returncode == 0, f"Mutation subcommand failed: {result.stderr}"
            assert "mutation" in result.stdout.lower()
        
        def test_raw_subcommand_exists(self):
            """Test that raw subcommand exists"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "raw", "-h"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT)
            )
            assert result.returncode == 0, f"Raw subcommand failed: {result.stderr}"
        
        def test_configure_returns_zero_on_success(self):
            """Test that configure commands return exit code 0 on success"""
            # Test configure show (should succeed without errors)
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "configure", "show"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT),
                timeout=10
            )
            # Should either succeed (0) or fail gracefully with proper error message
            # But should not crash with exit code 1 after printing success message
            if "success" in result.stdout.lower() and result.returncode != 0:
                pytest.fail(f"Configure command printed success but returned code {result.returncode}")
    
    
    class TestModelFiles:
        """Test that all model files exist and are valid"""
        
        @pytest.fixture(scope="class")
        def model_files(self):
            """Get all model JSON files"""
            if not MODELS_DIR.exists():
                pytest.skip(f"Models directory not found: {MODELS_DIR}")
            return list(MODELS_DIR.glob("*.json"))
        
        def test_models_directory_exists(self):
            """Test that models directory exists"""
            assert MODELS_DIR.exists(), f"Models directory not found: {MODELS_DIR}"
        
        def test_model_files_exist(self, model_files):
            """Test that model files exist"""
            assert len(model_files) > 0, "No model files found"
        
        def test_all_models_valid_json(self, model_files):
            """Test that all model files contain valid JSON"""
            errors = []
            for model_file in model_files:
                try:
                    with open(model_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                except json.JSONDecodeError as e:
                    errors.append(f"{model_file.name}: {str(e)}")
                except Exception as e:
                    errors.append(f"{model_file.name}: Unexpected error: {str(e)}")
            
            if errors:
                pytest.fail(f"Invalid JSON in model files:\n" + "\n".join(errors))
        
        def test_models_have_required_fields(self, model_files):
            """Test that model files have required fields"""
            required_fields = ["name", "type"]
            errors = []
            special_cases = {"query.siteLocation.json"}
            
            for model_file in model_files:
                if model_file.name in special_cases:
                    continue
                    
                try:
                    with open(model_file, 'r', encoding='utf-8') as f:
                        model_data = json.load(f)
                        
                    missing_fields = [field for field in required_fields 
                                    if field not in model_data]
                    if missing_fields:
                        errors.append(f"{model_file.name}: Missing fields {missing_fields}")
                except Exception as e:
                    errors.append(f"{model_file.name}: Error loading: {str(e)}")
            
            if errors:
                pytest.fail(f"Model validation errors:\n" + "\n".join(errors))
    
    
    class TestQueryPayloads:
        """Test that all query payload files exist and are valid"""
        
        @pytest.fixture(scope="class")
        def payload_files(self):
            """Get all query payload JSON files"""
            if not QUERY_PAYLOADS_DIR.exists():
                pytest.skip(f"Query payloads directory not found: {QUERY_PAYLOADS_DIR}")
            return list(QUERY_PAYLOADS_DIR.glob("*.json"))
        
        def test_payloads_directory_exists(self):
            """Test that query payloads directory exists"""
            assert QUERY_PAYLOADS_DIR.exists(), \
                f"Query payloads directory not found: {QUERY_PAYLOADS_DIR}"
        
        def test_payload_files_exist(self, payload_files):
            """Test that payload files exist"""
            assert len(payload_files) > 0, "No payload files found"
        
        def test_all_payloads_valid_json(self, payload_files):
            """Test that all payload files contain valid JSON"""
            errors = []
            for payload_file in payload_files:
                try:
                    with open(payload_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                except json.JSONDecodeError as e:
                    errors.append(f"{payload_file.name}: {str(e)}")
                except Exception as e:
                    errors.append(f"{payload_file.name}: Unexpected error: {str(e)}")
            
            if errors:
                pytest.fail(f"Invalid JSON in payload files:\n" + "\n".join(errors))
        
        def test_payloads_have_required_fields(self, payload_files):
            """Test that payload files have required GraphQL fields"""
            required_fields = ["query", "variables", "operationName"]
            errors = []
            
            for payload_file in payload_files:
                try:
                    with open(payload_file, 'r', encoding='utf-8') as f:
                        payload_data = json.load(f)
                        
                    missing_fields = [field for field in required_fields 
                                    if field not in payload_data]
                    if missing_fields:
                        errors.append(f"{payload_file.name}: Missing fields {missing_fields}")
                        
                    if "query" in payload_data:
                        if not isinstance(payload_data["query"], str) or not payload_data["query"].strip():
                            errors.append(f"{payload_file.name}: 'query' must be a non-empty string")
                    
                    if "variables" in payload_data:
                        if not isinstance(payload_data["variables"], dict):
                            errors.append(f"{payload_file.name}: 'variables' must be a dictionary")
                except Exception as e:
                    errors.append(f"{payload_file.name}: Error loading: {str(e)}")
            
            if errors:
                pytest.fail(f"Payload validation errors:\n" + "\n".join(errors))
        
        def test_query_operations_match_models(self, payload_files):
            """Test that query operations have corresponding model files"""
            if not MODELS_DIR.exists():
                pytest.skip("Models directory not found")
            
            # Load parent operations from clisettings.json
            skip_operations = set()
            clisettings_file = PROJECT_ROOT / "catocli" / "clisettings.json"
            if clisettings_file.exists():
                try:
                    with open(clisettings_file, 'r', encoding='utf-8') as f:
                        clisettings = json.load(f)
                        # Get parent operations that don't have their own model files
                        parent_ops = clisettings.get('childOperationParent', {})
                        for parent in parent_ops.keys():
                            skip_operations.add(f"query.{parent}.json")
                except Exception:
                    pass
            
            errors = []
            
            for payload_file in payload_files:
                if payload_file.name in skip_operations:
                    continue
                    
                operation_name = payload_file.stem
                model_file = MODELS_DIR / f"{operation_name}.json"
                
                if not model_file.exists():
                    errors.append(f"No model file for payload: {payload_file.name}")
            
            if errors:
                pytest.fail(f"Missing model files:\n" + "\n".join(errors))
    
    
    class TestQueryOperations:
        """Test individual query operations"""
        
        @pytest.fixture(scope="class")
        def query_operations(self):
            """Get all query operation names"""
            if not QUERY_PAYLOADS_DIR.exists():
                pytest.skip("Query payloads directory not found")
            
            operations = []
            for payload_file in QUERY_PAYLOADS_DIR.glob("query.*.json"):
                parts = payload_file.stem.split('.')
                if len(parts) >= 2:
                    operation = ' '.join(parts[1:])
                    operations.append((payload_file.stem, operation))
            return operations
        
        def test_query_operations_have_help(self, query_operations):
            """Test that all query operations have help text"""
            if not query_operations:
                pytest.skip("No query operations found")
            
            errors = []
            for operation_name, operation_cmd in query_operations:
                cmd = [PYTHON_CMD, "-m", "catocli", "query"] + operation_cmd.split() + ["-h"]
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd=str(PROJECT_ROOT),
                    timeout=10
                )
                
                if result.returncode != 0:
                    errors.append(f"{operation_name}: Help command failed")
            
            if errors and len(errors) > 10:
                pytest.fail(f"{len(errors)} query operations with help issues")
    
    
    class TestMutationOperations:
        """Test individual mutation operations"""
        
        @pytest.fixture(scope="class")
        def mutation_operations(self):
            """Get all mutation operation names"""
            if not QUERY_PAYLOADS_DIR.exists():
                pytest.skip("Query payloads directory not found")
            
            operations = []
            for payload_file in QUERY_PAYLOADS_DIR.glob("mutation.*.json"):
                parts = payload_file.stem.split('.')
                if len(parts) >= 2:
                    operation = ' '.join(parts[1:])
                    operations.append((payload_file.stem, operation))
            return operations
        
        def test_mutation_operations_have_help(self, mutation_operations):
            """Test that all mutation operations have help text"""
            if not mutation_operations:
                pytest.skip("No mutation operations found")
            
            errors = []
            for operation_name, operation_cmd in mutation_operations:
                cmd = [PYTHON_CMD, "-m", "catocli", "mutation"] + operation_cmd.split() + ["-h"]
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd=str(PROJECT_ROOT),
                    timeout=10
                )
                
                if result.returncode != 0:
                    errors.append(f"{operation_name}: Help command failed")
            
            if errors and len(errors) > 10:
                pytest.fail(f"{len(errors)} mutation operations with help issues")
    
    
    class TestDataIntegrity:
        """Test data integrity between models and payloads"""
        
        def test_payload_variables_match_model_args(self):
            """Test that payload variables align with model operationArgs"""
            if not MODELS_DIR.exists() or not QUERY_PAYLOADS_DIR.exists():
                pytest.skip("Required directories not found")
            
            errors = []
            for payload_file in list(QUERY_PAYLOADS_DIR.glob("*.json"))[:20]:
                operation_name = payload_file.stem
                model_file = MODELS_DIR / f"{operation_name}.json"
                
                if not model_file.exists():
                    continue
                
                try:
                    with open(payload_file, 'r', encoding='utf-8') as f:
                        payload_data = json.load(f)
                    
                    with open(model_file, 'r', encoding='utf-8') as f:
                        model_data = json.load(f)
                    
                    payload_vars = set(payload_data.get("variables", {}).keys())
                    model_args = set(model_data.get("operationArgs", {}).keys())
                    
                    extra_vars = payload_vars - model_args
                    if extra_vars:
                        errors.append(f"{operation_name}: Extra variables: {extra_vars}")
                except Exception:
                    pass
            
            if errors:
                pytest.fail(f"Data integrity issues:\n" + "\n".join(errors[:10]))
    
    
    class TestErrorHandling:
        """Test error handling for invalid inputs"""
        
        def test_invalid_json_handling(self):
            """Test that invalid JSON input is handled gracefully"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "query", "devices", "{invalid json}"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT),
                timeout=10
            )
            assert "error" in result.stderr.lower() or "error" in result.stdout.lower()
        
        def test_missing_required_args_handling(self):
            """Test that missing required arguments are handled"""
            result = subprocess.run(
                [PYTHON_CMD, "-m", "catocli", "query", "devices", "{}"],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_ROOT),
                timeout=10
            )
            assert result.returncode in [0, 1]
    
    
    class TestPackaging:
        """Test packaging and distribution files"""
        
        def test_manifest_includes_required_files(self):
            """Test that MANIFEST.in includes all required directories"""
            manifest_file = PROJECT_ROOT / "MANIFEST.in"
            
            if not manifest_file.exists():
                pytest.skip("MANIFEST.in not found")
            
            with open(manifest_file, 'r') as f:
                manifest_content = f.read()
            
            required_includes = ["models", "queryPayloads", "catocli/clisettings.json"]
            errors = []
            
            for required in required_includes:
                if required not in manifest_content:
                    errors.append(f"MANIFEST.in should include: {required}")
            
            if errors:
                pytest.fail("MANIFEST.in issues:\n" + "\n".join(errors))
        
        def test_setup_py_exists(self):
            """Test that setup.py exists"""
            setup_file = PROJECT_ROOT / "setup.py"
            assert setup_file.exists(), "setup.py not found"

except ImportError:
    # pytest not available, validation tests will be skipped
    pass


def main():
    parser = argparse.ArgumentParser(
        description='Run all CLI test suites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Test Suites (run in order):
  1. Validation Tests   - Pytest-based regression and validation tests
  2. Generated Tests    - Auto-generated from payloads_generated.json
  3. Custom Tests       - Custom tests from payloads_custom.json

Examples:
  # Run all test suites from current directory
  %(prog)s

  # Run tests from a specific test directory
  %(prog)s --dir /path/to/cato-cli/tests
  %(prog)s -d ~/projects/cato-cli/tests
  %(prog)s --dir ../other-branch/tests

  # Skip specific test suites
  %(prog)s --skip-validation
  %(prog)s --skip-generated --skip-custom

  # Filter tests by name/operation
  %(prog)s --operation appStats
  %(prog)s --test "custom test name"
  %(prog)s -o devices -v

  # Control output and execution
  %(prog)s --verbose
  %(prog)s --stop-on-fail
  %(prog)s -x -v

  # Export test results to individual JSON files (one per test)
  %(prog)s --json-output test_results/
  %(prog)s -j ./results --external-test-report-link https://example.com/report

  # Combine options
  %(prog)s --dir ../other-branch/tests --skip-validation --verbose
  %(prog)s -d ~/cato-cli/tests -o accountSnapshot -x
  %(prog)s -j test_results/ -v
        """
    )
    
    parser.add_argument(
        '--dir', '-d',
        type=Path,
        help='Specify the test files directory (default: current tests directory)',
        metavar='PATH'
    )
    parser.add_argument(
        '--skip-validation',
        action='store_true',
        help='Skip pytest validation tests'
    )
    parser.add_argument(
        '--skip-generated',
        action='store_true',
        help='Skip auto-generated tests'
    )
    parser.add_argument(
        '--skip-custom',
        action='store_true',
        help='Skip custom tests'
    )
    parser.add_argument(
        '--operation', '-o',
        help='Filter generated tests by operation name',
        metavar='NAME'
    )
    parser.add_argument(
        '--test', '-t',
        help='Filter custom tests by test name',
        metavar='NAME'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '--stop-on-fail', '-x',
        action='store_true',
        help='Stop on first failure'
    )
    parser.add_argument(
        '--json-output', '-j',
        type=str,
        help='Export test results to individual JSON files (path to output directory or file)',
        metavar='PATH'
    )
    parser.add_argument(
        '--external-test-report-link',
        type=str,
        help='External test report link to include in JSON output',
        metavar='URL'
    )
    parser.add_argument(
        '--s3-upload',
        action='store_true',
        help='Upload test results to S3'
    )
    parser.add_argument(
        '--s3-region',
        type=str,
        default='eu-central-1',
        help='AWS S3 region (default: eu-central-1)',
        metavar='REGION'
    )
    parser.add_argument(
        '--s3-bucket',
        type=str,
        default='external-test-results',
        help='AWS S3 bucket name (default: external-test-results)',
        metavar='BUCKET'
    )
    parser.add_argument(
        '--s3-test-framework-repo-name',
        type=str,
        help='Test framework repository name for S3 path',
        metavar='NAME'
    )
    parser.add_argument(
        '--s3-catomatic-cycle',
        type=str,
        help='Catomatic cycle name for S3 path',
        metavar='CYCLE'
    )
    parser.add_argument(
        '--s3-catomatic-run-id',
        type=str,
        help='Catomatic run ID for S3 path',
        metavar='ID'
    )
    parser.add_argument(
        '--s3-catomatic-suite-name',
        type=str,
        help='Catomatic suite name for S3 path (default: auto-detect from test type)',
        metavar='NAME'
    )
    parser.add_argument(
        '--s3-catomatic-timestamp',
        type=str,
        help='Catomatic timestamp in milliseconds (default: current timestamp)',
        metavar='TIMESTAMP'
    )
    parser.add_argument(
        '--s3-verify-ssl',
        action='store_true',
        help='Enable SSL certificate verification for S3 upload (disabled by default)'
    )
    
    args = parser.parse_args()
    
    # Set test directory if specified
    if args.dir:
        if not args.dir.exists():
            print(f"{Colors.RED}Error: Directory does not exist: {args.dir}{Colors.NC}")
            sys.exit(1)
        if not args.dir.is_dir():
            print(f"{Colors.RED}Error: Path is not a directory: {args.dir}{Colors.NC}")
            sys.exit(1)
        
        set_tests_directory(args.dir)
        
        if args.verbose:
            print(f"{Colors.CYAN}Using test directory: {TESTS_DIR}{Colors.NC}")
            print(f"{Colors.CYAN}Using project directory: {PROJECT_ROOT}{Colors.NC}")
    
    # Check if all suites are skipped
    if args.skip_validation and args.skip_generated and args.skip_custom:
        print("Error: All test suites are skipped. Nothing to run.")
        sys.exit(1)
    
    # Build S3 config if S3 upload is enabled
    s3_config = None
    if args.s3_upload:
        if not args.s3_test_framework_repo_name or not args.s3_catomatic_cycle or not args.s3_catomatic_run_id:
            print(f"{Colors.RED}Error: S3 upload requires --s3-test-framework-repo-name, --s3-catomatic-cycle, and --s3-catomatic-run-id{Colors.NC}")
            sys.exit(1)
        
        s3_config = {
            'region': args.s3_region,
            'bucket': args.s3_bucket,
            'testFrameworkRepoName': args.s3_test_framework_repo_name,
            'catomaticCycle': args.s3_catomatic_cycle,
            'catomaticRunId': args.s3_catomatic_run_id,
            'catomaticSuiteName': args.s3_catomatic_suite_name or '',
            'catomaticTimestamp': args.s3_catomatic_timestamp or ''
        }
    
    runner = AllTestsRunner(
        verbose=args.verbose,
        stop_on_fail=args.stop_on_fail,
        json_output=args.json_output,
        external_test_report_link=args.external_test_report_link,
        s3_config=s3_config,
        s3_verify_ssl=args.s3_verify_ssl
    )
    
    runner.run_all_suites(
        skip_validation=args.skip_validation,
        skip_generated=args.skip_generated,
        skip_custom=args.skip_custom,
        operation_filter=args.operation,
        test_filter=args.test
    )
    
    # Exit with failure if any tests failed
    failed = (runner.failed > 0 or 
             not getattr(runner, 'validation_passed', True) or
             not getattr(runner, 'generated_passed', True) or
             not getattr(runner, 'custom_passed', True))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()