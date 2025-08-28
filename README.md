# Cato Networks GraphQL API CLI

The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API](https://api.catonetworks.com/api/v1/graphql2) easily integrating into configurations management, orchestration or automation frameworks to support the DevOps model.

## Installation
    pip3 install catocli

## Authentication

The Cato CLI uses a profile-based authentication system similar to AWS CLI. You can configure multiple profiles for different environments or accounts.

### Quick Setup

```bash
# Configure your first profile (interactive)
catocli configure set

# Or configure non-interactively
catocli configure set --cato-token "your-api-token" --account-id "12345"
```

### Profile Management

```bash
# List profiles
catocli configure list

# Switch profiles
catocli configure use prod

# Show current profile
catocli configure show
```

### Legacy Environment Variables (deprecated)

For backward compatibility, you can still use environment variables:

```bash
export CATO_TOKEN="12345-abcde-12345-abcde"
export CATO_ACCOUNT_ID="12345"
export CATO_DEBUG=True  # Optional for debug logs
```

The CLI will automatically migrate these to a default profile on first run.

### Documentation

For detailed information about profile management, see [PROFILES.md](PROFILES.md).

[CLICK HERE](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API) to see how create an API key to authenticate.

## Running the CLI
	catocli -h
	catocli query -h
	catocli query entityLookup -h
	catocli query entityLookup '{"type":"country"}`
    
    // Override the accountID value as a cli argument
	catocli query entityLookup -accountID=12345 '{"type":"country"}`

## Check out run locally not as pip package
	git clone git@github.com:Cato-Networks/cato-cli.git
	cd cato-cli
	python3 -m catocli -h

This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8
## Requirements:
    python 3.6 or higher
    
## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## Usage:
    usage: catocli <resource> <command> [options]

    CLI for query, and mutation operations via API.

    Positional arguments:
      {entityLookup}
		entityLookup         entityLookup reference.

    Optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

## Installing the correct version for environment:
https://www.python.org/downloads/

