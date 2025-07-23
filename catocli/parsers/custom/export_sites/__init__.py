import catocli.parsers.custom.export_sites.export_sites as export_sites

def export_sites_parse(subparsers):
    """Create export_sites command parsers"""
    
    # Create the socket_sites parser (direct command, no subparsers)
    socket_sites_parser = subparsers.add_parser(
        'socket_sites', 
        help='Export consolidated site and socket data to JSON format',
        usage='catocli export socket_sites [-accountID <account_id>] [options]'
    )
    
    socket_sites_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    socket_sites_parser.add_argument('-siteIDs', help='Comma-separated list of site IDs to export (e.g., "132606,132964,133511")', required=False)
    socket_sites_parser.add_argument('--output-file-path', help='Full path including filename and extension for output file. If not specified, uses default: config_data/socket_site_data_{account_id}.json')
    socket_sites_parser.add_argument('--append-timestamp', action='store_true', help='Append timestamp to the filename after account ID (format: YYYY-MM-DD_HH-MM-SS)')
    socket_sites_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    socket_sites_parser.set_defaults(func=export_sites.export_socket_site_to_json)
    
    return socket_sites_parser
