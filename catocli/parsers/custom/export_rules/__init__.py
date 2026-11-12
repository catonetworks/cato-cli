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
  catocli export custom_apps --strip-ids

  # Export every registered type in one run
  catocli export all
  catocli export all --output-directory ./config_data --types if_rules,wf_rules

  # Produce a tenant-portable migration export (ids stripped) while keeping a raw archive copy for diffing
  catocli export all --strip-ids --no-account-suffix --output-directory migration_data/run1 --archive-directory migration_raw/run1''',
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

    # Add the 'all' command LAST, so export_subparsers already holds every
    # export subcommand registered above (sites, dependency objects, and
    # every rules type) - export_all_to_json derives its type list at
    # runtime from this same registry (passed through via
    # _export_subparsers below), so no second hardcoded type list exists;
    # a future export subcommand added anywhere above is picked up
    # automatically without touching this block.
    all_parser = export_subparsers.add_parser(
        'all',
        help="Run every registered 'catocli export <type>' subcommand in-process",
        usage='catocli export all [-accountID <account_id>] [options]',
        description='''Run every registered export type (sites, dependency objects, and all
policy-rule types) in-process - calling the same functions the individual
`catocli export <type>` subcommands call, not subprocesses - writing each
type's own default filename into one shared --output-directory.

Before exporting anything, a pre-flight check validates the active
credentials/permissions with a lightweight API call (the same check
`catocli configure set` runs before saving a profile) - on failure, nothing
is exported.

One failing type does not abort the run (continue-on-error by default); the
process exits non-zero if any requested type failed, after printing a
per-type progress line and a final summary (succeeded/failed counts and
error one-liners for each failed type). The one exception: if a type fails
with an access-denied error, the whole run aborts immediately regardless of
--fail-fast, since a key denied one API will almost always be denied every
remaining one too.

Examples:
  # Export every registered type into ./config_data (uses CATO_ACCOUNT_ID environment variable)
  catocli export all

  # Export everything into a custom directory, with a specific account
  catocli export all -accountID 12345 --output-directory ./config_data

  # Export only a subset of types
  catocli export all --types if_rules,wf_rules,groups,socket_sites

  # Stop at the first failing type instead of continuing
  catocli export all --fail-fast -v

  # Also keep a second raw copy of every successful export for redundancy/diffing
  catocli export all --archive-directory ./config_data_archive

  # Write canonical filenames (no _<accountID> suffix), e.g. for a Terraform config_data/ directory
  catocli export all --no-account-suffix

  # Produce a tenant-migration export: ids stripped from the primary files, a raw id-bearing copy kept for diffing
  catocli export all --strip-ids --no-account-suffix --output-directory migration_data/run1 --archive-directory migration_raw/run1''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    all_parser.add_argument('-accountID', help='Account ID to export from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    all_parser.add_argument('--output-directory', dest='output_directory', help='Shared output directory for every exported type (default: config_data)')
    all_parser.add_argument('--types', dest='types', help='Comma-separated list of export type names to run (default: every registered type - run `catocli export -h` to see the full list)')
    all_parser.add_argument('--fail-fast', dest='fail_fast', action='store_true', help='Stop at the first failing export type instead of continuing (default: continue and report every failure at the end)')
    all_parser.add_argument('--archive-directory', dest='archive_directory', help="Also write a second raw copy of every successful export into this directory, using the same basename as the primary --output-directory output - for redundancy/diffing (e.g. config_data_archive). Off by default. Composes with --strip-ids: the archive copy is ALWAYS the raw, id-bearing file - only the primary --output-directory copy is stripped.")
    all_parser.add_argument('--no-account-suffix', dest='no_account_suffix', action='store_true', help="Strip the trailing '_<accountID>' from each type's produced filename before the extension (e.g. all_ifw_rules_and_sections_15412.json -> all_ifw_rules_and_sections.json). Off by default - current account-suffixed filenames are kept unless this is set.")
    all_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=(
        "Produce a tenant-portable migration export: every type's PRIMARY output file in "
        "--output-directory has its tenant-specific/brownfield-import-key ids stripped - "
        "dependency objects (groups, global_ip_ranges, custom_apps, fqdn_containers, "
        "ip_range_containers, mailing_lists, subscription_groups, dhcp_relay_groups, "
        "static_hosts, allocated_ips, private_apps, app_connectors), socket_sites "
        "(site/license/interface/wifi ids), and every "
        "`*_rules` policy type (each rule's id, each section's section_id, each "
        "sub-policy's sub_policy_id/scope_rule_id) - while rule/section names and "
        "rules_in_sections/rules_in_policy ordering are always preserved. Each type's API "
        "is still called exactly once: with --archive-directory also set, the raw "
        "id-bearing file is archived FIRST, then the primary file is stripped in place. "
        "Also writes a CHECKLIST.md into --output-directory listing every file this run "
        "produced plus the manual re-resolution steps a target tenant still needs "
        "(id-only group members, mailing-list admin ids, Wi-Fi PSKs, licenses, physical "
        "socket re-registration). Off by default - this is the native-catocli replacement "
        "for the reference-architecture repo's scripts/migrate_tenant.py."
    ))
    all_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    all_parser.set_defaults(func=export_rules.export_all_to_json, _export_subparsers=export_subparsers)

    return export_parser
