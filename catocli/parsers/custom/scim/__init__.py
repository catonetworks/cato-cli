#!/usr/bin/env python3
"""
SCIM (System for Cross-domain Identity Management) parser for Cato CLI
Handles SCIM user and group management operations via the Cato SCIM API
"""

from .scim_commands import (
    scim_add_members,
    scim_create_group, 
    scim_create_user,
    scim_create_users_from_csv,
    scim_disable_group,
    scim_disable_user,
    scim_export_users,
    scim_find_group,
    scim_find_users,
    scim_get_group,
    scim_get_groups,
    scim_get_user,
    scim_get_users,
    scim_import_users,
    scim_remove_members,
    scim_rename_group,
    scim_update_group,
    scim_update_user
)
from ...utils.export_utils import add_common_export_arguments


def scim_parse(subparsers):
    """Register SCIM commands with the CLI parser"""
    
    # Create the main SCIM parser
    scim_parser = subparsers.add_parser(
        'scim',
        help='SCIM (System for Cross-domain Identity Management) operations',
        usage='catocli scim <subcommand> [options]',
        description='''SCIM operations for user and group management with import/export capabilities.

Common Examples:
  # Export users to JSON/CSV
  catocli scim export users -f json
  catocli scim export users -f csv --append-timestamp
  
  # Import users from files
  catocli scim import users users.csv
  catocli scim import users users.json -v
  
  # Generate templates for import
  catocli scim export users -gt -f csv
  
  # User management
  catocli scim create_user '{{"email":"user@company.com","given_name":"John","family_name":"Doe","external_id":"john123"}}'
  catocli scim get_users''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    scim_subparsers = scim_parser.add_subparsers(
        description='SCIM operations for user and group management',
        help='SCIM command operations'
    )
    
    # Add Members command
    add_members_parser = scim_subparsers.add_parser(
        'add_members',
        help='Add members to an existing SCIM group',
        usage='catocli scim add_members <json_input>'
    )
    add_members_parser.add_argument('json_input', help='JSON input with group_id and members (e.g., \'{"group_id": "group123", "members": [{"value": "user_id_1"}, {"value": "user_id_2"}]}\')') 
    add_members_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    add_members_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    add_members_parser.set_defaults(func=scim_add_members)
    
    # Create Group command
    create_group_parser = scim_subparsers.add_parser(
        'create_group',
        help='Create a new SCIM group',
        usage='catocli scim create_group <json_input>'
    )
    create_group_parser.add_argument('json_input', help='JSON input with group details (e.g., \'{"display_name": "Team Name", "external_id": "team123", "members": [{"value": "user_id_1"}]}\')') 
    create_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    create_group_parser.set_defaults(func=scim_create_group)
    
    # Create User command
    create_user_parser = scim_subparsers.add_parser(
        'create_user',
        help='Create a new SCIM user',
        usage='catocli scim create_user <json_input>'
    )
    create_user_parser.add_argument('json_input', help='JSON input with user details (e.g., \'{"email": "user@company.com", "given_name": "John", "family_name": "Doe", "external_id": "john123", "password": "optional", "active": true}\')') 
    create_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    create_user_parser.set_defaults(func=scim_create_user)
    
    # Create Users from CSV command
    create_users_csv_parser = scim_subparsers.add_parser(
        'create_users_from_csv',
        help='Create multiple SCIM users from a CSV file',
        usage='catocli scim create_users_from_csv <csv_file_path> [options]'
    )
    create_users_csv_parser.add_argument('csv_file_path', help='Path to CSV file containing user data (columns: email,given_name,family_name,external_id,password,active)')
    create_users_csv_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_users_csv_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    create_users_csv_parser.add_argument('--generate-template', '-gt', dest='generate_template', action='store_true', help='Generate CSV template file instead of processing users')
    create_users_csv_parser.set_defaults(func=scim_create_users_from_csv)
    
    # Import Users command
    import_users_parser = scim_subparsers.add_parser(
        'import',
        help='Import users from CSV or JSON files',
        usage='catocli scim import users <file_path> [options]'
    )
    import_subparsers = import_users_parser.add_subparsers(
        description='Import operations for users',
        help='Import command operations'
    )
    
    import_users_subparser = import_subparsers.add_parser(
        'users',
        help='Import users from CSV or JSON file',
        usage='catocli scim import users <file_path> [options]',
        description='''Import SCIM users from CSV or JSON files with automatic format detection.

Examples:
  # Import from CSV file (auto-detected)
  catocli scim import users users.csv

  # Import from JSON file with verbose output
  catocli scim import users users.json -v

  # Specify format explicitly
  catocli scim import users data.txt -f csv

  # Import with format detection and verbose output
  catocli scim import users /path/to/users.json -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    import_users_subparser.add_argument('file_path', help='Path to CSV or JSON file containing user data')
    import_users_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    import_users_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    import_users_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    import_users_subparser.set_defaults(func=scim_import_users)
    
    # Export Users command
    export_users_parser = scim_subparsers.add_parser(
        'export',
        help='Export users to CSV or JSON files',
        usage='catocli scim export users [options]'
    )
    export_subparsers = export_users_parser.add_subparsers(
        description='Export operations for users',
        help='Export command operations'
    )
    
    export_users_subparser = export_subparsers.add_parser(
        'users',
        help='Export users to CSV or JSON file',
        usage='catocli scim export users [options]',
        description='''Export SCIM users to CSV or JSON format with flexible filename and output options.

Examples:
  # Basic export
  catocli scim export users -f json

  # Custom filename with timestamp
  catocli scim export users -f csv --csv-filename users.csv --append-timestamp

  # Generate templates
  catocli scim export users -f json -gt
  catocli scim export users -f csv -gt --append-timestamp

  # Custom output directory
  catocli scim export users --output-directory /path/to/exports''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    # Add common export arguments using shared utility
    add_common_export_arguments(export_users_subparser)
    
    # Update help text for format-specific filenames
    for action in export_users_subparser._actions:
        if action.dest == 'json_filename':
            action.help = 'Override JSON file name (default: scim_users_export.json)'
        elif action.dest == 'csv_filename':
            action.help = 'Override CSV file name (default: scim_users_export.csv)'
    export_users_subparser.set_defaults(func=scim_export_users)
    
    # Disable Group command
    disable_group_parser = scim_subparsers.add_parser(
        'disable_group',
        help='Disable a SCIM group',
        usage='catocli scim disable_group <json_input>'
    )
    disable_group_parser.add_argument('json_input', help='JSON input with group_id (e.g., \'{"group_id": "group123"}\')') 
    disable_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    disable_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    disable_group_parser.set_defaults(func=scim_disable_group)
    
    # Disable User command
    disable_user_parser = scim_subparsers.add_parser(
        'disable_user',
        help='Disable a SCIM user',
        usage='catocli scim disable_user <json_input>'
    )
    disable_user_parser.add_argument('json_input', help='JSON input with user_id (e.g., \'{"user_id": "user123"}\')') 
    disable_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    disable_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    disable_user_parser.set_defaults(func=scim_disable_user)
    
    # Find Group command
    find_group_parser = scim_subparsers.add_parser(
        'find_group',
        help='Find SCIM groups by display name',
        usage='catocli scim find_group <json_input>'
    )
    find_group_parser.add_argument('json_input', help='JSON input with display_name (e.g., \'{"display_name": "Development Team"}\')') 
    find_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    find_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    find_group_parser.set_defaults(func=scim_find_group)
    
    # Find Users command
    find_users_parser = scim_subparsers.add_parser(
        'find_users',
        help='Find SCIM users by field and value',
        usage='catocli scim find_users <json_input>'
    )
    find_users_parser.add_argument('json_input', help='JSON input with field and value (e.g., \'{"field": "email", "value": "user@company.com"}\')') 
    find_users_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    find_users_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    find_users_parser.set_defaults(func=scim_find_users)
    
    # Get Group command
    get_group_parser = scim_subparsers.add_parser(
        'get_group',
        help='Get a specific SCIM group by ID',
        usage='catocli scim get_group <json_input>'
    )
    get_group_parser.add_argument('json_input', help='JSON input with group_id (e.g., \'{"group_id": "group123"}\')') 
    get_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    get_group_parser.set_defaults(func=scim_get_group)
    
    # Get Groups command
    get_groups_parser = scim_subparsers.add_parser(
        'get_groups',
        help='Get all SCIM groups',
        usage='catocli scim get_groups'
    )
    get_groups_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_groups_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    get_groups_parser.set_defaults(func=scim_get_groups)
    
    # Get User command
    get_user_parser = scim_subparsers.add_parser(
        'get_user',
        help='Get a specific SCIM user by ID',
        usage='catocli scim get_user <json_input>'
    )
    get_user_parser.add_argument('json_input', help='JSON input with user_id (e.g., \'{"user_id": "user123"}\')') 
    get_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    get_user_parser.set_defaults(func=scim_get_user)
    
    # Get Users command
    get_users_parser = scim_subparsers.add_parser(
        'get_users',
        help='Get all SCIM users',
        usage='catocli scim get_users'
    )
    get_users_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_users_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    get_users_parser.set_defaults(func=scim_get_users)
    
    # Remove Members command
    remove_members_parser = scim_subparsers.add_parser(
        'remove_members',
        help='Remove members from a SCIM group',
        usage='catocli scim remove_members <json_input>'
    )
    remove_members_parser.add_argument('json_input', help='JSON input with group_id and members (e.g., \'{"group_id": "group123", "members": [{"value": "user_id_1"}, {"value": "user_id_2"}]}\')') 
    remove_members_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    remove_members_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    remove_members_parser.set_defaults(func=scim_remove_members)
    
    # Rename Group command
    rename_group_parser = scim_subparsers.add_parser(
        'rename_group',
        help='Rename a SCIM group',
        usage='catocli scim rename_group <json_input>'
    )
    rename_group_parser.add_argument('json_input', help='JSON input with group_id and new_name (e.g., \'{"group_id": "group123", "new_name": "Updated Team Name"}\')') 
    rename_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    rename_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    rename_group_parser.set_defaults(func=scim_rename_group)
    
    # Update Group command
    update_group_parser = scim_subparsers.add_parser(
        'update_group',
        help='Update a SCIM group with complete group data',
        usage='catocli scim update_group <json_input>'
    )
    update_group_parser.add_argument('json_input', help='JSON input with group_id and group data (e.g., \'{"group_id": "group123", "group_data": {"schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"], "displayName": "Team"}}\')') 
    update_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    update_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    update_group_parser.set_defaults(func=scim_update_group)
    
    # Update User command
    update_user_parser = scim_subparsers.add_parser(
        'update_user',
        help='Update a SCIM user with complete user data',
        usage='catocli scim update_user <json_input>'
    )
    update_user_parser.add_argument('json_input', help='JSON input with user_id and user data (e.g., \'{"user_id": "user123", "user_data": {"schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"], "userName": "user@company.com"}}\')') 
    update_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    update_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    update_user_parser.set_defaults(func=scim_update_user)
    
    return scim_parser
