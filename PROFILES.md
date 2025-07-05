# Cato CLI Profile Management

The Cato CLI supports AWS CLI-style profile management for storing and managing multiple sets of credentials. This allows you to easily switch between different Cato environments (dev, staging, production) or accounts.

## Quick Start

### 1. Configure your first profile

```bash
# Interactive setup (recommended for first-time users)
catocli configure set

# Non-interactive setup
catocli configure set --cato-token "your-api-token" --account-id "12345"
```

### 2. List your profiles

```bash
catocli configure list
```

### 3. Switch profiles

```bash
catocli configure use prod
```

## Commands

### `catocli configure set`

Configure a profile with your Cato credentials.

**Usage:**
```bash
catocli configure set [--profile PROFILE] [options]
```

**Options:**
- `--profile PROFILE` - Profile name to configure (default: default)
- `--endpoint URL` - Cato API endpoint URL (default: https://api.catonetworks.com/api/v1/graphql2)
- `--cato-token TOKEN` - Your Cato API token
- `--account-id ID` - Your Cato account ID
- `--interactive` - Force interactive mode

**Examples:**
```bash
# Configure default profile interactively
catocli configure set

# Configure a specific profile
catocli configure set --profile prod --cato-token "your-token" --account-id "12345"

# Configure with custom endpoint
catocli configure set --profile dev --endpoint "https://dev-api.catonetworks.com/api/v1/graphql2"
```

### `catocli configure list`

List all configured profiles.

**Usage:**
```bash
catocli configure list
```

**Example output:**
```
Available profiles:

  default (current)
    Endpoint:   https://api.catonetworks.com/api/v1/graphql2
    Account ID: 12345

  prod
    Endpoint:   https://api.catonetworks.com/api/v1/graphql2
    Account ID: 67890

  dev
    Endpoint:   https://dev-api.catonetworks.com/api/v1/graphql2
    Account ID: 11111
```

### `catocli configure use`

Set the active profile.

**Usage:**
```bash
catocli configure use <profile>
```

**Example:**
```bash
catocli configure use prod
```

### `catocli configure show`

Show current profile configuration.

**Usage:**
```bash
catocli configure show [--profile PROFILE]
```

**Examples:**
```bash
# Show current active profile
catocli configure show

# Show specific profile
catocli configure show --profile prod
```

### `catocli configure delete`

Delete a profile.

**Usage:**
```bash
catocli configure delete <profile> [--force]
```

**Examples:**
```bash
# Delete with confirmation
catocli configure delete old-profile

# Force delete without confirmation
catocli configure delete old-profile --force
```

## Profile Storage

Profiles are stored in `~/.cato/credentials` in INI format:

```ini
[default]
endpoint = https://api.catonetworks.com/api/v1/graphql2
cato_token = your-api-token
account_id = 12345

[prod]
endpoint = https://api.catonetworks.com/api/v1/graphql2
cato_token = prod-api-token
account_id = 67890

[dev]
endpoint = https://dev-api.catonetworks.com/api/v1/graphql2
cato_token = dev-api-token
account_id = 11111
```

The current active profile is stored in `~/.cato/config`.

## Environment Variables

You can override the active profile using the `CATO_PROFILE` environment variable:

```bash
export CATO_PROFILE=prod
catocli query site list
```

## Migration from Environment Variables

If you have existing `CATO_TOKEN` and `CATO_ACCOUNT_ID` environment variables, the CLI will automatically create a default profile on first run. You can then configure additional profiles as needed.

## Security

- Credential files are stored with restrictive permissions (600) to protect your API tokens
- Tokens are never displayed in full - only the last 4 characters are shown for identification
- The CLI validates that profiles have all required credentials before use

## Troubleshooting

### "No Cato CLI profile configured"

You need to set up your first profile:
```bash
catocli configure set
```

### "Profile 'xyz' is missing required credentials"

Update the profile with missing credentials:
```bash
catocli configure set --profile xyz
```

### "Profile 'xyz' does not exist"

List available profiles and use a valid one:
```bash
catocli configure list
catocli configure use <valid-profile>
```

## Command Line Account ID Override

You can still override the account ID from the profile using the `-accountID` parameter:

```bash
catocli query site list -accountID 99999
```

This allows you to use a profile's token and endpoint while querying a different account.
