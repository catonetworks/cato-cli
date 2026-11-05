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
  catocli export socket_sites -gt -f csv

  # Export dependency objects (groups, global IP ranges, custom applications)
  catocli export groups
  catocli export global_ip_ranges
  catocli export custom_apps --strip-ids''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    export_subparsers = export_parser.add_subparsers(description='valid export operations', help='additional help')
    
    # Add sites export functionality
    from catocli.parsers.custom.export_sites import export_sites_parse
    export_sites_parse(export_subparsers)

    # Add dependency object export functionality (groups, global_ip_ranges, custom_apps)
    from catocli.parsers.custom.export_deps import export_deps_parse
    export_deps_parse(export_subparsers)

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


    # Add ts_rules command
    ts_rules_parser = export_subparsers.add_parser(
        'ts_rules',
        help='Export Terminal Server rules to JSON format',
        usage='catocli export ts_rules [-accountID <account_id>] [options]',
        description="""Export Terminal Server rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export ts_rules
  catocli export ts_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    ts_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    ts_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_ts_rules_and_sections_{account_id}.json)')
    ts_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    ts_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    ts_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ts_rules_parser.set_defaults(func=export_rules.export_ts_rules_to_json)

    # Add amfh_rules command
    amfh_rules_parser = export_subparsers.add_parser(
        'amfh_rules',
        help='Export Anti-Malware File Hash rules to JSON format',
        usage='catocli export amfh_rules [-accountID <account_id>] [options]',
        description="""Export Anti-Malware File Hash rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export amfh_rules
  catocli export amfh_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    amfh_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    amfh_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_amfh_rules_and_sections_{account_id}.json)')
    amfh_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    amfh_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    amfh_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    amfh_rules_parser.set_defaults(func=export_rules.export_amfh_rules_to_json)

    # Add ssia_rules command
    ssia_rules_parser = export_subparsers.add_parser(
        'ssia_rules',
        help='Export SDP Static IP Allocation rules to JSON format',
        usage='catocli export ssia_rules [-accountID <account_id>] [options]',
        description="""Export SDP Static IP Allocation rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export ssia_rules
  catocli export ssia_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    ssia_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    ssia_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_ssia_rules_and_sections_{account_id}.json)')
    ssia_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    ssia_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    ssia_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ssia_rules_parser.set_defaults(func=export_rules.export_ssia_rules_to_json)


    # Add dia_rules command
    dia_rules_parser = export_subparsers.add_parser(
        'dia_rules',
        help='Export Dynamic IP Allocation rules to JSON format',
        usage='catocli export dia_rules [-accountID <account_id>] [options]',
        description="""Export Dynamic IP Allocation rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export dia_rules
  catocli export dia_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    dia_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    dia_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_dia_rules_and_sections_{account_id}.json)')
    dia_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    dia_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    dia_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    dia_rules_parser.set_defaults(func=export_rules.export_dia_rules_to_json)

    # Add cc_rules command
    cc_rules_parser = export_subparsers.add_parser(
        'cc_rules',
        help='Export Client Connectivity rules to JSON format',
        usage='catocli export cc_rules [-accountID <account_id>] [options]',
        description="""Export Client Connectivity rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export cc_rules
  catocli export cc_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    cc_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    cc_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_cc_rules_and_sections_{account_id}.json)')
    cc_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    cc_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    cc_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    cc_rules_parser.set_defaults(func=export_rules.export_cc_rules_to_json)

    # Add st_rules command
    st_rules_parser = export_subparsers.add_parser(
        'st_rules',
        help='Export Split Tunnel rules to JSON format',
        usage='catocli export st_rules [-accountID <account_id>] [options]',
        description="""Export Split Tunnel rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export st_rules
  catocli export st_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    st_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    st_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_st_rules_and_sections_{account_id}.json)')
    st_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    st_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    st_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    st_rules_parser.set_defaults(func=export_rules.export_st_rules_to_json)


    # Add rpf_rules command
    rpf_rules_parser = export_subparsers.add_parser(
        'rpf_rules',
        help='Export Remote Port Forwarding rules to JSON format',
        usage='catocli export rpf_rules [-accountID <account_id>] [options]',
        description="""Export Remote Port Forwarding rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export rpf_rules
  catocli export rpf_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    rpf_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    rpf_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_rpf_rules_and_sections_{account_id}.json)')
    rpf_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    rpf_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    rpf_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    rpf_rules_parser.set_defaults(func=export_rules.export_rpf_rules_to_json)

    # Add swp_rules command
    swp_rules_parser = export_subparsers.add_parser(
        'swp_rules',
        help='Export Site Web Proxy rules to JSON format',
        usage='catocli export swp_rules [-accountID <account_id>] [options]',
        description="""Export Site Web Proxy rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export swp_rules
  catocli export swp_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    swp_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    swp_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_swp_rules_and_sections_{account_id}.json)')
    swp_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    swp_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    swp_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    swp_rules_parser.set_defaults(func=export_rules.export_swp_rules_to_json)


    # Add sb_rules command
    sb_rules_parser = export_subparsers.add_parser(
        'sb_rules',
        help='Export Socket Bypass rules to JSON format',
        usage='catocli export sb_rules [-accountID <account_id>] [options]',
        description="""Export Socket Bypass rules to JSON format for backup, analysis, or migration purposes.

Flat structure: sections and rules (no sub-policies for this policy type).

Examples:
  catocli export sb_rules
  catocli export sb_rules -accountID 12345""",
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    sb_rules_parser.add_argument('-accountID', help='Account ID to export rules from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    sb_rules_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: all_sb_rules_and_sections_{account_id}.json)')
    sb_rules_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    sb_rules_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    sb_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    sb_rules_parser.set_defaults(func=export_rules.export_sb_rules_to_json)

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
