import catocli.parsers.custom.export_sites.export_sites as export_sites
from ...utils.export_utils import add_name_filter_arguments

def export_sites_parse(subparsers):
    """Create export_sites command parsers"""
    
    # Create the socket_sites parser (direct command, no subparsers)
    socket_sites_parser = subparsers.add_parser(
        'socket_sites', 
        help='Export consolidated site and socket data to JSON or CSV format',
        usage='catocli export socket_sites [-accountID <account_id>] [options]',
        description='''Export consolidated site and socket data to JSON or CSV format with flexible filename and filtering options.

Examples:
  # Basic export to JSON (default format)
  catocli export socket_sites
  
  # Export to CSV with custom filename and timestamp
  catocli export socket_sites -f csv --csv-filename sites_export.csv --append-timestamp
  
  # Export specific sites with local IP calculation
  catocli export socket_sites --site-ids "1234,1235,1236" -clip -v
  
  # Generate template files
  catocli export socket_sites -gt -f json
  catocli export socket_sites -gt -f csv --append-timestamp
  
  # Export with custom output directory and account ID
  catocli export socket_sites -accountID 12345 --output-directory /path/to/exports
  
  # Export to JSON with custom filename and verbose output
  catocli export socket_sites -f json --json-filename my_sites.json -v
  
  # Export filtered sites to CSV with all options
  catocli export socket_sites -f csv --site-ids "100,200,300" --csv-filename filtered_sites.csv --append-timestamp --output-directory ./exports -clip -v

  # Export only specific named sites (escape a literal comma in a name with \\,)
  catocli export socket_sites --names "NA-US-RIC-BR,Finance\\, HR Branch"

  # Pull 2 named sites from a second tenant and merge them into this repo's socket_sites.json (JSON only)
  CATO_PROFILE=tenantB catocli export socket_sites --names "Site A,Site B" --merge-into ../config_data/socket_sites.json

  # Produce a tenant-portable export (ids stripped) for migrating sites into a different tenant
  catocli export socket_sites --strip-ids''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    socket_sites_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    socket_sites_parser.add_argument('--site-ids', '-siteIDs', dest='siteIDs', help='Comma-separated list of site IDs to filter and export (e.g., "1234,1235,1236"). If not specified, exports all sites.', required=False)

    # Format selection
    socket_sites_parser.add_argument('-f', '--format', dest='export_format', choices=['json', 'csv'], default='json',
                                    help='Export format: json (default) or csv')

    # Template generation option
    socket_sites_parser.add_argument('--generate-template', '-gt', dest='generate_template', action='store_true',
                                    help='Generate template files instead of exporting data (use -f to specify format: csv or json)')

    # Filename arguments (updated for both formats)
    socket_sites_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: socket_sites_{account_id}.json)')
    socket_sites_parser.add_argument('--csv-filename', dest='csv_filename', help='Override CSV file name (default: socket_sites_{account_id}.csv)')
    socket_sites_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    socket_sites_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')

    add_name_filter_arguments(
        socket_sites_parser,
        names_help=(
            'Comma-separated list of exact site names to export, instead of exporting every '
            'site. --merge-into is only supported with the default JSON format (-f json) - '
            'it upserts into a {"sites": [...]} JSON file, which has no CSV equivalent.'
        ),
    )

    socket_sites_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    socket_sites_parser.add_argument(
        '--strip-ids', dest='strip_ids', action='store_true',
        help=(
            'Make the JSON output tenant-portable by stripping source-tenant-specific ids '
            '(-f json only; ignored with -f csv): each site\'s own id, license_id/license_bw '
            '(a license must be re-assigned per site in the target tenant), '
            'wan_interfaces[].id, lan_interfaces[].id, network_ranges[].id, the native '
            'range\'s id (the "range_id" field), and wifi_ssids[].id. Does NOT strip Wi-Fi '
            'PSKs (the API never returns them on export, stripped or not - supply them '
            'separately in the target tenant) or anything else. Off by default.'
        ),
    )

    socket_sites_parser.set_defaults(func=export_sites.export_socket_sites_dispatcher)
    
    return socket_sites_parser


