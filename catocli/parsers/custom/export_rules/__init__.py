import catocli.parsers.custom.export_rules.export_rules as export_rules

def export_rules_parse(subparsers):
    """Create export command parsers"""
    
    # Create the main export parser
    export_parser = subparsers.add_parser('export', help='Export data to various formats', usage='catocli export <operation> [options]')
    export_subparsers = export_parser.add_subparsers(description='valid export operations', help='additional help')
    
    # Add sites export functionality
    from catocli.parsers.custom.export_sites import export_sites_parse
    export_sites_parse(export_subparsers)
    
    # Add if_rules command
    if_rules_parser = export_subparsers.add_parser(
        'if_rules', 
        help='Export Internet Firewall rules to JSON format',
        usage='catocli export if_rules [-accountID <account_id>] [options]'
    )
    
    if_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    if_rules_parser.add_argument('--output-file-path', help='Full path including filename and extension for output file. If not specified, uses default: config_data/all_ifw_rules_and_sections_{account_id}.json')
    if_rules_parser.add_argument('--append-timestamp', action='store_true', help='Append timestamp to the filename after account ID (format: YYYY-MM-DD_HH-MM-SS)')
    if_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    if_rules_parser.set_defaults(func=export_rules.export_if_rules_to_json)
    
    # Add wf_rules command
    wf_rules_parser = export_subparsers.add_parser(
        'wf_rules', 
        help='Export WAN Firewall rules to JSON format',
        usage='catocli export wf_rules [-accountID <account_id>] [options]'
    )
    
    wf_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    wf_rules_parser.add_argument('--output-file-path', help='Full path including filename and extension for output file. If not specified, uses default: config_data/all_wf_rules_and_sections_{account_id}.json')
    wf_rules_parser.add_argument('--append-timestamp', action='store_true', help='Append timestamp to the filename after account ID (format: YYYY-MM-DD_HH-MM-SS)')
    wf_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    wf_rules_parser.set_defaults(func=export_rules.export_wf_rules_to_json)
    
    return export_parser
