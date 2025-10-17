# CatoCLI Python Integration Guide - Unix/Linux/macOS

This guide demonstrates how to integrate CatoCLI with Python scripts on Unix-based systems (Linux, macOS) for automated network management and reporting tasks.

## Prerequisites

- Python 3.6 or higher
- CatoCLI installed (`pip3 install catocli`)
- Configured CatoCLI profile with valid credentials
- Unix-based operating system (Linux, macOS, etc.)

## Basic Python Integration

### Example 1: Account Management Automation

```python
import csv
import subprocess
import json
import os

def main():
    # Add a new Cato tenant
    parent_account_id = "12345"
    accountConfig = {
        "addAccountInput": {
            "name": "Demo-Customer",
            "description": "Demo Customer Account",
            "tenancy": "SINGLE_TENANT",
            "timezone": "America/New_York",
            "type": "CUSTOMER"
        }
    }
    addAccountCommand = "catocli mutation accountManagement addAccount -accountID="+parent_account_id+" '"+json.dumps(accountConfig)+"'"
    print(f"Adding tenant")
    result = exec_cli(addAccountCommand)
    print(result)
    new_account_id = result["data"]["accountManagement"]["addAccount"]["id"]
    admin_email = "youruser@yourcompany.com"

    addAdminConfig = {
        "addAdminInput": {
            "email": admin_email,
            "firstName": "Demo",
            "lastName": "Admin",
            "managedRoles": [
                {
                    "allowedEntities": [],
                    "role": {
                        "id": "1"
                    }
                }
            ],
            "passwordNeverExpires": True,
            "mfaEnabled": True,
            "resellerRoles": []
        }
    }
    addAdminCommand = "catocli mutation admin addAdmin -accountID="+new_account_id+" '"+json.dumps(addAdminConfig)+"'"
    print(f"Adding admin user: "+admin_email)
    result = exec_cli(addAdminCommand)
    print(result)
    print("\nnew_account_id: "+new_account_id)
    with open("account_config.txt", "w") as f:
        f.write('account_id = "'+new_account_id+'"')


## General purpose functions
def exec_cli(command):
    try:
        response = subprocess.run(command, shell=True, text=True, capture_output=True)
        result = json.loads(response.stdout)
    except Exception as e:
        print(f"Failed to execute command: {e}")
    return result

if __name__ == "__main__":
    main()
```

### Example 2: Simple Reporting Script

```python
import subprocess
import json

def main():
    account_id = "12345"
    query = {
        "timeFrame": "last.P1D",
        "labels": ["health", "bytesTotal", "lastMileLatency"]
    }
    
    command = "catocli query accountMetrics -accountID="+account_id+" '"+json.dumps(query)+"'"
    print("Getting account metrics")
    result = exec_cli(command)
    print(result)

def exec_cli(command):
    try:
        response = subprocess.run(command, shell=True, text=True, capture_output=True)
        result = json.loads(response.stdout)
    except Exception as e:
        print(f"Failed to execute command: {e}")
    return result

if __name__ == "__main__":
    main()
```

## Script Execution

### Making Scripts Executable

```bash
# Make the script executable
chmod +x catocli_automation.py

# Run the script
./catocli_automation.py
```

### Running with Python

```bash
# Run with Python 3
python3 catocli_automation.py

# Or with virtual environment
source venv/bin/activate
python catocli_automation.py
```

## Error Handling Best Practices

```python
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('catocli_automation.log'),
        logging.StreamHandler()
    ]
)

def safe_execute_command(command):
    """
    Safely execute CatoCLI command with proper error handling.
    """
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(
            command, 
            shell=True, 
            text=True, 
            capture_output=True, 
            check=True,
            timeout=300  # 5 minute timeout
        )
        logging.info("Command executed successfully")
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        logging.error("Command timed out")
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON response: {e}")
        raise
```

## Environment Variables

```python
import os

# Use environment variables for sensitive data
ACCOUNT_ID = os.getenv('CATO_ACCOUNT_ID')
ADMIN_EMAIL_DOMAIN = os.getenv('ADMIN_EMAIL_DOMAIN', 'yourcompany.com')

# Validate required environment variables
required_vars = ['CATO_ACCOUNT_ID']
for var in required_vars:
    if not os.getenv(var):
        print(f"❌ Required environment variable {var} is not set")
        sys.exit(1)
```

## Cron Integration

Create a cron job to run reports automatically:

```bash
# Edit crontab
crontab -e

# Add daily report generation at 6 AM
0 6 * * * /usr/bin/python3 /path/to/your/catocli_reporting.py

# Add weekly report on Sundays at 7 AM
0 7 * * 0 /usr/bin/python3 /path/to/your/weekly_report.py
```

## Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv catocli_env

# Activate virtual environment
source catocli_env/bin/activate

# Install dependencies
pip install catocli

# Create requirements file
pip freeze > requirements.txt

# Deactivate when done
deactivate
```

## Security Considerations

1. **Never hardcode credentials** in scripts
2. **Use environment variables** for sensitive data
3. **Set appropriate file permissions** (600 for scripts with sensitive data)
4. **Log activities** for audit trails
5. **Validate all inputs** before passing to CatoCLI
6. **Use subprocess safely** with proper error handling

## Troubleshooting

### Common Issues

1. **Command not found**: Ensure CatoCLI is in PATH
2. **Permission denied**: Check file permissions and execution rights
3. **JSON parsing errors**: Validate command output format
4. **Authentication failures**: Verify CatoCLI profile configuration

### Debug Mode

```python
import os

# Enable debug mode
os.environ['CATO_DEBUG'] = 'True'

# Add verbose output to commands
command = "catocli --debug query accountMetrics '{...}'"
```

This guide provides a foundation for integrating CatoCLI with Python on Unix systems. Adapt the examples to your specific use cases and always follow security best practices when handling credentials and sensitive data.