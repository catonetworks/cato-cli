import catocli.parsers.custom.export_sites.export_sites as export_sites

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
  catocli export socket_sites -f csv --site-ids "100,200,300" --csv-filename filtered_sites.csv --append-timestamp --output-directory ./exports -clip -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    
    socket_sites_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    socket_sites_parser.add_argument('--site-ids', '-siteIDs', dest='siteIDs', help='Comma-separated list of site IDs to filter and export (e.g., "1234,1235,1236"). If not specified, exports all sites.', required=False)
    socket_sites_parser.add_argument('-clip', '--calculate-local-ip', action='store_true', help='Calculate local IP addresses from subnet ranges (first usable IP)')
    
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
    
    socket_sites_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    socket_sites_parser.set_defaults(func=export_sites.export_socket_sites_dispatcher)
    
    return socket_sites_parser


