#!/usr/bin/env python3
"""
SCIM (System for Cross-domain Identity Management) parser for Cato CLI
Handles SCIM user and group management operations via the Cato SCIM API
"""

from .scim_commands import (
    scim_add_members,
    scim_create_group, 
    scim_create_user,
    scim_delete_group,
    scim_delete_user,
    scim_disable_group,
    scim_disable_user,
    scim_export_users,
    scim_export_groups,
    scim_find_group,
    scim_find_users,
    scim_get_group,
    scim_get_groups,
    scim_get_user,
    scim_get_users,
    scim_import_users,
    scim_import_groups,
    scim_patch_group,
    scim_patch_user,
    scim_purge_users,
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
        description='''SCIM operations for user and group management with comprehensive API support.

=== QUICK START EXAMPLES ===
  # Export users to JSON/CSV
  catocli scim export users -f json
  catocli scim export users -f csv --append-timestamp
  
  # Import users from files
  catocli scim import users users.csv
  catocli scim import users users.json
  
  # Generate templates for import
  catocli scim export users -gt -f csv

=== FULL API EXAMPLES ===

  # Create user with full UserDTO schema
  catocli scim create_user '{
    "source_id": 1,
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "john.doe@company.com",
    "externalId": "emp001",
    "name": {
      "givenName": "John",
      "familyName": "Doe"
    },
    "emails": [{
      "value": "john.doe@company.com",
      "primary": true,
      "type": "work"
    }],
    "active": true
  }'
  
  # Get user with all parameters
  catocli scim get_user '{
    "source_id": 1,
    "user_id": "usr456",
    "excluded_attributes": "password"
  }'
  
  # Search users with pagination
  catocli scim get_users '{
    "source_id": 1,
    "count": 50,
    "startIndex": 1,
    "params": {
      "filter": "emails[type eq \\"work\\"]"
    }
  }'
  
  # Patch user (partial update)
  catocli scim patch_user '{
    "source_id": 1,
    "user_id": "usr456",
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [
      {
        "op": "replace",
        "path": "active",
        "value": false
      },
      {
        "op": "replace",
        "path": "name.givenName",
        "value": "Jonathan"
      }
    ]
  }'

  # Create group with members
  catocli scim create_group '{
    "source_id": 1,
    "displayName": "Engineering Team",
    "externalId": "eng-team-001",
    "members": [
      {"value": "usr456"},
      {"value": "usr789"}
    ]
  }'
  
  # Delete operations
  catocli scim delete_user '{
    "source_id": 1,
    "user_id": "usr456"
  }'
  
  # Purge users (DESTRUCTIVE - disable then delete)
  catocli scim purge users users_to_delete.csv --source-id 1 -v

=== PARAMETER REFERENCE ===

Required Path Parameters (all operations):
  - accountID: String - SCIM account identifier (from ~/.cato config)
  - source_id: Integer - SCIM source identifier (command line parameter)
  - id: String - Resource ID (users/groups)

Optional Query Parameters:
  - excluded_attributes: String - Comma-separated attributes to exclude
  - count: Integer - Number of results per page (default: system defined)
  - startIndex: Integer - 1-based start index for pagination
  - params: Object - Additional query parameters (filters, etc.)

Supported PATCH Operations:
  - "add": Add new attribute/value
  - "remove": Remove attribute/value  
  - "replace": Replace attribute value''',
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
        help='Create a new SCIM user with full UserDTO schema support',
        usage='catocli scim create_user <json_input>',
        description='''Create a SCIM user with complete UserDTO schema support.

Required Parameters:
  - source_id: SCIM source identifier
  - userName (or email): Primary username/email
  - externalId (or external_id): External identifier
  - accountID: SCIM account identifier (from ~/.cato config)

Optional Parameters:
  - schemas: Array of SCIM schemas (default: core User schema)
  - name: Name object with givenName/familyName
  - emails: Array of email objects
  - phoneNumbers: Array of phone number objects
  - active: Boolean active status (default: true)
  - Cato extension data

Examples:
  # Simple user creation (backward compatible)
  catocli scim create_user '{
    "source_id": 1,
    "email": "john@company.com",
    "given_name": "John",
    "family_name": "Doe",
    "external_id": "emp001"
  }'
  
  # Full UserDTO schema
  catocli scim create_user '{
    "source_id": 1,
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "john.doe@company.com",
    "externalId": "emp001",
    "name": {
      "givenName": "John",
      "familyName": "Doe"
    },
    "emails": [{
      "value": "john.doe@company.com",
      "primary": true,
      "type": "work"
    }],
    "phoneNumbers": [{
      "value": "+1-555-123-4567",
      "primary": true,
      "type": "work"
    }],
    "active": true
  }'
  
  # With Cato extension
  catocli scim create_user '{
    "source_id": 1,
    "userName": "john@company.com",
    "externalId": "emp001",
    "urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User": {
      "onPremisesSecurityIdentifier": "S-1-5-21-...",
      "dirSyncEnabled": true
    }
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    create_user_parser.add_argument('json_input', help='JSON input with complete user data including account_id, source_id, and UserDTO fields')
    create_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    create_user_parser.set_defaults(func=scim_create_user)
    
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
        description='''Import SCIM users from CSV or JSON files with smart create/update detection and processed file output.

=== SMART CREATE/UPDATE DETECTION ===
The import automatically detects whether to create or update users based on the user_id column:
- If user_id is empty or missing: CREATE new user
- If user_id is present: UPDATE existing user

=== PROCESSED CSV OUTPUT ===
Use --write-processed to generate an updated CSV file with all user_ids populated:
- New users will have their generated user_ids filled in
- Existing users will retain their original user_ids
- Output format: original_name_processed_YYYYMMDD_HHMMSS.csv

=== CSV FORMAT ===
Required columns: email, given_name, family_name, external_id
Optional columns: user_id, password, active

=== EXAMPLES ===
  # Basic import (creates new users)
  catocli scim import users users.csv

  # Import with processed file output
  catocli scim import users users.csv --write-processed-file -v

  # Import existing users (CSV with user_id column populated)
  catocli scim import users existing_users.csv --write-processed-file

  # Mixed create/update (some rows have user_id, others don't)
  catocli scim import users mixed_users.csv --write-processed-file -v

  # JSON import with verbose output
  catocli scim import users users.json -v

  # Specify format explicitly
  catocli scim import users data.txt -f csv --write-processed-file
  catocli scim import users data.txt -f csv -wp

=== WORKFLOW EXAMPLE ===
1. Export users to get current data with user_ids:
   catocli scim export users -f csv --csv-filename current_users.csv

2. Edit the CSV file (add, modify, or remove users)

3. Re-import with processed output:
   catocli scim import users current_users.csv --write-processed-file
   catocli scim import users current_users.csv -wp

4. Use the processed file for future imports:
   catocli scim import users current_users_processed_20231201_143022.csv''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    import_users_subparser.add_argument('file_path', help='Path to CSV or JSON file containing user data')
    import_users_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    import_users_subparser.add_argument('-wp', '--write-processed-file', dest='write_processed', action='store_true', help='Write processed CSV file with all user_ids populated (format: original_name_processed_timestamp.csv)')
    import_users_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    import_users_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    import_users_subparser.set_defaults(func=scim_import_users)
    
    # Add groups import functionality
    import_groups_subparser = import_subparsers.add_parser(
        'groups',
        help='Import groups from CSV or JSON file',
        usage='catocli scim import groups <file_path> [options]',
        description='''Import SCIM groups from CSV or JSON files with automatic format detection.

Examples:
  # Import from CSV file (auto-detected)
  catocli scim import groups groups.csv

  # Import from JSON file with verbose output
  catocli scim import groups groups.json -v

  # Specify format explicitly
  catocli scim import groups data.txt -f csv

  # Import with format detection and verbose output
  catocli scim import groups /path/to/groups.json -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    import_groups_subparser.add_argument('file_path', help='Path to CSV or JSON file containing group data')
    import_groups_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    import_groups_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    import_groups_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    import_groups_subparser.set_defaults(func=scim_import_groups)
    
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
    
    # Add groups export functionality
    export_groups_subparser = export_subparsers.add_parser(
        'groups',
        help='Export groups to CSV or JSON file',
        usage='catocli scim export groups [options]',
        description='''Export SCIM groups to CSV or JSON format with flexible filename and output options.

Examples:
  # Basic export
  catocli scim export groups -f json

  # Custom filename with timestamp
  catocli scim export groups -f csv --csv-filename groups.csv --append-timestamp

  # Generate templates
  catocli scim export groups -f json -gt
  catocli scim export groups -f csv -gt --append-timestamp

  # Custom output directory
  catocli scim export groups --output-directory /path/to/exports''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    # Add common export arguments using shared utility
    add_common_export_arguments(export_groups_subparser)
    
    # Update help text for format-specific filenames
    for action in export_groups_subparser._actions:
        if action.dest == 'json_filename':
            action.help = 'Override JSON file name (default: scim_groups_export.json)'
        elif action.dest == 'csv_filename':
            action.help = 'Override CSV file name (default: scim_groups_export.csv)'
    export_groups_subparser.set_defaults(func=scim_export_groups)
    
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
        help='Get a specific SCIM user by ID with full parameter support',
        usage='catocli scim get_user <json_input>',
        description='''Retrieve a specific SCIM user with support for all swagger parameters.

Required Parameters:
  - source_id: SCIM source identifier  
  - user_id (or id): User identifier
  - accountID: SCIM account identifier (from ~/.cato config)

Optional Parameters:
  - excluded_attributes: Comma-separated list of attributes to exclude

Examples:
  # Basic user retrieval
  catocli scim get_user '{
    "source_id": 1,
    "user_id": "usr456"
  }'
  
  # Exclude sensitive attributes
  catocli scim get_user '{
    "source_id": 1,
    "user_id": "usr456",
    "excluded_attributes": "password,secret"
  }'
''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    get_user_parser.add_argument('json_input', help='JSON input with account_id, source_id, user_id, and optional excluded_attributes') 
    get_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    get_user_parser.set_defaults(func=scim_get_user)
    
    # Get Users command
    get_users_parser = scim_subparsers.add_parser(
        'get_users',
        help='Get SCIM users with pagination and search support',
        usage='catocli scim get_users [json_input]',
        description='''Retrieve SCIM users with full pagination and search capabilities.

Required Parameters:
  - source_id: SCIM source identifier
  - accountID: SCIM account identifier (from ~/.cato config)

Optional Parameters:
  - count: Number of results per page (integer)
  - startIndex (or start_index): 1-based start index for pagination
  - params: Object with additional query parameters (filters, etc.)

Examples:
  # Get all users (basic)
  catocli scim get_users \'{
    "source_id": 1
  }\'
  
  # Paginated results
  catocli scim get_users \'{
    "source_id": 1,
    "count": 50,
    "startIndex": 1
  }\'
  
  # With search filters
  catocli scim get_users \'{
    "source_id": 1,
    "count": 25,
    "startIndex": 1,
    "params": {
      "filter": "emails[type eq \\"work\\"]",
      "sortBy": "name.familyName",
      "sortOrder": "ascending"
    }
  }\' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    get_users_parser.add_argument('json_input', nargs='?', help='Optional JSON input with pagination and search parameters')
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
    
    # Patch User command
    patch_user_parser = scim_subparsers.add_parser(
        'patch_user',
        help='Patch a SCIM user with partial updates (PATCH operation)',
        usage='catocli scim patch_user <json_input>',
        description='''Perform partial updates on a SCIM user using PATCH operations.

Required Parameters:
  - source_id: SCIM source identifier
  - user_id (or id): User identifier
  - Operations: Array of patch operations
  - accountID: SCIM account identifier (from ~/.cato config)

Supported Operations:
  - "add": Add new attribute/value
  - "remove": Remove attribute/value
  - "replace": Replace attribute value

Examples:
  # Disable user
  catocli scim patch_user '{
    "source_id": 1,
    "user_id": "usr456",
    "Operations": [
      {
        "op": "replace",
        "path": "active",
        "value": false
      }
    ]
  }'
  
  # Update multiple fields
  catocli scim patch_user '{
    "source_id": 1,
    "user_id": "usr456",
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [
      {
        "op": "replace",
        "path": "name.givenName",
        "value": "Jonathan"
      },
      {
        "op": "add",
        "path": "phoneNumbers",
        "value": [{
          "value": "+1-555-987-6543",
          "type": "mobile"
        }]
      },
      {
        "op": "remove",
        "path": "emails[type eq \\"personal\\"]"
      }
    ]
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    patch_user_parser.add_argument('json_input', help='JSON input with patch operations for the user')
    patch_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    patch_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    patch_user_parser.set_defaults(func=scim_patch_user)
    
    # Delete User command
    delete_user_parser = scim_subparsers.add_parser(
        'delete_user',
        help='Delete a SCIM user (DELETE operation)',
        usage='catocli scim delete_user <json_input>'
    )
    delete_user_parser.add_argument('json_input', help='JSON input with account_id, source_id, and user_id (e.g., \'{"account_id": "acc123", "source_id": 1, "user_id": "usr456"}\')') 
    delete_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    delete_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    delete_user_parser.set_defaults(func=scim_delete_user)
    
    # Patch Group command
    patch_group_parser = scim_subparsers.add_parser(
        'patch_group',
        help='Patch a SCIM group with partial updates (PATCH operation)',
        usage='catocli scim patch_group <json_input>'
    )
    patch_group_parser.add_argument('json_input', help='JSON input with patch operations for the group (e.g., \'{"account_id": "acc123", "source_id": 1, "group_id": "grp456", "Operations": [{"op": "replace", "path": "displayName", "value": "New Name"}]}\')') 
    patch_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    patch_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    patch_group_parser.set_defaults(func=scim_patch_group)
    
    # Delete Group command
    delete_group_parser = scim_subparsers.add_parser(
        'delete_group',
        help='Delete a SCIM group (DELETE operation)',
        usage='catocli scim delete_group <json_input>'
    )
    delete_group_parser.add_argument('json_input', help='JSON input with account_id, source_id, and group_id (e.g., \'{"account_id": "acc123", "source_id": 1, "group_id": "grp456"}\')') 
    delete_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    delete_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    delete_group_parser.set_defaults(func=scim_delete_group)
    
    # Purge Users command
    purge_users_parser = scim_subparsers.add_parser(
        'purge',
        help='Purge SCIM users (disable then delete) from CSV or JSON files',
        usage='catocli scim purge users <file_path> --source-id <id> [options]'
    )
    purge_subparsers = purge_users_parser.add_subparsers(
        description='Purge operations for users',
        help='Purge command operations'
    )
    
    purge_users_subparser = purge_subparsers.add_parser(
        'users',
        help='Purge users by first disabling then deleting them',
        usage='catocli scim purge users <file_path> --source-id <id> [options]',
        description='''Purge SCIM users by first disabling then deleting them (DESTRUCTIVE OPERATION).

=== WARNING: DESTRUCTIVE OPERATION ===
This command will PERMANENTLY DELETE users from your SCIM system!
The operation is performed in two phases:
1. DISABLE all users (set active=false)
2. DELETE all users from the system

=== REQUIREMENTS ===
- File must contain user_id column/field with valid user IDs
- All users with valid user_ids will be processed
- Empty user_id entries are skipped

=== CONFIRMATION ===
By default, the command requires typing 'PURGE' to confirm the operation.
Use --force to skip confirmation (use with extreme caution!).

=== FILE COMPATIBILITY ===
Supports the same CSV/JSON files used by import/export commands:
- CSV: Must have user_id column (other columns ignored)
- JSON: Must have user_id field in each user object

=== EXAMPLES ===
  # Basic purge with confirmation
  catocli scim purge users users_processed.csv --source-id 1
  
  # Purge with verbose output
  catocli scim purge users users_to_delete.csv --source-id 1 -v
  
  # Force purge without confirmation (DANGEROUS!)
  catocli scim purge users old_users.json --source-id 1 --force
  
  # Purge with explicit format
  catocli scim purge users data.txt -f csv --source-id 1 -v

=== WORKFLOW EXAMPLE ===
1. Export current users:
   catocli scim export users -f csv --csv-filename all_users.csv
   
2. Filter users to delete (keep only users you want to purge):
   # Edit all_users.csv to contain only users to be purged
   
3. Purge the filtered users:
   catocli scim purge users users_to_purge.csv --source-id 1 -v

=== SAFETY NOTES ===
- Always backup your user data before purging
- Test with a small subset first
- Use --verbose to monitor progress
- The operation CANNOT be undone
- Users will be completely removed from the SCIM system''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    purge_users_subparser.add_argument('file_path', help='Path to CSV or JSON file containing user_ids to purge')
    purge_users_subparser.add_argument('--source-id', type=int, required=True, help='SCIM source identifier (required)')
    purge_users_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    purge_users_subparser.add_argument('--force', action='store_true', help='Skip confirmation prompt (DANGEROUS - use with extreme caution)')
    purge_users_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output with detailed progress')
    purge_users_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    purge_users_subparser.set_defaults(func=scim_purge_users)
    
    return scim_parser
