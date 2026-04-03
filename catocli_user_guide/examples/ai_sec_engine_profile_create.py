#!/usr/bin/env python3
"""
AI Security Engine Profile Creation Script

This script demonstrates how to create an AI Security Engine Profile
using catocli private commands with Python integration.

Prerequisites:
- catocli installed with private commands configured
- ~/.cato/settings.json with privateCommands configured
- ~/.cato/credentials with cookie and private_endpoint set for your profile

Usage:
    python3 ai_sec_engine_profile_create.py
"""

import subprocess
import json
import tempfile
import os


def main():
    # Define the AI Security Engine Profile configuration
    profile_config = {
        "name": "Kitchen Sink Engine Profile Test",
        "description": "test",
        "detectors_config": {
            "type": "logical_operand",
            "logical_operand": "or",
            "children": [
                {
                    "type": "detector",
                    "detector": "regex",
                    "config": {
                        "type": "regex",
                        "regex": "test regex",
                        "custom_metadata": {
                            "id": "74d8e0aa-db01-4a46-8f96-5eb3dde13a13",
                            "detection_name": "test custom detector"
                        }
                    }
                },
                {
                    "type": "detector",
                    "detector": "general_personal_information_address",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "general_personal_information_name",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "general_personal_information_phone_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "general_personal_information_email",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "financial_information_credit_card_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "financial_information_iban",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "financial_information_bank_account_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "financial_information_swift",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_driver_id",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_vehicle_identification_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_passport_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_ssn",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_us_individual_tax_identification_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_vat_id_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "identification_numbers_health_id_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "financial_information_crypto_address",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "personal_health_information_medical_record_number",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "personal_health_information_health_plan_beneficiary",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "technical_information_secret",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "technical_information_ip_address",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "technical_information_mac_address",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "technical_information_url",
                    "config": {"type": "excludable"}
                },
                {
                    "type": "detector",
                    "detector": "topic_code_sharing",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "financial_decisions",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "employment_decisions",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "recruitment_and_selection",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "medical_advice",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "confidential_medical_information",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "confidential_finance_information",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "salary_appearance",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "salary_fetching",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "security_controls_jailbreak",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "security_controls_obfuscation_attack",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "safety_controls_safety",
                    "config": {"type": "simple"}
                },
                {
                    "type": "detector",
                    "detector": "language",
                    "config": {
                        "type": "language",
                        "english_allowed": True
                    }
                }
            ]
        }
    }

    print("Creating AI Security Engine Profile...")
    result = exec_cli_private("aiSecEngineProfileCreate", profile_config)

    if result:
        print("Profile created successfully!")
        print(json.dumps(result, indent=2))
    else:
        print("Failed to create profile")


def exec_cli_private(command_name, payload):
    """
    Execute a catocli private command using --json-file for complex payloads.

    Using --json-file avoids shell parsing issues with complex nested JSON.
    """
    try:
        # Write payload to a temporary file to avoid shell parsing issues
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(payload, f, indent=2)
            temp_file = f.name

        try:
            command = f"catocli private {command_name} --json-file {temp_file}"
            print(f"Executing: catocli private {command_name}")

            response = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True,
                timeout=300  # 5 minute timeout
            )

            if response.returncode != 0:
                print(f"Command failed with error: {response.stderr}")
                return None

            result = json.loads(response.stdout)
            return result

        finally:
            # Clean up temporary file
            os.unlink(temp_file)

    except subprocess.TimeoutExpired:
        print("Command timed out")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")
        print(f"Raw output: {response.stdout}")
        return None
    except Exception as e:
        print(f"Failed to execute command: {e}")
        return None


def exec_cli(command):
    """
    Execute a standard catocli command (for non-private commands).
    """
    try:
        response = subprocess.run(command, shell=True, text=True, capture_output=True)
        result = json.loads(response.stdout)
    except Exception as e:
        print(f"Failed to execute command: {e}")
        result = None
    return result


if __name__ == "__main__":
    main()
