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
    socket_sites_parser.add_argument('--site-ids', '-siteIDs', dest='siteIDs', help='Comma-separated list of site IDs to filter and export (e.g., "1234,1235,1236"). If not specified, exports all sites.', required=False)
    socket_sites_parser.add_argument('-clip', '--calculate-local-ip', action='store_true', help='Calculate local IP addresses from subnet ranges (first usable IP)')
    socket_sites_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: socket_sites_{account_id}.json)')
    socket_sites_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to the JSON file name')
    socket_sites_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    socket_sites_parser.set_defaults(func=export_sites.export_socket_site_to_json)
    
    return socket_sites_parser
