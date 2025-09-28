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




def _parse_csv_users(file_path, verbose=False):
    """
    Parse users from CSV file
    
    Returns:
        List of user dictionaries or error response
    """
    users_data = []
    required_columns = ['email', 'given_name', 'family_name', 'external_id']
    optional_columns = ['password', 'active']
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
                
                user_data = {
                    'email': row['email'].strip(),
                    'given_name': row['given_name'].strip(),
                    'family_name': row['family_name'].strip(),
                    'external_id': row['external_id'].strip(),
                    'password': row.get('password', '').strip() or None,  # Convert empty string to None
                    'active': active,
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
    optional_fields = ['password', 'active']
    
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
                
                user_data = {
                    'email': user['email'].strip(),
                    'given_name': user['given_name'].strip(),
                    'family_name': user['family_name'].strip(),
                    'external_id': user['external_id'].strip(),
                    'password': user.get('password', '').strip() or None,
                    'active': active,
                    'row_number': idx
                }
                
                users_data.append(user_data)
    
    except Exception as e:
        return handle_scim_error(f"Error processing JSON file: {e}", verbose)
    
    return users_data


def _create_users_from_data(users_data, args):
    """
    Create users from parsed data using SCIM client
    """
    # Get SCIM client
    client = get_scim_client()
    
    # Create users and collect results
    results = []
    successful_users = []
    failed_users = []
    
    for user_data in users_data:
        row_num = user_data.pop('row_number')  # Remove row_number before API call
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Creating user: {user_data['email']}", file=sys.stderr)
        
        try:
            success, result = client.create_user(
                user_data['email'],
                user_data['given_name'],
                user_data['family_name'],
                user_data['external_id'],
                user_data['password'],
                user_data['active']
            )
            
            user_result = {
                'row_number': row_num,
                'email': user_data['email'],
                'success': success,
            }
            
            if success:
                user_result['user_id'] = result.get('id', 'unknown')
                if user_data['active']:
                    user_result['message'] = f"User '{user_data['email']}' created successfully"
                else:
                    user_result['message'] = f"User '{user_data['email']}' created successfully and disabled as requested"
                    if result.get('warning'):
                        user_result['warning'] = result['warning']
                successful_users.append(user_result)
            else:
                user_result['error'] = result.get('error', str(result))
                user_result['message'] = f"Failed to create user '{user_data['email']}': {user_result['error']}"
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
    
    # Format final response
    summary = {
        'total_users': len(users_data),
        'successful_users': len(successful_users),
        'failed_users': len(failed_users),
        'success_rate': f"{len(successful_users)}/{len(users_data)} ({len(successful_users)/len(users_data)*100:.1f}%)"
    }
    
    response = {
        'success': len(failed_users) == 0,  # Overall success only if no failures
        'operation': f"Import {len(users_data)} users",
        'summary': summary,
        'results': results
    }
    
    return [response]




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
    client = get_scim_client()
    
    if verbose:
        print("Fetching users from SCIM API...", file=sys.stderr)
    
    try:
        success, users_data = client.list_users()
        if not success:
            return handle_scim_error(f"Failed to fetch users: {users_data}", verbose)
        
        users = users_data.get('Resources', [])
        
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
            fieldnames = ['email', 'given_name', 'family_name', 'external_id', 'active', 'user_id']
            
            for user in users:
                emails = user.get('emails', [])
                email = emails[0].get('value') if emails else ''
                
                name = user.get('name', {})
                given_name = name.get('givenName', '')
                family_name = name.get('familyName', '')
                
                csv_data.append({
                    'email': email,
                    'given_name': given_name,
                    'family_name': family_name,
                    'external_id': user.get('externalId', ''),
                    'active': str(user.get('active', True)).lower(),
                    'user_id': user.get('id', '')
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
    Generate template files for user import
    
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
    
    # Create sample template data with helpful examples
    sample_users = [
        {
            'email': 'john.doe@example.com',
            'given_name': 'John',
            'family_name': 'Doe',
            'external_id': 'john.doe',
            'password': 'optional_password',
            'active': True if format_type == 'json' else 'true'  # Active user with password
        },
        {
            'email': 'jane.smith@example.com',
            'given_name': 'Jane', 
            'family_name': 'Smith',
            'external_id': 'jane.smith',
            'password': None if format_type == 'json' else '',  # No password for inactive user
            'active': False if format_type == 'json' else 'false'  # Will be created as active then disabled
        }
    ]
    
    try:
        if format_type == 'csv':
            fieldnames = ['email', 'given_name', 'family_name', 'external_id', 'password', 'active']
            result = write_csv_export(sample_users, output_path, fieldnames, verbose)
        elif format_type == 'json':
            result = write_json_export(sample_users, output_path, verbose)
        else:
            return handle_scim_error(f"Unsupported format for template: {format_type}", verbose)
        
        # Update result to indicate template generation
        result['operation'] = f"Generate {format_type.upper()} template"
        result['message'] = f"Template file created: {output_path}"
        
        return [result]
    
    except Exception as e:
        return handle_scim_error(f"Error generating template: {e}", verbose)


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
        client = get_scim_client()
        
        verbose = hasattr(args, 'verbose') and args.verbose
        format_type = getattr(args, 'format', 'json')
        
        if verbose:
            print("Fetching users from SCIM API...", file=sys.stderr)
        
        try:
            success, users_data = client.list_users()
            if not success:
                return handle_scim_error(f"Failed to fetch users: {users_data}", verbose)
            
            users = users_data.get('Resources', [])
            
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
                fieldnames = ['email', 'given_name', 'family_name', 'external_id', 'active', 'user_id']
                
                for user in users:
                    emails = user.get('emails', [])
                    email = emails[0].get('value') if emails else ''
                    
                    name = user.get('name', {})
                    given_name = name.get('givenName', '')
                    family_name = name.get('familyName', '')
                    
                    csv_data.append({
                        'email': email,
                        'given_name': given_name,
                        'family_name': family_name,
                        'external_id': user.get('externalId', ''),
                        'active': str(user.get('active', True)).lower(),
                        'user_id': user.get('id', '')
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


# Legacy function for backward compatibility
def scim_create_users_from_csv(args, configuration=None):
    """
    Create multiple SCIM users from a CSV file
    
    CSV format:
    email,given_name,family_name,external_id,password,active
    user1@example.com,John,Doe,john.doe,temp123,true
    user2@example.com,Jane,Smith,jane.smith,,true
    """
    try:
        # Check if template generation is requested
        if hasattr(args, 'generate_template') and args.generate_template:
            return _generate_user_template('csv', args)
        
        # Validate CSV file path - resolve relative to current working directory
        csv_file_path = args.csv_file_path
        
        # If it's not an absolute path, resolve it relative to current working directory
        if not os.path.isabs(csv_file_path):
            csv_file_path = os.path.join(os.getcwd(), csv_file_path)
        
        # Normalize the path
        csv_file_path = os.path.normpath(csv_file_path)
        
        if not os.path.exists(csv_file_path):
            # Provide helpful error message with current working directory
            cwd = os.getcwd()
            return handle_scim_error(
                f"CSV file not found: {csv_file_path}\n" +
                f"Current working directory: {cwd}\n" +
                f"Looking for file: {args.csv_file_path}", 
                args.verbose
            )
        
        if not os.path.isfile(csv_file_path):
            return handle_scim_error(f"Path is not a file: {csv_file_path}", args.verbose)
        
        # Read and validate CSV file
        users_data = []
        required_columns = ['email', 'given_name', 'family_name', 'external_id']
        optional_columns = ['password', 'active']
        all_columns = required_columns + optional_columns
        
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Validate CSV headers
                if not reader.fieldnames:
                    return handle_scim_error("CSV file has no headers", args.verbose)
                
                # Check for required columns
                missing_columns = [col for col in required_columns if col not in reader.fieldnames]
                if missing_columns:
                    return handle_scim_error(f"Missing required CSV columns: {', '.join(missing_columns)}", args.verbose)
                
                # Check for unexpected columns
                unexpected_columns = [col for col in reader.fieldnames if col not in all_columns]
                if unexpected_columns and hasattr(args, 'verbose') and args.verbose:
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
                            args.verbose
                        )
                    
                    # Parse and validate the 'active' field
                    active_str = row.get('active', 'true').strip().lower()
                    if active_str in ['true', '1', 'yes', 'y']:
                        active = True
                    elif active_str in ['false', '0', 'no', 'n']:
                        active = False
                    else:
                        active = True  # Default to true for invalid values
                        if hasattr(args, 'verbose') and args.verbose:
                            print(f"Warning: Row {row_num}: Invalid 'active' value '{row.get('active', '')}', defaulting to true", file=sys.stderr)
                    
                    user_data = {
                        'email': row['email'].strip(),
                        'given_name': row['given_name'].strip(),
                        'family_name': row['family_name'].strip(),
                        'external_id': row['external_id'].strip(),
                        'password': row.get('password', '').strip() or None,  # Convert empty string to None
                        'active': active,
                        'row_number': row_num
                    }
                    
                    users_data.append(user_data)
        
        except csv.Error as e:
            return handle_scim_error(f"Error reading CSV file: {e}", args.verbose)
        except Exception as e:
            return handle_scim_error(f"Error processing CSV file: {e}", args.verbose)
        
        if not users_data:
            return handle_scim_error("No valid user data found in CSV file", args.verbose)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Found {len(users_data)} users in CSV file", file=sys.stderr)
        
        # Get SCIM client
        client = get_scim_client()
        
        # Create users and collect results
        results = []
        successful_users = []
        failed_users = []
        
        for user_data in users_data:
            row_num = user_data.pop('row_number')  # Remove row_number before API call
            
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Creating user: {user_data['email']}", file=sys.stderr)
            
            try:
                success, result = client.create_user(
                    user_data['email'],
                    user_data['given_name'],
                    user_data['family_name'],
                    user_data['external_id'],
                    user_data['password'],
                    user_data['active']
                )
                
                user_result = {
                    'row_number': row_num,
                    'email': user_data['email'],
                    'success': success,
                }
                
                if success:
                    user_result['user_id'] = result.get('id', 'unknown')
                    user_result['message'] = f"User '{user_data['email']}' created successfully"
                    successful_users.append(user_result)
                else:
                    user_result['error'] = result.get('error', str(result))
                    user_result['message'] = f"Failed to create user '{user_data['email']}': {user_result['error']}"
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
        
        # Format final response
        summary = {
            'total_users': len(users_data),
            'successful_users': len(successful_users),
            'failed_users': len(failed_users),
            'success_rate': f"{len(successful_users)}/{len(users_data)} ({len(successful_users)/len(users_data)*100:.1f}%)"
        }
        
        response = {
            'success': len(failed_users) == 0,  # Overall success only if no failures
            'operation': f"Create {len(users_data)} users from CSV",
            'summary': summary,
            'results': results
        }
        
        # Print summary to stderr for user visibility
        if hasattr(args, 'verbose') and args.verbose:
            print(f"\nSummary:", file=sys.stderr)
            print(f"  Total users: {summary['total_users']}", file=sys.stderr)
            print(f"  Successful: {summary['successful_users']}", file=sys.stderr)
            print(f"  Failed: {summary['failed_users']}", file=sys.stderr)
            print(f"  Success rate: {summary['success_rate']}", file=sys.stderr)
        
        return [response]
        
    except Exception as e:
        return handle_scim_error(e, args.verbose)
