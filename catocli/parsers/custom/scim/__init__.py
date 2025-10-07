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
    scim_purge_groups,
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
  catocli scim create_user -p '{
    "source_id": 1,
    "userName": "test@company.com",
    "externalId": "test001",
    "given_name": "Test",
    "family_name": "User",
    "password": "SecurePass123!",
    "active": trie
  }'
  
  # Get user with all parameters
  catocli scim get_user -p '{
    "source_id": 1,
    "user_id": "usr456",
    "excluded_attributes": "password"
  }'
  
  # Search users with pagination
  catocli scim get_users -p '{
    "source_id": 1,
    "count": 50,
    "startIndex": 1,
    "params": {
      "filter": "emails[type eq \\"work\\"]"
    }
  }'
  
  # Patch user (partial update)
  catocli scim patch_user -p '{
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
  catocli scim create_group -p '{
    "source_id": 1,
    "displayName": "Engineering Team",
    "externalId": "eng-team-001",
    "members": [
      {"value": "usr456"},
      {"value": "usr789"}
    ]
  }'
  
  # Delete operations
  catocli scim delete_user -p '{
    "source_id": 1,
    "user_id": "usr456"
  }'
  
  # Purge users (DESTRUCTIVE - disable then delete)
  catocli scim purge users users_to_delete.csv -v

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
        usage='catocli scim add_members <json_input>',
        description='''Add members to an existing SCIM group.

Required Parameters:
  - group_id: SCIM group ID to add members to
  - members: Array of member objects with "value" field containing user IDs

Examples:
  # Add single member to group
  catocli scim add_members '{ "group_id": "grp123", "members": [{ "value": "usr456" }] }'
  
  # Add multiple members with pretty print
  catocli scim add_members -p '{
    "group_id": "grp123",
    "members": [
      { "value": "usr456" },
      { "value": "usr789" },
      { "value": "usr321" }
    ]
  }'
  
  # With verbose output
  catocli scim add_members -v '{ "group_id": "grp123", "members": [{ "value": "usr456" }] }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    add_members_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id and members (e.g., \'{"group_id": "group123", "members": [{"value": "user_id_1"}, {"value": "user_id_2"}]}\')') 
    add_members_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    add_members_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    add_members_parser.set_defaults(func=scim_add_members)
    
    # Create Group command
    create_group_parser = scim_subparsers.add_parser(
        'create_group',
        help='Create a new SCIM group',
        usage='catocli scim create_group <json_input>',
        description='''Create a new SCIM group with optional members.

Required Parameters:
  - displayName (or display_name): Group display name
  - externalId (or external_id): External identifier for the group

Optional Parameters:
  - members: Array of member objects with "value" field containing user IDs

Examples:
  # Basic group creation
  catocli scim create_group '{ "displayName": "Engineering Team", "externalId": "eng-001" }'
  
  # Create group with members using pretty print
  catocli scim create_group -p '{
    "displayName": "Development Team",
    "externalId": "dev-team-001",
    "members": [
      { "value": "usr456" },
      { "value": "usr789" }
    ]
  }'
  
  # Alternative field names
  catocli scim create_group '{ "display_name": "Marketing", "external_id": "mkt-001" }'
  
  # With verbose output
  catocli scim create_group -v -p '{
    "displayName": "QA Team", 
    "externalId": "qa-001"
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    create_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group details (e.g., \'{"display_name": "Team Name", "external_id": "team123", "members": [{"value": "user_id_1"}]}\')') 
    create_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    create_group_parser.set_defaults(func=scim_create_group)
    
    # Create User command
    create_user_parser = scim_subparsers.add_parser(
        'create_user',
        help='Create a new SCIM user',
        usage='catocli scim create_user <json_input>',
        description='''Create a SCIM user with the supported parameters.

Required Parameters:
  - source_id: SCIM source identifier
  - userName: Primary username/email address
  - externalId: External identifier
  - name: Name object with givenName and familyName
  - accountID: SCIM account identifier (from ~/.cato config)

Optional Parameters:
  - email: Email address (alternative to userName)
  - given_name/family_name: Alternative to name object
  - external_id: Alternative to externalId
  - password: User password (generated if not provided)
  - active: Boolean active status (default: true)

Examples:
  # Basic user creation with name object
  catocli scim create_user -p '{
    "source_id": 1,
    "userName": "john.doe@company.com",
    "externalId": "emp001",
    "name": {
      "givenName": "John",
      "familyName": "Doe"
    }
  }'
  
  # Alternative format with separate name fields
  catocli scim create_user -p '{
    "source_id": 1,
    "email": "jane.smith@company.com",
    "external_id": "emp002",
    "given_name": "Jane",
    "family_name": "Smith",
    "active": true
  }'
  
  # Multiline JSON with pretty print
  catocli scim create_user -p '{
    "source_id": 1,
    "userName": "john.doe@company.com",
    "externalId": "emp001",
    "name": {
      "givenName": "John",
      "familyName": "Doe"
    },
    "active": true
  }'
  
  # With password specified
  catocli scim create_user -p '{
    "source_id": 1,
    "userName": "test@company.com",
    "externalId": "test001",
    "given_name": "Test",
    "family_name": "User",
    "password": "SecurePass123!",
    "active": false
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    create_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with user data including source_id, userName, externalId, and name fields')
    create_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    create_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
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
    import_users_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    import_users_subparser.set_defaults(func=scim_import_users)
    
    # Add groups import functionality
    import_groups_subparser = import_subparsers.add_parser(
        'groups',
        help='Import groups from CSV or JSON file',
        usage='catocli scim import groups <file_path> [options]',
        description='''Import SCIM groups from CSV or JSON files with smart create/update detection and processed file output.

=== SMART CREATE/UPDATE DETECTION ===
The import automatically detects whether to create or update groups based on the group_id column:
- If group_id is empty or missing: CREATE new group
- If group_id is present: UPDATE existing group

=== PROCESSED FILE OUTPUT ===
Use --write-processed-file to generate an updated file with all group_ids populated:
- New groups will have their generated group_ids filled in
- Existing groups will retain their original group_ids
- Output format: original_name_processed_YYYYMMDD_HHMMSS.ext
- All other data (display_name, external_id, member_external_ids) preserved exactly as in original file

=== CSV FORMAT ===
Required columns: display_name, external_id
Optional columns: group_id, member_external_ids (pipe-separated list of user external_ids)

=== EXAMPLES ===
  # Basic import (creates new groups)
  catocli scim import groups groups.csv

  # Import with processed file output
  catocli scim import groups groups.csv --write-processed-file -v

  # Import existing groups (CSV with group_id column populated)
  catocli scim import groups existing_groups.csv --write-processed-file

  # Mixed create/update (some rows have group_id, others don't)
  catocli scim import groups mixed_groups.csv --write-processed-file -v

  # JSON import with verbose output
  catocli scim import groups groups.json -v

  # Specify format explicitly
  catocli scim import groups data.txt -f csv --write-processed-file
  catocli scim import groups data.txt -f csv -wp

=== WORKFLOW EXAMPLE ===
1. Export groups to get current data with group_ids:
   catocli scim export groups -f csv --csv-filename current_groups.csv

2. Edit the CSV file (add, modify, or remove groups)

3. Re-import with processed output:
   catocli scim import groups current_groups.csv --write-processed-file
   catocli scim import groups current_groups.csv -wp

4. Use the processed file for future imports:
   catocli scim import groups current_groups_processed_20231201_143022.csv''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    import_groups_subparser.add_argument('file_path', help='Path to CSV or JSON file containing group data')
    import_groups_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    import_groups_subparser.add_argument('-wp', '--write-processed-file', dest='write_processed', action='store_true', help='Write processed file with all group_ids populated (format: original_name_processed_timestamp.ext)')
    import_groups_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    import_groups_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
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
        usage='catocli scim disable_group <json_input>',
        description='''Disable (delete) a SCIM group by ID.

Required Parameters:
  - group_id: SCIM group ID to disable

Examples:
  # Disable a group
  catocli scim disable_group '{ "group_id": "grp123" }'
  
  # With pretty print and verbose output
  catocli scim disable_group -p -v '{
    "group_id": "grp456"
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    disable_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id (e.g., \'{"group_id": "group123"}\')') 
    disable_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    disable_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    disable_group_parser.set_defaults(func=scim_disable_group)
    
    # Disable User command
    disable_user_parser = scim_subparsers.add_parser(
        'disable_user',
        help='Disable a SCIM user',
        usage='catocli scim disable_user <json_input>',
        description='''Disable (delete) a SCIM user by ID.

Required Parameters:
  - user_id: SCIM user ID to disable

Examples:
  # Disable a user
  catocli scim disable_user '{ "user_id": "usr123" }'
  
  # With pretty print and verbose output
  catocli scim disable_user -p -v '{
    "user_id": "usr456"
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    disable_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with user_id (e.g., \'{"user_id": "user123"}\')') 
    disable_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    disable_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    disable_user_parser.set_defaults(func=scim_disable_user)
    
    # Find Group command
    find_group_parser = scim_subparsers.add_parser(
        'find_group',
        help='Find SCIM groups by display name',
        usage='catocli scim find_group <json_input>',
        description='''Find SCIM groups by their display name.

Required Parameters:
  - display_name: Group display name to search for

Examples:
  # Find groups by exact display name
  catocli scim find_group '{ "display_name": "Engineering Team" }'
  
  # Multiline JSON with pretty print
  catocli scim find_group -p '{
    "display_name": "Development Team"
  }'
  
  # With verbose output
  catocli scim find_group -v '{ "display_name": "Marketing" }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    find_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with display_name (e.g., \'{"display_name": "Development Team"}\')') 
    find_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    find_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    find_group_parser.set_defaults(func=scim_find_group)
    
    # Find Users command
    find_users_parser = scim_subparsers.add_parser(
        'find_users',
        help='Find SCIM users by field and value',
        usage='catocli scim find_users <json_input>',
        description='''Find SCIM users by searching specific fields.

Required Parameters:
  - field: Field to search (userName, email, givenName, familyName, externalId)
  - value: Value to search for

Supported Fields:
  - userName: Search by username
  - email: Search by email address  
  - givenName: Search by first name
  - familyName: Search by last name
  - externalId: Search by external ID

Examples:
  # Find user by email
  catocli scim find_users '{ "field": "email", "value": "user@company.com" }'
  
  # Find user by username with pretty print
  catocli scim find_users -p '{
    "field": "userName",
    "value": "john.doe@company.com"
  }'
  
  # Find users by external ID
  catocli scim find_users '{ "field": "externalId", "value": "emp001" }'
  
  # Find users by last name with verbose output
  catocli scim find_users -v -p '{
    "field": "familyName",
    "value": "Smith"
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    find_users_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with field and value (e.g., \'{"field": "email", "value": "user@company.com"}\')') 
    find_users_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    find_users_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    find_users_parser.set_defaults(func=scim_find_users)
    
    # Get Group command
    get_group_parser = scim_subparsers.add_parser(
        'get_group',
        help='Get a specific SCIM group by ID',
        usage='catocli scim get_group <json_input>',
        description='''Retrieve a specific SCIM group by its ID.

Required Parameters:
  - group_id: SCIM group ID to retrieve

Examples:
  # Get group details
  catocli scim get_group '{ "group_id": "grp123" }'
  
  # With pretty print and verbose output
  catocli scim get_group -v '{
    "group_id": "grp456"
  }' -p  ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    get_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id (e.g., \'{"group_id": "group123"}\')') 
    get_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    get_group_parser.set_defaults(func=scim_get_group)
    
    # Get Groups command
    get_groups_parser = scim_subparsers.add_parser(
        'get_groups',
        help='Get all SCIM groups',
        usage='catocli scim get_groups',
        description='''Retrieve all SCIM groups in the system.

No parameters required - this command fetches all groups.

Examples:
  # Get all groups
  catocli scim get_groups
  
  # With pretty print output
  catocli scim get_groups -p
  
  # With verbose and pretty output
  catocli scim get_groups -p -v ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    get_groups_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_groups_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
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
  catocli scim get_user -p '{
    "source_id": 1,
    "user_id": "usr456"
  }'
  
  # Exclude sensitive attributes
  catocli scim get_user -p '{
    "source_id": 1,
    "user_id": "usr456",
    "excluded_attributes": "password,secret"
  }'
''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    get_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with account_id, source_id, user_id, and optional excluded_attributes') 
    get_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    get_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
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
    get_users_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    get_users_parser.set_defaults(func=scim_get_users)
    
    # Remove Members command
    remove_members_parser = scim_subparsers.add_parser(
        'remove_members',
        help='Remove members from a SCIM group',
        usage='catocli scim remove_members <json_input>',
        description='''Remove members from an existing SCIM group.

Required Parameters:
  - group_id: SCIM group ID to remove members from
  - members: Array of member objects with "value" field containing user IDs

Examples:
  # Remove single member from group
  catocli scim remove_members '{ "group_id": "grp123", "members": [{ "value": "usr456" }] }'
  
  # Remove multiple members with pretty print
  catocli scim remove_members -p '{
    "group_id": "grp123",
    "members": [
      { "value": "usr456" },
      { "value": "usr789" }
    ]
  }'
  
  # With verbose output
  catocli scim remove_members -v '{ "group_id": "grp123", "members": [{ "value": "usr456" }] }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    remove_members_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id and members (e.g., \'{"group_id": "group123", "members": [{"value": "user_id_1"}, {"value": "user_id_2"}]}\')') 
    remove_members_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    remove_members_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    remove_members_parser.set_defaults(func=scim_remove_members)
    
    # Rename Group command
    rename_group_parser = scim_subparsers.add_parser(
        'rename_group',
        help='Rename a SCIM group',
        usage='catocli scim rename_group <json_input>',
        description='''Rename an existing SCIM group.

Required Parameters:
  - group_id: SCIM group ID to rename
  - new_name: New display name for the group

Examples:
  # Rename a group
  catocli scim rename_group '{ "group_id": "grp123", "new_name": "Updated Team Name" }'
  
  # With pretty print and verbose output
  catocli scim rename_group -p -v '{
    "group_id": "grp456",
    "new_name": "Engineering Team v2"
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    rename_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id and new_name (e.g., \'{"group_id": "group123", "new_name": "Updated Team Name"}\')') 
    rename_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    rename_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    rename_group_parser.set_defaults(func=scim_rename_group)
    
    # Update Group command
    update_group_parser = scim_subparsers.add_parser(
        'update_group',
        help='Update a SCIM group with complete group data',
        usage='catocli scim update_group <json_input>',
        description='''Update a SCIM group with complete group data (PUT operation).

Required Parameters:
  - group_id: SCIM group ID to update
  - group_data: Complete group data object with SCIM schemas

Examples:
  # Update group with complete data
  catocli scim update_group -p '{
    "group_id": "grp123",
    "group_data": {
      "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
      "displayName": "Updated Team Name",
      "externalId": "team-001",
      "members": [
        { "value": "usr456" },
        { "value": "usr789" }
      ]
    }
  }'
  
  # Basic group update
  catocli scim update_group '{ "group_id": "grp123", "group_data": { "displayName": "New Name" } }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    update_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with group_id and group data (e.g., \'{"group_id": "group123", "group_data": {"schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"], "displayName": "Team"}}\')') 
    update_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    update_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    update_group_parser.set_defaults(func=scim_update_group)
    
    # Update User command
    update_user_parser = scim_subparsers.add_parser(
        'update_user',
        help='Update a SCIM user with complete user data',
        usage='catocli scim update_user <json_input>',
        description='''Update a SCIM user with complete user data (PUT operation).

Required Parameters:
  - user_id (or id): SCIM user ID to update
  - account_id: SCIM account identifier
  - source_id: SCIM source identifier
  - user_data: Complete user data object with SCIM schemas

Examples:
  # Update user with complete data
  catocli scim update_user -p '{
    "user_id": "usr123",
    "account_id": "acc456",
    "source_id": 1,
    "user_data": {
      "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
      "userName": "updated.user@company.com",
      "name": {
        "givenName": "Updated",
        "familyName": "User"
      },
      "active": true
    }
  }'
  
  # Basic user update
  catocli scim update_user '{ "user_id": "usr123", "account_id": "acc456", "source_id": 1, "user_data": { "active": false } }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    update_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with user_id and user data (e.g., \'{"user_id": "user123", "user_data": {"schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"], "userName": "user@company.com"}}\')') 
    update_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    update_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
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
  catocli scim patch_user -p '{
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
  catocli scim patch_user -p '{
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
    patch_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with patch operations for the user')
    patch_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    patch_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    patch_user_parser.set_defaults(func=scim_patch_user)
    
    # Delete User command
    delete_user_parser = scim_subparsers.add_parser(
        'delete_user',
        help='Delete a SCIM user (DELETE operation)',
        usage='catocli scim delete_user <json_input>',
        description='''Permanently delete a SCIM user (DELETE operation).

Required Parameters:
  - user_id (or id): SCIM user ID to delete
  - account_id: SCIM account identifier
  - source_id: SCIM source identifier

Examples:
  # Delete a user
  catocli scim delete_user '{ "user_id": "usr123", "account_id": "acc456", "source_id": 1 }'
  
  # With pretty print and verbose output
  catocli scim delete_user -p -v '{
    "user_id": "usr456",
    "account_id": "acc789",
    "source_id": 1
  }'
  
  # Using alternative ID field name
  catocli scim delete_user '{ "id": "usr123", "account_id": "acc456", "source_id": 1 }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    delete_user_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with account_id, source_id, and user_id (e.g., \'{"account_id": "acc123", "source_id": 1, "user_id": "usr456"}\')') 
    delete_user_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    delete_user_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    delete_user_parser.set_defaults(func=scim_delete_user)
    
    # Patch Group command
    patch_group_parser = scim_subparsers.add_parser(
        'patch_group',
        help='Patch a SCIM group with partial updates (PATCH operation)',
        usage='catocli scim patch_group <json_input>',
        description='''Perform partial updates on a SCIM group using PATCH operations.

Required Parameters:
  - group_id (or id): SCIM group ID to patch
  - account_id: SCIM account identifier
  - source_id: SCIM source identifier
  - Operations: Array of patch operations

Supported Operations:
  - "add": Add new attribute/value
  - "remove": Remove attribute/value
  - "replace": Replace attribute value

Examples:
  # Update group display name
  catocli scim patch_group -p '{
    "group_id": "grp123",
    "account_id": "acc456",
    "source_id": 1,
    "Operations": [
      {
        "op": "replace",
        "path": "displayName",
        "value": "Updated Team Name"
      }
    ]
  }'
  
  # Add and remove members
  catocli scim patch_group -p '{
    "group_id": "grp123",
    "account_id": "acc456",
    "source_id": 1,
    "Operations": [
      {
        "op": "add",
        "path": "members",
        "value": [{ "value": "usr789" }]
      },
      {
        "op": "remove",
        "path": "members[value eq \\"usr456\\"]"
      }
    ]
  }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    patch_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with patch operations for the group (e.g., \'{"account_id": "acc123", "source_id": 1, "group_id": "grp456", "Operations": [{"op": "replace", "path": "displayName", "value": "New Name"}]}\')') 
    patch_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    patch_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    patch_group_parser.set_defaults(func=scim_patch_group)
    
    # Delete Group command
    delete_group_parser = scim_subparsers.add_parser(
        'delete_group',
        help='Delete a SCIM group (DELETE operation)',
        usage='catocli scim delete_group <json_input>',
        description='''Permanently delete a SCIM group (DELETE operation).

Required Parameters:
  - group_id (or id): SCIM group ID to delete
  - account_id: SCIM account identifier
  - source_id: SCIM source identifier

Examples:
  # Delete a group
  catocli scim delete_group '{ "group_id": "grp123", "account_id": "acc456", "source_id": 1 }'
  
  # With pretty print and verbose output
  catocli scim delete_group -p -v '{
    "group_id": "grp456",
    "account_id": "acc789",
    "source_id": 1
  }'
  
  # Using alternative ID field name
  catocli scim delete_group '{ "id": "grp123", "account_id": "acc456", "source_id": 1 }' ''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    delete_group_parser.add_argument('json_input', nargs='?', default='{}', help='JSON input with account_id, source_id, and group_id (e.g., \'{"account_id": "acc123", "source_id": 1, "group_id": "grp456"}\')') 
    delete_group_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    delete_group_parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    delete_group_parser.set_defaults(func=scim_delete_group)
    
    # Purge Users command
    purge_users_parser = scim_subparsers.add_parser(
        'purge',
        help='Purge SCIM users (disable then delete) from CSV or JSON files',
        usage='catocli scim purge users <file_path> [options]'
    )
    purge_subparsers = purge_users_parser.add_subparsers(
        description='Purge operations for users',
        help='Purge command operations'
    )
    
    purge_users_subparser = purge_subparsers.add_parser(
        'users',
        help='Purge users by first disabling then deleting them',
        usage='catocli scim purge users <file_path> [options]',
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
- SCIM credentials must be configured in your profile with valid URL and token

=== CONFIRMATION ===
By default, the command requires typing 'PURGE' to confirm the operation.
Use --force to skip confirmation (use with extreme caution!).

=== FILE COMPATIBILITY ===
Supports the same CSV/JSON files used by import/export commands:
- CSV: Must have user_id column (other columns ignored)
- JSON: Must have user_id field in each user object

=== EXAMPLES ===
  # Basic purge with confirmation
  catocli scim purge users users_processed.csv
  
  # Purge with verbose output
  catocli scim purge users users_to_delete.csv -v
  
  # Force purge without confirmation (DANGEROUS!)
  catocli scim purge users old_users.json --force
  
  # Purge with explicit format
  catocli scim purge users data.txt -f csv -v

=== WORKFLOW EXAMPLE ===
1. Export current users:
   catocli scim export users -f csv --csv-filename all_users.csv
   
2. Filter users to delete (keep only users you want to purge):
   # Edit all_users.csv to contain only users to be purged
   
3. Purge the filtered users:
   catocli scim purge users users_to_purge.csv -v

=== SAFETY NOTES ===
- Always backup your user data before purging
- Test with a small subset first
- Use --verbose to monitor progress
- The operation CANNOT be undone
- Users will be completely removed from the SCIM system''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    purge_users_subparser.add_argument('file_path', help='Path to CSV or JSON file containing user_ids to purge')
    purge_users_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    purge_users_subparser.add_argument('--force', action='store_true', help='Skip confirmation prompt (DANGEROUS - use with extreme caution)')
    purge_users_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output with detailed progress')
    purge_users_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    purge_users_subparser.set_defaults(func=scim_purge_users)
    
    # Purge Groups subcommand
    purge_groups_subparser = purge_subparsers.add_parser(
        'groups',
        help='Purge groups by deleting them',
        usage='catocli scim purge groups <file_path> [options]',
        description='''Purge SCIM groups by deleting them (DESTRUCTIVE OPERATION).

=== WARNING: DESTRUCTIVE OPERATION ===
This command will PERMANENTLY DELETE groups from your SCIM system!
The operation will DELETE all groups from the system.

=== REQUIREMENTS ===
- File must contain group_id column/field with valid group IDs
- All groups with valid group_ids will be processed
- Empty group_id entries are skipped
- SCIM credentials must be configured in your profile with valid URL and token

=== CONFIRMATION ===
By default, the command requires typing 'PURGE' to confirm the operation.
Use --force to skip confirmation (use with extreme caution!).

=== FILE COMPATIBILITY ===
Supports the same CSV/JSON files used by import/export commands:
- CSV: Must have group_id column (other columns ignored)
- JSON: Must have group_id field in each group object

=== EXAMPLES ===
  # Basic purge with confirmation
  catocli scim purge groups groups_processed.csv
  
  # Purge with verbose output
  catocli scim purge groups groups_to_delete.csv -v
  
  # Force purge without confirmation (DANGEROUS!)
  catocli scim purge groups old_groups.json --force
  
  # Purge with explicit format
  catocli scim purge groups data.txt -f csv -v

=== WORKFLOW EXAMPLE ===
1. Export current groups:
   catocli scim export groups -f csv --csv-filename all_groups.csv
   
2. Filter groups to delete (keep only groups you want to purge):
   # Edit all_groups.csv to contain only groups to be purged
   
3. Purge the filtered groups:
   catocli scim purge groups groups_to_purge.csv -v

=== SAFETY NOTES ===
- Always backup your group data before purging
- Test with a small subset first
- Use --verbose to monitor progress
- The operation CANNOT be undone
- Groups will be completely removed from the SCIM system''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    purge_groups_subparser.add_argument('file_path', help='Path to CSV or JSON file containing group_ids to purge')
    purge_groups_subparser.add_argument('-f', '--format', choices=['csv', 'json'], help='File format (auto-detected if not specified)')
    purge_groups_subparser.add_argument('--force', action='store_true', help='Skip confirmation prompt (DANGEROUS - use with extreme caution)')
    purge_groups_subparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output with detailed progress')
    purge_groups_subparser.add_argument('-p', '--pretty', action='store_true', help='Pretty print output')
    purge_groups_subparser.set_defaults(func=scim_purge_groups)
    
    return scim_parser
