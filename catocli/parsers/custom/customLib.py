import os
import json
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
from ..parserApiClient import validateArgs

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