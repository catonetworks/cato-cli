import catocli.parsers.custom.export_rules.export_rules as export_rules

def export_rules_parse(subparsers):
    """Create export command parsers"""
    
    # Create the main export parser
    export_parser = subparsers.add_parser(
        'export', 
        help='Export data to various formats', 
        usage='catocli export <operation> [options]',
        description='''Export various types of data from Cato Networks to JSON or CSV formats for backup, analysis, or migration.

Common Examples:
  # Export site and socket data
  catocli export socket_sites
  catocli export socket_sites -f csv --append-timestamp
  
  # Export firewall rules
  catocli export if_rules -v
  catocli export wf_rules -accountID 12345
  
  # Export with filtering and custom output
  catocli export socket_sites --site-ids "100,200,300" --output-directory ./backups
  
  # Generate templates for import operations
  catocli export socket_sites -gt -f csv''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    export_subparsers = export_parser.add_subparsers(description='valid export operations', help='additional help')
    
    # Add sites export functionality
    from catocli.parsers.custom.export_sites import export_sites_parse
    export_sites_parse(export_subparsers)
    
    # Add if_rules command
    if_rules_parser = export_subparsers.add_parser(
        'if_rules', 
        help='Export Internet Firewall rules to JSON format',
        usage='catocli export if_rules [-accountID <account_id>] [options]',
        description='''Export Internet Firewall rules to JSON format for backup, analysis, or migration purposes.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export if_rules
  
  # Export with specific account ID
  catocli export if_rules -accountID 12345
  
  # Export with custom filename and timestamp
  catocli export if_rules --json-filename my_firewall_rules.json --append-timestamp
  
  # Export to custom directory
  catocli export if_rules --output-directory ./exports
  
  # Export with all options
  catocli export if_rules --json-filename firewall_backup --append-timestamp --output-directory ./backups -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    
    if_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    if_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_ifw_rules_and_sections_{account_id}.json)')
    if_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    if_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    if_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    if_rules_parser.set_defaults(func=export_rules.export_if_rules_to_json)
    
    # Add wf_rules command
    wf_rules_parser = export_subparsers.add_parser(
        'wf_rules', 
        help='Export WAN Firewall rules to JSON format',
        usage='catocli export wf_rules [-accountID <account_id>] [options]',
        description='''Export WAN Firewall rules to JSON format for backup, analysis, or migration purposes.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export wf_rules
  
  # Export with specific account ID
  catocli export wf_rules -accountID 12345
  
  # Export with custom filename and timestamp
  catocli export wf_rules --json-filename wan_firewall_rules.json --append-timestamp
  
  # Export to custom directory
  catocli export wf_rules --output-directory ./exports
  
  # Export with all options
  catocli export wf_rules --json-filename wan_firewall_backup --append-timestamp --output-directory ./backups -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    
    wf_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    wf_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_wf_rules_and_sections_{account_id}.json)')
    wf_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    wf_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    wf_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    wf_rules_parser.set_defaults(func=export_rules.export_wf_rules_to_json)

    # Add tls_rules command
    tls_rules_parser = export_subparsers.add_parser(
        'tls_rules', 
        help='Export TLS Inspection rules to JSON format',
        usage='catocli export tls_rules [-accountID <account_id>] [options]',
        description='''Export TLS Inspection rules to JSON format for backup, analysis, or migration purposes.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export tls_rules
  
  # Export with specific account ID
  catocli export tls_rules -accountID 12345
  
  # Export with custom filename and timestamp
  catocli export tls_rules --json-filename tls_inspection_rules.json --append-timestamp
  
  # Export to custom directory
  catocli export tls_rules --output-directory ./exports
  
  # Export with all options
  catocli export tls_rules --json-filename tls_backup --append-timestamp --output-directory ./backups -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    
    tls_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    tls_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_tls_rules_and_sections_{account_id}.json)')
    tls_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    tls_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    tls_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    tls_rules_parser.set_defaults(func=export_rules.export_tls_rules_to_json)

    # Add wnw_rules command
    wnw_rules_parser = export_subparsers.add_parser(
        'wnw_rules', 
        help='Export WAN Network rules to JSON format',
        usage='catocli export wnw_rules [-accountID <account_id>] [options]',
        description='''Export WAN Network rules to JSON format for backup, analysis, or migration purposes.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export wnw_rules
  
  # Export with specific account ID
  catocli export wnw_rules -accountID 12345
  
  # Export with custom filename and timestamp
  catocli export wnw_rules --json-filename wan_network_rules.json --append-timestamp
  
  # Export to custom directory
  catocli export wnw_rules --output-directory ./exports
  
  # Export with all options
  catocli export wnw_rules --json-filename wan_network_backup --append-timestamp --output-directory ./backups -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    
    wnw_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    wnw_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_wnw_rules_and_sections_{account_id}.json)')
    wnw_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    wnw_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    wnw_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    wnw_rules_parser.set_defaults(func=export_rules.export_wnw_rules_to_json)


    return export_parser
