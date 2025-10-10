# SCIM (System for Cross-domain Identity Management) Commands

The Cato CLI provides comprehensive support for SCIM operations to manage users and groups via the Cato SCIM API. This enables automated user provisioning and group management for identity providers and custom integrations.

## Prerequisites

Before using SCIM commands, you need to configure SCIM credentials in your profile:

1. **SCIM URL**: The SCIM service endpoint provided by Cato
   - Format: `https://scimservice.catonetworks.com:4443/scim/v2/{accountId}/{sourceId}`
   - Example: `https://scimservice.catonetworks.com:4443/scim/v2/12345/67890`

2. **SCIM Bearer Token**: Authentication token for SCIM access
   - Example: `cfda146dc7c12345abcde`

## Configuration

### Add SCIM Credentials to Profile

```bash
# Interactive configuration (recommended)
catocli configure set

# Non-interactive configuration
catocli configure set --scim-url "https://scimservice.catonetworks.com:4443/scim/v2/12345/67890" --scim-token "your-bearer-token"

# Add SCIM credentials to specific profile
catocli configure set --profile production --scim-url "your-scim-url" --scim-token "your-bearer-token"
```

### View Profile with SCIM Credentials

```bash
catocli configure show
```

For detailed setup instructions, see: [Using the Cato SCIM API for Custom SCIM Apps](https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps)

## User Management Commands

### Get All Users

```bash
# Get all SCIM users
catocli scim get_users

# With verbose output
catocli scim get_users --verbose

# With pretty-printed JSON
catocli scim get_users --pretty
```

### Get Specific User

```bash
# Get user by SCIM ID
catocli scim get_user "6283630dfd7ec758a8bf4b61"

# With verbose output
catocli scim get_user "6283630dfd7ec758a8bf4b61" --verbose
```

### Find Users

```bash
# Find users by email
catocli scim find_users email "john.doe@company.com"

# Find users by username
catocli scim find_users userName "john.doe"

# Find users by given name (first name)
catocli scim find_users givenName "John"

# Find users by family name (last name)
catocli scim find_users familyName "Doe"
```

### Create User

```bash
# Create a new user (password will be auto-generated)
catocli scim create_user "jane.doe@company.com" "Jane" "Doe" "external123"

# Create user with specific password
catocli scim create_user "jane.doe@company.com" "Jane" "Doe" "external123" --password "SecurePass123!"

# Create inactive user
catocli scim create_user "jane.doe@company.com" "Jane" "Doe" "external123" --inactive

# Create active user (default behavior)
catocli scim create_user "jane.doe@company.com" "Jane" "Doe" "external123" --active
```

### Update User

```bash
# Update user with complete user data (JSON format)
catocli scim update_user "6283630dfd7ec758a8bf4b61" '{
  "userName": "john.doe@company.com",
  "name": {
    "givenName": "John",
    "familyName": "Doe"
  },
  "emails": [
    {
      "primary": true,
      "value": "john.doe@company.com",
      "type": "work"
    }
  ],
  "active": true
}'
```

### Disable User

```bash
# Disable a user by SCIM ID
catocli scim disable_user "6283630dfd7ec758a8bf4b61"

# With verbose output
catocli scim disable_user "6283630dfd7ec758a8bf4b61" --verbose
```

## Group Management Commands

### Get All Groups

```bash
# Get all SCIM groups
catocli scim get_groups

# With verbose output
catocli scim get_groups --verbose

# With pretty-printed JSON
catocli scim get_groups --pretty
```

### Get Specific Group

```bash
# Get group by SCIM ID
catocli scim get_group "6283630dfd7ec758a8bf4b62"

# With verbose output
catocli scim get_group "6283630dfd7ec758a8bf4b62" --verbose
```

### Find Groups

```bash
# Find groups by display name
catocli scim find_group "Development Team"

# With verbose output
catocli scim find_group "Development Team" --verbose
```

### Create Group

```bash
# Create a new group without members
catocli scim create_group "Marketing Team" "marketing-external-id"

# Create group with initial members
catocli scim create_group "Sales Team" "sales-external-id" '[
  {"value": "6283630dfd7ec758a8bf4b61"},
  {"value": "6283630dfd7ec758a8bf4b62"}
]'
```

### Update Group

```bash
# Update group with complete group data
catocli scim update_group "6283630dfd7ec758a8bf4b62" '{
  "displayName": "Updated Team Name",
  "members": [
    {
      "value": "6283630dfd7ec758a8bf4b61",
      "display": "john.doe@company.com"
    }
  ]
}'
```

### Rename Group

```bash
# Rename a group
catocli scim rename_group "6283630dfd7ec758a8bf4b62" "New Team Name"

# With verbose output
catocli scim rename_group "6283630dfd7ec758a8bf4b62" "New Team Name" --verbose
```

### Disable Group

```bash
# Disable a group by SCIM ID
catocli scim disable_group "6283630dfd7ec758a8bf4b62"

# With verbose output
catocli scim disable_group "6283630dfd7ec758a8bf4b62" --verbose
```

## Group Membership Management

### Add Members to Group

```bash
# Add single member to group
catocli scim add_members "6283630dfd7ec758a8bf4b62" '[{"value": "6283630dfd7ec758a8bf4b61"}]'

# Add multiple members to group
catocli scim add_members "6283630dfd7ec758a8bf4b62" '[
  {"value": "6283630dfd7ec758a8bf4b61"},
  {"value": "6283630dfd7ec758a8bf4b63"},
  {"value": "6283630dfd7ec758a8bf4b64"}
]'

# With verbose output
catocli scim add_members "group-id" '[{"value": "user-id"}]' --verbose
```

### Remove Members from Group

```bash
# Remove single member from group
catocli scim remove_members "6283630dfd7ec758a8bf4b62" '[{"value": "6283630dfd7ec758a8bf4b61"}]'

# Remove multiple members from group
catocli scim remove_members "6283630dfd7ec758a8bf4b62" '[
  {"value": "6283630dfd7ec758a8bf4b61"},
  {"value": "6283630dfd7ec758a8bf4b63"}
]'
```

## Common Options

All SCIM commands support these common options:

- `--verbose` or `-v`: Show detailed output and progress information
- `--pretty` or `-p`: Pretty print JSON output for better readability

## Error Handling

If SCIM credentials are missing or invalid, you'll see helpful error messages:

```bash
$ catocli scim get_users
ERROR: Profile 'default' is missing SCIM credentials: scim_url, scim_token
Run 'catocli configure set --profile default' to add SCIM credentials.
For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps
```

## JSON Format Examples

### User JSON Structure

```json
{
  "id": "6283630dfd7ec758a8bf4b61",
  "userName": "john.doe@company.com",
  "name": {
    "givenName": "John",
    "familyName": "Doe"
  },
  "emails": [
    {
      "primary": true,
      "value": "john.doe@company.com",
      "type": "work"
    }
  ],
  "active": true
}
```

### Group JSON Structure

```json
{
  "id": "6283630dfd7ec758a8bf4b62",
  "displayName": "Development Team",
  "members": [
    {
      "value": "6283630dfd7ec758a8bf4b61",
      "display": "john.doe@company.com"
    }
  ]
}
```

### Member Array Format

```json
[
  {"value": "6283630dfd7ec758a8bf4b61"},
  {"value": "6283630dfd7ec758a8bf4b62"}
]
```

## Integration Examples

### Bulk User Creation from CSV

```bash
#!/bin/bash
# Read CSV file and create users
while IFS=',' read -r email given_name family_name; do
    catocli scim create_user "$email" "$given_name" "$family_name" --verbose
done < users.csv
```

### Group Membership Sync

```bash
#!/bin/bash
# Add users to a group
GROUP_ID="6283630dfd7ec758a8bf4b62"
USER_IDS=("6283630dfd7ec758a8bf4b61" "6283630dfd7ec758a8bf4b63")

# Build members JSON array
MEMBERS_JSON="["
for i in "${!USER_IDS[@]}"; do
    if [ $i -ne 0 ]; then
        MEMBERS_JSON+=","
    fi
    MEMBERS_JSON+="{\"value\": \"${USER_IDS[$i]}\"}"
done
MEMBERS_JSON+="]"

# Add members to group
catocli scim add_members "$GROUP_ID" "$MEMBERS_JSON" --verbose
```

## Support

For SCIM API setup and configuration assistance, refer to:
- [Using the Cato SCIM API for Custom SCIM Apps](https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps)

For CLI-specific issues, use the `--verbose` flag to get detailed error information and check your profile configuration with `catocli configure show`.
