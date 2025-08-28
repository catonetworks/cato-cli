import os
import json
import subprocess
import glob
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
    variablesObj = { "accountID": (params.get("accountID") if params.get("accountID") else params.get("accountId"))}

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


# def getEntityLookup(args, configuration, account_id, entity_type, indexIdName=None):
#     """
#     Get entity lookup data from the API and return entities indexed by entityID or custom ID from helperFields
    
#     Args:
#         args: Command line arguments containing verbose and other options
#         configuration: API configuration object
#         account_id: The account ID to use for the lookup
#         entity_type: The type of entity to lookup (e.g., "site", "vpnUser", "host", etc.)
#         indexIdName: Optional name of the ID attribute in helperFields to use for indexing instead of entity.id
        
#     Returns:
#         dict: A dictionary with entity IDs (or custom IDs) as keys and entity information as values
#               Format: {"entityID1": {"id": "entityID1", "name": "entityName", "type": "entityType", "description": "desc", "indexId": "customID"}, ...}
#     """
#     # Define the entity lookup query
#     entity_query = {
#         "query": "query entityLookup ( $accountID:ID! $type:EntityType! $sortInput:[SortInput] $lookupFilterInput:[LookupFilterInput] ) { entityLookup ( accountID:$accountID type:$type sort:$sortInput filters:$lookupFilterInput ) { items { entity { id name type } description helperFields } total } }",
#         "variables": {
#             "accountID": account_id,
#             "type": entity_type
#         },
#         "operationName": "entityLookup"
#     }
    
#     # Create API client instance with params
#     # Create the API client instance
#     entity_api_client = ApiClient(configuration)

#     # Show masked API key in verbose mode (without affecting actual API calls)
#     if hasattr(args, 'verbose') and args.verbose and 'x-api-key' in entity_api_client.configuration.api_key:
#         print(f"Entity Lookup API Key (masked): ***MASKED***")

#     # Create the API instance
#     entity_query_instance = CallApi(entity_api_client)
#     params = {
#         'v': hasattr(args, 'verbose') and args.verbose,  # verbose mode
#         'f': 'json',  # format
#         'p': False,  # pretty print
#         't': False   # test mode
#     }

#     try:
#         # Call the entity lookup API
#         entity_response = entity_query_instance.call_api(entity_query, params)
#         entity_data = entity_response[0] if entity_response else {}
        
#         # Show raw API response in verbose mode
#         if hasattr(args, 'verbose') and args.verbose:
#             print("\n" + "=" * 80)
#             print(f"{entity_type.upper()} LOOKUP API RESPONSE:")
#             print("=" * 80)
#             print(json.dumps(entity_data, indent=2))
#             print("=" * 80 + "\n")
        
#         # Check for GraphQL errors in entity response
#         if 'errors' in entity_data:
#             error_messages = [error.get('message', 'Unknown error') for error in entity_data['errors']]
#             raise Exception(f"{entity_type} lookup API returned errors: {', '.join(error_messages)}")
        
#         if not entity_data or 'data' not in entity_data:
#             raise ValueError(f"Failed to retrieve {entity_type} data from API")
        
#         # Extract entity data and create indexed structure
#         entities = {}
#         entity_lookup = entity_data.get('data', {}).get('entityLookup', {})
#         entity_items = entity_lookup.get('items', [])
        
#         if hasattr(args, 'verbose') and args.verbose:
#             print(f"Processing {len(entity_items)} {entity_type}s from entity lookup")
#             if indexIdName:
#                 print(f"Using custom index field: {indexIdName}")
        
#         for item in entity_items:
#             entity = item.get('entity', {})
#             entity_id = entity.get('id')
#             helper_fields = item.get('helperFields', [])
            
#             # Determine the index key to use
#             index_key = entity_id  # Default to entity ID
#             custom_id = None
            
#             if indexIdName and helper_fields:
#                 # Look for the custom ID in helperFields
#                 for field in helper_fields:
#                     if field.get('name') == indexIdName:
#                         custom_id = field.get('value')
#                         if custom_id:
#                             index_key = custom_id
#                         break
            
#             if index_key:
#                 entity_data = {
#                     'id': entity_id,
#                     'name': entity.get('name', ''),
#                     'type': entity.get('type', ''),
#                     'description': item.get('description', ''),
#                     'helperFields': helper_fields
#                 }
                
#                 # Add the custom index ID if it was found and used
#                 if custom_id and indexIdName:
#                     entity_data['indexId'] = custom_id
#                     entity_data['indexIdName'] = indexIdName
                
#                 entities[index_key] = entity_data
                
#                 if hasattr(args, 'verbose') and args.verbose and custom_id:
#                     print(f"Entity {entity_id} indexed by {indexIdName}: {custom_id}")
        
#         if hasattr(args, 'verbose') and args.verbose:
#             index_type = f"custom field '{indexIdName}'" if indexIdName else "entity ID"
#             print(f"Successfully indexed {len(entities)} {entity_type}s by {index_type}")
            
#         return entities
        
#     except ApiException as e:
#         raise Exception(f"{entity_type} lookup API call failed - {e}")
#     except Exception as e:
#         raise Exception(f"Unexpected error during {entity_type} lookup API call - {e}")

def makeCall(args, configuration, query):    
    # Create API client instance with params
    instance = CallApi(ApiClient(configuration))
    params = {
        'v': hasattr(args, 'verbose') and args.verbose,  # verbose mode
        'f': 'json',  # format
        'p': False,  # pretty print
        't': False   # test mode
    }
    
    try:
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

        return response

    except ApiException as e:
        raise Exception(f"API call failed - {e}")
    except Exception as e:
        raise Exception(f"Unexpected error during API call - {e}")

def writeDataToFile(data, args, account_id=None, default_filename_template="data_{account_id}.json", default_directory="config_data"):
    """
    Write data to a file with flexible output path configuration
    
    Args:
        data: The data to write to file (will be JSON serialized)
        args: Command line arguments containing output_file_path and verbose options
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
