#!/usr/bin/env python3
"""
SCIM command implementations for Cato CLI
Handles all SCIM user and group management operations
"""

import json
import sys
from .scim_client import get_scim_client


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


def scim_add_members(args, configuration=None):
    """Add members to an existing SCIM group"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
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
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        display_name = json_data.get('display_name')
        external_id = json_data.get('external_id')
        members = json_data.get('members', [])
        
        if not display_name:
            return handle_scim_error("Missing required field: display_name", args.verbose)
        if not external_id:
            return handle_scim_error("Missing required field: external_id", args.verbose)
        
        # Validate members format if provided
        if members:
            if not isinstance(members, list):
                return handle_scim_error("Members must be a JSON array", args.verbose)
            
            for member in members:
                if not isinstance(member, dict) or 'value' not in member:
                    return handle_scim_error("Each member must be an object with a 'value' field", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
        success, result = client.create_group(display_name, external_id, members)
        
        return format_scim_response(
            success, result, f"Create group '{display_name}'",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_create_user(args, configuration=None):
    """Create a new SCIM user"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        email = json_data.get('email')
        given_name = json_data.get('given_name')
        family_name = json_data.get('family_name')
        external_id = json_data.get('external_id')
        password = json_data.get('password')
        active = json_data.get('active', True)  # Default to True
        
        if not email:
            return handle_scim_error("Missing required field: email", args.verbose)
        if not given_name:
            return handle_scim_error("Missing required field: given_name", args.verbose)
        if not family_name:
            return handle_scim_error("Missing required field: family_name", args.verbose)
        if not external_id:
            return handle_scim_error("Missing required field: external_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
        success, result = client.create_user(
            email, given_name, family_name, external_id, password, active
        )
        
        return format_scim_response(
            success, result, f"Create user '{email}'",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_disable_group(args, configuration=None):
    """Disable a SCIM group"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        user_id = json_data.get('user_id')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        display_name = json_data.get('display_name')
        
        if not display_name:
            return handle_scim_error("Missing required field: display_name", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
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
        valid_fields = ['userName', 'email', 'givenName', 'familyName']
        if field not in valid_fields:
            return handle_scim_error(f"Invalid field. Must be one of: {', '.join(valid_fields)}", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        group_id = json_data.get('group_id')
        
        if not group_id:
            return handle_scim_error("Missing required field: group_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
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
        client = get_scim_client()
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
    """Get a specific SCIM user by ID"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        user_id = json_data.get('user_id')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
        success, result = client.get_user(user_id)
        
        return format_scim_response(
            success, result, f"Get user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_get_users(args, configuration=None):
    """Get all SCIM users"""
    try:
        # Get SCIM client and execute operation
        client = get_scim_client()
        success, result = client.get_users()
        
        if success:
            # Format the results to show count
            formatted_result = {
                "total_users": len(result),
                "users": result
            }
            return format_scim_response(
                success, formatted_result, "Get all users",
                args.verbose, args.pretty
            )
        else:
            return format_scim_response(
                success, result, "Get all users",
                args.verbose, args.pretty
            )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_remove_members(args, configuration=None):
    """Remove members from a SCIM group"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
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
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
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
        client = get_scim_client()
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
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
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
        client = get_scim_client()
        success, result = client.update_group(group_id, group_data)
        
        return format_scim_response(
            success, result, f"Update group {group_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)


def scim_update_user(args, configuration=None):
    """Update a SCIM user with complete user data"""
    try:
        # Parse JSON input
        try:
            json_data = json.loads(args.json_input)
        except json.JSONDecodeError as e:
            return handle_scim_error(f"Invalid JSON input: {e}", args.verbose)
        
        # Validate required fields
        if not isinstance(json_data, dict):
            return handle_scim_error("Input must be a JSON object", args.verbose)
            
        user_id = json_data.get('user_id')
        user_data = json_data.get('user_data')
        
        if not user_id:
            return handle_scim_error("Missing required field: user_id", args.verbose)
        if not user_data:
            return handle_scim_error("Missing required field: user_data", args.verbose)
        
        # Validate user data format
        if not isinstance(user_data, dict):
            return handle_scim_error("User data must be a JSON object", args.verbose)
        
        # Get SCIM client and execute operation
        client = get_scim_client()
        success, result = client.update_user(user_id, user_data)
        
        return format_scim_response(
            success, result, f"Update user {user_id}",
            args.verbose, args.pretty
        )
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)
