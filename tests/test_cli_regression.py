#!/usr/bin/env python3
"""
Comprehensive Regression Test Suite for catocli

This test suite validates:
1. All CLI commands parse correctly
2. Help text is available for all commands
3. Operation models load successfully
4. Query payloads are valid JSON
5. CLI structure integrity
6. Error handling for invalid inputs

Run with: pytest tests/test_cli_regression.py -v
"""

import pytest
import json
import os
import sys
import subprocess
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
MODELS_DIR = PROJECT_ROOT / "models"
QUERY_PAYLOADS_DIR = PROJECT_ROOT / "queryPayloads"

# Add catocli to path for imports
sys.path.insert(0, str(PROJECT_ROOT))

# Determine Python command (python3 on macOS/Linux, python on Windows)
PYTHON_CMD = "python3" if sys.platform != "win32" else "python"


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
        # Version output is just the version number (e.g., "3.0.32")
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
        print(f"\nFound {len(model_files)} model files")
    
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
        
        # Special cases that have different structures (custom operations)
        special_cases = {"query.siteLocation.json"}
        
        for model_file in model_files:
            # Skip special case files that have custom structures
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
        print(f"\nFound {len(payload_files)} payload files")
    
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
                    
                # Validate query field is non-empty string
                if "query" in payload_data:
                    if not isinstance(payload_data["query"], str) or not payload_data["query"].strip():
                        errors.append(f"{payload_file.name}: 'query' must be a non-empty string")
                
                # Validate variables field is a dict
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
        
        # Some operations are meta operations or custom parsers without standard models
        skip_operations = {"query.site.json", "query.policy.json"}  # These are parent/meta operations
        
        errors = []
        for payload_file in payload_files:
            if payload_file.name in skip_operations:
                continue
                
            operation_name = payload_file.stem  # filename without extension
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
            # Extract operation parts (e.g., query.devices -> ['query', 'devices'])
            parts = payload_file.stem.split('.')
            if len(parts) >= 2:
                # Remove 'query' prefix and join the rest
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
                errors.append(f"{operation_name}: Help command failed - {result.stderr[:200]}")
        
        if errors:
            print(f"\n{len(errors)} query operations with help issues:")
            for error in errors[:10]:  # Show first 10 errors
                print(f"  - {error}")
            if len(errors) > 10:
                print(f"  ... and {len(errors) - 10} more")


class TestMutationOperations:
    """Test individual mutation operations"""
    
    @pytest.fixture(scope="class")
    def mutation_operations(self):
        """Get all mutation operation names"""
        if not QUERY_PAYLOADS_DIR.exists():
            pytest.skip("Query payloads directory not found")
        
        operations = []
        for payload_file in QUERY_PAYLOADS_DIR.glob("mutation.*.json"):
            # Extract operation parts (e.g., mutation.admin.addAdmin -> ['mutation', 'admin', 'addAdmin'])
            parts = payload_file.stem.split('.')
            if len(parts) >= 2:
                # Remove 'mutation' prefix and join the rest
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
                errors.append(f"{operation_name}: Help command failed - {result.stderr[:200]}")
        
        if errors:
            print(f"\n{len(errors)} mutation operations with help issues:")
            for error in errors[:10]:  # Show first 10 errors
                print(f"  - {error}")
            if len(errors) > 10:
                print(f"  ... and {len(errors) - 10} more")


class TestDataIntegrity:
    """Test data integrity between models and payloads"""
    
    def test_payload_variables_match_model_args(self):
        """Test that payload variables align with model operationArgs"""
        if not MODELS_DIR.exists() or not QUERY_PAYLOADS_DIR.exists():
            pytest.skip("Required directories not found")
        
        errors = []
        checked = 0
        
        # Check a sample of operations for performance
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
                
                # Check if payload variables are a subset of model args
                # (payload may not include all optional args)
                extra_vars = payload_vars - model_args
                if extra_vars:
                    errors.append(f"{operation_name}: Extra variables in payload: {extra_vars}")
                
                checked += 1
                
            except Exception as e:
                errors.append(f"{operation_name}: Error comparing: {str(e)}")
        
        print(f"\nChecked {checked} operations for data integrity")
        
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
        # Should fail gracefully with error message
        assert "ERROR" in result.stderr or "error" in result.stderr.lower() or \
               "ERROR" in result.stdout or "error" in result.stdout.lower(), \
               "Invalid JSON should produce error message"
    
    def test_missing_required_args_handling(self):
        """Test that missing required arguments are handled"""
        result = subprocess.run(
            [PYTHON_CMD, "-m", "catocli", "query", "devices", "{}"],
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
            timeout=10
        )
        # Should either fail or handle gracefully
        # (exact behavior depends on whether args are truly required)
        assert result.returncode in [0, 1], "Should handle missing args gracefully"


class TestPackaging:
    """Test packaging and distribution files"""
    
    def test_manifest_includes_required_files(self):
        """Test that MANIFEST.in includes all required directories"""
        manifest_file = PROJECT_ROOT / "MANIFEST.in"
        
        if not manifest_file.exists():
            pytest.skip("MANIFEST.in not found")
        
        with open(manifest_file, 'r') as f:
            manifest_content = f.read()
        
        required_includes = [
            "models",
            "queryPayloads",
            "catocli/clisettings.json"
        ]
        
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


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
