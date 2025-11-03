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
import re

# Import shared utilities
from catocli.Utils.graphql_utils import (
    loadJSON,
    renderCamelCase,
    validateArgs,
    loadIntrospectionTypes,
    generateGraphqlPayload,
    postProcessBareComplexFields,
    expandFieldWithIntrospection,
    renderArgsAndFields
)

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

def preprocess_json_input(json_string):
    """
    Preprocess JSON input to handle common formatting issues from different shells
    
    Args:
        json_string: Raw JSON string that may have formatting issues
        
    Returns:
        Cleaned JSON string ready for parsing
    """
    if not json_string or json_string.strip() == "":
        return "{}"
    
    # Remove BOM if present
    json_string = json_string.lstrip('\ufeff')
    
    # Strip leading and trailing whitespace
    json_string = json_string.strip()
    
    # If it's already valid JSON, return as-is
    try:
        json.loads(json_string)
        # Try to load json and print response
        return json_string
    except (json.JSONDecodeError, ValueError):
        pass
    
    # If all preprocessing fails, return original for proper error reporting
    return json_string


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
        
    # Load configuration for output formatting
    csv_function = None
    output_format = getattr(args, 'format', None)
    raw_output = getattr(args, 'raw_output', False)
    default_override = None

    try:
        settings = loadJSON("clisettings.json")
        csv_supported_operations = settings.get("queryOperationCsvOutput", {})
        default_overrides = settings.get("queryOperationDefaultFormatOverrides", {})
        default_override = default_overrides.get(operation_name)
    except Exception as e:
        csv_supported_operations = {}
        default_override = None

    # Determine effective format
    # Priority: -raw flag -> raw/original; -f -> explicit; config override -> default; fallback -> json
    effective_format = 'json'
    if raw_output:
        effective_format = 'raw'
    elif output_format in ['json', 'csv']:
        effective_format = output_format
    elif default_override and default_override.get('enabled'):
        effective_format = default_override.get('default_format', 'json')

    # If CSV requested, validate support - check both new and legacy systems
    if effective_format == 'csv':
        # First check new format override system
        if default_override and default_override.get('format_function'):
            csv_function = default_override.get('format_function')
        else:
            # Fallback to legacy CSV system for backward compatibility
            csv_function = csv_supported_operations.get(operation_name)
        
        if not csv_function:
            # List all operations that support CSV from both systems
            supported_ops = list(csv_supported_operations.keys())
            if default_overrides:
                for op_name, config in default_overrides.items():
                    if config.get('enabled') and config.get('format_function'):
                        supported_ops.append(op_name)
            
            print(f"ERROR: CSV output not supported for operation '{operation_name}'")
            print(f"Supported CSV operations: {sorted(list(set(supported_ops))) if supported_ops else 'none'}")
            return None
        
    variables_obj = {}
    
    # Parse JSON input with robust preprocessing and error handling
    if params["json"]:
        try:
            # Preprocess JSON to handle formatting issues from different shells
            preprocessed_json = preprocess_json_input(params["json"])
            variables_obj = json.loads(preprocessed_json)
            if not isinstance(variables_obj, dict):
                print("ERROR: JSON input must be an object/dictionary")
                return None
        except ValueError as e:
            print(f"ERROR: Invalid JSON syntax: {e}")
            print(f"Raw input received (first 200 chars): {repr(params['json'][:200])}")
            print(f"After preprocessing (first 200 chars): {repr(preprocessed_json[:200])}")
            print("Example: '{\"yourKey\":\"yourValue\"}'")
            return None
        except Exception as e:
            print(f"ERROR: Unexpected error parsing JSON: {e}")
            print(f"Input received: {params['json'][:100]}{'...' if len(params['json']) > 100 else ''}")
            return None
    else:
        # Default to empty object if no json provided
        variables_obj = {}
    
    # Handle variable name mapping for XDR stories
    if operation_name == "query.xdr.stories" and "storyInput" in variables_obj:
        story_input = variables_obj["storyInput"]
        # Map storyFilterInput to filter if needed
        if "storyFilterInput" in story_input:
            story_input["filter"] = story_input.pop("storyFilterInput")
        # Map pagingInput to paging if needed
        if "pagingInput" in story_input:
            story_input["paging"] = story_input.pop("pagingInput")
    
    # Handle account ID for different operation types
    # IMPORTANT: Add account ID to variables_obj, don't replace it
    if operation_name in ["query.eventsFeed", "query.auditFeed"]:
        # Only add accountIDs if not already provided in JSON
        if "accountIDs" not in variables_obj:
            variables_obj["accountIDs"] = [configuration.accountID]
    elif "accountId" in operation.get("args", {}):
        # Only add accountId if not already provided in JSON
        if "accountId" not in variables_obj:
            variables_obj["accountId"] = configuration.accountID
    else:
        # Only add accountID if not already provided in JSON
        if "accountID" not in variables_obj:
            variables_obj["accountID"] = configuration.accountID
    
    # Validation logic
    if params["t"] or params.get("skip_validation", False):
        # Skip validation when using -t flag or --skip-validation flag
        is_ok = True
    else:
        is_ok, invalid_vars, message = validateArgs(variables_obj, operation)
    
    if is_ok:
        body = generateGraphqlPayload_local(variables_obj, operation, operation_name)
        
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
                    
                    # Return None to prevent JSON output to stdout when streaming to network/sentinel
                    return None
                
                # Apply formatting based on effective format
                if effective_format == 'raw' or not default_override:
                    # Raw format - return only the data portion, not HTTP headers/status
                    # UNLESS verbose mode is enabled, in which case we need the full response for header printing
                    verbose_mode = params.get('v', False)
                    if verbose_mode:
                        # In verbose mode, preserve the full response tuple [data, status, headers]
                        return response
                    elif isinstance(response, (list, tuple)) and len(response) > 0:
                        return response[0]  # Extract just the data portion
                    else:
                        return response
                elif effective_format == 'csv' and csv_function and response:
                    # CSV formatting requested
                    try:
                        # Get the response data (handle both list and tuple responses)
                        if isinstance(response, (list, tuple)) and len(response) > 0:
                            response_data = response[0]
                        else:
                            response_data = response
                        
                        # Add Utils directory to path and import formatter_utils
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        utils_dir = os.path.join(os.path.dirname(current_dir), 'Utils')
                        if utils_dir not in sys.path:
                            sys.path.insert(0, utils_dir)
                        
                        # Import the formatter_utils module
                        import formatter_utils
                        
                        # Use the centralized format_to_csv function
                        csv_output = None
                        if hasattr(formatter_utils, 'format_to_csv'):
                            # Use format_to_csv with the operation name
                            csv_output = formatter_utils.format_to_csv(response_data, operation_name)
                        elif hasattr(formatter_utils, csv_function):
                            # Fallback to direct function call for legacy support
                            csv_formatter_func = getattr(formatter_utils, csv_function)
                            
                            # Check if this is a new format function that takes output_format parameter
                            if default_override and default_override.get('format_function') == csv_function:
                                # New format functions that support output_format parameter
                                csv_output = csv_formatter_func(response_data, output_format='csv')
                            else:
                                # Legacy CSV functions that only take response_data
                                csv_output = csv_formatter_func(response_data)
                        else:
                            # CSV formatter function not found
                            print(f"ERROR: CSV formatter function '{csv_function}' not found")
                            # Return clean error response instead of raw response with HTTP headers
                            return [{"error": f"CSV formatter function '{csv_function}' not found", "operation": operation_name, "success": False}]
                        
                        # Handle CSV output regardless of which formatter path was used
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
                            # Normalize path separators for better cross-platform display
                            display_path = output_path.replace(os.sep, '/')
                            return [{"success": True, "output_file": display_path, "operation": operation_name}]
                        elif csv_output is None:
                            # Formatter returned None, indicating we should fall back to raw response
                            print("INFO: No processable data found, returning raw API response")
                            # Extract just the data portion to avoid HTTP headers
                            if isinstance(response, (list, tuple)) and len(response) > 0:
                                return response[0]
                            else:
                                return response
                        else:
                            print("WARNING: CSV formatter returned empty result - no data available for the specified criteria")
                            # Return clean error response instead of raw response with HTTP headers
                            return [{"error": "No data available for CSV export", "operation": operation_name, "success": False}]
                    except Exception as e:
                        print(f"ERROR: Failed to format CSV output: {e}")
                        # Return clean error response instead of raw response with HTTP headers
                        return [{"error": f"Failed to format CSV output: {str(e)}", "operation": operation_name, "success": False}]
                elif effective_format == 'json' and default_override and default_override.get('format_function') and response:
                    # Enhanced JSON formatting requested
                    try:
                        # Get the response data (handle both list and tuple responses)
                        if isinstance(response, (list, tuple)) and len(response) > 0:
                            response_data = response[0]
                        else:
                            response_data = response
                        
                        # Add Utils directory to path and import formatter_utils module for format functions
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        utils_dir = os.path.join(os.path.dirname(current_dir), 'Utils')
                        if utils_dir not in sys.path:
                            sys.path.insert(0, utils_dir)
                        
                        # Import the formatter_utils module (which contains format functions)
                        import formatter_utils
                        
                        # Use the centralized format_to_csv function which can handle JSON output too
                        format_function = default_override.get('format_function')
                        if hasattr(formatter_utils, 'format_to_csv'):
                            # The individual formatters handle JSON output internally when called from format_to_csv
                            # We need to directly call the specific formatter for JSON output
                            try:
                                # Dynamic import of the specific formatter function
                                if format_function == 'format_app_stats':
                                    from formatter_app_stats import format_app_stats
                                    formatted_output = format_app_stats(response_data, output_format='json')
                                elif format_function == 'format_app_stats_timeseries':
                                    from formatter_app_stats_timeseries import format_app_stats_timeseries
                                    formatted_output = format_app_stats_timeseries(response_data, output_format='json')
                                elif format_function == 'format_account_metrics':
                                    from formatter_account_metrics import format_account_metrics
                                    formatted_output = format_account_metrics(response_data, output_format='json')
                                elif format_function == 'format_socket_port_metrics_timeseries':
                                    from formatter_socket_port_metrics_timeseries import format_socket_port_metrics_timeseries
                                    formatted_output = format_socket_port_metrics_timeseries(response_data, output_format='json')
                                elif format_function == 'format_events_timeseries':
                                    from formatter_events_timeseries import format_events_timeseries
                                    formatted_output = format_events_timeseries(response_data, output_format='json')
                                else:
                                    formatted_output = None
                            except ImportError:
                                formatted_output = None
                            
                            # Handle the formatted output from individual formatters
                            if formatted_output is None:
                                # Formatter returned None, indicating we should fall back to raw response
                                print("INFO: No processable data found, returning raw API response")
                                return response_data
                            else:
                                # Pretty print the formatted JSON directly to stdout
                                print(formatted_output)
                                return None  # Return None to prevent further processing/output
                        elif hasattr(formatter_utils, format_function):
                            formatter_func = getattr(formatter_utils, format_function)
                            formatted_output = formatter_func(response_data, output_format='json')
                            
                            if formatted_output is None:
                                # Formatter returned None, indicating we should fall back to raw response
                                print("INFO: No processable data found, returning raw API response")
                                return response_data
                            else:
                                # Pretty print the formatted JSON directly to stdout
                                print(formatted_output)
                                return None  # Return None to prevent further processing/output
                        else:
                            print(f"WARNING: Formatter function '{format_function}' not found, using original response")
                            return response
                    except Exception as e:
                        print(f"ERROR: Failed to apply enhanced JSON formatting: {e}")
                        # Instead of returning the raw response which may contain non-serializable objects,
                        # extract just the JSON data portion to avoid HTTPHeaderDict serialization errors
                        try:
                            if isinstance(response, (list, tuple)) and len(response) > 0:
                                response_data = response[0]
                            else:
                                response_data = response
                            return response_data
                        except Exception:
                            # If we can't extract data safely, return a minimal error response
                            return [{"error": "Failed to format response and fallback failed", "original_error": str(e)}]
                
                return response
                
            except ApiException as e:
                return e
    else:
        print(f"ERROR: {message}")
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
    
    # Load the site location data (not the model definition) with proper UTF-8 encoding
    try:
        import os
        import json
        # Find the full path to the models directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(os.path.dirname(current_dir))
        models_file = os.path.join(root_dir, "models", f"{operation_name}.json")
        
        # Load with explicit UTF-8 encoding to fix Windows charmap issues
        with open(models_file, 'r', encoding='utf-8') as f:
            site_data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load site location data: {e}")
        return None
        
    try:
        # Use the same robust JSON preprocessing as other functions
        preprocessed_json = preprocess_json_input(params["json"])
        variables_obj = json.loads(preprocessed_json)
    except ValueError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        print(f"Raw input received (first 200 chars): {repr(params['json'][:200])}")
        print(f"After preprocessing (first 200 chars): {repr(preprocessed_json[:200])}")
        pretty_example = {
            "filters": [
                {
                    "search": "Your city here",
                    "field": "city",
                    "operation": "exact"
                }
            ]
        }
        print(f"Example: catocli query siteLocation '{json.dumps(pretty_example, indent=2)}' -p")
        return None
        
    # Validate filters structure
    if not variables_obj.get("filters"):
        print("ERROR: Missing 'filters' array in request")
        pretty_example = {
            "filters": [
                {
                    "search": "Your city here",
                    "field": "city",
                    "operation": "exact"
                }
            ]
        }
        print(f"Example: catocli query siteLocation '{json.dumps(pretty_example, indent=2)}' -p")
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
        # Use the same robust JSON preprocessing as other functions
        preprocessed_json = preprocess_json_input(params["json"])
        body = json.loads(preprocessed_json)
        
        # Validate GraphQL request structure
        if not isinstance(body, dict):
            print("ERROR: Request must be a JSON object")
            return None
            
        if "query" not in body:
            print("ERROR: Request must contain a 'query' field")
            return None
            
    except ValueError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        print(f"Attempted to parse: {params['json'][:100]}{'...' if len(params['json']) > 100 else ''}")
        return None
    except Exception as e:
        print(f"ERROR: Unexpected error parsing request: {e}")
        print(f"Input received: {params['json'][:100]}{'...' if len(params['json']) > 100 else ''}")
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


def collectUsedVariables(variables_obj, definition):
    """
    Recursively collect all variables that are used in the GraphQL query fields
    
    Args:
        variables_obj: Variables available for the query
        definition: Field definition to analyze
        
    Returns:
        Set of variable names that are used in the query
    """
    used_variables = set()
    
    if not definition or not isinstance(definition, dict) or 'fields' not in definition:
        return used_variables
    
    for field_name in definition['fields']:
        field = definition['fields'][field_name]
        
        # Check if field has arguments that use variables (with actual values)
        if field.get("args") and not isinstance(field['args'], list):
            for arg_name in field['args']:
                arg = field['args'][arg_name]
                # Only collect variables that have actual values (not empty/null)
                if arg["varName"] in variables_obj and variables_obj[arg["varName"]] is not None and variables_obj[arg["varName"]] != "" and variables_obj[arg["varName"]] != [] and variables_obj[arg["varName"]] != {}:
                    used_variables.add(arg["varName"])
        
        # Recursively check nested fields
        if field.get("type") and field['type'].get('definition'):
            if field['type']['definition'].get('fields'):
                used_variables.update(collectUsedVariables(variables_obj, field['type']['definition']))
            elif field['type']['definition'].get('inputFields'):
                # Handle inputFields as well
                nested_def = field['type']['definition']
                for subfield_name in nested_def.get('inputFields', {}):
                    subfield = nested_def['inputFields'][subfield_name]
                    if subfield.get('type') and subfield['type'].get('definition'):
                        used_variables.update(collectUsedVariables(variables_obj, subfield['type']['definition']))
    
    return used_variables


def generateGraphqlPayload_local(variables_obj, operation, operation_name):
    """
    Local wrapper around the shared GraphQL payload generation function.
    
    This wrapper provides the renderArgsAndFields function and custom_client to the shared implementation.
    """
    # Define a local renderArgsAndFields function that passes custom_client
    def local_renderArgsAndFields(response_arg_str, variables_obj, cur_operation, definition, operation_name, indent, dynamic_operation_args=None):
        return renderArgsAndFields(response_arg_str, variables_obj, cur_operation, definition, operation_name, indent, dynamic_operation_args, custom_client)
    
    # Call the shared implementation with the local renderArgsAndFields function
    return generateGraphqlPayload(
        variables_obj, 
        operation, 
        operation_name, 
        renderArgsAndFields_func=local_renderArgsAndFields
    )

def get_help(path):
    """
    Enhanced help generation with comprehensive README parsing
    Supports extracting multi-line JSON examples including -p formatted ones
    """
    try:
        # Import the universal help formatter
        from ..Utils.help_formatter import get_universal_help
        
        # Use auto mode for catolib-generated commands to enable schema-based examples
        help_source = "auto" if ('query_' in path or 'mutation_' in path) else "readme"
        return get_universal_help(path, help_source)
    except ImportError:
        # Fallback to enhanced local implementation if import fails
        return get_help_enhanced(path)

def get_help_enhanced(path):
    """
    Enhanced local help generation with better README parsing
    Specifically extracts comprehensive JSON examples from README files
    """
    match_cmd = f"catocli {path.replace('_', ' ')}"
    pwd = os.path.dirname(__file__)
    doc = f"{path}/README.md"
    abs_path = os.path.join(pwd, doc)
    
    # If not found, try custom path (for commands like query_eventsFeed)
    if not os.path.exists(abs_path):
        custom_doc = f"custom/{path}/README.md"
        custom_abs_path = os.path.join(pwd, custom_doc)
        if os.path.exists(custom_abs_path):
            abs_path = custom_abs_path
    
    try:
        with open(abs_path, "r", encoding='utf-8') as f:
            content = f.read()
        
        examples = []
        
        # Extract ALL commands in backticks that match our command
        import re
        # Look for commands in backticks - use non-greedy matching
        backtick_pattern = r'`(catocli[^`]+)`'
        backtick_matches = re.findall(backtick_pattern, content)
        
        for cmd in backtick_matches:
            if match_cmd in cmd and '{' in cmd:
                # This is a command with JSON - add it to examples
                examples.append(cmd.strip())
        
        # If we found comprehensive examples, format them nicely
        if examples:
            result = "\n"
            for i, example in enumerate(examples):
                if i > 0:  # Add spacing between examples
                    result += "\n"
                result += f"{example}\n"
            
            # Add platform-specific hints for macOS/Unix
            result += "\nTIP: Multi-line JSON is fully supported in Unix shells.\n"
            return result
        else:
            # No JSON examples found, look for any examples with our command
            simple_examples = []
            for cmd in backtick_matches:
                if match_cmd in cmd:
                    simple_examples.append(cmd.strip())
            
            if simple_examples:
                result = "\n"
                for example in simple_examples:
                    result += f"{example}\n"
                result += "\nTIP: Multi-line JSON is fully supported in Unix shells.\n"
                return result
            else:
                # No examples found at all
                return f"\nUsage: {match_cmd} <json> [options]\nUse {match_cmd} -h for detailed help.\n"
            
    except FileNotFoundError:
        return f"\nUsage: {match_cmd} <json> [options]\nUse {match_cmd} -h for detailed help.\n"
    except Exception as e:
        return f"\nError loading help: {e}\nUsage: {match_cmd} <json> [options]\n"

def expandUnionFragment(union_type_name, introspection_types, indent):
    """Expand a union type into its full field structure"""
    if union_type_name not in introspection_types:
        return ""
    
    type_def = introspection_types[union_type_name]
    if type_def['kind'] != 'OBJECT' or not type_def.get('fields'):
        return ""
    
    fragment_str = ""
    for field in type_def['fields']:
        field_name = field['name']
        fragment_str += f"{indent}\t\t{field_name}"
        
        # Handle nested object fields
        if field['type']['kind'] == 'OBJECT' or (field['type']['kind'] == 'NON_NULL' and field['type']['ofType']['kind'] == 'OBJECT'):
            nested_type_name = field['type']['name'] if field['type']['kind'] == 'OBJECT' else field['type']['ofType']['name']
            if nested_type_name in introspection_types:
                nested_def = introspection_types[nested_type_name]
                if nested_def.get('fields'):
                    fragment_str += " {\n"
                    for nested_field in nested_def['fields']:
                        fragment_str += f"{indent}\t\t\t{nested_field['name']}\n"
                    fragment_str += f"{indent}\t\t}}"
        
        # Handle list types
        elif field['type']['kind'] == 'LIST' or (field['type']['kind'] == 'NON_NULL' and field['type']['ofType']['kind'] == 'LIST'):
            list_type = field['type']['ofType'] if field['type']['kind'] == 'NON_NULL' else field['type']
            if list_type['ofType']['kind'] == 'OBJECT':
                nested_type_name = list_type['ofType']['name']
                if nested_type_name in introspection_types:
                    nested_def = introspection_types[nested_type_name]
                    if nested_def.get('fields'):
                        fragment_str += " {\n"
                        for nested_field in nested_def['fields']:
                            fragment_str += f"{indent}\t\t\t{nested_field['name']}\n"
                        fragment_str += f"{indent}\t\t}}"
        
        fragment_str += "\n"
    
    return fragment_str

def should_skip_complex_field(field):
    """
    Determine if a field should be skipped because it's a complex object type
    that would require subfield selections but doesn't have proper definitions
    
    Args:
        field: Field definition from the GraphQL schema
        
    Returns:
        bool: True if field should be skipped, False otherwise
    """
    if not field.get('type'):
        return False
    
    field_type = field['type']
    
    # Check if this is a direct object type or list of objects that needs subfields
    # but doesn't have proper field definitions to expand
    if field_type.get('kind'):
        kind = field_type['kind']
        
        # Handle both single kind and array of kinds
        if isinstance(kind, list):
            # Check for OBJECT or LIST containing OBJECT types
            has_object = 'OBJECT' in kind
            has_list = 'LIST' in kind
            
            # If it's an object or list of objects
            if has_object or has_list:
                # Check if we have proper field definitions to expand
                definition = field_type.get('definition')
                if not definition or not definition.get('fields'):
                    # This is a complex type without proper subfield definitions - skip it
                    return True
        elif isinstance(kind, str):
            # Single kind - check if it's OBJECT
            if kind == 'OBJECT':
                definition = field_type.get('definition')
                if not definition or not definition.get('fields'):
                    return True
    
    return False


# postProcessBareComplexFields is imported from shared utilities
def postProcessBareComplexFields_local_backup(field_selection_str, base_indent):
    """Post-process the generated field selection to expand any bare complex fields.
    
    This function scans the field selection string for fields that appear as bare fields
    but actually need subfield selections based on introspection data.
    
    Args:
        field_selection_str: The generated field selection string
        base_indent: The base indentation level
    
    Returns:
        Field selection string with all complex fields properly expanded
    """
    try:
        introspection_types = loadIntrospectionTypes()
    except:
        return field_selection_str  # Return unchanged if introspection fails
    
    if not introspection_types:
        return field_selection_str
    
    # Common complex field names that often need expansion
    complex_fields_to_check = [
        'threatType', 'similarStoriesData', 'osDetails', 'loggedOnUsers', 'rbacGroup', 'alerts',
        'drillDownFilter', 'extra', 'mitres', 'timeSeries', 'targets', 'events', 'flows',
        'threatPreventionsEvents', 'networkIncidentTimeline', 'linkDetails', 'ispDetails', 
        'contacts', 'incidentTimeline', 'analystFeedback', 'device', 'site', 'user',
        'bgpConnection', 'ilmmDetails', 'accountOperationIncident'
    ]
    
    lines = field_selection_str.split('\n')
    processed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        line_expanded = False
        
        # Check each complex field
        for field_name in complex_fields_to_check:
            # Check if this line contains a bare field (ends with field name, no { after it)
            if (field_name in line and 
                line.strip().endswith(field_name) and 
                '{' not in line and 
                not line.strip().endswith(':')):
                
                # Determine indentation
                indent_match = len(line) - len(line.lstrip())
                current_indent = '\t' * (indent_match // 4)  # Convert spaces to tabs
                
                # Find the type name for this field in introspection data
                field_type_candidates = [
                    'AnalystFeedbackThreatType',  # threatType
                    'SimilarStoryData',           # similarStoriesData  
                    'OsDetails',                  # osDetails
                    'EndpointUser',               # loggedOnUsers
                    'RbacGroup',                  # rbacGroup
                    'MicrosoftDefenderEndpointAlert',  # alerts (Microsoft)
                    'CatoEndpointAlert',          # alerts (Cato)
                    'StoryDrillDownFilter',       # drillDownFilter
                    'Extra',                      # extra
                    'Mitre',                      # mitres
                    'IncidentTimeseries',         # timeSeries
                    'IncidentTargetRep',          # targets
                    'Event',                      # events
                    'IncidentFlow',               # flows
                    'ThreatPreventionEvents',     # threatPreventionsEvents
                    'NetworkTimelineEvent',       # networkIncidentTimeline
                    'IlmmLinkDetails',            # linkDetails
                    'IlmmIspDetails',             # ispDetails
                    'IlmmContact',                # contacts
                    'AccountOperationsTimelineBase', # incidentTimeline
                    'DeviceRef',                  # device
                    'SiteRef',                    # site
                    'UserRef',                    # user
                    'BgpConnection',              # bgpConnection
                    'IlmmDetails',                # ilmmDetails
                    'AccountOperationIncident'    # accountOperationIncident
                ]
                
                # Try to find matching type for expansion based on field name
                expansion = ""
                
                # Create a more specific mapping of field names to types
                field_type_mapping = {
                    'threatType': 'AnalystFeedbackThreatType',
                    'similarStoriesData': 'SimilarStoryData',
                    'osDetails': 'OsDetails',
                    'loggedOnUsers': 'EndpointUser',
                    'rbacGroup': 'RbacGroup',
                    'alerts': ['MicrosoftDefenderEndpointAlert', 'CatoEndpointAlert'],
                    'drillDownFilter': 'StoryDrillDownFilter',
                    'extra': 'Extra',
                    'mitres': 'Mitre',
                    'timeSeries': 'IncidentTimeseries',
                    'targets': 'IncidentTargetRep',
                    'events': 'Event',
                    'flows': 'IncidentFlow',
                    'threatPreventionsEvents': 'ThreatPreventionEvents',
                    'networkIncidentTimeline': 'NetworkTimelineEvent',
                    'linkDetails': 'IlmmLinkDetails',
                    'ispDetails': 'IlmmIspDetails',
                    'contacts': 'IlmmContact',
                    'incidentTimeline': 'AccountOperationsTimelineBase',
                    'device': 'DeviceRef',
                    'site': 'SiteRef', 
                    'user': 'UserRef',
                    'bgpConnection': 'BgpConnection',
                    'ilmmDetails': 'IlmmDetails'
                }
                
                # Get the correct type name for this field
                candidate_types = []
                if field_name in field_type_mapping:
                    mapping = field_type_mapping[field_name]
                    if isinstance(mapping, list):
                        candidate_types = mapping
                    else:
                        candidate_types = [mapping]
                
                # Try each candidate type
                for candidate_type in candidate_types:
                    if candidate_type in introspection_types:
                        type_def = introspection_types[candidate_type]
                        if type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                            expansion = expandFieldWithIntrospection(field_name, candidate_type, current_indent)
                            if expansion:
                                break
                
                # If we found an expansion, replace the bare field
                if expansion:
                    # Create the expanded field
                    expanded_field = f"{current_indent}{field_name} {{\n{expansion}{current_indent}}}\n"
                    processed_lines.append(expanded_field)
                    line_expanded = True
                    break
        
        # If line wasn't expanded, keep it as is
        if not line_expanded:
            processed_lines.append(line + '\n' if not line.endswith('\n') else line)
        
        i += 1
    
    return ''.join(processed_lines).rstrip() + ('\n' if field_selection_str.endswith('\n') else '')


# expandFieldWithIntrospection is imported from shared utilities
def expandFieldWithIntrospection_local_backup(field_name, field_type_name, indent, already_expanded_fields=None):
    """Use introspection data to expand a field that needs subfield selections.
    
    Enhanced version that provides comprehensive expansion for complex GraphQL types,
    with better handling of nested objects and lists.
    
    Args:
        field_name: The name of the field to expand
        field_type_name: The GraphQL type name for this field
        indent: Current indentation level
        already_expanded_fields: Set of field names already expanded to prevent cycles
    
    Returns:
        String containing the expanded field with its subfields, or empty string if not expandable
    """
    if already_expanded_fields is None:
        already_expanded_fields = set()
    
    if field_name in already_expanded_fields:
        return ""  # Prevent infinite recursion
    
    already_expanded_fields.add(field_name)
    
    # Load introspection data
    introspection_types = loadIntrospectionTypes()
    if field_type_name not in introspection_types:
        already_expanded_fields.remove(field_name)
        return ""  # Can't expand without introspection data
    
    type_def = introspection_types[field_type_name]
    
    # Only expand complex types
    if type_def.get('kind') not in ['OBJECT', 'INTERFACE', 'UNION']:
        already_expanded_fields.remove(field_name)
        return ""  # Simple types don't need expansion
    
    result = ""
    
    if type_def.get('kind') == 'OBJECT' and type_def.get('fields'):
        # Expand object fields with better handling of complex nested types
        simple_fields = []
        complex_fields = []
        
        for introspection_field in type_def['fields']:
            field_name_inner = introspection_field['name']
            field_type_info = introspection_field.get('type', {})
            
            # Navigate through type wrappers to find the core type
            current_type = field_type_info
            while current_type and current_type.get('ofType'):
                current_type = current_type['ofType']
            
            if current_type and current_type.get('kind'):
                if current_type['kind'] in ['SCALAR', 'ENUM']:
                    # Simple field - add directly
                    simple_fields.append(field_name_inner)
                elif current_type.get('name'):
                    # Complex field - check if it needs expansion
                    inner_type_name = current_type['name']
                    if inner_type_name in introspection_types:
                        inner_type_def = introspection_types[inner_type_name]
                        if inner_type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                            # This is a complex field that needs expansion
                            complex_fields.append((field_name_inner, inner_type_name))
                        else:
                            simple_fields.append(field_name_inner)
                    else:
                        simple_fields.append(field_name_inner)
            else:
                simple_fields.append(field_name_inner)
        
        # Add simple fields
        for simple_field in simple_fields:
            result += f"{indent}\t{simple_field}\n"
        
        # Add complex fields with recursive expansion (increased depth limit)
        for complex_field_name, complex_type_name in complex_fields:
            if complex_field_name not in already_expanded_fields and len(already_expanded_fields) < 6:  # Increased limit
                expansion = expandFieldWithIntrospection(complex_field_name, complex_type_name, indent + "\t", already_expanded_fields.copy())
                if expansion:
                    result += f"{indent}\t{complex_field_name} {{\n{expansion}{indent}\t}}\n"
                else:
                    # Fallback: add minimal expansion for known complex types
                    if complex_type_name in introspection_types:
                        complex_type_def = introspection_types[complex_type_name]
                        if complex_type_def.get('fields'):
                            # Add a simple expansion with key fields
                            result += f"{indent}\t{complex_field_name} {{\n"
                            # Add commonly expected fields for GraphQL objects
                            common_fields = ['id', 'name', 'value', 'type', 'status', 'description']
                            added_fields = []
                            for cf in complex_type_def['fields']:
                                if cf['name'] in common_fields:
                                    result += f"{indent}\t\t{cf['name']}\n"
                                    added_fields.append(cf['name'])
                            # If no common fields found, add first few fields
                            if not added_fields:
                                for cf in complex_type_def['fields'][:3]:
                                    field_type = cf.get('type', {})
                                    core_type = field_type
                                    while core_type and core_type.get('ofType'):
                                        core_type = core_type['ofType']
                                    if core_type and core_type.get('kind') in ['SCALAR', 'ENUM']:
                                        result += f"{indent}\t\t{cf['name']}\n"
                            result += f"{indent}\t}}\n"
                        else:
                            result += f"{indent}\t{complex_field_name}\n"
                    else:
                        result += f"{indent}\t{complex_field_name}\n"
            else:
                result += f"{indent}\t{complex_field_name}\n"
    
    elif type_def.get('kind') in ['INTERFACE', 'UNION'] and type_def.get('possibleTypes'):
        # Add __typename for interface/union types
        result += f"{indent}\t__typename\n"
        
        # Add inline fragments for each possible type (more comprehensive)
        for possible_type in type_def['possibleTypes']:
            possible_type_name = possible_type.get('name')
            if possible_type_name and possible_type_name in introspection_types:
                possible_type_def = introspection_types[possible_type_name]
                if possible_type_def.get('fields'):
                    result += f"{indent}\t... on {possible_type_name} {{\n"
                    
                    # Expand fields within this fragment (increased depth)
                    if len(already_expanded_fields) < 4:  # Increased fragment depth
                        for poss_field in possible_type_def['fields']:
                            poss_field_name = poss_field['name']
                            poss_field_type_info = poss_field.get('type', {})
                            
                            # Get the core type
                            current_type = poss_field_type_info
                            while current_type and current_type.get('ofType'):
                                current_type = current_type['ofType']
                            
                            if current_type and current_type.get('kind'):
                                if current_type['kind'] in ['SCALAR', 'ENUM']:
                                    result += f"{indent}\t\t{poss_field_name}\n"
                                elif current_type.get('name') and current_type['name'] in introspection_types:
                                    # Check if this field needs further expansion
                                    inner_type_def = introspection_types[current_type['name']]
                                    if inner_type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                                        # Recursively expand complex fields in fragments
                                        inner_expansion = expandFieldWithIntrospection(poss_field_name, current_type['name'], indent + "\t", already_expanded_fields.copy())
                                        if inner_expansion:
                                            result += f"{indent}\t\t{poss_field_name} {{\n{inner_expansion}{indent}\t\t}}\n"
                                        else:
                                            result += f"{indent}\t\t{poss_field_name}\n"
                                    else:
                                        result += f"{indent}\t\t{poss_field_name}\n"
                                else:
                                    result += f"{indent}\t\t{poss_field_name}\n"
                            else:
                                result += f"{indent}\t\t{poss_field_name}\n"
                    
                    result += f"{indent}\t}}\n"
    
    already_expanded_fields.remove(field_name)
    return result




# Binary/Multipart request functions (preserved from original)
def createRawBinaryRequest(args, configuration):
    """Handle multipart/form-data requests for file uploads and binary content"""
    params = vars(args)
    
    # Parse the JSON body with robust preprocessing
    try:
        preprocessed_json = preprocess_json_input(params["json"])
        body = json.loads(preprocessed_json)
    except ValueError as e:
        print(f"ERROR: JSON argument must be valid json: {e}")
        print(f"Attempted to parse: {params['json'][:100]}{'...' if len(params['json']) > 100 else ''}")
        return
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Input received: {params['json'][:100]}{'...' if len(params['json']) > 100 else ''}")
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
    
    # Parse input JSON variables with robust preprocessing
    try:
        json_input = params.get('json', '{}')
        preprocessed_json = preprocess_json_input(json_input)
        variables = json.loads(preprocessed_json)
    except ValueError as e:
        print(f"ERROR: Invalid JSON input: {e}")
        json_input = params.get('json', '{}')
        print(f"Attempted to parse: {json_input[:100]}{'...' if len(json_input) > 100 else ''}")
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
                            # Normalize path separators for better cross-platform display
                            display_path = output_path.replace(os.sep, '/')
                            return [{"success": True, "output_file": display_path, "operation": csv_operation, "private_command": private_command}]
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
