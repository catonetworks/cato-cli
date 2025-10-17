# CatoCLI Python Integration Guide - Windows

This guide demonstrates how to integrate CatoCLI with Python scripts on Windows systems for automated network management and reporting tasks.

## Prerequisites

- Python 3.6 or higher (from python.org or Microsoft Store)
- CatoCLI installed (`pip install catocli`)
- Configured CatoCLI profile with valid credentials
- Windows 10/11 or Windows Server 2016+

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
    addAccountCommand = "catocli mutation accountManagement addAccount -accountID="+parent_account_id+" '"+json.dumps(accountConfig).replace('"','\\\"')+"'"
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
    addAdminCommand = "catocli mutation admin addAdmin -accountID="+new_account_id+" '"+json.dumps(addAdminConfig).replace('"','\\\"')+"'"
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
        result = None
    return result

if __name__ == "__main__":
    main()
```

### Example 2: Simple Reporting Script

```python
import subprocess
import json

def main():
    query = {
        "timeFrame": "last.P1D",
        "labels": ["health", "bytesTotal", "lastMileLatency"]
    }
    
    command = 'catocli query accountMetrics "'+json.dumps(query).replace('"','\\\"')+'"'
    print("Getting account metrics")
    result = exec_cli(command)
    print(result)

def exec_cli(command):
    try:
        response = subprocess.run(command, shell=True, text=True, capture_output=True)
        result = json.loads(response.stdout)
    except Exception as e:
        print(f"Failed to execute command: {e}")
        result = None
    return result

if __name__ == "__main__":
    main()
```

## Windows-Specific Considerations

### PowerShell Integration

```python
def execute_catocli_powershell(command):
    """
    Execute CatoCLI command through PowerShell for better Windows compatibility.
    """
    powershell_command = f'powershell.exe -Command "{command}"'
    
    result = subprocess.run(
        powershell_command,
        shell=True,
        text=True,
        capture_output=True,
        check=True
    )
    
    return json.loads(result.stdout)
```

### Command Prompt Batch File

Create a `catocli_report.bat` file:

```batch
@echo off
echo Running CatoCLI Python Report...
python catocli_reporting.py
if %ERRORLEVEL% neq 0 (
    echo Script failed with error level %ERRORLEVEL%
    pause
    exit /b %ERRORLEVEL%
)
echo Report completed successfully
pause
```

## Script Execution Methods

### Method 1: Direct Python Execution

```cmd
# Run with Python
python catocli_automation.py

# Or with full path
C:\Python39\python.exe catocli_automation.py
```

### Method 2: PowerShell Execution

```powershell
# Run in PowerShell
python.exe .\catocli_automation.py

# Or with execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
python.exe .\catocli_automation.py
```

### Method 3: Task Scheduler Integration

```python
import winreg

def create_scheduled_task():
    """
    Example of creating a scheduled task programmatically.
    Note: Requires administrative privileges
    """
    script_path = os.path.abspath(__file__)
    python_exe = sys.executable
    
    command = f'schtasks /create /tn "CatoCLI Daily Report" /tr "{python_exe} {script_path}" /sc daily /st 06:00'
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Scheduled task created successfully")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create scheduled task: {e}")
```

## Error Handling for Windows

```python
import logging
import tempfile

# Setup Windows-compatible logging
log_dir = os.path.join(tempfile.gettempdir(), "catocli_logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'catocli_automation.log')),
        logging.StreamHandler()
    ]
)

def safe_execute_command_windows(command):
    """
    Safely execute CatoCLI command with Windows-specific error handling.
    """
    try:
        logging.info(f"Executing command: {command}")
        
        # Create a temporary batch file for complex commands
        with tempfile.NamedTemporaryFile(mode='w', suffix='.bat', delete=False) as bat_file:
            bat_file.write('@echo off\n')
            bat_file.write(f'{command}\n')
            bat_file_path = bat_file.name
        
        try:
            result = subprocess.run(
                bat_file_path,
                text=True,
                capture_output=True,
                check=True,
                timeout=300
            )
            logging.info("Command executed successfully")
            return json.loads(result.stdout)
        finally:
            # Clean up temporary file
            os.unlink(bat_file_path)
            
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

## Environment Variables (Windows)

```python
import os

# Windows environment variable handling
def setup_windows_environment():
    """Set up Windows-specific environment variables."""
    
    # Check for environment variables
    account_id = os.environ.get('CATO_ACCOUNT_ID')
    if not account_id:
        print("❌ CATO_ACCOUNT_ID environment variable not set")
        print("Set it using: set CATO_ACCOUNT_ID=your_account_id")
        sys.exit(1)
    
    # Set up paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "reports")
    os.makedirs(output_dir, exist_ok=True)
    
    return account_id, output_dir

# Set environment variables via script
def set_environment_variables():
    """Example of setting environment variables programmatically."""
    os.environ['CATO_ACCOUNT_ID'] = '12345'
    os.environ['CATO_OUTPUT_DIR'] = r'C:\Reports\Cato'
    
    # Optionally persist to Windows registry
    # Note: Requires appropriate permissions
```

## Windows Task Scheduler Setup

### Create Task via Command Line

```batch
@echo off
rem Create scheduled task for daily reports
schtasks /create ^
    /tn "CatoCLI Daily Report" ^
    /tr "python.exe C:\Scripts\catocli_reporting.py" ^
    /sc daily ^
    /st 06:00 ^
    /ru SYSTEM

rem Create task for weekly reports
schtasks /create ^
    /tn "CatoCLI Weekly Report" ^
    /tr "python.exe C:\Scripts\catocli_weekly.py" ^
    /sc weekly ^
    /d SUN ^
    /st 07:00 ^
    /ru SYSTEM
```

### PowerShell Task Creation

```powershell
# Create scheduled task using PowerShell
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "C:\Scripts\catocli_reporting.py"
$trigger = New-ScheduledTaskTrigger -Daily -At 6:00AM
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$task = New-ScheduledTask -Action $action -Trigger $trigger -Settings $settings
Register-ScheduledTask -TaskName "CatoCLI Daily Report" -InputObject $task
```

## Virtual Environment Setup (Windows)

```cmd
rem Create virtual environment
python -m venv catocli_env

rem Activate virtual environment
catocli_env\Scripts\activate

rem Install dependencies
pip install catocli

rem Create requirements file
pip freeze > requirements.txt

rem Deactivate when done
deactivate
```

## Security Considerations (Windows)

1. **File Permissions**: Use `icacls` to set appropriate permissions
2. **User Account Control**: Run with appropriate privileges
3. **Windows Defender**: Add exclusions if needed
4. **Registry Access**: Be careful with registry modifications

```batch
rem Set file permissions
icacls "catocli_automation.py" /grant:r "Users:(R)"
icacls "catocli_automation.py" /grant:r "Administrators:(F)"

rem Remove inheritance and set specific permissions
icacls "config.txt" /inheritance:r /grant:r "Administrators:(F)"
```

## Troubleshooting Windows Issues

### Common Windows-Specific Problems

1. **Path Issues**: Use `os.path.join()` for cross-platform paths
2. **Encoding Issues**: Specify `encoding='utf-8'` when opening files
3. **Permission Errors**: Run as administrator when needed
4. **PowerShell Execution Policy**: Adjust execution policy settings

### Debug Commands

```python
import platform

def debug_environment():
    """Print debug information about the Windows environment."""
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Current directory: {os.getcwd()}")
    print(f"PATH: {os.environ.get('PATH', 'Not set')}")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    
    # Check if catocli is available
    try:
        result = subprocess.run("catocli --version", shell=True, capture_output=True, text=True)
        print(f"CatoCLI version: {result.stdout.strip()}")
    except Exception as e:
        print(f"CatoCLI not found: {e}")
```

## Windows Service Integration

```python
import win32service
import win32serviceutil
import win32event

class CatoCLIService(win32serviceutil.ServiceFramework):
    """Windows Service for CatoCLI automation."""
    
    _svc_name_ = "CatoCLIService"
    _svc_display_name_ = "Cato Networks CLI Automation Service"
    _svc_description_ = "Automated Cato Networks reporting and management"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        
    def SvcDoRun(self):
        # Your service logic here
        self.main_service_loop()
        
    def main_service_loop(self):
        # Implement your automation logic
        pass

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(CatoCLIService)
```

This Windows guide provides comprehensive examples for integrating CatoCLI with Python on Windows systems, including Windows-specific considerations, task scheduling, and troubleshooting guidance.