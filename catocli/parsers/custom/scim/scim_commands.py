#!/usr/bin/env python3
"""
SCIM command implementations for Cato CLI
Handles all SCIM user and group management operations
"""

import json
import sys
import csv
import os
from .scim_client import get_scim_client
from ...utils.export_utils import (
    generate_export_filename,
    resolve_export_path,
    write_json_export,
    write_csv_export,
    ensure_output_directory
)
from ....Utils.cliutils import get_package_resource


def handle_scim_error(error_message, verbose=False):
    """
    Handle SCIM errors with appropriate user messaging
    
    Args:
        error_message: The error message to display
        verbose: Whether to show verbose error output
    
    Returns:
        List containing error response for CLI output
    """
    if verbose:
        print(f"SCIM Error: {error_message}", file=sys.stderr)
    
    return [{"success": False, "error": str(error_message)}]


def format_scim_response(success, data, operation, verbose=False, pretty=False):
    """
    Format SCIM API responses for CLI output
    
    Args:
        success: Boolean indicating if operation succeeded
        data: Response data from SCIM API
        operation: Description of the operation performed
        verbose: Whether to show verbose output
        pretty: Whether to pretty print JSON
    
    Returns:
        List containing formatted response for CLI output
    """
    if not success:
        error_msg = data.get('error', str(data))
        if verbose:
            print(f"SCIM {operation} failed: {error_msg}", file=sys.stderr)
        return [{"success": False, "error": error_msg, "operation": operation}]
    
    if verbose:
        print(f"SCIM {operation} completed successfully", file=sys.stderr)
    
    response = {
        "success": True,
        "operation": operation,
        "data": data
    }
    
    return [response]


def get_json_input(args):
    """
    Get JSON input from arguments, with support for multi-line interactive input when -p flag is used.
    
    Args:
        args: Command line arguments object
        
    Returns:
        tuple: (json_data, error_message)
               json_data is the parsed JSON object or None if error
               error_message is the error string or None if successful
    """
    try:
        # Handle interactive multi-line JSON input when -p flag is used
        json_input = getattr(args, 'json_input', '{}')
        
        if hasattr(args, 'pretty') and args.pretty:
            print("Enter JSON input (press Enter on a blank line to finish):")
            lines = []
            try:
                while True:
                    line = input()
                    if line.strip() == "":
                        break
                    lines.append(line)
                json_input = '\n'.join(lines)
                if not json_input.strip():
                    json_input = '{}'
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                return None, "Input cancelled by user"
        
        # Parse JSON input
        try:
            json_data = json.loads(json_input)
            return json_data, None
        except json.JSONDecodeError as e:
            return None, f"Invalid JSON input: {e}"
            
    except Exception as e:
        return None, f"Error processing JSON input: {e}"


def scim_add_members(args, configuration=None):
    """Add members to an existing SCIM group"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        members = json_data.get('members')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        if not members:
            return handle_scim_error("Missing required field: members", args.verbose)
        
        # Validate members format
        if not isinstance(members, list):
            return handle_scim_error("Members must be a JSON array", args.verbose)
        
        for member in members:
            if not isinstance(member, dict) or 'value' not in member:
                return handle_scim_error("Each member must be an object with a 'value' field", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.add_members(group_id, members)
        
        return format_scim_response(
            success, result, f"Add members to group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_create_group(args, configuration=None):
    """Create a new SCIM group"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract group properties - support both displayName and display_name formats
        display_name = json_data.get('displayName') or json_data.get('display_name')
        external_id = json_data.get('externalId') or json_data.get('external_id')
        
        # Validate required fields
        if not display_name:
            return handle_scim_error("Missing required field: displayName (or display_name)", args.verbose)
        if not external_id:
            return handle_scim_error("Missing required field: externalId (or external_id)", args.verbose)
        
        # Handle members array
        members = json_data.get('members', [])
        if members:
            if not isinstance(members, list):
                return handle_scim_error("Members must be a JSON array", args.verbose)
            
            # Validate and normalize members format
            normalized_members = []
            for i, member in enumerate(members):
                if isinstance(member, str):
                    # Convert string ID to proper member object
                    normalized_members.append({"value": member})
                elif isinstance(member, dict):
                    if 'value' not in member:
                        return handle_scim_error(f"Member {i+1} must have a 'value' field", args.verbose)
                    normalized_members.append(member)
                else:
                    return handle_scim_error(f"Member {i+1} must be a string ID or object with 'value' field", args.verbose)
            
            members = normalized_members
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        
        # Check if SCIM client is configured
        if client is None:
            return handle_scim_error(
                "SCIM client is not configured. Please ensure your SCIM credentials are set up correctly.\n"
                "Run 'catocli configure scim' to configure SCIM credentials, or\n"
                "Check your ~/.cato/settings.json file for 'scim_url' and 'scim_token' settings.\n"
                "For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps",
                args.verbose
            )
        
        success, result = client.create_group(display_name, external_id, members)
        
        return format_scim_response(
            success, result, f"Create group '{display_name}'",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_create_user(args, configuration=None):
    """Create a new SCIM user with full UserDTO schema support"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        source_id = json_data.get('source_id')
        
        # Extract user data (can be in 'user_data' field or directly in json_data)
        user_data = json_data.get('user_data', json_data)
        
        # Get accountID from configuration
        account_id = getattr(args, 'accountID', None) or getattr(configuration, 'accountID', None) if configuration else None
        
        if not account_id:
            return handle_scim_error("Missing accountID. Please ensure your Cato configuration is set up correctly.", args.verbose)
        if not source_id:
            return handle_scim_error("Missing required field: source_id", args.verbose)
        
        # Build complete UserDTO according to swagger schema
        user_dto = {
            "schemas": user_data.get('schemas', ["urn:ietf:params:scim:schemas:core:2.0:User"]),
            "userName": user_data.get('userName') or user_data.get('email'),
            "externalId": user_data.get('externalId') or user_data.get('external_id'),
            "active": user_data.get('active', True)
        }
        
        # Handle name object
        name_data = user_data.get('name', {})
        if user_data.get('given_name') or user_data.get('family_name'):
            name_data = {
                "givenName": user_data.get('given_name') or name_data.get('givenName'),
                "familyName": user_data.get('family_name') or name_data.get('familyName')
            }
        if name_data:
            user_dto["name"] = name_data
        
        # Handle emails array
        emails = user_data.get('emails', [])
        if not emails and user_data.get('email'):
            emails = [{
                "value": user_data.get('email'),
                "primary": True,
                "type": "work"
            }]
        if emails:
            user_dto["emails"] = emails
        
        # Handle phone numbers array
        phone_numbers = user_data.get('phoneNumbers', [])
        if phone_numbers:
            user_dto["phoneNumbers"] = phone_numbers
        
        # Handle Cato extension
        cato_extension = user_data.get('urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User')
        if cato_extension:
            user_dto["urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User"] = cato_extension
        
        # Validate required fields
        if not user_dto.get('userName'):
            return handle_scim_error("Missing required field: userName (or email)", args.verbose)
        if not user_dto.get('externalId'):
            return handle_scim_error("Missing required field: externalId (or external_id)", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        
        # Extract parameters for the existing create_user method
        email = user_dto.get('userName')
        given_name = user_dto.get('name', {}).get('givenName') or user_data.get('given_name')
        family_name = user_dto.get('name', {}).get('familyName') or user_data.get('family_name')
        external_id = user_dto.get('externalId')
        password = user_data.get('password')  # May be None
        active = user_dto.get('active', True)
        
        success, result = client.create_user(email, given_name, family_name, external_id, password, active)
        
        return format_scim_response(
            success, result, f"Create user '{user_dto.get('userName')}'",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_disable_group(args, configuration=None):
    """Disable a SCIM group"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.disable_group(group_id)
        
        return format_scim_response(
            success, result, f"Disable group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_disable_user(args, configuration=None):
    """Disable a SCIM user"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        user_id = json_data.get('user_id')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.disable_user(user_id)
        
        return format_scim_response(
            success, result, f"Disable user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_find_group(args, configuration=None):
    """Find SCIM groups by display name"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        display_name = json_data.get('display_name')
        
        if not display_name:
            return handle_scim_error("Missing required field: display_name", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.find_group(display_name)
        
        if success:
            # Format the results to show count
            formatted_result = {
                "groups_found": len(result),
                "groups": result
            }
            return format_scim_response(
                success, formatted_result, f"Find groups named '{display_name}'",
                args.verbose, args.pretty
            )
        else:
            return format_scim_response(
                success, result, f"Find groups named '{display_name}'",
                args.verbose, args.pretty
            )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_find_users(args, configuration=None):
    """Find SCIM users by field and value"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        field = json_data.get('field')
        value = json_data.get('value')
        
        if not field:
            return handle_scim_error("Missing required field: field", args.verbose)
        if not value:
            return handle_scim_error("Missing required field: value", args.verbose)
        
        # Validate field value
        valid_fields = ['userName', 'email', 'givenName', 'familyName', 'externalId']
        if field not in valid_fields:
            return handle_scim_error(f"Invalid field. Must be one of: {', '.join(valid_fields)}", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.find_users(field, value)
        
        if success:
            # Format the results to show count
            formatted_result = {
                "users_found": len(result),
                "search_field": field,
                "search_value": value,
                "users": result
            }
            return format_scim_response(
                success, formatted_result, f"Find users by {field}='{value}'",
                args.verbose, args.pretty
            )
        else:
            return format_scim_response(
                success, result, f"Find users by {field}='{value}'",
                args.verbose, args.pretty
            )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_get_group(args, configuration=None):
    """Get a specific SCIM group by ID"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.get_group(group_id)
        
        return format_scim_response(
            success, result, f"Get group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_get_groups(args, configuration=None):
    """Get all SCIM groups"""
    try:
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.get_groups()
        
        if success:
            # Format the results to show count
            formatted_result = {
                "total_groups": len(result),
                "groups": result
            }
            return format_scim_response(
                success, formatted_result, "Get all groups",
                args.verbose, args.pretty
            )
        else:
            return format_scim_response(
                success, result, "Get all groups",
                args.verbose, args.pretty
            )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_get_user(args, configuration=None):
    """Get a specific SCIM user by ID with full swagger parameter support"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        # Extract required path parameters
        user_id = json_data.get('user_id') or json_data.get('id')
        
        # Extract optional query parameters
        excluded_attributes = json_data.get('excluded_attributes')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id (or id)", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.get_user(user_id, excluded_attributes)
        
        return format_scim_response(
            success, result, f"Get user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_get_users(args, configuration=None):
    """Get all SCIM users with pagination and search support"""
    try:
        # Parse JSON input if provided, otherwise use empty dict
        json_data = {}
        if hasattr(args, 'json_input') and args.json_input:
            try:
                json_data = json.loads(args.json_input)
            except json.JSONDecodeError as e:
                return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Extract optional query parameters
        count = json_data.get('count')
        start_index = json_data.get('start_index') or json_data.get('startIndex')
        params = json_data.get('params', {})
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.get_users(count, start_index, params)
        
        if success:
            # Handle both direct array response and ListResponse format
            if isinstance(result, list):
                formatted_result = {
                    "total_users": len(result),
                    "users": result
                }
            else:
                # Handle ListResponseUserDTO format
                formatted_result = {
                    "total_results": result.get('totalResults', 0),
                    "start_index": result.get('startIndex', 1),
                    "items_per_page": result.get('itemsPerPage', len(result.get('Resources', []))),
                    "users": result.get('Resources', [])
                }
            return format_scim_response(
                success, formatted_result, "Get users",
                args.verbose, args.pretty
            )
        else:
            return format_scim_response(
                success, result, "Get users",
                args.verbose, args.pretty
            )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_remove_members(args, configuration=None):
    """Remove members from a SCIM group"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        members = json_data.get('members')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        if not members:
            return handle_scim_error("Missing required field: members", args.verbose)
        
        # Validate members format
        if not isinstance(members, list):
            return handle_scim_error("Members must be a JSON array", args.verbose)
        
        for member in members:
            if not isinstance(member, dict) or 'value' not in member:
                return handle_scim_error("Each member must be an object with a 'value' field", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.remove_members(group_id, members)
        
        return format_scim_response(
            success, result, f"Remove members from group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_rename_group(args, configuration=None):
    """Rename a SCIM group"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        new_name = json_data.get('new_name')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        if not new_name:
            return handle_scim_error("Missing required field: new_name", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.rename_group(group_id, new_name)
        
        return format_scim_response(
            success, result, f"Rename group {group_id} to '{new_name}'",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_update_group(args, configuration=None):
    """Update a SCIM group with complete group data"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        group_data = json_data.get('group_data')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        if not group_data:
            return handle_scim_error("Missing required field: group_data", args.verbose)
        
        # Validate group data format
        if not isinstance(group_data, dict):
            return handle_scim_error("Group data must be a JSON object", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.update_group(group_id, group_data)
        
        return format_scim_response(
            success, result, f"Update group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_update_user(args, configuration=None):
    """Update a SCIM user with complete user data (PUT operation)"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        user_id = json_data.get('user_id') or json_data.get('id')
        user_data = json_data.get('user_data', json_data)
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id (or id)", args.verbose)
        if not user_data:
            return handle_scim_error("Missing required field: user_data", args.verbose)
        
        # Validate user data format
        if not isinstance(user_data, dict):
            return handle_scim_error("User data must be a JSON object", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.update_user(user_id, user_data)
        
        return format_scim_response(
            success, result, f"Update user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_patch_user(args, configuration=None):
    """Patch a SCIM user with partial updates (PATCH operation)"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        user_id = json_data.get('user_id') or json_data.get('id')
        
        # Extract patch request data
        patch_data = json_data.get('patch_data', json_data)
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id (or id)", args.verbose)
        
        # Build PatchRequestDTO according to swagger schema
        patch_request = {
            "schemas": patch_data.get('schemas', ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]),
            "Operations": patch_data.get('Operations', [])
        }
        
        # If operations are provided directly, use them
        if 'operations' in patch_data:
            patch_request["Operations"] = patch_data['operations']
        
        # Validate operations format
        if not patch_request["Operations"]:
            return handle_scim_error("Missing required field: Operations (or operations)", args.verbose)
        
        if not isinstance(patch_request["Operations"], list):
            return handle_scim_error("Operations must be an array", args.verbose)
        
        # Validate each operation
        for i, op in enumerate(patch_request["Operations"]):
            if not isinstance(op, dict):
                return handle_scim_error(f"Operation {i+1} must be an object", args.verbose)
            if 'op' not in op:
                return handle_scim_error(f"Operation {i+1}: Missing required field 'op'", args.verbose)
            if op['op'] not in ['add', 'remove', 'replace']:
                return handle_scim_error(f"Operation {i+1}: Invalid operation '{op['op']}'. Must be 'add', 'remove', or 'replace'", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.patch_user(user_id, patch_request)
        
        return format_scim_response(
            success, result, f"Patch user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_delete_user(args, configuration=None):
    """Delete a SCIM user (DELETE operation)"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        user_id = json_data.get('user_id') or json_data.get('id')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id (or id)", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.delete_user(user_id)
        
        return format_scim_response(
            success, result, f"Delete user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_patch_group(args, configuration=None):
    """Patch a SCIM group with partial updates (PATCH operation)"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        group_id = json_data.get('group_id') or json_data.get('id')
        
        # Extract patch request data
        patch_data = json_data.get('patch_data', json_data)
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id (or id)", args.verbose)
        
        # Build PatchRequestDTO according to swagger schema
        patch_request = {
            "schemas": patch_data.get('schemas', ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]),
            "Operations": patch_data.get('Operations', [])
        }
        
        # If operations are provided directly, use them
        if 'operations' in patch_data:
            patch_request["Operations"] = patch_data['operations']
        
        # Validate operations format
        if not patch_request["Operations"]:
            return handle_scim_error("Missing required field: Operations (or operations)", args.verbose)
        
        if not isinstance(patch_request["Operations"], list):
            return handle_scim_error("Operations must be an array", args.verbose)
        
        # Validate each operation
        for i, op in enumerate(patch_request["Operations"]):
            if not isinstance(op, dict):
                return handle_scim_error(f"Operation {i+1} must be an object", args.verbose)
            if 'op' not in op:
                return handle_scim_error(f"Operation {i+1}: Missing required field 'op'", args.verbose)
            if op['op'] not in ['add', 'remove', 'replace']:
                return handle_scim_error(f"Operation {i+1}: Invalid operation '{op['op']}'. Must be 'add', 'remove', or 'replace'", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.patch_group(group_id, patch_request)
        
        return format_scim_response(
            success, result, f"Patch group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_delete_group(args, configuration=None):
    """Delete a SCIM group (DELETE operation)"""
    try:
        # Parse JSON input directly from args (like standard catocli commands)
        json_input = getattr(args, 'json_input', '{}')
        
        try:
            json_data = json.loads(json_input)
            if not isinstance(json_data, dict):
                return handle_scim_error("JSON input must be an object/dictionary", args.verbose)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON syntax: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
        
        # Extract required path parameters
        group_id = json_data.get('group_id') or json_data.get('id')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id (or id)", args.verbose)
        
        # Get SCIM client and execute operation
        # accountId and sourceId are automatically extracted from the SCIM URL in credentials
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        success, result = client.delete_group(group_id)
        
        return format_scim_response(
            success, result, f"Delete group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def _parse_csv_users(file_path, verbose=False):
    """
    Parse users from CSV file with support for user_id column to determine create vs update operations
    
    Returns:
        List of user dictionaries or error response
    """
    users_data = []
    required_columns = ['email', 'given_name', 'family_name', 'external_id']
    optional_columns = ['password', 'active', 'user_id']
    all_columns = required_columns + optional_columns
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Validate CSV headers
            if not reader.fieldnames:
                return handle_scim_error("CSV file has no headers", verbose)
            
            # Check for required columns
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                return handle_scim_error(f"Missing required CSV columns: {', '.join(missing_columns)}", verbose)
            
            # Check for unexpected columns
            unexpected_columns = [col for col in reader.fieldnames if col not in all_columns]
            if unexpected_columns and verbose:
                print(f"Warning: Unexpected CSV columns will be ignored: {', '.join(unexpected_columns)}", file=sys.stderr)
            
            # Read and validate each row
            for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is headers
                # Validate required fields
                missing_fields = []
                for field in required_columns:
                    if not row.get(field, '').strip():
                        missing_fields.append(field)
                
                if missing_fields:
                    return handle_scim_error(
                        f"Row {row_num}: Missing required fields: {', '.join(missing_fields)}", 
                        verbose
                    )
                
                # Parse and validate the 'active' field
                active_str = row.get('active', 'true').strip().lower()
                if active_str in ['true', '1', 'yes', 'y']:
                    active = True
                elif active_str in ['false', '0', 'no', 'n']:
                    active = False
                else:
                    active = True  # Default to true for invalid values
                    if verbose:
                        print(f"Warning: Row {row_num}: Invalid 'active' value '{row.get('active', '')}', defaulting to true", file=sys.stderr)
                
                # Check if user_id is present to determine create vs update operation
                user_id = row.get('user_id', '').strip()
                operation_type = 'update' if user_id else 'create'
                
                user_data = {
                    'email': row['email'].strip(),
                    'given_name': row['given_name'].strip(),
                    'family_name': row['family_name'].strip(),
                    'external_id': row['external_id'].strip(),
                    'password': row.get('password', '').strip() or None,  # Convert empty string to None
                    'active': active,
                    'user_id': user_id if user_id else None,
                    'operation_type': operation_type,
                    'row_number': row_num
                }
                
                users_data.append(user_data)
    
    except csv.Error as e:
        return handle_scim_error(f"Error reading CSV file: {e}", verbose)
    except Exception as e:
        return handle_scim_error(f"Error processing CSV file: {e}", verbose)
    
    return users_data


def _parse_json_users(file_path, verbose=False):
    """
    Parse users from JSON file
    
    Returns:
        List of user dictionaries or error response
    """
    required_fields = ['email', 'given_name', 'family_name', 'external_id']
    optional_fields = ['password', 'active', 'user_id']
    
    try:
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            try:
                data = json.load(jsonfile)
            except json.JSONDecodeError as e:
                return handle_scim_error(f"Invalid JSON file: {e}", verbose)
            
            # Handle both array of users and single user object
            if isinstance(data, dict):
                data = [data]  # Convert single user to array
            elif not isinstance(data, list):
                return handle_scim_error("JSON file must contain an array of user objects or a single user object", verbose)
            
            users_data = []
            for idx, user in enumerate(data, start=1):
                if not isinstance(user, dict):
                    return handle_scim_error(f"User {idx}: Must be a JSON object", verbose)
                
                # Check required fields
                missing_fields = [field for field in required_fields if not user.get(field, '').strip()]
                if missing_fields:
                    return handle_scim_error(
                        f"User {idx}: Missing required fields: {', '.join(missing_fields)}", 
                        verbose
                    )
                
                # Validate and normalize the active field
                active = user.get('active', True)
                if isinstance(active, str):
                    active_str = active.strip().lower()
                    if active_str in ['true', '1', 'yes', 'y']:
                        active = True
                    elif active_str in ['false', '0', 'no', 'n']:
                        active = False
                    else:
                        active = True  # Default to true
                        if verbose:
                            print(f"Warning: User {idx}: Invalid 'active' value '{user.get('active', '')}', defaulting to true", file=sys.stderr)
                elif not isinstance(active, bool):
                    active = True  # Default to true for non-boolean values
                    if verbose:
                        print(f"Warning: User {idx}: Non-boolean 'active' value, defaulting to true", file=sys.stderr)
                
                # Check if user_id is present to determine create vs update operation
                user_id = user.get('user_id', '').strip() if isinstance(user.get('user_id'), str) else user.get('user_id')
                user_id = user_id if user_id else None
                operation_type = 'update' if user_id else 'create'
                
                user_data = {
                    'email': user['email'].strip(),
                    'given_name': user['given_name'].strip(),
                    'family_name': user['family_name'].strip(),
                    'external_id': user['external_id'].strip(),
                    'password': user.get('password', '').strip() or None,
                    'active': active,
                    'user_id': user_id,
                    'operation_type': operation_type,
                    'row_number': idx
                }
                
                users_data.append(user_data)
    
    except Exception as e:
        return handle_scim_error(f"Error processing JSON file: {e}", verbose)
    
    return users_data


def _create_users_from_data(users_data, args):
    """
    Create or update users from parsed data using SCIM client
    Supports both create and update operations based on presence of user_id
    """
    # Get SCIM client
    client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
    
    # Process users and collect results
    results = []
    successful_users = []
    failed_users = []
    create_count = 0
    update_count = 0
    
    for user_data in users_data:
        row_num = user_data.pop('row_number')  # Remove row_number before API call
        operation_type = user_data.pop('operation_type', 'create')
        user_id = user_data.get('user_id')
        
        if hasattr(args, 'verbose') and args.verbose:
            operation_desc = "Updating" if operation_type == 'update' else "Creating"
            print(f"{operation_desc} user: {user_data['email']}", file=sys.stderr)
        
        try:
            if operation_type == 'update' and user_id:
                # Update existing user
                # Build user data for update in SCIM format
                scim_user_data = {
                    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
                    "userName": user_data['email'],
                    "name": {
                        "givenName": user_data['given_name'],
                        "familyName": user_data['family_name']
                    },
                    "emails": [
                        {
                            "primary": True,
                            "value": user_data['email']
                        }
                    ],
                    "externalId": user_data['external_id'],
                    "active": user_data['active']
                }
                
                # Only add password if provided
                if user_data['password']:
                    scim_user_data['password'] = user_data['password']
                
                success, result = client.update_user(user_id, scim_user_data)
                update_count += 1
            else:
                # Create new user
                success, result = client.create_user(
                    user_data['email'],
                    user_data['given_name'],
                    user_data['family_name'],
                    user_data['external_id'],
                    user_data['password'],
                    user_data['active']
                )
                create_count += 1
            
            user_result = {
                'row_number': row_num,
                'email': user_data['email'],
                'success': success,
                'operation': operation_type,
                'original_user_id': user_id  # Keep track of original user_id
            }
            
            if success:
                # Get user_id from result (for creates) or use existing (for updates)
                result_user_id = result.get('id', user_id)
                user_result['user_id'] = result_user_id
                
                # Update the original user_data with the user_id for processed CSV
                user_data['user_id'] = result_user_id
                
                if operation_type == 'update':
                    user_result['message'] = f"User '{user_data['email']}' updated successfully"
                else:
                    if user_data['active']:
                        user_result['message'] = f"User '{user_data['email']}' created successfully"
                    else:
                        user_result['message'] = f"User '{user_data['email']}' created successfully and disabled as requested"
                        if result.get('warning'):
                            user_result['warning'] = result['warning']
                successful_users.append(user_result)
            else:
                user_result['error'] = result.get('error', str(result))
                operation_desc = "update" if operation_type == 'update' else "create"
                user_result['message'] = f"Failed to {operation_desc} user '{user_data['email']}': {user_result['error']}"
                failed_users.append(user_result)
            
            results.append(user_result)
            
        except Exception as e:
            user_result = {
                'row_number': row_num,
                'email': user_data['email'],
                'success': False,
                'error': str(e),
                'message': f"Error creating user '{user_data['email']}': {str(e)}"
            }
            failed_users.append(user_result)
            results.append(user_result)
    
    # Write processed file if requested
    processed_file_path = None
    if hasattr(args, 'write_processed') and args.write_processed and hasattr(args, 'file_path'):
        # Determine file format from original file
        _, ext = os.path.splitext(args.file_path.lower())
        if ext == '.csv':
            processed_file_path = _write_processed_csv(users_data, args.file_path, results, args)
        elif ext in ['.json', '.jsonl']:
            processed_file_path = _write_processed_json(users_data, args.file_path, results, args)
        else:
            # Default to CSV if format can't be determined
            processed_file_path = _write_processed_csv(users_data, args.file_path, results, args)
    
    # Format final response
    summary = {
        'total_users': len(users_data),
        'created_users': create_count,
        'updated_users': update_count,
        'successful_users': len(successful_users),
        'failed_users': len(failed_users),
        'success_rate': f"{len(successful_users)}/{len(users_data)} ({len(successful_users)/len(users_data)*100:.1f}%)"
    }
    
    response = {
        'success': len(failed_users) == 0,  # Overall success only if no failures
        'operation': f"Import {len(users_data)} users ({create_count} created, {update_count} updated)",
        'summary': summary
    }
    
    if processed_file_path:
        response['processed_file'] = processed_file_path
    
    return [response]


def _write_processed_csv(users_data, original_file_path, results, args):
    """
    Write processed CSV file with updated user_ids from create/update operations
    
    Args:
        users_data: List of processed user data with updated user_ids
        original_file_path: Path to the original CSV file
        results: List of operation results
        args: Command line arguments
    
    Returns:
        Path to the processed CSV file
    """
    import datetime
    
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate processed filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = os.path.splitext(original_file_path)[0]
    processed_file_path = f"{base_path}_processed_{timestamp}.csv"
    
    if verbose:
        print(f"Writing processed CSV file: {processed_file_path}", file=sys.stderr)
    
    try:
        # Define fieldnames with user_id first
        fieldnames = ['user_id', 'email', 'given_name', 'family_name', 'external_id', 'password', 'active']
        
        with open(processed_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Write processed user data
            for user_data in users_data:
                # Create row with all required fields
                row = {
                    'user_id': user_data.get('user_id', ''),
                    'email': user_data.get('email', ''),
                    'given_name': user_data.get('given_name', ''),
                    'family_name': user_data.get('family_name', ''),
                    'external_id': user_data.get('external_id', ''),
                    'password': user_data.get('password', ''),
                    'active': str(user_data.get('active', True)).lower()
                }
                writer.writerow(row)
        
        if verbose:
            print(f"Successfully wrote processed CSV: {processed_file_path}", file=sys.stderr)
            
        return processed_file_path
        
    except Exception as e:
        if verbose:
            print(f"Error writing processed CSV file: {e}", file=sys.stderr)
        return None


def _write_processed_json(users_data, original_file_path, results, args):
    """
    Write processed JSON file with updated user_ids from create/update operations
    
    Args:
        users_data: List of processed user data with updated user_ids
        original_file_path: Path to the original JSON file
        results: List of operation results
        args: Command line arguments
    
    Returns:
        Path to the processed JSON file
    """
    import datetime
    
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate processed filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = os.path.splitext(original_file_path)[0]
    processed_file_path = f"{base_path}_processed_{timestamp}.json"
    
    if verbose:
        print(f"Writing processed JSON file: {processed_file_path}", file=sys.stderr)
    
    try:
        # Prepare JSON data with updated user_ids
        json_data = []
        for user_data in users_data:
            # Clean up the user data for JSON output
            clean_user_data = {
                'user_id': user_data.get('user_id', ''),
                'email': user_data.get('email', ''),
                'given_name': user_data.get('given_name', ''),
                'family_name': user_data.get('family_name', ''),
                'external_id': user_data.get('external_id', ''),
                'password': user_data.get('password'),
                'active': user_data.get('active', True)
            }
            # Remove None values to keep JSON clean
            clean_user_data = {k: v for k, v in clean_user_data.items() if v is not None}
            json_data.append(clean_user_data)
        
        with open(processed_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(json_data, jsonfile, indent=2, sort_keys=True)
        
        if verbose:
            print(f"Successfully wrote processed JSON: {processed_file_path}", file=sys.stderr)
            
        return processed_file_path
        
    except Exception as e:
        if verbose:
            print(f"Error writing processed JSON file: {e}", file=sys.stderr)
        return None


def _write_processed_csv_groups(groups_data, original_file_path, results, args):
    """
    Write processed CSV file with updated group_ids from create/update operations
    
    Args:
        groups_data: List of processed group data with updated group_ids
        original_file_path: Path to the original CSV file
        results: List of operation results
        args: Command line arguments
    
    Returns:
        Path to the processed CSV file
    """
    import datetime
    
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate processed filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = os.path.splitext(original_file_path)[0]
    processed_file_path = f"{base_path}_processed_{timestamp}.csv"
    
    if verbose:
        print(f"Writing processed CSV file: {processed_file_path}", file=sys.stderr)
    
    try:
        # Define fieldnames with group_id first
        fieldnames = ['group_id', 'display_name', 'external_id', 'member_external_ids']
        
        with open(processed_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Write processed group data
            for group_data in groups_data:
                # Convert member_external_ids list back to pipe-separated string for CSV
                member_external_ids = group_data.get('member_external_ids', [])
                if isinstance(member_external_ids, list):
                    member_external_ids_str = '|'.join(member_external_ids) if member_external_ids else ''
                else:
                    member_external_ids_str = str(member_external_ids) if member_external_ids else ''
                
                # Create row with all required fields
                row = {
                    'group_id': group_data.get('group_id', ''),
                    'display_name': group_data.get('display_name', ''),
                    'external_id': group_data.get('external_id', ''),
                    'member_external_ids': member_external_ids_str
                }
                writer.writerow(row)
        
        if verbose:
            print(f"Successfully wrote processed CSV: {processed_file_path}", file=sys.stderr)
            
        return processed_file_path
        
    except Exception as e:
        if verbose:
            print(f"Error writing processed CSV file: {e}", file=sys.stderr)
        return None


def _write_processed_json_groups(groups_data, original_file_path, results, args):
    """
    Write processed JSON file with updated group_ids from create/update operations
    
    Args:
        groups_data: List of processed group data with updated group_ids
        original_file_path: Path to the original JSON file
        results: List of operation results
        args: Command line arguments
    
    Returns:
        Path to the processed JSON file
    """
    import datetime
    
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate processed filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = os.path.splitext(original_file_path)[0]
    processed_file_path = f"{base_path}_processed_{timestamp}.json"
    
    if verbose:
        print(f"Writing processed JSON file: {processed_file_path}", file=sys.stderr)
    
    try:
        # Prepare JSON data with updated group_ids
        json_data = []
        for group_data in groups_data:
            # Clean up the group data for JSON output
            clean_group_data = {
                'group_id': group_data.get('group_id', ''),
                'display_name': group_data.get('display_name', ''),
                'external_id': group_data.get('external_id', ''),
                'member_external_ids': group_data.get('member_external_ids', [])
            }
            # Remove empty values to keep JSON clean
            clean_group_data = {k: v for k, v in clean_group_data.items() if v not in ('', [], None)}
            json_data.append(clean_group_data)
        
        with open(processed_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(json_data, jsonfile, indent=2, sort_keys=True)
        
        if verbose:
            print(f"Successfully wrote processed JSON: {processed_file_path}", file=sys.stderr)
            
        return processed_file_path
        
    except Exception as e:
        if verbose:
            print(f"Error writing processed JSON file: {e}", file=sys.stderr)
        return None


def scim_import_users(args):
    """
    Import users from CSV or JSON file
    
    Args:
        args: Command line arguments with file_path, format, and verbose
    
    Returns:
        List of operation results
    """
    file_path = args.file_path
    format_type = args.format
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Resolve file path
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
    
    # Check if file exists
    if not os.path.isfile(file_path):
        return handle_scim_error(f"File not found: {file_path}", verbose)
    
    # Auto-detect format if not specified
    if not format_type:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.csv':
            format_type = 'csv'
        elif ext == '.json':
            format_type = 'json'
        else:
            return handle_scim_error(
                "Could not auto-detect file format. Please specify format with -f/--format", 
                verbose
            )
    
    if verbose:
        print(f"Importing users from {format_type.upper()} file: {file_path}", file=sys.stderr)
    
    # Parse users based on format
    if format_type == 'csv':
        users_data = _parse_csv_users(file_path, verbose)
    elif format_type == 'json':
        users_data = _parse_json_users(file_path, verbose)
    else:
        return handle_scim_error(f"Unsupported format: {format_type}. Supported formats: csv, json", verbose)
    
    # Check if parsing failed (returns error response)
    if isinstance(users_data, list) and len(users_data) == 1 and users_data[0].get('success') == False:
        return users_data  # Return error response as-is
    
    if not users_data:
        return handle_scim_error("No users found in file", verbose)
    
    if verbose:
        print(f"Found {len(users_data)} users to import", file=sys.stderr)
    
    # Create users
    return _create_users_from_data(users_data, args)


def scim_export_users(args):
    """
    Export users to CSV or JSON file
    
    Args:
        args: Command line arguments with format, output_file, generate_template, etc.
    
    Returns:
        List of operation results
    """
    format_type = args.format or 'json'  # Default to JSON
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Handle template generation
    if hasattr(args, 'generate_template') and args.generate_template:
        return _generate_user_template(format_type, args)
    
    # Get SCIM client and fetch users
    client = get_scim_client(verbose=verbose)
    
    if verbose:
        print("Fetching users from SCIM API...", file=sys.stderr)
    
    try:
        success, users_data = client.get_users()
        if not success:
            return handle_scim_error(f"Failed to fetch users: {users_data}", verbose)
        
        users = users_data if isinstance(users_data, list) else users_data.get('Resources', [])
        
        if not users:
            if verbose:
                print("No users found", file=sys.stderr)
            return [{
                'success': True,
                'operation': 'Export users',
                'message': 'No users found to export',
                'user_count': 0
            }]
        
        if verbose:
            print(f"Found {len(users)} users to export", file=sys.stderr)
        
    except Exception as e:
        return handle_scim_error(f"Error fetching users: {e}", verbose)
    
    # Generate filename using shared utilities
    filename = generate_export_filename(
        args, "scim_users_export", format_type
    )
    
    # Resolve full path
    output_path = resolve_export_path(args, filename)
    
    # Ensure output directory exists
    try:
        ensure_output_directory(output_path, verbose)
    except Exception as e:
        return handle_scim_error(str(e), verbose)
    
    if verbose:
        print(f"Exporting {len(users)} users to {format_type.upper()} file: {output_path}", file=sys.stderr)
    
    # Export users based on format
    try:
        if format_type == 'csv':
            # Transform users to CSV format
            csv_data = []
            fieldnames = ['user_id', 'email', 'given_name', 'family_name', 'external_id', 'active']
            
            for user in users:
                emails = user.get('emails', [])
                email = emails[0].get('value') if emails else ''
                
                name = user.get('name', {})
                given_name = name.get('givenName', '')
                family_name = name.get('familyName', '')
                
                csv_data.append({
                    'user_id': user.get('id', ''),
                    'email': email,
                    'given_name': given_name,
                    'family_name': family_name,
                    'external_id': user.get('externalId', ''),
                    'active': str(user.get('active', True)).lower()
                })
            
            result = write_csv_export(csv_data, output_path, fieldnames, verbose)
            return [result]
            
        elif format_type == 'json':
            # Transform users to simplified format
            json_data = []
            
            for user in users:
                emails = user.get('emails', [])
                email = emails[0].get('value') if emails else ''
                
                name = user.get('name', {})
                given_name = name.get('givenName', '')
                family_name = name.get('familyName', '')
                
                json_data.append({
                    'email': email,
                    'given_name': given_name,
                    'family_name': family_name,
                    'external_id': user.get('externalId', ''),
                    'active': user.get('active', True),
                    'user_id': user.get('id', '')
                })
            
            result = write_json_export(json_data, output_path, verbose)
            return [result]
            
        else:
            return handle_scim_error(f"Unsupported format: {format_type}. Supported formats: csv, json", verbose)
            
    except Exception as e:
        return handle_scim_error(f"Error exporting users: {e}", verbose)


def _generate_user_template(format_type, args):
    """
    Generate template files for user import using embedded template files
    
    Args:
        format_type: 'csv' or 'json'
        args: Command line arguments
    
    Returns:
        List of operation results
    """
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate filename using shared utilities
    filename = generate_export_filename(
        args, "scim_users_template", format_type
    )
    
    # Resolve full path
    output_path = resolve_export_path(args, filename)
    
    # Ensure output directory exists
    try:
        ensure_output_directory(output_path, verbose)
    except Exception as e:
        return handle_scim_error(str(e), verbose)
    
    try:
        # Load template content from embedded template files
        template_filename = f"scim_users.{format_type}"
        
        # Get template content from package resources
        template_content = get_package_resource('catocli.templates', template_filename)
        
        # Write template content directly to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        if verbose:
            print(f"Successfully copied embedded template to: {output_path}", file=sys.stderr)
        
        # Create result similar to write_*_export functions
        result = {
            'success': True,
            'output_file': output_path,
            'format': format_type,
            'record_count': 3  # Our templates have 3 example users
        }
        
        # Update result to indicate template generation
        result['operation'] = f"Generate {format_type.upper()} template"
        result['message'] = f"Template file created: {output_path}"
        
        return [result]
    
    except Exception as e:
        return handle_scim_error(f"Error generating template: {e}", verbose)


def scim_purge_users(args, configuration=None):
    """
    Purge SCIM users from CSV or JSON file by first disabling then deleting them
    Requires user_id to be present in the source file
    
    Args:
        args: Command line arguments with file_path, format, and other options
        configuration: Optional configuration (unused)
    
    Returns:
        List of operation results
    """
    try:
        # Validate file path - resolve relative to current working directory
        file_path = args.file_path
        
        # If it's not an absolute path, resolve it relative to current working directory
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Normalize the path
        file_path = os.path.normpath(file_path)
        
        if not os.path.exists(file_path):
            # Provide helpful error message with current working directory
            cwd = os.getcwd()
            return handle_scim_error(
                f"Purge file not found: {file_path}\n" +
                f"Current working directory: {cwd}\n" +
                f"Looking for file: {args.file_path}", 
                args.verbose
            )
        
        if not os.path.isfile(file_path):
            return handle_scim_error(f"Path is not a file: {file_path}", args.verbose)
        
        # Determine format from file extension or explicit format argument
        file_format = getattr(args, 'format', None)
        if not file_format:
            # Auto-detect from extension
            _, ext = os.path.splitext(file_path.lower())
            if ext == '.csv':
                file_format = 'csv'
            elif ext in ['.json', '.jsonl']:
                file_format = 'json'
            else:
                return handle_scim_error(
                    f"Cannot determine file format from extension '{ext}'. " +
                    "Use -f/--format to specify 'json' or 'csv'", 
                    args.verbose
                )
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Purging users from {file_format.upper()} file: {file_path}", file=sys.stderr)
        
        # Parse the file to extract user_ids
        user_ids = _parse_user_ids_for_purge(file_path, file_format, args.verbose)
        
        if isinstance(user_ids, list) and len(user_ids) == 1 and 'error' in user_ids[0]:
            return user_ids  # Return error from parsing
        
        if not user_ids:
            return handle_scim_error("No valid user IDs found in file for purging", args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Found {len(user_ids)} user IDs to purge", file=sys.stderr)
            print(f"WARNING: This will DISABLE and then DELETE {len(user_ids)} users!", file=sys.stderr)
        
        # Confirm purge operation if not forced
        if not getattr(args, 'force', False):
            print(f"\nWARNING: You are about to PURGE {len(user_ids)} users!")
            print("This will:")
            print("1. DISABLE all users")
            print("2. DELETE all users")
            print("This operation CANNOT be undone!\n")
            
            try:
                confirmation = input("Type 'PURGE' to confirm this destructive operation: ")
                if confirmation != 'PURGE':
                    return [{
                        'success': False,
                        'operation': 'Purge users',
                        'message': 'Operation cancelled by user',
                        'cancelled': True
                    }]
            except (KeyboardInterrupt, EOFError):
                return [{
                    'success': False,
                    'operation': 'Purge users',
                    'message': 'Operation cancelled by user (Ctrl+C)',
                    'cancelled': True
                }]
        
        # Note: accountID and sourceID are embedded in the SCIM URL configured in the profile
        # We no longer need to extract them separately as the SCIM client handles this automatically
        
        # Perform purge operations
        return _purge_users_from_ids(user_ids, args)
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def _parse_user_ids_for_purge(file_path, file_format, verbose=False):
    """
    Parse user IDs from CSV or JSON file for purging operations
    Only extracts user_ids, ignoring other fields
    
    Args:
        file_path: Path to the file
        file_format: 'csv' or 'json'
        verbose: Whether to show verbose output
    
    Returns:
        List of user IDs or error response
    """
    user_ids = []
    
    try:
        if file_format == 'csv':
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Validate CSV headers
                if not reader.fieldnames:
                    return handle_scim_error("CSV file has no headers", verbose)
                
                # Check if user_id column exists
                if 'user_id' not in reader.fieldnames:
                    return handle_scim_error("CSV file must contain a 'user_id' column for purge operations", verbose)
                
                # Extract user IDs
                for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is headers
                    user_id = row.get('user_id', '').strip()
                    if user_id:
                        user_ids.append({
                            'user_id': user_id,
                            'row_number': row_num,
                            'email': row.get('email', '').strip() or 'unknown'
                        })
                    elif verbose:
                        print(f"Warning: Row {row_num}: Empty user_id, skipping", file=sys.stderr)
        
        elif file_format == 'json':
            with open(file_path, 'r', encoding='utf-8') as jsonfile:
                try:
                    data = json.load(jsonfile)
                except json.JSONDecodeError as e:
                    return handle_scim_error(f"Invalid JSON file: {e}", verbose)
                
                # Handle both array of users and single user object
                if isinstance(data, dict):
                    data = [data]  # Convert single user to array
                elif not isinstance(data, list):
                    return handle_scim_error("JSON file must contain an array of user objects or a single user object", verbose)
                
                # Extract user IDs
                for idx, user in enumerate(data, start=1):
                    if not isinstance(user, dict):
                        continue
                    
                    user_id = user.get('user_id')
                    if isinstance(user_id, str):
                        user_id = user_id.strip()
                    
                    if user_id:
                        user_ids.append({
                            'user_id': user_id,
                            'row_number': idx,
                            'email': user.get('email', 'unknown')
                        })
                    elif verbose:
                        print(f"Warning: User {idx}: Empty or missing user_id, skipping", file=sys.stderr)
        
        else:
            return handle_scim_error(f"Unsupported format: {file_format}", verbose)
    
    except Exception as e:
        return handle_scim_error(f"Error parsing file: {e}", verbose)
    
    if verbose:
        print(f"Extracted {len(user_ids)} user IDs from {file_format.upper()} file", file=sys.stderr)
    
    return user_ids


def _purge_users_from_ids(user_ids, args):
    """
    Purge users by first disabling them, then deleting them
    
    Args:
        user_ids: List of user ID dictionaries
        args: Command line arguments
    
    Returns:
        List of operation results
    """
    verbose = hasattr(args, 'verbose') and args.verbose
    client = get_scim_client(verbose=verbose)
    
    # Extract accountId and sourceId from the SCIM URL
    # URL format: https://scimservice.catonetworks.com:4443/scim/v2/{accountId}/{sourceId}
    import urllib.parse
    try:
        parsed_url = urllib.parse.urlparse(client.baseurl)
        path_parts = parsed_url.path.strip('/').split('/')
        # Expected path: ['scim', 'v2', 'accountId', 'sourceId']
        if len(path_parts) >= 4 and path_parts[0] == 'scim' and path_parts[1] == 'v2':
            account_id = path_parts[2]
            source_id = int(path_parts[3])  # sourceId is an integer
        else:
            if verbose:
                print(f"Warning: Could not parse accountId/sourceId from SCIM URL: {client.baseurl}", file=sys.stderr)
                print("Attempting to continue with placeholder values...", file=sys.stderr)
            account_id = "unknown"
            source_id = 0
    except Exception as e:
        if verbose:
            print(f"Error parsing SCIM URL: {e}", file=sys.stderr)
            print("Attempting to continue with placeholder values...", file=sys.stderr)
        account_id = "unknown"
        source_id = 0
    
    # Track results for both operations
    disable_results = []
    delete_results = []
    overall_results = []
    
    successful_disables = 0
    failed_disables = 0
    successful_deletes = 0
    failed_deletes = 0
    
    if verbose:
        print(f"\nPhase 1: Disabling {len(user_ids)} users...", file=sys.stderr)
    
    # Phase 1: Disable all users
    for i, user_info in enumerate(user_ids, 1):
        user_id = user_info['user_id']
        email = user_info.get('email', 'unknown')
        
        if verbose:
            print(f"  [{i}/{len(user_ids)}] Disabling user: {email} ({user_id})", file=sys.stderr)
        
        try:
            # Use PATCH to disable the user
            patch_request = {
                "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
                "Operations": [
                    {
                        "op": "replace",
                        "path": "active",
                        "value": False
                    }
                ]
            }
            
            success, result = client.patch_user(user_id, account_id, source_id, patch_request)
            
            disable_result = {
                'user_id': user_id,
                'email': email,
                'operation': 'disable',
                'success': success,
                'row_number': user_info.get('row_number')
            }
            
            if success:
                disable_result['message'] = f"User '{email}' ({user_id}) disabled successfully"
                successful_disables += 1
            else:
                disable_result['error'] = result.get('error', str(result))
                disable_result['message'] = f"Failed to disable user '{email}' ({user_id}): {disable_result['error']}"
                failed_disables += 1
            
            disable_results.append(disable_result)
            
        except Exception as e:
            disable_result = {
                'user_id': user_id,
                'email': email,
                'operation': 'disable',
                'success': False,
                'error': str(e),
                'message': f"Error disabling user '{email}' ({user_id}): {str(e)}",
                'row_number': user_info.get('row_number')
            }
            disable_results.append(disable_result)
            failed_disables += 1
    
    if verbose:
        print(f"Phase 1 complete: {successful_disables} disabled, {failed_disables} failed", file=sys.stderr)
        print(f"\nPhase 2: Deleting {len(user_ids)} users...", file=sys.stderr)
    
    # Phase 2: Delete all users (regardless of disable success/failure)
    for i, user_info in enumerate(user_ids, 1):
        user_id = user_info['user_id']
        email = user_info.get('email', 'unknown')
        
        if verbose:
            print(f"  [{i}/{len(user_ids)}] Deleting user: {email} ({user_id})", file=sys.stderr)
        
        try:
            success, result = client.delete_user(user_id, account_id, source_id)
            
            delete_result = {
                'user_id': user_id,
                'email': email,
                'operation': 'delete',
                'success': success,
                'row_number': user_info.get('row_number')
            }
            
            if success:
                delete_result['message'] = f"User '{email}' ({user_id}) deleted successfully"
                successful_deletes += 1
            else:
                delete_result['error'] = result.get('error', str(result))
                delete_result['message'] = f"Failed to delete user '{email}' ({user_id}): {delete_result['error']}"
                failed_deletes += 1
            
            delete_results.append(delete_result)
            
        except Exception as e:
            delete_result = {
                'user_id': user_id,
                'email': email,
                'operation': 'delete',
                'success': False,
                'error': str(e),
                'message': f"Error deleting user '{email}' ({user_id}): {str(e)}",
                'row_number': user_info.get('row_number')
            }
            delete_results.append(delete_result)
            failed_deletes += 1
    
    if verbose:
        print(f"Phase 2 complete: {successful_deletes} deleted, {failed_deletes} failed", file=sys.stderr)
    
    # Combine results for overall reporting
    for i, user_info in enumerate(user_ids):
        disable_result = disable_results[i] if i < len(disable_results) else {}
        delete_result = delete_results[i] if i < len(delete_results) else {}
        
        overall_result = {
            'user_id': user_info['user_id'],
            'email': user_info.get('email', 'unknown'),
            'row_number': user_info.get('row_number'),
            'disable_success': disable_result.get('success', False),
            'delete_success': delete_result.get('success', False),
            'overall_success': delete_result.get('success', False),  # Overall success is based on delete success
        }
        
        # Build combined message
        disable_status = "✓" if disable_result.get('success') else "✗"
        delete_status = "✓" if delete_result.get('success') else "✗"
        overall_result['message'] = f"Disable: {disable_status}, Delete: {delete_status} - {overall_result['email']} ({overall_result['user_id']})"
        
        # Include errors if any
        errors = []
        if disable_result.get('error'):
            errors.append(f"Disable: {disable_result['error']}")
        if delete_result.get('error'):
            errors.append(f"Delete: {delete_result['error']}")
        if errors:
            overall_result['errors'] = errors
        
        overall_results.append(overall_result)
    
    # Build final summary
    total_users = len(user_ids)
    fully_successful = sum(1 for r in overall_results if r['overall_success'])
    
    summary = {
        'total_users': total_users,
        'disable_phase': {
            'successful': successful_disables,
            'failed': failed_disables,
            'success_rate': f"{successful_disables}/{total_users} ({successful_disables/total_users*100:.1f}%)"
        },
        'delete_phase': {
            'successful': successful_deletes,
            'failed': failed_deletes,
            'success_rate': f"{successful_deletes}/{total_users} ({successful_deletes/total_users*100:.1f}%)"
        },
        'overall': {
            'fully_successful': fully_successful,
            'partially_successful': total_users - fully_successful,
            'success_rate': f"{fully_successful}/{total_users} ({fully_successful/total_users*100:.1f}%)"
        }
    }
    
    response = {
        'success': fully_successful == total_users,
        'operation': f"Purge {total_users} users (disable + delete)",
        'summary': summary
    }
    
    # Only include detailed results if verbose mode is enabled
    if verbose:
        response['results'] = overall_results
    
    return [response]


def scim_import_users(args, configuration=None):
    """
    Import multiple SCIM users from JSON or CSV file
    
    Supports both formats:
    CSV format: email,given_name,family_name,external_id,password,active
    JSON format: [{"email": "...", "given_name": "...", ...}, ...]
    """
    try:
        # Template generation is not supported for import users
        # Use 'catocli scim export users -gt' to generate templates
        
        # Validate file path - resolve relative to current working directory
        file_path = args.file_path
        
        # If it's not an absolute path, resolve it relative to current working directory
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Normalize the path
        file_path = os.path.normpath(file_path)
        
        if not os.path.exists(file_path):
            # Provide helpful error message with current working directory
            cwd = os.getcwd()
            return handle_scim_error(
                f"Import file not found: {file_path}\n" +
                f"Current working directory: {cwd}\n" +
                f"Looking for file: {args.file_path}", 
                args.verbose
            )
        
        if not os.path.isfile(file_path):
            return handle_scim_error(f"Path is not a file: {file_path}", args.verbose)
        
        # Determine format from file extension or explicit format argument
        file_format = getattr(args, 'import_format', None)
        if not file_format:
            # Auto-detect from extension
            _, ext = os.path.splitext(file_path.lower())
            if ext == '.csv':
                file_format = 'csv'
            elif ext in ['.json', '.jsonl']:
                file_format = 'json'
            else:
                return handle_scim_error(
                    f"Cannot determine file format from extension '{ext}'. " +
                    "Use -f/--format to specify 'json' or 'csv'", 
                    args.verbose
                )
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Importing users from {file_format.upper()} file: {file_path}", file=sys.stderr)
        
        # Parse the file based on format
        if file_format == 'csv':
            users_data = _parse_csv_users(file_path, args.verbose)
        elif file_format == 'json':
            users_data = _parse_json_users(file_path, args.verbose)
        else:
            return handle_scim_error(f"Unsupported format: {file_format}", args.verbose)
        
        if isinstance(users_data, list) and len(users_data) == 1 and 'error' in users_data[0]:
            return users_data  # Return error from parsing
        
        if not users_data:
            return handle_scim_error("No valid user data found in file", args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Found {len(users_data)} users to import", file=sys.stderr)
        
        # Get SCIM client and import users
        return _create_users_from_data(users_data, args)
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


# =============================================================================
# GROUP OPERATIONS (Import, Export, Purge)
# =============================================================================

def _parse_csv_groups(file_path, verbose=False):
    """
    Parse groups from CSV file with support for group_id column to determine create vs update operations
    
    Returns:
        List of group dictionaries or error response
    """
    groups_data = []
    required_columns = ['display_name', 'external_id']
    optional_columns = ['member_external_ids', 'group_id']
    all_columns = required_columns + optional_columns
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Validate CSV headers
            if not reader.fieldnames:
                return handle_scim_error("CSV file has no headers", verbose)
            
            # Check for required columns
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                return handle_scim_error(f"Missing required CSV columns: {', '.join(missing_columns)}", verbose)
            
            # Check for unexpected columns
            unexpected_columns = [col for col in reader.fieldnames if col not in all_columns]
            if unexpected_columns and verbose:
                print(f"Warning: Unexpected CSV columns will be ignored: {', '.join(unexpected_columns)}", file=sys.stderr)
            
            # Read and validate each row
            for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is headers
                # Validate required fields
                missing_fields = []
                for field in required_columns:
                    if not row.get(field, '').strip():
                        missing_fields.append(field)
                
                if missing_fields:
                    return handle_scim_error(
                        f"Row {row_num}: Missing required fields: {', '.join(missing_fields)}", 
                        verbose
                    )
                
                # Parse member external IDs if provided (pipe-delimited format)
                member_external_ids_str = row.get('member_external_ids', '').strip()
                member_external_ids = []
                if member_external_ids_str:
                    # Split by pipe delimiter and clean up
                    member_external_ids = [ext_id.strip() for ext_id in member_external_ids_str.split('|') if ext_id.strip()]
                
                # Check if group_id is present to determine create vs update operation
                group_id = row.get('group_id', '').strip()
                operation_type = 'update' if group_id else 'create'
                
                group_data = {
                    'display_name': row['display_name'].strip(),
                    'external_id': row['external_id'].strip(),
                    'member_external_ids': member_external_ids,
                    'group_id': group_id if group_id else None,
                    'operation_type': operation_type,
                    'row_number': row_num
                }
                
                groups_data.append(group_data)
    
    except csv.Error as e:
        return handle_scim_error(f"Error reading CSV file: {e}", verbose)
    except Exception as e:
        return handle_scim_error(f"Error processing CSV file: {e}", verbose)
    
    return groups_data


def _parse_json_groups(file_path, verbose=False):
    """
    Parse groups from JSON file
    
    Returns:
        List of group dictionaries or error response
    """
    required_fields = ['display_name', 'external_id']
    optional_fields = ['member_external_ids', 'group_id']
    
    try:
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            try:
                data = json.load(jsonfile)
            except json.JSONDecodeError as e:
                return handle_scim_error(f"Invalid JSON file: {e}", verbose)
            
            # Handle both array of groups and single group object
            if isinstance(data, dict):
                data = [data]  # Convert single group to array
            elif not isinstance(data, list):
                return handle_scim_error("JSON file must contain an array of group objects or a single group object", verbose)
            
            groups_data = []
            for idx, group in enumerate(data, start=1):
                if not isinstance(group, dict):
                    return handle_scim_error(f"Group {idx}: Must be a JSON object", verbose)
                
                # Check required fields
                missing_fields = [field for field in required_fields if not group.get(field, '').strip()]
                if missing_fields:
                    return handle_scim_error(
                        f"Group {idx}: Missing required fields: {', '.join(missing_fields)}", 
                        verbose
                    )
                
                # Validate member_external_ids format if provided
                member_external_ids = group.get('member_external_ids', [])
                if member_external_ids and not isinstance(member_external_ids, list):
                    return handle_scim_error(f"Group {idx}: member_external_ids must be an array", verbose)
                
                # Check if group_id is present to determine create vs update operation
                group_id = group.get('group_id', '').strip() if isinstance(group.get('group_id'), str) else group.get('group_id')
                group_id = group_id if group_id else None
                operation_type = 'update' if group_id else 'create'
                
                group_data = {
                    'display_name': group['display_name'].strip(),
                    'external_id': group['external_id'].strip(),
                    'member_external_ids': member_external_ids,
                    'group_id': group_id,
                    'operation_type': operation_type,
                    'row_number': idx
                }
                
                groups_data.append(group_data)
    
    except Exception as e:
        return handle_scim_error(f"Error processing JSON file: {e}", verbose)
    
    return groups_data


def _create_groups_from_data(groups_data, args):
    """
    Create or update groups from parsed data using SCIM client
    Supports both create and update operations based on presence of group_id
    """
    # Get SCIM client
    client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
    
    # Check if SCIM client is configured
    if client is None:
        return handle_scim_error(
            "SCIM client is not configured. Please ensure your SCIM credentials are set up correctly.\n"
            "Run 'catocli configure scim' to configure SCIM credentials, or\n"
            "Check your ~/.cato/settings.json file for 'scim_url' and 'scim_token' settings.\n"
            "For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps",
            hasattr(args, 'verbose') and args.verbose
        )
    
    # Collect all unique external_ids that need to be looked up
    all_external_ids = set()
    for group_data in groups_data:
        member_external_ids = group_data.get('member_external_ids', [])
        all_external_ids.update(member_external_ids)
    
    # Bulk lookup user_ids by external_ids
    user_id_map = {}
    if all_external_ids:
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Looking up user IDs for {len(all_external_ids)} external IDs: {list(all_external_ids)}", file=sys.stderr)
        
        success, user_id_map = client.find_users_by_external_ids(list(all_external_ids))
        if not success:
            return handle_scim_error("Failed to lookup user IDs by external IDs", hasattr(args, 'verbose') and args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            found_count = len([k for k, v in user_id_map.items() if v])
            print(f"Found user IDs for {found_count}/{len(all_external_ids)} external IDs", file=sys.stderr)
            if user_id_map:
                print(f"User ID mapping: {user_id_map}", file=sys.stderr)
    
    # Convert member_external_ids to members arrays for all groups
    for group_data in groups_data:
        member_external_ids = group_data.get('member_external_ids', [])
        members = []
        
        if member_external_ids:
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Processing {len(member_external_ids)} members for group {group_data['display_name']}", file=sys.stderr)
            
            # Convert external_ids to user_ids using the bulk lookup
            for external_id in member_external_ids:
                user_id = user_id_map.get(external_id)
                if user_id:
                    members.append({
                        "value": user_id,
                        "$ref": f"Users/{user_id}",
                        "display": external_id  # Use external_id as display name for reference
                    })
                else:
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"Warning: User with external ID '{external_id}' not found for group {group_data['display_name']}", file=sys.stderr)
            
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Resolved {len(members)}/{len(member_external_ids)} members for group {group_data['display_name']}", file=sys.stderr)
        
        # Set group members in proper SCIM format
        group_data['members'] = members
        
        # Keep member_external_ids for processed file output - will be handled later
    
    # Process groups and collect results
    results = []
    successful_groups = []
    failed_groups = []
    create_count = 0
    update_count = 0
    
    for group_data in groups_data:
        row_num = group_data.pop('row_number')  # Remove row_number before API call
        operation_type = group_data.pop('operation_type', 'create')
        group_id = group_data.get('group_id')
        
        if hasattr(args, 'verbose') and args.verbose:
            operation_desc = "Updating" if operation_type == 'update' else "Creating"
            print(f"{operation_desc} group: {group_data['display_name']}", file=sys.stderr)
        
        try:
            if operation_type == 'update' and group_id:
                # Update existing group
                # Build group data for update in SCIM format
                scim_group_data = {
                    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
                    "displayName": group_data['display_name'],
                    "externalId": group_data['external_id']
                }
                
                # Add members if provided
                if group_data.get('members'):
                    scim_group_data["members"] = group_data['members']
                
                success, result = client.update_group(group_id, scim_group_data)
                update_count += 1
            else:
                # Create new group
                success, result = client.create_group(
                    group_data['display_name'],
                    group_data['external_id'],
                    group_data.get('members', [])
                )
                create_count += 1
            
            group_result = {
                'row_number': row_num,
                'display_name': group_data['display_name'],
                'success': success,
                'operation': operation_type,
                'original_group_id': group_id  # Keep track of original group_id
            }
            
            if success:
                # Get group_id from result (for creates) or use existing (for updates)
                result_group_id = result.get('id', group_id)
                group_result['group_id'] = result_group_id
                
                # Update the original group_data with the group_id for processed files
                group_data['group_id'] = result_group_id
                
                if operation_type == 'update':
                    group_result['message'] = f"Group '{group_data['display_name']}' updated successfully"
                else:
                    group_result['message'] = f"Group '{group_data['display_name']}' created successfully"
                    if result.get('warning'):
                        group_result['warning'] = result['warning']
                successful_groups.append(group_result)
            else:
                group_result['error'] = result.get('error', str(result))
                operation_desc = "update" if operation_type == 'update' else "create"
                group_result['message'] = f"Failed to {operation_desc} group '{group_data['display_name']}': {group_result['error']}"
                failed_groups.append(group_result)
            
            results.append(group_result)
            
        except Exception as e:
            group_result = {
                'row_number': row_num,
                'display_name': group_data['display_name'],
                'success': False,
                'error': str(e),
                'message': f"Error creating group '{group_data['display_name']}': {str(e)}"
            }
            failed_groups.append(group_result)
            results.append(group_result)
    
    # Collect member resolution statistics
    total_members_requested = len(all_external_ids)
    total_members_resolved = len(user_id_map)
    unresolved_external_ids = [ext_id for ext_id in all_external_ids if ext_id not in user_id_map]
    
    # Format final response
    summary = {
        'total_groups': len(groups_data),
        'created_groups': create_count,
        'updated_groups': update_count,
        'successful_groups': len(successful_groups),
        'failed_groups': len(failed_groups),
        'success_rate': f"{len(successful_groups)}/{len(groups_data)} ({len(successful_groups)/len(groups_data)*100:.1f}%)",
        'members': {
            'total_members_requested': total_members_requested,
            'total_members_resolved': total_members_resolved,
            'member_resolution_rate': f"{total_members_resolved}/{total_members_requested} ({total_members_resolved/total_members_requested*100:.1f}%)" if total_members_requested > 0 else "0/0 (N/A)",
            'unresolved_external_ids': unresolved_external_ids
        }
    }
    
    # Write processed file if requested
    processed_file_path = None
    if hasattr(args, 'write_processed') and args.write_processed and hasattr(args, 'file_path'):
        # Determine file format from original file
        _, ext = os.path.splitext(args.file_path.lower())
        if ext == '.csv':
            processed_file_path = _write_processed_csv_groups(groups_data, args.file_path, results, args)
        elif ext in ['.json', '.jsonl']:
            processed_file_path = _write_processed_json_groups(groups_data, args.file_path, results, args)
        else:
            # Default to CSV if format can't be determined
            processed_file_path = _write_processed_csv_groups(groups_data, args.file_path, results, args)
    
    # Provide verbose summary of member resolution
    if hasattr(args, 'verbose') and args.verbose and total_members_requested > 0:
        print(f"\nMember Resolution Summary:", file=sys.stderr)
        print(f"  Total member external IDs requested: {total_members_requested}", file=sys.stderr)
        print(f"  Member external IDs resolved: {total_members_resolved}", file=sys.stderr)
        print(f"  Member resolution rate: {total_members_resolved/total_members_requested*100:.1f}%", file=sys.stderr)
        
        if unresolved_external_ids:
            print(f"  Unresolved external IDs: {', '.join(unresolved_external_ids)}", file=sys.stderr)
            print(f"  Note: Unresolved users may be inactive or have different external IDs", file=sys.stderr)
    
    response = {
        'success': len(failed_groups) == 0,  # Overall success only if no failures
        'operation': f"Import {len(groups_data)} groups ({create_count} created, {update_count} updated)",
        'summary': summary
    }
    
    if processed_file_path:
        response['processed_file'] = processed_file_path
    
    return [response]


def _generate_group_template(format_type, args):
    """
    Generate template files for group import using embedded template files
    
    Args:
        format_type: 'csv' or 'json'
        args: Command line arguments
    
    Returns:
        List of operation results
    """
    verbose = hasattr(args, 'verbose') and args.verbose
    
    # Generate filename using shared utilities
    filename = generate_export_filename(
        args, "scim_groups_template", format_type
    )
    
    # Resolve full path
    output_path = resolve_export_path(args, filename)
    
    # Ensure output directory exists
    try:
        ensure_output_directory(output_path, verbose)
    except Exception as e:
        return handle_scim_error(str(e), verbose)
    
    try:
        # Load template content from embedded template files
        template_filename = f"scim_groups.{format_type}"
        
        # Get template content from package resources
        template_content = get_package_resource('catocli.templates', template_filename)
        
        # Write template content directly to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        if verbose:
            print(f"Successfully copied embedded template to: {output_path}", file=sys.stderr)
        
        # Create result similar to write_*_export functions
        result = {
            'success': True,
            'output_file': output_path,
            'format': format_type,
            'record_count': 2  # Our templates have 2 example groups
        }
        
        # Update result to indicate template generation
        result['operation'] = f"Generate {format_type.upper()} template"
        result['message'] = f"Template file created: {output_path}"
        
        return [result]
    
    except Exception as e:
        return handle_scim_error(f"Error generating template: {e}", verbose)


def scim_export_groups(args, configuration=None):
    """
    Export SCIM groups to JSON or CSV format
    """
    try:
        # Check if template generation is requested
        if hasattr(args, 'generate_template') and args.generate_template:
            format_type = getattr(args, 'format', 'json')
            return _generate_group_template(format_type, args)
        
        # Get SCIM client and fetch groups
        verbose = hasattr(args, 'verbose') and args.verbose
        client = get_scim_client(verbose=verbose)
        format_type = getattr(args, 'format', 'json')
        
        if verbose:
            print("Fetching groups from SCIM API...", file=sys.stderr)
        
        try:
            success, groups_data = client.get_groups()
            if not success:
                return handle_scim_error(f"Failed to fetch groups: {groups_data}", verbose)
            
            groups = groups_data if isinstance(groups_data, list) else groups_data.get('Resources', [])
            
            if not groups:
                if verbose:
                    print("No groups found", file=sys.stderr)
                return [{
                    'success': True,
                    'operation': 'Export groups',
                    'message': 'No groups found to export',
                    'group_count': 0
                }]
            
            if verbose:
                print(f"Found {len(groups)} groups to export", file=sys.stderr)
            
        except Exception as e:
            return handle_scim_error(f"Error fetching groups: {e}", verbose)
        
        # Generate filename using shared utilities
        filename = generate_export_filename(
            args, "scim_groups_export", format_type
        )
        
        # Resolve full path
        output_path = resolve_export_path(args, filename)
        
        # Ensure output directory exists
        try:
            ensure_output_directory(output_path, verbose)
        except Exception as e:
            return handle_scim_error(str(e), verbose)
        
        if verbose:
            print(f"Exporting {len(groups)} groups to {format_type.upper()} file: {output_path}", file=sys.stderr)
        
        # First, get all users to build a user_id -> external_id mapping
        if verbose:
            print("Fetching users to resolve member external_ids...", file=sys.stderr)
        
        user_id_to_external_id = {}
        try:
            success, users_data = client.get_users()
            if success:
                users = users_data if isinstance(users_data, list) else users_data.get('Resources', [])
                for user in users:
                    user_id = user.get('id')
                    external_id = user.get('externalId')
                    if user_id and external_id:
                        user_id_to_external_id[user_id] = external_id
                        
                if verbose:
                    print(f"Built mapping for {len(user_id_to_external_id)} users", file=sys.stderr)
            else:
                if verbose:
                    print(f"Warning: Could not fetch users for external_id mapping: {users_data}", file=sys.stderr)
        except Exception as e:
            if verbose:
                print(f"Warning: Error fetching users for external_id mapping: {e}", file=sys.stderr)
        
        # Export groups based on format
        try:
            if format_type == 'csv':
                # Transform groups to CSV format
                csv_data = []
                fieldnames = ['group_id', 'display_name', 'external_id', 'member_external_ids']
                
                for group in groups:
                    # Format members as comma-delimited external_ids for CSV
                    members = group.get('members', [])
                    # Extract external_ids from member objects
                    external_ids = []
                    for member in members:
                        # Members in SCIM groups have 'value' field containing user_id
                        # Look up the external_id for each user_id
                        user_id = member.get('value', '')
                        if user_id:
                            external_id = user_id_to_external_id.get(user_id)
                            if external_id:
                                external_ids.append(external_id)
                            elif verbose:
                                print(f"Warning: Could not find external_id for user_id {user_id} in group {group.get('displayName', 'unknown')}", file=sys.stderr)
                    
                    member_external_ids_str = '|'.join(external_ids)
                    
                    csv_data.append({
                        'group_id': group.get('id', ''),
                        'display_name': group.get('displayName', ''),
                        'external_id': group.get('externalId', ''),
                        'member_external_ids': member_external_ids_str
                    })
                
                result = write_csv_export(csv_data, output_path, fieldnames, verbose)
                return [result]
                
            elif format_type == 'json':
                # Transform groups to simplified format
                json_data = []
                
                for group in groups:
                    # For JSON, also use external_ids format for consistency
                    members = group.get('members', [])
                    external_ids = []
                    for member in members:
                        # Look up the external_id for each user_id (same as CSV logic)
                        user_id = member.get('value', '')
                        if user_id:
                            external_id = user_id_to_external_id.get(user_id)
                            if external_id:
                                external_ids.append(external_id)
                            elif verbose:
                                print(f"Warning: Could not find external_id for user_id {user_id} in group {group.get('displayName', 'unknown')}", file=sys.stderr)
                    
                    json_data.append({
                        'display_name': group.get('displayName', ''),
                        'external_id': group.get('externalId', ''),
                        'member_external_ids': external_ids,  # Array format for JSON
                        'group_id': group.get('id', '')
                    })
                
                result = write_json_export(json_data, output_path, verbose)
                return [result]
                
            else:
                return handle_scim_error(f"Unsupported format: {format_type}. Supported formats: csv, json", verbose)
                
        except Exception as e:
            return handle_scim_error(f"Error exporting groups: {e}", verbose)
            
    except Exception as e:
        return handle_scim_error(e, verbose)


def scim_import_groups(args, configuration=None):
    """
    Import multiple SCIM groups from JSON or CSV file
    
    Supports both formats:
    CSV format: display_name,external_id,member_external_ids,group_id
    JSON format: [{"display_name": "...", "external_id": "...", "member_external_ids": [...], ...}, ...]
    """
    try:
        # Validate file path - resolve relative to current working directory
        file_path = args.file_path
        
        # If it's not an absolute path, resolve it relative to current working directory
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Normalize the path
        file_path = os.path.normpath(file_path)
        
        if not os.path.exists(file_path):
            # Provide helpful error message with current working directory
            cwd = os.getcwd()
            return handle_scim_error(
                f"Import file not found: {file_path}\n" +
                f"Current working directory: {cwd}\n" +
                f"Looking for file: {args.file_path}", 
                args.verbose
            )
        
        if not os.path.isfile(file_path):
            return handle_scim_error(f"Path is not a file: {file_path}", args.verbose)
        
        # Determine format from file extension or explicit format argument
        file_format = getattr(args, 'format', None)
        if not file_format:
            # Auto-detect from extension
            _, ext = os.path.splitext(file_path.lower())
            if ext == '.csv':
                file_format = 'csv'
            elif ext in ['.json', '.jsonl']:
                file_format = 'json'
            else:
                return handle_scim_error(
                    f"Cannot determine file format from extension '{ext}'. " +
                    "Use -f/--format to specify 'json' or 'csv'", 
                    args.verbose
                )
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Importing groups from {file_format.upper()} file: {file_path}", file=sys.stderr)
        
        # Parse the file based on format
        if file_format == 'csv':
            groups_data = _parse_csv_groups(file_path, args.verbose)
        elif file_format == 'json':
            groups_data = _parse_json_groups(file_path, args.verbose)
        else:
            return handle_scim_error(f"Unsupported format: {file_format}", args.verbose)
        
        if isinstance(groups_data, list) and len(groups_data) == 1 and 'error' in groups_data[0]:
            return groups_data  # Return error from parsing
        
        if not groups_data:
            return handle_scim_error("No valid group data found in file", args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Found {len(groups_data)} groups to import", file=sys.stderr)
        
        # Get SCIM client and import groups
        return _create_groups_from_data(groups_data, args)
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def _parse_group_ids_for_purge(file_path, file_format, verbose=False):
    """
    Parse group IDs from CSV or JSON file for purging operations
    Only extracts group_ids, ignoring other fields
    
    Args:
        file_path: Path to the file
        file_format: 'csv' or 'json'
        verbose: Whether to show verbose output
    
    Returns:
        List of group IDs or error response
    """
    group_ids = []
    
    try:
        if file_format == 'csv':
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Validate CSV headers
                if not reader.fieldnames:
                    return handle_scim_error("CSV file has no headers", verbose)
                
                # Check if group_id column exists
                if 'group_id' not in reader.fieldnames:
                    return handle_scim_error("CSV file must contain a 'group_id' column for purge operations", verbose)
                
                # Extract group IDs
                for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is headers
                    group_id = row.get('group_id', '').strip()
                    if group_id:
                        # Support both displayName and display_name column names
                        display_name = row.get('displayName', '').strip() or row.get('display_name', '').strip() or 'unknown'
                        group_ids.append({
                            'group_id': group_id,
                            'row_number': row_num,
                            'displayName': display_name
                        })
                    elif verbose:
                        print(f"Warning: Row {row_num}: Empty group_id, skipping", file=sys.stderr)
        
        elif file_format == 'json':
            with open(file_path, 'r', encoding='utf-8') as jsonfile:
                try:
                    data = json.load(jsonfile)
                except json.JSONDecodeError as e:
                    return handle_scim_error(f"Invalid JSON file: {e}", verbose)
                
                # Handle both array of groups and single group object
                if isinstance(data, dict):
                    data = [data]  # Convert single group to array
                elif not isinstance(data, list):
                    return handle_scim_error("JSON file must contain an array of group objects or a single group object", verbose)
                
                # Extract group IDs
                for idx, group in enumerate(data, start=1):
                    if not isinstance(group, dict):
                        continue
                    
                    group_id = group.get('group_id')
                    if isinstance(group_id, str):
                        group_id = group_id.strip()
                    
                    if group_id:
                        # Support both displayName and display_name field names
                        display_name = group.get('displayName', '') or group.get('display_name', '') or 'unknown'
                        group_ids.append({
                            'group_id': group_id,
                            'row_number': idx,
                            'displayName': display_name
                        })
                    elif verbose:
                        print(f"Warning: Group {idx}: Empty or missing group_id, skipping", file=sys.stderr)
        
        else:
            return handle_scim_error(f"Unsupported format: {file_format}", verbose)
    
    except Exception as e:
        return handle_scim_error(f"Error parsing file: {e}", verbose)
    
    if verbose:
        print(f"Extracted {len(group_ids)} group IDs from {file_format.upper()} file", file=sys.stderr)
    
    return group_ids


def _purge_groups_from_ids(group_ids, args):
    """
    Purge groups by first disabling them, then deleting them
    
    Args:
        group_ids: List of group ID dictionaries
        args: Command line arguments
    
    Returns:
        List of operation results
    """
    verbose = hasattr(args, 'verbose') and args.verbose
    client = get_scim_client(verbose=verbose)
    
    # Extract accountId and sourceId from the SCIM URL
    # URL format: https://scimservice.catonetworks.com:4443/scim/v2/{accountId}/{sourceId}
    import urllib.parse
    try:
        parsed_url = urllib.parse.urlparse(client.baseurl)
        path_parts = parsed_url.path.strip('/').split('/')
        # Expected path: ['scim', 'v2', 'accountId', 'sourceId']
        if len(path_parts) >= 4 and path_parts[0] == 'scim' and path_parts[1] == 'v2':
            account_id = path_parts[2]
            source_id = int(path_parts[3])  # sourceId is an integer
        else:
            if verbose:
                print(f"Warning: Could not parse accountId/sourceId from SCIM URL: {client.baseurl}", file=sys.stderr)
                print("Attempting to continue with placeholder values...", file=sys.stderr)
            account_id = "unknown"
            source_id = 0
    except Exception as e:
        if verbose:
            print(f"Error parsing SCIM URL: {e}", file=sys.stderr)
            print("Attempting to continue with placeholder values...", file=sys.stderr)
        account_id = "unknown"
        source_id = 0
    
    # Track results for both operations
    disable_results = []
    delete_results = []
    overall_results = []
    
    successful_disables = 0
    failed_disables = 0
    successful_deletes = 0
    failed_deletes = 0
    
    if verbose:
        print(f"\nPhase 1: Disabling {len(group_ids)} groups...", file=sys.stderr)
    
    # Phase 1: Disable all groups (using PATCH to set active=false equivalent or similar)
    # Note: Groups don't have an 'active' field like users, so we'll skip to delete directly
    # But for consistency with users, we'll show a "disable" phase that just marks them for deletion
    for i, group_info in enumerate(group_ids, 1):
        group_id = group_info['group_id']
        display_name = group_info.get('displayName', 'unknown')
        
        if verbose:
            print(f"  [{i}/{len(group_ids)}] Marking group for deletion: {display_name} ({group_id})", file=sys.stderr)
        
        # For groups, we don't have a disable operation, so we'll mark this as successful
        disable_result = {
            'group_id': group_id,
            'displayName': display_name,
            'operation': 'mark_for_deletion',
            'success': True,
            'message': f"Group '{display_name}' ({group_id}) marked for deletion",
            'row_number': group_info.get('row_number')
        }
        
        disable_results.append(disable_result)
        successful_disables += 1
    
    if verbose:
        print(f"Phase 1 complete: {successful_disables} marked for deletion, {failed_disables} failed", file=sys.stderr)
        print(f"\nPhase 2: Deleting {len(group_ids)} groups...", file=sys.stderr)
    
    # Phase 2: Delete all groups
    for i, group_info in enumerate(group_ids, 1):
        group_id = group_info['group_id']
        display_name = group_info.get('displayName', 'unknown')
        
        if verbose:
            print(f"  [{i}/{len(group_ids)}] Deleting group: {display_name} ({group_id})", file=sys.stderr)
        
        try:
            success, result = client.delete_group(group_id, account_id, source_id)
            
            delete_result = {
                'group_id': group_id,
                'displayName': display_name,
                'operation': 'delete',
                'success': success,
                'row_number': group_info.get('row_number')
            }
            
            if success:
                delete_result['message'] = f"Group '{display_name}' ({group_id}) deleted successfully"
                successful_deletes += 1
            else:
                delete_result['error'] = result.get('error', str(result))
                delete_result['message'] = f"Failed to delete group '{display_name}' ({group_id}): {delete_result['error']}"
                failed_deletes += 1
            
            delete_results.append(delete_result)
            
        except Exception as e:
            delete_result = {
                'group_id': group_id,
                'displayName': display_name,
                'operation': 'delete',
                'success': False,
                'error': str(e),
                'message': f"Error deleting group '{display_name}' ({group_id}): {str(e)}",
                'row_number': group_info.get('row_number')
            }
            delete_results.append(delete_result)
            failed_deletes += 1
    
    if verbose:
        print(f"Phase 2 complete: {successful_deletes} deleted, {failed_deletes} failed", file=sys.stderr)
    
    # Combine results for overall reporting
    for i, group_info in enumerate(group_ids):
        disable_result = disable_results[i] if i < len(disable_results) else {}
        delete_result = delete_results[i] if i < len(delete_results) else {}
        
        overall_result = {
            'group_id': group_info['group_id'],
            'displayName': group_info.get('displayName', 'unknown'),
            'row_number': group_info.get('row_number'),
            'disable_success': disable_result.get('success', False),
            'delete_success': delete_result.get('success', False),
            'overall_success': delete_result.get('success', False),  # Overall success is based on delete success
        }
        
        # Build combined message
        disable_status = "✓" if disable_result.get('success') else "✗"
        delete_status = "✓" if delete_result.get('success') else "✗"
        overall_result['message'] = f"Mark: {disable_status}, Delete: {delete_status} - {overall_result['displayName']} ({overall_result['group_id']})"
        
        # Include errors if any
        errors = []
        if disable_result.get('error'):
            errors.append(f"Mark: {disable_result['error']}")
        if delete_result.get('error'):
            errors.append(f"Delete: {delete_result['error']}")
        if errors:
            overall_result['errors'] = errors
        
        overall_results.append(overall_result)
    
    # Build final summary
    total_groups = len(group_ids)
    fully_successful = sum(1 for r in overall_results if r['overall_success'])
    
    summary = {
        'total_groups': total_groups,
        'mark_phase': {
            'successful': successful_disables,
            'failed': failed_disables,
            'success_rate': f"{successful_disables}/{total_groups} ({successful_disables/total_groups*100:.1f}%)"
        },
        'delete_phase': {
            'successful': successful_deletes,
            'failed': failed_deletes,
            'success_rate': f"{successful_deletes}/{total_groups} ({successful_deletes/total_groups*100:.1f}%)"
        },
        'overall': {
            'fully_successful': fully_successful,
            'partially_successful': total_groups - fully_successful,
            'success_rate': f"{fully_successful}/{total_groups} ({fully_successful/total_groups*100:.1f}%)"
        }
    }
    
    response = {
        'success': fully_successful == total_groups,
        'operation': f"Purge {total_groups} groups (mark + delete)",
        'summary': summary
    }
    
    # Only include detailed results if verbose mode is enabled
    if verbose:
        response['results'] = overall_results
    
    return [response]


def scim_purge_groups(args, configuration=None):
    """
    Purge SCIM groups from CSV or JSON file by deleting them
    Requires group_id to be present in the source file
    
    Args:
        args: Command line arguments with file_path, format, and other options
        configuration: Optional configuration (unused)
    
    Returns:
        List of operation results
    """
    try:
        # Validate file path - resolve relative to current working directory
        file_path = args.file_path
        
        # If it's not an absolute path, resolve it relative to current working directory
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Normalize the path
        file_path = os.path.normpath(file_path)
        
        if not os.path.exists(file_path):
            # Provide helpful error message with current working directory
            cwd = os.getcwd()
            return handle_scim_error(
                f"Purge file not found: {file_path}\n" +
                f"Current working directory: {cwd}\n" +
                f"Looking for file: {args.file_path}", 
                args.verbose
            )
        
        if not os.path.isfile(file_path):
            return handle_scim_error(f"Path is not a file: {file_path}", args.verbose)
        
        # Determine format from file extension or explicit format argument
        file_format = getattr(args, 'format', None)
        if not file_format:
            # Auto-detect from extension
            _, ext = os.path.splitext(file_path.lower())
            if ext == '.csv':
                file_format = 'csv'
            elif ext in ['.json', '.jsonl']:
                file_format = 'json'
            else:
                return handle_scim_error(
                    f"Cannot determine file format from extension '{ext}'. " +
                    "Use -f/--format to specify 'json' or 'csv'", 
                    args.verbose
                )
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Purging groups from {file_format.upper()} file: {file_path}", file=sys.stderr)
        
        # Parse the file to extract group_ids
        group_ids = _parse_group_ids_for_purge(file_path, file_format, args.verbose)
        
        if isinstance(group_ids, list) and len(group_ids) == 1 and 'error' in group_ids[0]:
            return group_ids  # Return error from parsing
        
        if not group_ids:
            return handle_scim_error("No valid group IDs found in file for purging", args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Found {len(group_ids)} group IDs to purge", file=sys.stderr)
            print(f"WARNING: This will DELETE {len(group_ids)} groups!", file=sys.stderr)
        
        # Confirm purge operation if not forced
        if not getattr(args, 'force', False):
            print(f"\nWARNING: You are about to PURGE {len(group_ids)} groups!")
            print("This will:")
            print("1. DELETE all groups")
            print("This operation CANNOT be undone!\n")
            
            try:
                confirmation = input("Type 'PURGE' to confirm this destructive operation: ")
                if confirmation != 'PURGE':
                    return [{
                        'success': False,
                        'operation': 'Purge groups',
                        'message': 'Operation cancelled by user',
                        'cancelled': True
                    }]
            except (KeyboardInterrupt, EOFError):
                return [{
                    'success': False,
                    'operation': 'Purge groups',
                    'message': 'Operation cancelled by user (Ctrl+C)',
                    'cancelled': True
                }]
        
        # Note: accountID and sourceID are embedded in the SCIM URL configured in the profile
        # We no longer need to extract them separately as the SCIM client handles this automatically
        
        # Perform purge operations
        return _purge_groups_from_ids(group_ids, args)
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_export_users(args, configuration=None):
    """
    Export SCIM users to JSON or CSV format
    """
    try:
        # Check if template generation is requested
        if hasattr(args, 'generate_template') and args.generate_template:
            format_type = getattr(args, 'format', 'json')
            return _generate_user_template(format_type, args)
        
        # Get SCIM client and fetch users
        client = get_scim_client(verbose=hasattr(args, 'verbose') and args.verbose)
        
        verbose = hasattr(args, 'verbose') and args.verbose
        format_type = getattr(args, 'format', 'json')
        
        if verbose:
            print("Fetching users from SCIM API...", file=sys.stderr)
        
        try:
            success, users_data = client.get_users()
            if not success:
                return handle_scim_error(f"Failed to fetch users: {users_data}", verbose)
            
            users = users_data if isinstance(users_data, list) else users_data.get('Resources', [])
            
            if not users:
                if verbose:
                    print("No users found", file=sys.stderr)
                return [{
                    'success': True,
                    'operation': 'Export users',
                    'message': 'No users found to export',
                    'user_count': 0
                }]
            
            if verbose:
                print(f"Found {len(users)} users to export", file=sys.stderr)
            
        except Exception as e:
            return handle_scim_error(f"Error fetching users: {e}", verbose)
        
        # Generate filename using shared utilities
        filename = generate_export_filename(
            args, "scim_users_export", format_type
        )
        
        # Resolve full path
        output_path = resolve_export_path(args, filename)
        
        # Ensure output directory exists
        try:
            ensure_output_directory(output_path, verbose)
        except Exception as e:
            return handle_scim_error(str(e), verbose)
        
        if verbose:
            print(f"Exporting {len(users)} users to {format_type.upper()} file: {output_path}", file=sys.stderr)
        
        # Export users based on format
        try:
            if format_type == 'csv':
                # Transform users to CSV format
                csv_data = []
                fieldnames = ['user_id', 'email', 'given_name', 'family_name', 'external_id', 'active']
                
                for user in users:
                    emails = user.get('emails', [])
                    email = emails[0].get('value') if emails else ''
                    
                    name = user.get('name', {})
                    given_name = name.get('givenName', '')
                    family_name = name.get('familyName', '')
                    
                    csv_data.append({
                        'user_id': user.get('id', ''),
                        'email': email,
                        'given_name': given_name,
                        'family_name': family_name,
                        'external_id': user.get('externalId', ''),
                        'active': str(user.get('active', True)).lower()
                    })
                
                result = write_csv_export(csv_data, output_path, fieldnames, verbose)
                return [result]
                
            elif format_type == 'json':
                # Transform users to simplified format
                json_data = []
                
                for user in users:
                    emails = user.get('emails', [])
                    email = emails[0].get('value') if emails else ''
                    
                    name = user.get('name', {})
                    given_name = name.get('givenName', '')
                    family_name = name.get('familyName', '')
                    
                    json_data.append({
                        'email': email,
                        'given_name': given_name,
                        'family_name': family_name,
                        'external_id': user.get('externalId', ''),
                        'active': user.get('active', True),
                        'user_id': user.get('id', '')
                    })
                
                result = write_json_export(json_data, output_path, verbose)
                return [result]
                
            else:
                return handle_scim_error(f"Unsupported format: {format_type}. Supported formats: csv, json", verbose)
                
        except Exception as e:
            return handle_scim_error(f"Error exporting users: {e}", verbose)
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)



