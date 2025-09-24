"""
Custom Parser API Client for Cato CLI

This module provides enhanced GraphQL query generation and API request handling
for the Cato Networks CLI tool. It includes improved field expansion logic,
better error handling, and support for custom query templates.

Key improvements over the original:
- Enhanced renderArgsAndFields function with better field expansion
- Improved error handling and validation
- Support for custom query templates and field overrides
- Better handling of nested field structures
- Enhanced debugging capabilities
"""

import codecs
import json
import os
import sys
from graphql_client import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
import pprint
import uuid
import string
from urllib3.filepost import encode_multipart_formdata
import base64
import hmac
import hashlib
import datetime
import ssl
import urllib.request
import urllib.error
import socket

class CustomAPIClient:
    """Enhanced API Client with custom query generation capabilities"""
    
    def __init__(self):
        self.custom_field_mappings = {
            # Define custom field expansions for specific operations
            "query.appStats": {
                "records": [
                    "fieldsUnitTypes",
                    "fieldsMap", 
                    "trends",
                    "prevTimeFrame",
                    "flatFields"
                ]
            }
        }
    
    def get_custom_fields(self, operation_name, field_name):
        """Get custom field expansions for a specific operation and field"""
        if operation_name in self.custom_field_mappings:
            return self.custom_field_mappings[operation_name].get(field_name, [])
        return []


# Global instance for field mappings
custom_client = CustomAPIClient()


def createRequest(args, configuration):
    """
    Enhanced request creation with improved error handling and validation
    
    Args:
        args: Command line arguments
        configuration: API configuration object
        
    Returns:
        API response or error object
    """
    params = vars(args)
    
    # Process output routing options
    network_config, sentinel_config = process_output_options(args)
    
    instance = CallApi(ApiClient(configuration))
    operation_name = params["operation_name"]
    
    try:
        operation = loadJSON(f"models/{operation_name}.json")
    except Exception as e:
        print(f"ERROR: Failed to load operation model for {operation_name}: {e}")
        return None
        
    # Load CSV configuration for this operation
    csv_function = None
    output_format = getattr(args, 'format', 'json')  # Default to json if -f not provided
    
    if output_format == 'csv':
        try:
            settings = loadJSON("clisettings.json")
            csv_supported_operations = settings.get("queryOperationCsvOutput", {})
            csv_function = csv_supported_operations.get(operation_name)
        except Exception as e:
            print(f"WARNING: Could not load CSV settings: {e}")
            csv_function = None
        
        if not csv_function:
            print(f"ERROR: CSV output not supported for operation '{operation_name}'")
            print(f"Supported CSV operations: {list(csv_supported_operations.keys()) if 'csv_supported_operations' in locals() else 'none'}")
            return None
        
    variables_obj = {}
    
    # Parse JSON input with better error handling (including for -t flag)
    if params["json"]:
        try:
            variables_obj = json.loads(params["json"])
            if not isinstance(variables_obj, dict):
                print("ERROR: JSON input must be an object/dictionary")
                return None
        except ValueError as e:
            print(f"ERROR: Invalid JSON syntax: {e}")
            print("Example: '{\"yourKey\":\"yourValue\"}'")
            return None
        except Exception as e:
            print(f"ERROR: Unexpected error parsing JSON: {e}")
            return None
    else:
        # Default to empty object if no json provided
        variables_obj = {}
    
    # Handle account ID for different operation types
    if operation_name in ["query.eventsFeed", "query.auditFeed"]:
        # Only add accountIDs if not already provided in JSON
        if "accountIDs" not in variables_obj:
            variables_obj["accountIDs"] = [configuration.accountID]
    elif "accountId" in operation.get("args", {}):
        variables_obj["accountId"] = configuration.accountID
    else:
        variables_obj["accountID"] = configuration.accountID
    
    # Validation logic
    if params["t"] or params.get("skip_validation", False):
        # Skip validation when using -t flag or --skip-validation flag
        is_ok = True
    else:
        is_ok, invalid_vars, message = validateArgs(variables_obj, operation)
    
    if is_ok:
        body = generateGraphqlPayload(variables_obj, operation, operation_name)
        
        if params["t"]:
            # Use dynamically generated query with custom field mappings
            print(body["query"])
            return None
        else:
            try:
                response = instance.call_api(body, params)
                
                # Handle output routing if network or sentinel options are specified
                if (network_config or sentinel_config) and response:
                    # Get the response data
                    response_data = response[0] if isinstance(response, list) and len(response) > 0 else response
                    
                    # Send to network endpoint if specified
                    if network_config:
                        send_events_to_network(response_data, network_config['host'], network_config['port'])
                    
                    # Send to Sentinel if specified  
                    if sentinel_config:
                        # Convert response to JSON bytes for Sentinel
                        json_data = json.dumps(response_data).encode('utf-8')
                        result_code = post_sentinel_data(
                            sentinel_config['customer_id'], 
                            sentinel_config['shared_key'], 
                            json_data
                        )
                        print(f"Sentinel API response code: {result_code}")
                
                # Apply CSV formatting if requested
                if output_format == 'csv' and csv_function and response:
                    try:
                        # Import the CSV formatter dynamically
                        # Get the response data (handle both list and tuple responses)
                        if isinstance(response, (list, tuple)) and len(response) > 0:
                            response_data = response[0]
                        else:
                            response_data = response
                        
                        # Add Utils directory to path and import csv_formatter
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        utils_dir = os.path.join(os.path.dirname(current_dir), 'Utils')
                        if utils_dir not in sys.path:
                            sys.path.insert(0, utils_dir)
                        
                        # Import the csv_formatter module
                        import csv_formatter
                        
                        # Call the appropriate CSV formatter function
                        if hasattr(csv_formatter, csv_function):
                            csv_formatter_func = getattr(csv_formatter, csv_function)
                            csv_output = csv_formatter_func(response_data)
                            
                            if csv_output:
                                # Determine output directory (reports) in current folder
                                reports_dir = os.path.join(os.getcwd(), 'reports')
                                if not os.path.exists(reports_dir):
                                    os.makedirs(reports_dir)
                                
                                # Default filename is the operation name (second segment) lowercased
                                op_base = operation_name.split('.')[-1].lower()
                                default_filename = f"{op_base}.csv"
                                filename = default_filename
                                
                                # Override filename if provided
                                if hasattr(args, 'csv_filename') and getattr(args, 'csv_filename'):
                                    filename = getattr(args, 'csv_filename')
                                    # Ensure .csv extension
                                    if not filename.lower().endswith('.csv'):
                                        filename += '.csv'
                                
                                # Append timestamp if requested
                                if hasattr(args, 'append_timestamp') and getattr(args, 'append_timestamp'):
                                    ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                                    name, ext = os.path.splitext(filename)
                                    filename = f"{name}_{ts}{ext}"
                                
                                output_path = os.path.join(reports_dir, filename)
                                
                                # Write CSV to file
                                try:
                                    with open(output_path, 'w', encoding='utf-8', newline='') as f:
                                        f.write(csv_output)
                                except Exception as write_err:
                                    print(f"ERROR: Failed to write CSV to file {output_path}: {write_err}")
                                    # Fallback: return CSV to stdout behavior
                                    return [{"__csv_output__": csv_output}]
                                
                                if params.get('v'):
                                    print(f"Saved CSV report to: {output_path}")
                                
                                # Return structured response similar to export functions
                                return [{"success": True, "output_file": output_path, "operation": operation_name}]
                            else:
                                print("WARNING: CSV formatter returned empty result")
                                return response
                        else:
                            print(f"ERROR: CSV formatter function '{csv_function}' not found")
                            return response
                    except Exception as e:
                        print(f"ERROR: Failed to format CSV output: {e}")
                        return response
                
                return response
                
            except ApiException as e:
                return e
    else:
        print(f"ERROR: {message}, {', '.join(invalid_vars)}")
        try:
            query_payload_file = f"queryPayloads/{operation_name}.json"
            query_payload = loadJSON(query_payload_file)
            print(f"\nExample: catocli {operation_name.replace('.', ' ')} {json.dumps(query_payload['variables'])}")
        except Exception as e:
            print(f"ERROR: Could not load query example: {e}")


def querySiteLocation(args, configuration):
    """
    Enhanced site location query with better validation
    """
    params = vars(args)
    operation_name = params["operation_name"]
    
    # Load the site location data (not the model definition)
    try:
        site_data = loadJSON(f"models/{operation_name}.json")
    except Exception as e:
        print(f"ERROR: Failed to load site location data: {e}")
        return None
        
    try:
        variables_obj = json.loads(params["json"])
    except ValueError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        print("Example: '{\"filters\":[{\"search\": \"Your city here\",\"field\":\"city\",\"operation\":\"exact\"}]}'")
        return None
        
    # Validate filters structure
    if not variables_obj.get("filters"):
        print("ERROR: Missing 'filters' array in request")
        print("Example: '{\"filters\":[{\"search\": \"Your city here\",\"field\":\"city\",\"operation\":\"exact\"}]}'")
        return None
        
    if not isinstance(variables_obj.get("filters"), list):
        print("ERROR: 'filters' must be an array")
        return None
    
    # Validate each filter
    required_fields = ["search", "field", "operation"]
    valid_fields = ['countryName', 'stateName', 'city']
    valid_operations = ['startsWith', 'endsWith', 'exact', 'contains']
    
    for i, filter_obj in enumerate(variables_obj["filters"]):
        if not isinstance(filter_obj, dict):
            print(f"ERROR: Filter {i} must be an object with 'search', 'field', and 'operation' properties")
            return None
            
        # Check required fields
        for field in required_fields:
            if field not in filter_obj:
                print(f"ERROR: Filter {i} missing required field '{field}'")
                return None
                
        # Validate field values
        search = filter_obj.get("search")
        field = filter_obj.get("field")
        operation = filter_obj.get("operation")
        
        if not isinstance(search, str) or len(search) < 3:
            print(f"ERROR: Filter {i} 'search' must be a string with at least 3 characters")
            return None
            
        if field not in valid_fields:
            print(f"ERROR: Filter {i} 'field' must be one of: {', '.join(valid_fields)}")
            return None
            
        if operation not in valid_operations:
            print(f"ERROR: Filter {i} 'operation' must be one of: {', '.join(valid_operations)}")
            return None
    
    # Process results using the site location data
    response = {"data": []}
    
    # Search through the site location data
    for key, site_obj in site_data.items():
        is_match = True
        for filter_obj in variables_obj["filters"]:
            search = filter_obj.get("search")
            field = filter_obj.get("field") 
            operation_type = filter_obj.get("operation")
            
            if field in site_obj:
                field_value = str(site_obj[field])
                if operation_type == "startsWith" and not field_value.startswith(search):
                    is_match = False
                    break
                elif operation_type == "endsWith" and not field_value.endswith(search):
                    is_match = False
                    break
                elif operation_type == "exact" and field_value != search:
                    is_match = False
                    break
                elif operation_type == "contains" and search not in field_value:
                    is_match = False
                    break
            else:
                is_match = False
                break
                
        if is_match:
            response["data"].append(site_obj)
    
    # Return response in the format expected by CLI driver (as a list)
    # The CLI driver expects response[0] to contain the actual data
    return [response]


def process_output_options(args):
    """
    Process network streaming and sentinel output options
    
    Returns:
        tuple: (network_config, sentinel_config) where each is None or dict with parsed options
    """
    network_config = None
    sentinel_config = None
    
    # Process network options
    if hasattr(args, 'stream_events') and args.stream_events is not None:
        network_elements = args.stream_events.split(":")
        if len(network_elements) != 2:
            print("Error: -n value must be in the form of host:port")
            sys.exit(1)
        
        try:
            host = network_elements[0]
            port = int(network_elements[1])
            network_config = {'host': host, 'port': port}
        except ValueError:
            print("Error: -n port must be a valid integer")
            sys.exit(1)
    
    # Process sentinel options  
    if hasattr(args, 'sentinel') and args.sentinel is not None:
        sentinel_elements = args.sentinel.split(":")
        if len(sentinel_elements) != 2:
            print("Error: -z value must be in the form of customerid:sharedkey")
            sys.exit(1)
        
        customer_id = sentinel_elements[0]
        shared_key = sentinel_elements[1]
        sentinel_config = {'customer_id': customer_id, 'shared_key': shared_key}
    
    return network_config, sentinel_config


def send_events_to_network(data, host, port):
    """
    Send events over network to host:port TCP
    
    Args:
        data: JSON data to send
        host: Target hostname or IP
        port: Target port number
    """
    try:
        # Convert data to JSON string if it's not already
        if isinstance(data, (dict, list)):
            json_data = json.dumps(data)
        else:
            json_data = str(data)
        
        # Create TCP socket and send data
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall(json_data.encode('utf-8'))
            
        print(f"Successfully sent data to {host}:{port}")
        
    except socket.error as e:
        print(f"Network error sending to {host}:{port}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error sending data to network: {e}")
        sys.exit(1)


def build_signature(customer_id, shared_key, date, content_length):
    """
    Build the API signature for Sentinel
    
    Args:
        customer_id: Azure customer ID
        shared_key: Shared key for authentication
        date: RFC1123 date string
        content_length: Length of content being sent
        
    Returns:
        Authorization header value
    """
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"POST\n{content_length}\napplication/json\n{x_headers}\n/api/logs"
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    authorization = "SharedKey {}:{}".format(customer_id, encoded_hash)
    return authorization


def post_sentinel_data(customer_id, shared_key, body):
    """
    Build and send a request to the POST API for Sentinel
    
    Args:
        customer_id: Azure customer ID
        shared_key: Shared key for authentication  
        body: JSON data to send (as bytes)
        
    Returns:
        Response code from the API
    """
    rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)
    signature = build_signature(customer_id, shared_key, rfc1123date, content_length)
    
    headers = {
        'content-type': 'application/json',
        'Authorization': signature,
        'Log-Type': 'CatoEvents',
        'Time-generated-field': 'event_timestamp',
        'x-ms-date': rfc1123date
    }
    
    no_verify = ssl._create_unverified_context()
    
    try:
        request = urllib.request.Request(
            url='https://' + customer_id + '.ods.opinsights.azure.com/api/logs?api-version=2016-04-01',
            data=body,
            headers=headers
        )
        response = urllib.request.urlopen(request, context=no_verify)
        return response.code
    except urllib.error.URLError as e:
        print(f"Azure API ERROR:{e}")
        sys.exit(1)
    except OSError as e:
        print(f"Azure API ERROR: {e}")
        sys.exit(1)


def createRawRequest(args, configuration):
    """
    Enhanced raw request handling with better error reporting
    """
    params = vars(args)
    
    # Process output routing options
    network_config, sentinel_config = process_output_options(args)
    
    # Handle endpoint override
    if hasattr(args, 'endpoint') and args.endpoint:
        configuration.host = args.endpoint
    
    # Check if binary/multipart mode is enabled
    if hasattr(args, 'binary') and args.binary:
        return createRawBinaryRequest(args, configuration)
        
    instance = CallApi(ApiClient(configuration))
    
    try:
        body = json.loads(params["json"])
        
        # Validate GraphQL request structure
        if not isinstance(body, dict):
            print("ERROR: Request must be a JSON object")
            return None
            
        if "query" not in body:
            print("ERROR: Request must contain a 'query' field")
            return None
            
    except ValueError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        return None
    except Exception as e:
        print(f"ERROR: Unexpected error parsing request: {e}")
        return None
    
    if params["t"]:
        if params["p"]:
            print(json.dumps(body, indent=2, sort_keys=True).replace("\\n", "\n").replace("\\t", "\t"))
        else:
            print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    ", " ").replace("  ", " "))
        return None
    else:
        try:
            response = instance.call_api(body, params)
            
            # Handle output routing if network or sentinel options are specified
            if (network_config or sentinel_config) and response:
                # Get the response data
                response_data = response[0] if isinstance(response, list) and len(response) > 0 else response
                
                # Send to network endpoint if specified
                if network_config:
                    send_events_to_network(response_data, network_config['host'], network_config['port'])
                
                # Send to Sentinel if specified  
                if sentinel_config:
                    # Convert response to JSON bytes for Sentinel
                    json_data = json.dumps(response_data).encode('utf-8')
                    result_code = post_sentinel_data(
                        sentinel_config['customer_id'], 
                        sentinel_config['shared_key'], 
                        json_data
                    )
                    print(f"Sentinel API response code: {result_code}")
            
            return response
            
        except ApiException as e:
            print(f"ERROR: API request failed: {e}")
            return None


def generateGraphqlPayload(variables_obj, operation, operation_name):
    """
    Enhanced GraphQL payload generation with improved field handling
    
    Args:
        variables_obj: Variables for the GraphQL query
        operation: Operation definition from schema
        operation_name: Name of the operation (e.g., 'query.appStats')
        
    Returns:
        Complete GraphQL request payload
    """
    indent = "\t"
    query_str = ""
    variable_str = ""
    
    # Generate variable declarations
    for var_name in variables_obj:
        if var_name in operation["operationArgs"]:
            variable_str += operation["operationArgs"][var_name]["requestStr"]
    
    # Build query structure
    operation_ary = operation_name.split(".")
    operation_type = operation_ary.pop(0)
    query_str = f"{operation_type} "
    query_str += renderCamelCase(".".join(operation_ary))
    query_str += f" ( {variable_str}) {{\n"
    query_str += f"{indent}{operation['name']} ( "
    
    # Add operation arguments
    for arg_name in operation["args"]:
        arg = operation["args"][arg_name]
        if arg["varName"] in variables_obj:
            query_str += arg["responseStr"]
    
    # Generate field selection with enhanced rendering
    query_str += ") {\n" + renderArgsAndFields("", variables_obj, operation, operation["type"]["definition"], operation_name, "\t\t") + "\t}"
    query_str += f"{indent}\n}}"
    
    body = {
        "query": query_str,
        "variables": variables_obj,
        "operationName": renderCamelCase(".".join(operation_ary)),
    }
    return body


def get_help(path):
    """
    Enhanced help generation with better error handling
    Stop including catocli examples after "Advanced Usage" section
    Add dynamic GitHub link if advanced examples exist
    Handle multi-line JSON examples properly for -p flag
    """
    match_cmd = f"catocli {path.replace('_', ' ')}"
    pwd = os.path.dirname(__file__)
    doc = f"{path}/README.md"
    abs_path = os.path.join(pwd, doc)
    new_line = "\nEXAMPLES:\n"
    
    # Check if advanced examples exist by looking for example file in schema directory
    # Convert path format (e.g., query_appStats -> query.appStats)
    operation_name = path.replace('_', '.', 1)  # Only replace first underscore
    schema_dir = os.path.dirname(os.path.dirname(pwd))  # Go up two levels to get to root
    example_file_path = os.path.join(schema_dir, "schema", "examples", f"{operation_name}.md")
    has_advanced_examples = os.path.exists(example_file_path)
    
    try:
        with open(abs_path, "r") as f:
            lines = f.readlines()
            
        # Flag to stop processing after Advanced Usage section
        stop_after_advanced = False
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Check if we've hit the Advanced Usage section
            if "Advanced Usage" in line or "## Advanced" in line:
                stop_after_advanced = True
                i += 1
                continue
                
            # Skip catocli examples after Advanced Usage
            if stop_after_advanced and match_cmd in line:
                i += 1
                continue
                
            # Include catocli examples before Advanced Usage
            if match_cmd in line:
                # Check if this is a -p example with multi-line JSON
                if "-p '" in line and line.rstrip().endswith("{"):
                    # This is the start of a multi-line JSON example
                    clean_line = line.replace("<br /><br />", "").replace("`", "")
                    complete_example = clean_line
                    
                    # Continue reading lines until we find the closing quote and brace
                    i += 1
                    while i < len(lines):
                        json_line = lines[i]
                        complete_example += json_line
                        
                        # Check if this line ends the JSON (ends with }' and optional whitespace)
                        if json_line.strip().endswith("}'"): 
                            break
                        i += 1
                    
                    new_line += complete_example
                else:
                    # Regular single-line example
                    clean_line = line.replace("<br /><br />", "").replace("`", "")
                    new_line += f"{clean_line}\n"
            
            i += 1
        
        # Add GitHub link if advanced examples exist
        if has_advanced_examples:
            new_line += f"\nPlease see advanced usage examples at the following:\n"
            new_line += f"https://github.com/catonetworks/cato-cli/tree/main/catocli/parsers/{path}\n"
                
    except FileNotFoundError:
        new_line += f"No examples found for {match_cmd}\n"
        # Still add GitHub link if advanced examples exist
        if has_advanced_examples:
            new_line += f"\nPlease see advanced usage examples at the following:\n"
            new_line += f"https://github.com/catonetworks/cato-cli/tree/main/catocli/parsers/{path}\n"
    except Exception as e:
        new_line += f"Error loading help: {e}\n"
        
    return new_line


def validateArgs(variables_obj, operation):
    """
    Enhanced argument validation with detailed error reporting
    Skip required field validation to allow any request to be sent
    """
    is_ok = True
    invalid_vars = []
    message = "Arguments are missing or have invalid values: "
    
    # Skip all validation - allow any request to be sent to the API
    # This allows users to send any GraphQL request and see the API response directly
    
    return is_ok, invalid_vars, message


def loadJSON(file):
    """
    Enhanced JSON loading with better error handling and path resolution
    """
    module_dir = os.path.dirname(__file__)
    
    # Special handling for clisettings.json - it's in catocli/ directory
    if file == "clisettings.json":
        # From parsers/ go up to catocli/ and look for clisettings.json
        catocli_dir = os.path.dirname(module_dir)  # Go up from parsers/ to catocli/
        file_path = os.path.join(catocli_dir, file)
    else:
        # For other files (like models), navigate up two directory levels (from parsers/ to catocli/ to root)
        module_dir = os.path.dirname(module_dir)  # Go up from parsers/
        module_dir = os.path.dirname(module_dir)  # Go up from catocli/
        file_path = os.path.join(module_dir, file)
    
    try:
        with open(file_path, 'r') as data:
            config = json.load(data)
            return config
    except FileNotFoundError:
        logging.error(f"File \"{file_path}\" not found.")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in file \"{file_path}\": {e}")
        raise
    except Exception as e:
        logging.error(f"Error loading file \"{file_path}\": {e}")
        raise


def renderCamelCase(path_str):
    """
    Convert dot-separated path to camelCase
    
    Args:
        path_str: Dot-separated string like 'app.stats'
        
    Returns:
        camelCase string like 'appStats'
    """
    if not path_str:
        return ""
        
    result = ""
    path_ary = path_str.split(".")
    
    for i, path in enumerate(path_ary):
        if not path:  # Skip empty parts
            continue
            
        if i == 0:
            result += path[0].lower() + path[1:] if len(path) > 1 else path.lower()
        else:
            result += path[0].upper() + path[1:] if len(path) > 1 else path.upper()
            
    return result


def renderArgsAndFields(response_arg_str, variables_obj, cur_operation, definition, operation_name, indent):
    """
    ENHANCED field rendering with custom field expansion support
    
    This is the key function that generates the GraphQL field selection.
    It now includes support for custom field expansions defined in custom_field_mappings.
    
    Args:
        response_arg_str: Current field string being built
        variables_obj: Variables for the query
        cur_operation: Current operation definition  
        definition: Field definitions
        operation_name: Name of the operation (for custom mappings)
        indent: Current indentation level
        
    Returns:
        Complete field selection string
    """
    if not definition or not isinstance(definition, dict) or 'fields' not in definition:
        return response_arg_str
    
    # DEBUG: Print fields for debugging
    # print(f"DEBUG: renderArgsAndFields - operation_name={operation_name}, fields={list(definition['fields'].keys())}", file=sys.stderr)
        
    for field_name in definition['fields']:
        field = definition['fields'][field_name]
        field_display_name = field.get('alias', field['name'])
        
        # Check if field has arguments and whether they are present in variables
        should_include_field = True
        args_present = False
        arg_str = ""
        
        if field.get("args") and not isinstance(field['args'], list):
            if len(list(field['args'].keys())) > 0:
                # Field has arguments - check if any are required or present
                arg_str = " ( "
                required_args_missing = False
                
                for arg_name in field['args']:
                    arg = field['args'][arg_name]
                    if arg["varName"] in variables_obj:
                        arg_str += arg['responseStr'] + " "
                        args_present = True
                    elif arg.get("required", False):
                        # Required argument is missing
                        required_args_missing = True
                        break
                        
                arg_str += ") "
                
                # Only exclude field if required arguments are missing
                # If all arguments are optional, include the field even without arguments
                should_include_field = not required_args_missing
        
        # Only process field if we should include it
        if should_include_field:
            response_arg_str += f"{indent}{field_display_name}"
            if args_present:
                response_arg_str += arg_str
        
        # ENHANCED: Check for custom field expansions first
        custom_fields = custom_client.get_custom_fields(operation_name, field['name'])
        if should_include_field and custom_fields:
            response_arg_str += "  {\n"
            for custom_field in custom_fields:
                response_arg_str += f"{indent}\t{custom_field}\n"
            response_arg_str += f"{indent}}}\n"
        
        # Standard nested field processing (only if no custom fields defined)
        elif should_include_field and field.get("type") and field['type'].get('definition') and field['type']['definition']['fields'] is not None:
            response_arg_str += " {\n"
            for subfield_index in field['type']['definition']['fields']:
                subfield = field['type']['definition']['fields'][subfield_index]
                subfield_name = subfield.get('alias', subfield['name'])
                response_arg_str += f"{indent}\t{subfield_name}"
                
                if subfield.get("args") and len(list(subfield["args"].keys())) > 0:
                    sub_args_present = False
                    sub_arg_str = " ( "
                    for arg_name in subfield['args']:
                        arg = subfield['args'][arg_name]
                        if arg["varName"] in variables_obj:
                            sub_args_present = True
                            sub_arg_str += arg['responseStr'] + " "
                    sub_arg_str += " )"
                    if sub_args_present:
                        response_arg_str += sub_arg_str
                
                if subfield.get("type") and subfield['type'].get("definition") and (subfield['type']['definition'].get("fields") or subfield['type']['definition'].get('inputFields')):
                    response_arg_str += " {\n"
                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, subfield['type']['definition'], operation_name, indent + "\t\t")
                    if subfield['type']['definition'].get('possibleTypes'):
                        possible_types = subfield['type']['definition']['possibleTypes']
                        # Handle both list and dict formats for possibleTypes
                        if isinstance(possible_types, list):
                            for possible_type in possible_types:
                                if isinstance(possible_type, dict) and 'name' in possible_type:
                                    # Only create fragment if there are actually fields to render
                                    if possible_type.get('fields') or possible_type.get('inputFields'):
                                        response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                        response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t")
                                        response_arg_str += f"{indent}\t\t}}\n"
                        elif isinstance(possible_types, dict):
                            for possible_type_name in possible_types:
                                possible_type = possible_types[possible_type_name]
                                # Only create fragment if there are actually fields to render
                                if possible_type.get('fields') or possible_type.get('inputFields'):
                                    response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t")
                                    response_arg_str += f"{indent}\t\t}}\n"
                    response_arg_str += f"{indent}\t}}"
                elif subfield.get('type') and subfield['type'].get('definition') and subfield['type']['definition'].get('possibleTypes'):
                    response_arg_str += " {\n"
                    response_arg_str += f"{indent}\t\t__typename\n"
                    possible_types = subfield['type']['definition']['possibleTypes']
                    # Handle both list and dict formats for possibleTypes
                    if isinstance(possible_types, list):
                        for possible_type in possible_types:
                            if isinstance(possible_type, dict) and 'name' in possible_type:
                                # Only create fragment if there are actually fields to render
                                if possible_type.get('fields') or possible_type.get('inputFields'):
                                    response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t")
                                    response_arg_str += f"{indent}\t\t}}\n"
                    elif isinstance(possible_types, dict):
                        for possible_type_name in possible_types:
                            possible_type = possible_types[possible_type_name]
                            # Only create fragment if there are actually fields to render
                            if possible_type.get('fields') or possible_type.get('inputFields'):
                                response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t")
                                response_arg_str += f"{indent}\t\t}}\n"
                    response_arg_str += f"{indent}\t}}\n"
                response_arg_str += "\n"
                
            if field['type']['definition'].get('possibleTypes'):
                for possible_type_name in field['type']['definition']['possibleTypes']:
                    possible_type = field['type']['definition']['possibleTypes'][possible_type_name]
                    response_arg_str += f"{indent}\t... on {possible_type['name']} {{\n"
                    if possible_type.get('fields') or possible_type.get('inputFields'):
                        response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t")
                    response_arg_str += f"{indent}\t}}\n"
            response_arg_str += f"{indent}}}\n"
        
        # Handle inputFields
        if should_include_field and field.get('type') and field['type'].get('definition') and field['type']['definition'].get('inputFields'):
            response_arg_str += " {\n"
            for subfield_name in field['type']['definition'].get('inputFields'):
                subfield = field['type']['definition']['inputFields'][subfield_name]
                # Enhanced aliasing logic for inputFields
                if (subfield.get('type') and subfield['type'].get('name') and 
                    cur_operation.get('fieldTypes', {}).get(subfield['type']['name']) and 
                    subfield.get('type', {}).get('kind') and 
                    'SCALAR' not in str(subfield['type']['kind'])):
                    subfield_name = f"{subfield['name']}{field['type']['definition']['name']}: {subfield['name']}"
                else:
                    subfield_name = subfield['name']
                response_arg_str += f"{indent}\t{subfield_name}"
                if subfield.get('type') and subfield['type'].get('definition') and (subfield['type']['definition'].get('fields') or subfield['type']['definition'].get('inputFields')):
                    response_arg_str += " {\n"
                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, subfield['type']['definition'], operation_name, indent + "\t\t")
                    response_arg_str += f"{indent}\t}}\n"
            if field['type']['definition'].get('possibleTypes'):
                for possible_type_name in field['type']['definition']['possibleTypes']:
                    possible_type = field['type']['definition']['possibleTypes'][possible_type_name]
                    response_arg_str += f"{indent}... on {possible_type['name']} {{\n"
                    if possible_type.get('fields') or possible_type.get('inputFields'):
                        response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t")
                    response_arg_str += f"{indent}\t}}\n"
            response_arg_str += f"{indent}}}\n"
        
        if should_include_field:
            response_arg_str += "\n"
    
    return response_arg_str


# Binary/Multipart request functions (preserved from original)
def createRawBinaryRequest(args, configuration):
    """Handle multipart/form-data requests for file uploads and binary content"""
    params = vars(args)
    
    # Parse the JSON body
    try:
        body = json.loads(params["json"])
    except ValueError as e:
        print(f"ERROR: JSON argument must be valid json: {e}")
        return
    except Exception as e:
        print(f"ERROR: {e}")
        return
    
    # Build form data
    form_fields = {}
    files = []
    
    # Add the operations field containing the GraphQL payload
    form_fields['operations'] = json.dumps(body)
    
    # Handle file mappings if files are specified
    if hasattr(args, 'files') and args.files:
        # Build the map object for file uploads
        file_map = {}
        for i, (field_name, file_path) in enumerate(args.files):
            file_index = str(i + 1)
            file_map[file_index] = [field_name]
            
            # Read file content
            try:
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                files.append((file_index, (os.path.basename(file_path), file_content, 'application/octet-stream')))
            except IOError as e:
                print(f"ERROR: Could not read file {file_path}: {e}")
                return
                
        # Add the map field
        form_fields['map'] = json.dumps(file_map)
    
    # Test mode - just print the request structure
    if params.get("t") == True:
        print("Multipart form data request:")
        if params.get("p") == True:
            print(f"Operations: {json.dumps(json.loads(form_fields.get('operations')), indent=2)}")
        else:
            print(f"Operations: {form_fields.get('operations')}")
        if 'map' in form_fields:
            print(f"Map: {form_fields.get('map')}")
        if files:
            print(f"Files: {[f[0] + ': ' + f[1][0] for f in files]}")
        return None
    
    # Perform the multipart request
    try:
        return sendMultipartRequest(configuration, form_fields, files, params)
    except Exception as e:
        # Safely handle exception string conversion
        try:
            error_str = str(e)
        except Exception:
            error_str = f"Exception of type {type(e).__name__}"
        
        if params.get("v") == True:
            import traceback
            print(f"ERROR: Failed to send multipart request: {error_str}")
            traceback.print_exc()
        else:
            print(f"ERROR: Failed to send multipart request: {error_str}")
        return None


# Additional helper functions for private commands and specialized operations
# (These are preserved from the original implementation)

def get_private_help(command_name, command_config):
    """Generate comprehensive help text for a private command"""
    usage = f"catocli private {command_name}"
    
    # Create comprehensive JSON example with all arguments (excluding accountId)
    if 'arguments' in command_config:
        json_example = {}
        for arg in command_config['arguments']:
            arg_name = arg.get('name')
            # Skip accountId since it's handled by standard -accountID CLI argument
            if arg_name and arg_name.lower() != 'accountid':
                if 'example' in arg:
                    # Use explicit example if provided
                    json_example[arg_name] = arg['example']
                elif 'default' in arg:
                    # Use default value if available
                    json_example[arg_name] = arg['default']
                else:
                    # Generate placeholder based on type
                    arg_type = arg.get('type', 'string')
                    if arg_type == 'string':
                        json_example[arg_name] = f"<{arg_name}>"
                    elif arg_type == 'object':
                        if 'struct' in arg:
                            # Use struct definition
                            json_example[arg_name] = arg['struct']
                        else:
                            json_example[arg_name] = {}
                    else:
                        json_example[arg_name] = f"<{arg_name}>"
                        
        if json_example:
            # Format JSON nicely for readability in help
            json_str = json.dumps(json_example, indent=2)
            usage += f" '{json_str}'"
    
    # Add common options
    usage += " [-t] [-v] [-p]"
    
    # Add command-specific arguments with descriptions (excluding accountId)
    if 'arguments' in command_config:
        filtered_args = [arg for arg in command_config['arguments'] if arg.get('name', '').lower() != 'accountid']
        if filtered_args:
            usage += "\n\nArguments:"
            for arg in filtered_args:
                arg_name = arg.get('name')
                arg_type = arg.get('type', 'string')
                arg_default = arg.get('default')
                arg_example = arg.get('example')
                
                if arg_name:
                    usage += f"\n  --{arg_name}: {arg_type}"
                    if arg_default is not None:
                        usage += f" (default: {arg_default})"
                    if arg_example is not None and arg_example != arg_default:
                        usage += f" (example: {json.dumps(arg_example) if isinstance(arg_example, (dict, list)) else arg_example})"
    
    # Add standard accountID information
    usage += "\n\nStandard Arguments:"
    usage += "\n  -accountID: Account ID (taken from profile, can be overridden)"
    
    # Add payload file info if available
    if 'payloadFilePath' in command_config:
        usage += f"\n\nPayload template: {command_config['payloadFilePath']}"
    
    # Add batch processing info if configured
    if 'batchSize' in command_config:
        usage += f"\nBatch size: {command_config['batchSize']}"
        if 'paginationParam' in command_config:
            usage += f" (pagination: {command_config['paginationParam']})"
    
    # Add examples section if available
    if 'examples' in command_config and command_config['examples']:
        usage += "\n\nEXAMPLES:\n"
        for i, example in enumerate(command_config['examples']):
            description = example.get('description', '')
            command = example.get('command', '')
            
            if description and command:
                usage += f"{description}:\n{command}\n"
                # Add a blank line between examples (except for the last one)
                if i < len(command_config['examples']) - 1:
                    usage += "\n"
    
    return usage


def load_payload_template(command_config):
    """Load and return the GraphQL payload template for a private command"""
    try:
        payload_path = command_config.get('payloadFilePath')
        if not payload_path:
            raise ValueError("Missing payloadFilePath in command configuration")
        
        # Construct the full path relative to the settings directory
        settings_dir = os.path.expanduser("~/.cato")
        full_payload_path = os.path.join(settings_dir, payload_path)
        
        # Load the payload file using the standard JSON loading mechanism
        try:
            with open(full_payload_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Payload file not found: {full_payload_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in payload file {full_payload_path}: {e}")
    except Exception as e:
        raise ValueError(f"Failed to load payload template: {e}")


def set_nested_value(obj, path, value):
    """Set a value at a nested path in an object using jQuery-style JSON path syntax"""
    import re
    
    # Parse the path into components handling both dot notation and array indices
    path_parts = []
    for part in path.split('.'):
        # Check if this part contains array notation like 'items[0]'
        array_matches = re.findall(r'([^\[]+)(?:\[(\d+)\])?', part)
        for match in array_matches:
            key, index = match
            if key:  # Add the key part
                path_parts.append(key)
            if index:  # Add the array index part
                path_parts.append(int(index))
    
    current = obj
    
    # Navigate to the parent of the target location
    for i, part in enumerate(path_parts[:-1]):
        next_part = path_parts[i + 1]
        
        if isinstance(part, int):
            # Current part is an array index
            if not isinstance(current, list):
                raise ValueError(f"Expected array at path component {i}, got {type(current).__name__}")
            
            # Extend array if necessary
            while len(current) <= part:
                current.append(None)
            
            # Initialize the array element if it doesn't exist
            if current[part] is None:
                if isinstance(next_part, int):
                    current[part] = []  # Next part is array index, so create array
                else:
                    current[part] = {}  # Next part is object key, so create object
            
            current = current[part]
            
        else:
            # Current part is an object key
            if not isinstance(current, dict):
                raise ValueError(f"Expected object at path component {i}, got {type(current).__name__}")
            
            # Create the key if it doesn't exist
            if part not in current:
                if isinstance(next_part, int):
                    current[part] = []  # Next part is array index, so create array
                else:
                    current[part] = {}  # Next part is object key, so create object
            
            current = current[part]
    
    # Set the final value
    final_part = path_parts[-1]
    if isinstance(final_part, int):
        # Final part is an array index
        if not isinstance(current, list):
            raise ValueError(f"Expected array at final path component, got {type(current).__name__}")
        
        # Extend array if necessary
        while len(current) <= final_part:
            current.append(None)
        
        current[final_part] = value
    else:
        # Final part is an object key
        if not isinstance(current, dict):
            raise ValueError(f"Expected object at final path component, got {type(current).__name__}")
        
        current[final_part] = value


def apply_template_variables(template, variables, private_config):
    """Apply variables to the template using path-based insertion and template replacement"""
    if not template or not isinstance(template, dict):
        return template
    
    # Make a deep copy to avoid modifying the original
    import copy
    result = copy.deepcopy(template)
    
    # First, handle path-based variable insertion from private_config
    if private_config and 'arguments' in private_config:
        for arg in private_config['arguments']:
            arg_name = arg.get('name')
            arg_paths = arg.get('path', [])
            
            if arg_name and arg_name in variables and arg_paths:
                # Insert the variable value at each specified path
                for path in arg_paths:
                    try:
                        set_nested_value(result, path, variables[arg_name])
                    except Exception as e:
                        # If path insertion fails, continue to template replacement
                        pass
    
    # Second, handle traditional template variable replacement as fallback
    def traverse_and_replace(obj, path=""):
        if isinstance(obj, dict):
            for key, value in list(obj.items()):
                new_path = f"{path}.{key}" if path else key
                
                # Check if this is a template variable (string that starts with '{{')
                if isinstance(value, str) and value.startswith('{{') and value.endswith('}}'):
                    # Extract variable name
                    var_name = value[2:-2].strip()
                    
                    # Replace with actual value if available
                    if var_name in variables:
                        obj[key] = variables[var_name]
                
                # Recursively process nested objects
                else:
                    traverse_and_replace(value, new_path)
                    
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                traverse_and_replace(item, f"{path}[{i}]")
    
    traverse_and_replace(result)
    return result


def createPrivateRequest(args, configuration):
    """Handle private command execution using GraphQL payload templates"""
    params = vars(args)
    
    # Get the private command configuration
    private_command = params.get('private_command')
    private_config = params.get('private_config')
    
    if not private_command or not private_config:
        print("ERROR: Missing private command configuration")
        return None
    
    # Load private settings and apply ONLY for private commands
    try:
        settings_file = os.path.expanduser("~/.cato/settings.json")
        with open(settings_file, 'r') as f:
            private_settings = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        private_settings = {}
    
    # Override endpoint if specified in private settings
    if 'baseUrl' in private_settings:
        configuration.host = private_settings['baseUrl']
    
    # Add custom headers from private settings
    if 'headers' in private_settings and isinstance(private_settings['headers'], dict):
        if not hasattr(configuration, 'custom_headers'):
            configuration.custom_headers = {}
        for key, value in private_settings['headers'].items():
            configuration.custom_headers[key] = value
    
    # Parse input JSON variables
    try:
        variables = json.loads(params.get('json', '{}'))
    except ValueError as e:
        print(f"ERROR: Invalid JSON input: {e}")
        return None
    
    # Apply default values from settings configuration first
    for arg in private_config.get('arguments', []):
        arg_name = arg.get('name')
        if arg_name and 'default' in arg:
            variables[arg_name] = arg['default']
    
    # Apply profile account ID as fallback (lower priority than settings defaults)
    if configuration and hasattr(configuration, 'accountID'):
        if 'accountID' not in variables and 'accountId' not in variables:
            variables['accountID'] = configuration.accountID
            variables['accountId'] = configuration.accountID
        elif 'accountID' in variables and 'accountId' not in variables:
            variables['accountId'] = variables['accountID']
        elif 'accountId' in variables and 'accountID' not in variables:
            variables['accountID'] = variables['accountId']
    
    # Apply CLI argument values (highest priority)
    for arg in private_config.get('arguments', []):
        arg_name = arg.get('name')
        if arg_name:
            # Handle special case for accountId
            if arg_name.lower() == 'accountid':
                if hasattr(args, 'accountID') and getattr(args, 'accountID') is not None:
                    arg_value = getattr(args, 'accountID')
                    variables['accountID'] = arg_value
                    variables['accountId'] = arg_value
                elif hasattr(args, 'accountId') and getattr(args, 'accountId') is not None:
                    arg_value = getattr(args, 'accountId')
                    variables['accountID'] = arg_value
                    variables['accountId'] = arg_value
            else:
                if hasattr(args, arg_name):
                    arg_value = getattr(args, arg_name)
                    if arg_value is not None:
                        # Handle type conversion based on argument configuration
                        arg_type = arg.get('type', 'string')
                        if arg_type == 'array' and not isinstance(arg_value, list):
                            # Convert string to single-element array
                            variables[arg_name] = [arg_value]
                        else:
                            variables[arg_name] = arg_value
    
    # Load the payload template
    try:
        payload_template = load_payload_template(private_config)
    except ValueError as e:
        print(f"ERROR: {e}")
        return None
    
    # Apply variables to the template
    body = apply_template_variables(payload_template, variables, private_config)
    
    # Test mode - just print the request
    if params.get('t'):
        if params.get('p'):
            print(json.dumps(body, indent=2, sort_keys=True))
        else:
            print(json.dumps(body))
        return None
    
    # Execute the GraphQL request
    try:
        response = sendPrivateGraphQLRequest(configuration, body, params)
        
        # Handle CSV output if requested and configured
        output_format = getattr(args, 'format', 'json')  # Default to json if -f not provided
        if output_format == 'csv' and 'csvOutputOperation' in private_config:
            csv_operation = private_config['csvOutputOperation']
            
            # Load CSV configuration from clisettings.json
            try:
                settings = loadJSON("clisettings.json")
                csv_supported_operations = settings.get("queryOperationCsvOutput", {})
                csv_function = csv_supported_operations.get(csv_operation)
            except Exception as e:
                print(f"WARNING: Could not load CSV settings: {e}")
                csv_function = None
            
            if csv_function and response:
                try:
                    # Get the response data (handle both list and tuple responses)
                    if isinstance(response, (list, tuple)) and len(response) > 0:
                        response_data = response[0]
                    else:
                        response_data = response
                    
                    # Add Utils directory to path and import csv_formatter
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    utils_dir = os.path.join(os.path.dirname(current_dir), 'Utils')
                    if utils_dir not in sys.path:
                        sys.path.insert(0, utils_dir)
                    
                    # Import the csv_formatter module
                    import csv_formatter
                    
                    # Call the appropriate CSV formatter function
                    if hasattr(csv_formatter, csv_function):
                        csv_formatter_func = getattr(csv_formatter, csv_function)
                        csv_output = csv_formatter_func(response_data)
                        
                        if csv_output:
                            # Determine output directory (reports) in current folder
                            reports_dir = os.path.join(os.getcwd(), 'reports')
                            if not os.path.exists(reports_dir):
                                os.makedirs(reports_dir)
                            
                            # Default filename is the private command name lowercased
                            default_filename = f"{private_command}.csv"
                            filename = default_filename
                            
                            # Override filename if provided
                            if hasattr(args, 'csv_filename') and getattr(args, 'csv_filename'):
                                filename = getattr(args, 'csv_filename')
                                # Ensure .csv extension
                                if not filename.lower().endswith('.csv'):
                                    filename += '.csv'
                            
                            # Append timestamp if requested
                            if hasattr(args, 'append_timestamp') and getattr(args, 'append_timestamp'):
                                ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                                name, ext = os.path.splitext(filename)
                                filename = f"{name}_{ts}{ext}"
                            
                            output_path = os.path.join(reports_dir, filename)
                            
                            # Write CSV to file
                            try:
                                with open(output_path, 'w', encoding='utf-8', newline='') as f:
                                    f.write(csv_output)
                            except Exception as write_err:
                                print(f"ERROR: Failed to write CSV to file {output_path}: {write_err}")
                                # Fallback: return CSV to stdout behavior
                                return [{"__csv_output__": csv_output}]
                            
                            if params.get('v'):
                                print(f"Saved CSV report to: {output_path}")
                            
                            # Return structured response similar to export functions
                            return [{"success": True, "output_file": output_path, "operation": csv_operation, "private_command": private_command}]
                        else:
                            print("WARNING: CSV formatter returned empty result")
                            return response
                    else:
                        print(f"ERROR: CSV formatter function '{csv_function}' not found")
                        return response
                except Exception as e:
                    print(f"ERROR: Failed to format CSV output: {e}")
                    return response
            else:
                if not csv_function:
                    print(f"ERROR: CSV output not supported for private command '{private_command}' with operation '{csv_operation}'")
                    print(f"Available CSV operations: {list(csv_supported_operations.keys()) if 'csv_supported_operations' in locals() else 'none'}")
                return response
        
        return response
        
    except Exception as e:
        return e


def sendMultipartRequest(configuration, form_fields, files, params):
    """Send a multipart/form-data request directly using urllib3"""
    import urllib3
    
    # Create pool manager
    pool_manager = urllib3.PoolManager(
        cert_reqs='CERT_NONE' if not getattr(configuration, 'verify_ssl', False) else 'CERT_REQUIRED'
    )
    
    # Prepare form data
    fields = []
    for key, value in form_fields.items():
        fields.append((key, value))
    
    for file_key, (filename, content, content_type) in files:
        fields.append((file_key, (filename, content, content_type)))
    
    # Encode multipart data
    body_data, content_type = encode_multipart_formdata(fields)
    
    # Prepare headers
    headers = {
        'Content-Type': content_type,
        'User-Agent': f"Cato-CLI-v{getattr(configuration, 'version', 'unknown')}"
    }
    
    # Add API key if not using custom headers
    using_custom_headers = hasattr(configuration, 'custom_headers') and configuration.custom_headers
    if not using_custom_headers and hasattr(configuration, 'api_key') and configuration.api_key and 'x-api-key' in configuration.api_key:
        headers['x-api-key'] = configuration.api_key['x-api-key']
    
    # Add custom headers
    if using_custom_headers:
        headers.update(configuration.custom_headers)
    
    # Verbose output
    if params.get("v"):
        print(f"Host: {getattr(configuration, 'host', 'unknown')}")
        masked_headers = headers.copy()
        if 'x-api-key' in masked_headers:
            masked_headers['x-api-key'] = '***MASKED***'
        print(f"Request Headers: {json.dumps(masked_headers, indent=4, sort_keys=True)}")
        print(f"Content-Type: {content_type}")
        print(f"Form fields: {list(form_fields.keys())}")
        print(f"Files: {[f[0] for f in files]}\n")
    
    try:
        # Make the request
        resp = pool_manager.request(
            'POST',
            getattr(configuration, 'host', 'https://api.catonetworks.com/api/v1/graphql'),
            body=body_data,
            headers=headers
        )
        
        # Parse response
        if resp.status < 200 or resp.status >= 300:
            reason = resp.reason if resp.reason is not None else "Unknown Error"
            error_msg = f"HTTP {resp.status}: {reason}"
            if resp.data:
                try:
                    error_msg += f"\n{resp.data.decode('utf-8')}"
                except Exception:
                    error_msg += f"\n{resp.data}"
            print(f"ERROR: {error_msg}")
            return None
        
        try:
            response_data = json.loads(resp.data.decode('utf-8'))
        except json.JSONDecodeError:
            response_data = resp.data.decode('utf-8')
        
        return [response_data]
        
    except Exception as e:
        # Safely handle exception string conversion
        try:
            error_str = str(e)
        except Exception:
            error_str = f"Exception of type {type(e).__name__}"
        print(f"ERROR: Network/request error: {error_str}")
        return None


def sendPrivateGraphQLRequest(configuration, body, params):
    """Send a GraphQL request for private commands without User-Agent header"""
    import urllib3
    
    # Create pool manager
    pool_manager = urllib3.PoolManager(
        cert_reqs='CERT_NONE' if not getattr(configuration, 'verify_ssl', False) else 'CERT_REQUIRED'
    )
    
    # Prepare headers WITHOUT User-Agent
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Add API key if not using custom headers
    using_custom_headers = hasattr(configuration, 'custom_headers') and configuration.custom_headers
    if not using_custom_headers and hasattr(configuration, 'api_key') and configuration.api_key and 'x-api-key' in configuration.api_key:
        headers['x-api-key'] = configuration.api_key['x-api-key']
    
    # Add custom headers
    if using_custom_headers:
        headers.update(configuration.custom_headers)
    
    # Encode headers to handle Unicode characters properly
    encoded_headers = {}
    for key, value in headers.items():
        # Ensure header values are properly encoded as strings
        if isinstance(value, str):
            # Replace problematic Unicode characters that can't be encoded in latin-1
            value = value.encode('utf-8', errors='replace').decode('latin-1', errors='replace')
        encoded_headers[key] = value
    headers = encoded_headers
    
    # Verbose output
    if params.get("v"):
        print(f"Host: {getattr(configuration, 'host', 'unknown')}")
        masked_headers = headers.copy()
        if 'x-api-key' in masked_headers:
            masked_headers['x-api-key'] = '***MASKED***'
        if 'Cookie' in masked_headers:
            masked_headers['Cookie'] = '***MASKED***'
        print(f"Request Headers: {json.dumps(masked_headers, indent=4, sort_keys=True)}")
        print(f"Request Data: {json.dumps(body, indent=4, sort_keys=True)}\n")
    
    # Prepare request body
    body_data = json.dumps(body).encode('utf-8')
    
    try:
        # Make the request
        resp = pool_manager.request(
            'POST',
            getattr(configuration, 'host', 'https://api.catonetworks.com/api/v1/graphql'),
            body=body_data,
            headers=headers
        )
        
        # Parse response
        if resp.status < 200 or resp.status >= 300:
            reason = resp.reason if resp.reason is not None else "Unknown Error"
            error_msg = f"HTTP {resp.status}: {reason}"
            if resp.data:
                try:
                    error_msg += f"\n{resp.data.decode('utf-8')}"
                except Exception:
                    error_msg += f"\n{resp.data}"
            print(f"ERROR: {error_msg}")
            return None
        
        try:
            response_data = json.loads(resp.data.decode('utf-8'))
        except json.JSONDecodeError:
            response_data = resp.data.decode('utf-8')
        
        # Return in the same format as the regular API client
        return [response_data]
        
    except Exception as e:
        # Safely handle exception string conversion
        try:
            error_str = str(e)
        except Exception:
            error_str = f"Exception of type {type(e).__name__}"
        print(f"ERROR: Network/request error: {error_str}")
        return None
