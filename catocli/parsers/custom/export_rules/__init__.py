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

    # Add pa_rules command
    pa_rules_parser = export_subparsers.add_parser(
        'pa_rules',
        help='Export Private Access rules to JSON format',
        usage='catocli export pa_rules [-accountID <account_id>] [options]',
        description="""Export Private Access (privateAccess) rules to JSON format for backup, analysis, or migration purposes.

Flat ordered rule list (no sections in the terraform surface yet, no
sub-policies), consumed by the terraform-cato-bulk-private-access module.

Examples:
  catocli export pa_rules
  catocli export pa_rules -accountID 12345
  catocli export pa_rules --json-filename my_pa_rules.json""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    pa_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    pa_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_pa_rules_{account_id}.json)')
    pa_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    pa_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    pa_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    pa_rules_parser.set_defaults(func=export_rules.export_pa_rules_to_json)

    # Add apc_rules command
    apc_rules_parser = export_subparsers.add_parser(
        'apc_rules',
        help='Export Application Control rules to JSON format',
        usage='catocli export apc_rules [-accountID <account_id>] [options]',
        description="""Export Application Control rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export apc_rules
  catocli export apc_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    apc_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    apc_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_apc_rules_and_sections_{account_id}.json)')
    apc_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    apc_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    apc_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    apc_rules_parser.set_defaults(func=export_rules.export_apc_rules_to_json)

    # Add atr_rules command
    atr_rules_parser = export_subparsers.add_parser(
        'atr_rules',
        help='Export App Tenant Restriction rules to JSON format',
        usage='catocli export atr_rules [-accountID <account_id>] [options]',
        description="""Export App Tenant Restriction rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export atr_rules
  catocli export atr_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    atr_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    atr_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_atr_rules_and_sections_{account_id}.json)')
    atr_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    atr_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    atr_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    atr_rules_parser.set_defaults(func=export_rules.export_atr_rules_to_json)

    # Add ao_rules command
    ao_rules_parser = export_subparsers.add_parser(
        'ao_rules',
        help='Export ZTNA Always-On rules to JSON format',
        usage='catocli export ao_rules [-accountID <account_id>] [options]',
        description='''Export ZTNA Always-On (ztnaAlwaysOn) rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules only (no sub-policies exist for this policy
type), consumed by the terraform-cato-bulk-ao-rules module.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export ao_rules

  # Export with specific account ID
  catocli export ao_rules -accountID 12345

  # Export with custom filename
  catocli export ao_rules --json-filename my_ao_rules.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    ao_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    ao_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_ao_rules_and_sections_{account_id}.json)')
    ao_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    ao_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    ao_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ao_rules_parser.set_defaults(func=export_rules.export_ao_rules_to_json)

    # Add lan_fw_rules command
    lan_fw_rules_parser = export_subparsers.add_parser(
        'lan_fw_rules',
        help='Export LAN Firewall (socketLan) rules to JSON format',
        usage='catocli export lan_fw_rules [-accountID <account_id>] [options]',
        description='''Export LAN Firewall (socketLan) rules to JSON format for backup, analysis, or migration purposes.

Exports the full structure: sections (main and sub-policy owned), sub-policies
with their scope, network rules, and each network rule's nested child firewall
rules, plus the rules_in_sections ordering table consumed by the
terraform-cato-bulk-lan-fw-rules module.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export lan_fw_rules

  # Export with specific account ID
  catocli export lan_fw_rules -accountID 12345

  # Export with custom filename and timestamp
  catocli export lan_fw_rules --json-filename my_lan_rules.json --append-timestamp

  # Export to custom directory
  catocli export lan_fw_rules --output-directory ./exports''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    lan_fw_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    lan_fw_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_lan_fw_rules_and_sections_{account_id}.json)')
    lan_fw_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    lan_fw_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    lan_fw_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    lan_fw_rules_parser.set_defaults(func=export_rules.export_lan_fw_rules_to_json)

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
