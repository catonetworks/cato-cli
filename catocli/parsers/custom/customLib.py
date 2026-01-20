import os
import json
import subprocess
import glob
import time
from pathlib import Path
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
from ..customParserApiClient import validateArgs

def entityTypeList(args, configuration):
    params = vars(args)
    operation = { 
        "operationArgs": {
            "accountID": {
                "name": "accountID",
                "required": True,
            }
        }
    }
    # Use accountID from configuration (profile) or fall back to command line parameter
    account_id = configuration.accountID if configuration and hasattr(configuration, 'accountID') else (params.get("accountID") or params.get("accountId"))
    variablesObj = { "accountID": account_id }

    # Create the API client instance
    api_client = ApiClient(configuration)

    # Show masked API key in verbose mode (without affecting actual API calls)
    if hasattr(args, 'verbose') and args.verbose and 'x-api-key' in api_client.configuration.api_key:
        print(f"API Key (masked): ***MASKED***")

    # Create the API instance
    instance = CallApi(api_client)
    operationName = params["operation_name"]
    query = '''query entityLookup ( $type:EntityType! $accountID:ID! $search:String ) {
        entityLookup ( accountID:$accountID type:$type search:$search ) {
            '''+params["operation_name"]+'''s: items {
                description
                '''+params["operation_name"]+''': entity {
                    id
                    name
                    type
                }
            }
        }
    }'''
    body = {
        "query": query,
        "operationName": "entityLookup",
        "variables": {
            "accountID": configuration.accountID,
            "type": params["operation_name"],
            "search": (params.get("s") if params.get("s")!=None else "")
        }
    }
    
    isOk, invalidVars, message = validateArgs(variablesObj,operation)
    if isOk==True:        
        if params["t"]==True:
            if params["p"]==True:
                print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
            else:
                print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
            return None
        else:
            try:
                response = instance.call_api(body,params)
                if params["v"]==True:
                    print(json.dumps(response[0]))
                elif params["f"]=="json":
                    if params["p"]==True:
                        print(json.dumps(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"),indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
                    else:
                        print(json.dumps(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s")))
                else:
                    if len(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"))==0:
                        print("No results found")
                    else:
                        print("id,name,type,description")
                        for site in response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"):
                            print(site.get(params["operation_name"]).get('id')+","+site.get(params["operation_name"]).get('name')+","+site.get(params["operation_name"]).get('type')+","+site.get('description'))
            except ApiException as e:
                return e
    else:
        print("ERROR: "+message,", ".join(invalidVars))


def makeCall(args, configuration, query):
    # Create API client instance with params
    instance = CallApi(ApiClient(configuration))
    params = {
        'v': hasattr(args, 'verbose') and args.verbose,  # verbose mode
        'f': 'json',  # format
        'p': False,  # pretty print
        't': False   # test mode
    }

    # Retry configuration: attempt 1 (immediate), attempt 2 (after 15s), attempt 3 (after 30s)
    max_attempts = 3
    retry_delays = [0, 15, 30]  # seconds to wait before each attempt

    last_exception = None

    for attempt in range(max_attempts):
        try:
            # Wait before retry (skip on first attempt)
            if attempt > 0:
                delay = retry_delays[attempt]
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Retrying API call in {delay} seconds (attempt {attempt + 1}/{max_attempts})...")
                time.sleep(delay)

            # Call the API directly
            # NOTE: The API client (graphql_client/api_client_types.py lines 106-108)
            # automatically prints error responses and exits on GraphQL errors.
            # This means our custom error handling below may not be reached if there are GraphQL errors.
            response = instance.call_api(query, params)
            response = response[0] if response else {}

            # Show raw API response in verbose mode
            if hasattr(args, 'verbose') and args.verbose:
                print("\n" + "=" * 80)
                print("RAW API RESPONSE:")
                print("=" * 80)
                print(json.dumps(response, indent=2))
                print("=" * 80 + "\n")

            # Check for GraphQL errors first (may not be reached due to API client behavior)
            if 'errors' in response:
                error_messages = [error.get('message', 'Unknown error') for error in response['errors']]
                raise Exception(f"API returned errors: {', '.join(error_messages)}")

            if not response or 'data' not in response:
                raise ValueError("Failed to retrieve data from API")

            # Success - return the response
            if attempt > 0 and hasattr(args, 'verbose') and args.verbose:
                print(f"API call succeeded on attempt {attempt + 1}")
            return response

        except ApiException as e:
            last_exception = e
            error_msg = str(e)

            # Check if it's a timeout, 502/503, or rate limit error that should be retried
            is_retryable = (
                '502 Bad Gateway' in error_msg or
                '503 Service Unavailable' in error_msg or
                'timeout' in error_msg.lower() or
                'timed out' in error_msg.lower() or
                'rate limit' in error_msg.lower()
            )

            if is_retryable and attempt < max_attempts - 1:
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"API call failed with retryable error (attempt {attempt + 1}/{max_attempts}): {error_msg}")
                continue  # Retry
            else:
                # Non-retryable error or final attempt
                raise Exception(f"API call failed - {e}")

        except Exception as e:
            last_exception = e
            error_msg = str(e)
            
            # Check if it's a rate limit error that should be retried
            is_retryable = 'rate limit' in error_msg.lower()
            
            if is_retryable and attempt < max_attempts - 1:
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"API call failed with retryable error (attempt {attempt + 1}/{max_attempts}): {error_msg}")
                continue  # Retry
            else:
                # Non-retryable error or final attempt
                raise Exception(f"Unexpected error during API call - {e}")

    # If we exhausted all retries
    raise Exception(f"API call failed after {max_attempts} attempts - {last_exception}")

def writeDataToFile(data, args, account_id=None, default_filename_template="data_{account_id}.json", default_directory="config_data"):
    """
    Write data to a file with flexible output path configuration
    
    Args:
        data: The data to write to file (will be JSON serialized)
        args: Command line arguments containing output_file_path, output_directory and verbose options
        account_id: Optional account ID for default filename generation
        default_filename_template: Template for default filename (use {account_id} placeholder)
        default_directory: Default directory for output files
        
    Returns:
        str: The path of the file that was written
        
    Raises:
        Exception: If file writing fails
    """
    # Set up output file path
    if hasattr(args, 'output_file_path') and args.output_file_path:
        output_file = args.output_file_path
        destination_dir = os.path.dirname(output_file)
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Using output file path: {output_file}")
    else:
        # Use output_directory from args if provided, otherwise use default_directory
        if hasattr(args, 'output_directory') and args.output_directory:
            destination_dir = args.output_directory
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Using custom output directory: {destination_dir}")
        else:
            destination_dir = default_directory
        
        if account_id:
            filename = default_filename_template.format(account_id=account_id)
        else:
            # If no account_id provided, remove the placeholder
            filename = default_filename_template.replace("_{account_id}", "")
        output_file = os.path.join(destination_dir, filename)
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Using default path: {output_file}")
    
    # Create destination directory if it doesn't exist
    if destination_dir and not os.path.exists(destination_dir):
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Creating directory: {destination_dir}")
        os.makedirs(destination_dir)

    try:
        # Write the data to the file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Successfully wrote data to: {output_file}")
            
        return output_file
        
    except Exception as e:
        raise Exception(f"Failed to write data to file {output_file}: {str(e)}")

def getAccountID(args, configuration):
    """
    Get the account ID from command line arguments, configuration, or environment variable.
    
    Args:
        args: Command line arguments
        configuration: API configuration object
        
    Returns:
        str: The account ID to use for API calls
        
    Raises:
        ValueError: If no account ID is provided or found
    """
    account_id = None
    if hasattr(args, 'accountID') and args.accountID:
        account_id = args.accountID
    elif hasattr(configuration, 'accountID') and configuration.accountID:
        account_id = configuration.accountID
    else:
        account_id = os.getenv('CATO_ACCOUNT_ID')
    
    if not account_id:
        raise ValueError("Account ID is required. Provide it using the -accountID flag or set CATO_ACCOUNT_ID environment variable.")
    
    return account_id

def check_terraform_binary():
    """Check if terraform binary is available"""
    try:
        result = subprocess.run(['terraform', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip().split('\n')[0]
        else:
            return False, "Terraform binary not found or not working"
    except FileNotFoundError:
        return False, "Terraform binary not found in PATH"
    except Exception as e:
        return False, f"Error checking terraform binary: {e}"


def check_terraform_config_files():
    """Check if Terraform configuration files exist in current directory"""
    tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
    if tf_files:
        return True, tf_files
    else:
        return False, []


def check_terraform_init():
    """Check if Terraform has been initialized"""
    terraform_dir = Path('.terraform')
    if terraform_dir.exists() and terraform_dir.is_dir():
        # Check for providers
        providers_dir = terraform_dir / 'providers'
        if providers_dir.exists():
            return True, "Terraform is initialized"
        else:
            return False, "Terraform directory exists but no providers found"
    else:
        return False, "Terraform not initialized (.terraform directory not found)"


def check_module_exists(module_name):
    """Check if the specified module exists in Terraform configuration"""
    try:
        # Remove 'module.' prefix if present
        clean_module_name = module_name.replace('module.', '')
        
        # Method 1: Check .tf files directly for module definitions
        tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
        for tf_file in tf_files:
            try:
                with open(tf_file, 'r') as f:
                    content = f.read()
                    # Look for module "module_name" blocks
                    if f'module "{clean_module_name}"' in content or f"module '{clean_module_name}'" in content:
                        return True, f"Module '{clean_module_name}' found in {tf_file}"
            except Exception as e:
                print(f"Warning: Could not read {tf_file}: {e}")
                continue
        
        # Method 2: Try terraform show -json as fallback
        try:
            result = subprocess.run(
                ['terraform', 'show', '-json'],
                capture_output=True,
                text=True,
                cwd=Path.cwd()
            )
            
            if result.returncode == 0:
                state_data = json.loads(result.stdout)
                
                # Check if module exists in configuration
                if 'configuration' in state_data and state_data['configuration']:
                    modules = state_data.get('configuration', {}).get('root_module', {}).get('module_calls', {})
                    if clean_module_name in modules:
                        return True, f"Module '{clean_module_name}' found in Terraform state"
                
                # Also check in planned_values for modules
                if 'planned_values' in state_data and state_data['planned_values']:
                    modules = state_data.get('planned_values', {}).get('root_module', {}).get('child_modules', [])
                    for module in modules:
                        module_addr = module.get('address', '')
                        if clean_module_name in module_addr:
                            return True, f"Module '{clean_module_name}' found in planned values"
        except (subprocess.SubprocessError, json.JSONDecodeError) as e:
            print(f"Warning: Could not check terraform state: {e}")
        
        return False, f"Module '{clean_module_name}' not found in Terraform configuration files"
            
    except Exception as e:
        return False, f"Error checking module existence: {e}"


def validate_terraform_environment(module_name, verbose=False):
    """Validate the complete Terraform environment"""
    print("\n Validating Terraform environment...")
    
    # 1. Check terraform binary
    print("\n Checking Terraform binary...")
    has_terraform, terraform_msg = check_terraform_binary()
    if not has_terraform:
        raise Exception(f" Terraform not available: {terraform_msg}")
    if verbose:
        print(f" {terraform_msg}")
    else:
        print(" Terraform binary found")
    
    # 2. Check for configuration files
    print("\n Checking Terraform configuration files...")
    has_config, config_files = check_terraform_config_files()
    if not has_config:
        raise Exception(" No Terraform configuration files (.tf or .tf.json) found in current directory")
    if verbose:
        print(f" Found {len(config_files)} configuration files: {', '.join(config_files)}")
    else:
        print(f" Found {len(config_files)} Terraform configuration files")
    
    # 3. Check if terraform is initialized
    print("\n Checking Terraform initialization...")
    is_initialized, init_msg = check_terraform_init()
    if not is_initialized:
        raise Exception(f" {init_msg}. Run 'terraform init' first.")
    if verbose:
        print(f" {init_msg}")
    else:
        print(" Terraform is initialized")
    
    # 4. Check if the specified module exists
    print(f"\n Checking if module '{module_name}' exists...")
    module_exists, module_msg = check_module_exists(module_name)
    if not module_exists:
        raise Exception(f" {module_msg}. Please add the module to your Terraform configuration first.")
    if verbose:
        print(f" {module_msg}")
    else:
        print(f" Module '{module_name}' found")
    
    # 5. Check if modules are properly installed by running terraform validate
    print("\n Checking if modules are properly installed...")
    try:
        result = subprocess.run(
            ['terraform', 'validate'],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        if result.returncode != 0:
            error_output = result.stderr.strip()
            if "module is not yet installed" in error_output or "Module not installed" in error_output:
                raise Exception(f" Terraform modules are not installed. Please run 'terraform init' to install all required modules.")
            else:
                raise Exception(f" Terraform validation failed:\n\n{error_output}")
        
        print(" All modules are properly installed")
        
    except subprocess.SubprocessError as e:
        raise Exception(f" Failed to validate Terraform configuration: {e}")
    
    print("\n All Terraform environment checks passed!")



def check_terraform_config_files():
    """Check if Terraform configuration files exist in current directory"""
    tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
    if tf_files:
        return True, tf_files
    else:
        return False, []


def check_terraform_init():
    """Check if Terraform has been initialized"""
    terraform_dir = Path('.terraform')
    if terraform_dir.exists() and terraform_dir.is_dir():
        # Check for providers
        providers_dir = terraform_dir / 'providers'
        if providers_dir.exists():
            return True, "Terraform is initialized"
        else:
            return False, "Terraform directory exists but no providers found"
    else:
        return False, "Terraform not initialized (.terraform directory not found)"


def check_module_exists(module_name):
    """Check if the specified module exists in Terraform configuration"""
    try:
        # Remove 'module.' prefix if present
        clean_module_name = module_name.replace('module.', '')
        
        # Method 1: Check .tf files directly for module definitions
        tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
        for tf_file in tf_files:
            try:
                with open(tf_file, 'r') as f:
                    content = f.read()
                    # Look for module "module_name" blocks
                    if f'module "{clean_module_name}"' in content or f"module '{clean_module_name}'" in content:
                        return True, f"Module '{clean_module_name}' found in {tf_file}"
            except Exception as e:
                print(f"Warning: Could not read {tf_file}: {e}")
                continue
        
        # Method 2: Try terraform show -json as fallback
        try:
            result = subprocess.run(
                ['terraform', 'show', '-json'],
                capture_output=True,
                text=True,
                cwd=Path.cwd()
            )
            
            if result.returncode == 0:
                state_data = json.loads(result.stdout)
                
                # Check if module exists in configuration
                if 'configuration' in state_data and state_data['configuration']:
                    modules = state_data.get('configuration', {}).get('root_module', {}).get('module_calls', {})
                    if clean_module_name in modules:
                        return True, f"Module '{clean_module_name}' found in Terraform state"
                
                # Also check in planned_values for modules
                if 'planned_values' in state_data and state_data['planned_values']:
                    modules = state_data.get('planned_values', {}).get('root_module', {}).get('child_modules', [])
                    for module in modules:
                        module_addr = module.get('address', '')
                        if clean_module_name in module_addr:
                            return True, f"Module '{clean_module_name}' found in planned values"
        except (subprocess.SubprocessError, json.JSONDecodeError) as e:
            print(f"Warning: Could not check terraform state: {e}")
        
        return False, f"Module '{clean_module_name}' not found in Terraform configuration files"
            
    except Exception as e:
        return False, f"Error checking module existence: {e}"


def clean_csv_file(filepath, verbose=False):
    """
    Clean up CSV file by:
    1. Removing any completely empty lines (lines with only commas or whitespace)
    2. Ensuring file ends without trailing newline (no \r\n at end)
    3. Preserving Windows line endings (\r\n) for all non-final lines
    
    This prevents issues with Terraform's csvdecode() function treating trailing
    newlines as empty rows, which can cause module validation failures.
    
    Args:
        filepath: Path to the CSV file to clean
        verbose: Whether to print debug information
    """
    try:
        # Read the entire file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into lines while preserving line ending info
        lines = content.splitlines(keepends=False)  # Get lines without endings
        
        # Filter out empty lines (lines that are empty or only contain commas/whitespace)
        cleaned_lines = []
        for line in lines:
            # Remove all commas and whitespace to check if truly empty
            test_line = line.replace(',', '').strip()
            if test_line:  # If there's any content besides commas/whitespace
                cleaned_lines.append(line)
        
        # Write back with proper line endings
        # All lines except the last get \r\n, last line gets no trailing newline
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            for idx, line in enumerate(cleaned_lines):
                f.write(line)
                # Add \r\n to all lines except the last one
                if idx < len(cleaned_lines) - 1:
                    f.write('\r\n')
        
        if verbose:
            removed_count = len(lines) - len(cleaned_lines)
            if removed_count > 0:
                print(f"DEBUG: Cleaned CSV {filepath}: removed {removed_count} empty line(s)")
            print(f"DEBUG: CSV file ends without trailing newline")
                
    except Exception as e:
        if verbose:
            print(f"Warning: Could not clean CSV file {filepath}: {e}")
