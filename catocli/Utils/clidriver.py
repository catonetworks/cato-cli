
import os
import argparse
import json
import catocli
from graphql_client import Configuration
from graphql_client.api_client import ApiException
from ..parsers.customParserApiClient import get_help
from .profile_manager import get_profile_manager
from .version_checker import check_for_updates, force_check_updates
import traceback
import sys
sys.path.insert(0, 'vendor')
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Initialize profile manager
profile_manager = get_profile_manager()
CATO_DEBUG = bool(os.getenv("CATO_DEBUG", False))
from ..parsers.raw import raw_parse
from ..parsers.custom import custom_parse
from ..parsers.custom_private import private_parse
from ..parsers.query_siteLocation import query_siteLocation_parse
from ..parsers.custom.query_eventsFeed import query_eventsFeed_parse
from ..parsers.query_socketPortMetrics import query_socketPortMetrics_parse
from ..parsers.query_socketPortMetricsTimeSeries import query_socketPortMetricsTimeSeries_parse
from ..parsers.query_accountMetrics import query_accountMetrics_parse
from ..parsers.query_hardwareManagement import query_hardwareManagement_parse
from ..parsers.query_events import query_events_parse
from ..parsers.query_eventsTimeSeries import query_eventsTimeSeries_parse
from ..parsers.query_auditFeed import query_auditFeed_parse
from ..parsers.query_container import query_container_parse
from ..parsers.query_admins import query_admins_parse
from ..parsers.query_entityLookup import query_entityLookup_parse
from ..parsers.query_accountRoles import query_accountRoles_parse
from ..parsers.query_accountBySubdomain import query_accountBySubdomain_parse
from ..parsers.query_subDomains import query_subDomains_parse
from ..parsers.query_appStats import query_appStats_parse
from ..parsers.query_appStatsTimeSeries import query_appStatsTimeSeries_parse
from ..parsers.query_admin import query_admin_parse
from ..parsers.query_servicePrincipalAdmin import query_servicePrincipalAdmin_parse
from ..parsers.query_accountManagement import query_accountManagement_parse
from ..parsers.query_sandbox import query_sandbox_parse
from ..parsers.query_popLocations import query_popLocations_parse
from ..parsers.query_licensing import query_licensing_parse
from ..parsers.query_hardware import query_hardware_parse
from ..parsers.query_enterpriseDirectory import query_enterpriseDirectory_parse
from ..parsers.query_devices import query_devices_parse
from ..parsers.query_accountSnapshot import query_accountSnapshot_parse
from ..parsers.query_catalogs import query_catalogs_parse
from ..parsers.query_xdr import query_xdr_parse
from ..parsers.query_site import query_site_parse
from ..parsers.query_policy import query_policy_parse
from ..parsers.query_groups import query_groups_parse
from ..parsers.mutation_xdr import mutation_xdr_parse
from ..parsers.mutation_site import mutation_site_parse
from ..parsers.mutation_policy import mutation_policy_parse
from ..parsers.mutation_container import mutation_container_parse
from ..parsers.mutation_sites import mutation_sites_parse
from ..parsers.mutation_accountManagement import mutation_accountManagement_parse
from ..parsers.mutation_sandbox import mutation_sandbox_parse
from ..parsers.mutation_licensing import mutation_licensing_parse
from ..parsers.mutation_hardware import mutation_hardware_parse
from ..parsers.mutation_groups import mutation_groups_parse
from ..parsers.mutation_admin import mutation_admin_parse
from ..parsers.mutation_enterpriseDirectory import mutation_enterpriseDirectory_parse

def show_version_info(args, configuration=None):
    print(f"catocli version {catocli.__version__}")
    
    if not args.current_only:
        if args.check_updates:
            # Force check for updates
            is_newer, latest_version, source = force_check_updates()
        else:
            # Regular check (uses cache)
            is_newer, latest_version, source = check_for_updates(show_if_available=False)
        
        if latest_version:
            if is_newer:
                print(f"Latest version: {latest_version} (from {source}) - UPDATE AVAILABLE!")
                print()
                print("To upgrade, run:")
                print("pip install --upgrade catocli")
            else:
                print(f"Latest version: {latest_version} (from {source}) - You are up to date!")
        else:
            print("Unable to check for updates (check your internet connection)")
    return [{"success": True, "current_version": catocli.__version__, "latest_version": latest_version if not args.current_only else None}]
        
def get_configuration(skip_api_key=False):
    configuration = Configuration()
    configuration.verify_ssl = False
    configuration.debug = CATO_DEBUG
    configuration.version = "{}".format(catocli.__version__)
    
    # Try to migrate from environment variables first
    profile_manager.migrate_from_environment()
    
    # Get credentials from profile
    credentials = profile_manager.get_credentials()
    if not credentials:
        print("No Cato CLI profile configured.")
        print("Run 'catocli configure set' to set up your credentials.")
        exit(1)

    if not credentials.get('cato_token') or not credentials.get('account_id'):
        profile_name = profile_manager.get_current_profile()
        print(f"Profile '{profile_name}' is missing required credentials.")
        print(f"Run 'catocli configure set --profile {profile_name}' to update your credentials.")
        exit(1)
    
    # Use standard endpoint from profile for regular API calls
    configuration.host = credentials['endpoint']
        
    # Only set API key if not using custom headers file
    # (Private settings are handled separately in createPrivateRequest)
    if not skip_api_key:
        configuration.api_key["x-api-key"] = credentials['cato_token']
    configuration.accountID = credentials['account_id']
    
    return configuration

defaultReadmeStr = """
The Cato CLI is a command-line interface tool designed to simplify the management and automation of Cato Networks’ configurations and operations. 
It enables users to interact with Cato’s API for tasks such as managing Cato Management Application (CMA) site and account configurations, security policies, retrieving events, etc.


For assistance in generating syntax for the cli to perform various operations, please refer to the Cato API Explorer application.


https://github.com/catonetworks/cato-api-explorer
"""

parser = argparse.ArgumentParser(prog='catocli', usage='%(prog)s <operationType> <operationName> [options]', description=defaultReadmeStr)
parser.add_argument('--version', action='version', version=catocli.__version__)
parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
subparsers = parser.add_subparsers()

# Version command - enhanced with update checking
version_parser = subparsers.add_parser('version', help='Show version information and check for updates')
version_parser.add_argument('--check-updates', action='store_true', help='Force check for updates (ignores cache)')
version_parser.add_argument('--current-only', action='store_true', help='Show only current version')
version_parser.set_defaults(func=show_version_info)

custom_parsers = custom_parse(subparsers)
private_parsers = private_parse(subparsers)
raw_parsers = subparsers.add_parser('raw', help='Raw GraphQL', usage=get_help("raw"))
raw_parser = raw_parse(raw_parsers)
query_parser = subparsers.add_parser('query', help='Query', usage='catocli query <operationName> [options]')
query_subparsers = query_parser.add_subparsers(description='valid subcommands', help='additional help')
query_siteLocation_parser = query_siteLocation_parse(query_subparsers)
query_eventsFeed_parser = query_eventsFeed_parse(query_subparsers)
mutation_parser = subparsers.add_parser('mutation', help='Mutation', usage='catocli mutation <operationName> [options]')
mutation_subparsers = mutation_parser.add_subparsers(description='valid subcommands', help='additional help')

query_socketPortMetrics_parser = query_socketPortMetrics_parse(query_subparsers)
query_socketPortMetricsTimeSeries_parser = query_socketPortMetricsTimeSeries_parse(query_subparsers)
query_accountMetrics_parser = query_accountMetrics_parse(query_subparsers)
query_hardwareManagement_parser = query_hardwareManagement_parse(query_subparsers)
query_events_parser = query_events_parse(query_subparsers)
query_eventsTimeSeries_parser = query_eventsTimeSeries_parse(query_subparsers)
query_auditFeed_parser = query_auditFeed_parse(query_subparsers)
query_container_parser = query_container_parse(query_subparsers)
query_admins_parser = query_admins_parse(query_subparsers)
query_entityLookup_parser = query_entityLookup_parse(query_subparsers)
query_accountRoles_parser = query_accountRoles_parse(query_subparsers)
query_accountBySubdomain_parser = query_accountBySubdomain_parse(query_subparsers)
query_subDomains_parser = query_subDomains_parse(query_subparsers)
query_appStats_parser = query_appStats_parse(query_subparsers)
query_appStatsTimeSeries_parser = query_appStatsTimeSeries_parse(query_subparsers)
query_admin_parser = query_admin_parse(query_subparsers)
query_servicePrincipalAdmin_parser = query_servicePrincipalAdmin_parse(query_subparsers)
query_accountManagement_parser = query_accountManagement_parse(query_subparsers)
query_sandbox_parser = query_sandbox_parse(query_subparsers)
query_popLocations_parser = query_popLocations_parse(query_subparsers)
query_licensing_parser = query_licensing_parse(query_subparsers)
query_hardware_parser = query_hardware_parse(query_subparsers)
query_enterpriseDirectory_parser = query_enterpriseDirectory_parse(query_subparsers)
query_devices_parser = query_devices_parse(query_subparsers)
query_accountSnapshot_parser = query_accountSnapshot_parse(query_subparsers)
query_catalogs_parser = query_catalogs_parse(query_subparsers)
query_xdr_parser = query_xdr_parse(query_subparsers)
query_site_parser = query_site_parse(query_subparsers)
query_policy_parser = query_policy_parse(query_subparsers)
query_groups_parser = query_groups_parse(query_subparsers)
mutation_xdr_parser = mutation_xdr_parse(mutation_subparsers)
mutation_site_parser = mutation_site_parse(mutation_subparsers)
mutation_policy_parser = mutation_policy_parse(mutation_subparsers)
mutation_container_parser = mutation_container_parse(mutation_subparsers)
mutation_sites_parser = mutation_sites_parse(mutation_subparsers)
mutation_accountManagement_parser = mutation_accountManagement_parse(mutation_subparsers)
mutation_sandbox_parser = mutation_sandbox_parse(mutation_subparsers)
mutation_licensing_parser = mutation_licensing_parse(mutation_subparsers)
mutation_hardware_parser = mutation_hardware_parse(mutation_subparsers)
mutation_groups_parser = mutation_groups_parse(mutation_subparsers)
mutation_admin_parser = mutation_admin_parse(mutation_subparsers)
mutation_enterpriseDirectory_parser = mutation_enterpriseDirectory_parse(mutation_subparsers)


def parse_headers(header_strings):
    headers = {}
    if header_strings:
        for header_string in header_strings:
            if ':' not in header_string:
                print(f"ERROR: Invalid header format '{header_string}'. Use 'Key: Value' format.")
                exit(1)
            key, value = header_string.split(':', 1)
            headers[key.strip()] = value.strip()
    return headers

def parse_headers_from_file(file_path):
    headers = {}
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' not in line:
                    print(f"ERROR: Invalid header format in {file_path} at line {line_num}: '{line}'. Use 'Key: Value' format.")
                    exit(1)
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"ERROR: Headers file '{file_path}' not found.")
        exit(1)
    except IOError as e:
        print(f"ERROR: Could not read headers file '{file_path}': {e}")
        exit(1)
    return headers

def main(args=None):
    # Check if no arguments provided or help is requested
    if args is None:
        args = sys.argv[1:]

    # Show version check when displaying help or when no command specified
    if not args or '-h' in args or '--help' in args:
        # Check for updates in background (non-blocking)
        try:
            check_for_updates(show_if_available=True)
        except Exception:
            # Don't let version check interfere with CLI operation
            pass

    args = parser.parse_args(args=args)
    try:
        # Skip authentication for configure commands
        if hasattr(args, 'func') and hasattr(args.func, '__module__') and 'configure' in str(args.func.__module__):
            response = args.func(args, None)
        else:
            # Check if using headers file to determine if we should skip API key
            # Note: Private settings should NOT affect regular API calls - only private commands
            using_headers_file = hasattr(args, 'headers_file') and args.headers_file
            
            # Get configuration from profiles
            configuration = get_configuration(skip_api_key=using_headers_file)
            
            # Parse custom headers if provided
            custom_headers = {}
            if hasattr(args, 'headers') and args.headers:
                custom_headers.update(parse_headers(args.headers))
            if hasattr(args, 'headers_file') and args.headers_file:
                custom_headers.update(parse_headers_from_file(args.headers_file))
            if custom_headers:
                configuration.custom_headers.update(custom_headers)
            # Handle account ID override (applies to all commands except raw)
            if args.func.__name__ not in ["createRawRequest"]:
                if hasattr(args, 'accountID') and args.accountID is not None:
                    # Command line override takes precedence
                    configuration.accountID = args.accountID
                # Otherwise use the account ID from the profile (already set in get_configuration)
            response = args.func(args, configuration)

        if type(response) == ApiException:
            print("ERROR! Status code: {}".format(response.status))
            print(response)
        else:
            if response!=None:
                # Check if this is CSV output
                if (isinstance(response, list) and len(response) > 0 and 
                    isinstance(response[0], dict) and "__csv_output__" in response[0]):
                    # Print CSV output directly without JSON formatting
                    print(response[0]["__csv_output__"], end='')
                else:
                    # Standard JSON output
                    print(json.dumps(response[0], sort_keys=True, indent=4))
    except KeyboardInterrupt:
        print('Operation cancelled by user (Ctrl+C).')
        exit(130)  # Standard exit code for SIGINT
    except Exception as e:
        if isinstance(e, AttributeError):
            print('Missing arguments. Usage: catocli <operation> -h')
            if args.v==True:
                print('ERROR: ',e)
                traceback.print_exc()
        else:
            print('ERROR: ',e)
            traceback.print_exc()
    exit(1)
