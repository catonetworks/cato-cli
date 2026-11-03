import catocli.parsers.custom.import_rules_to_tf.import_rules_to_tf as import_rules_to_tf

def rule_import_parse(subparsers):
    """Create import command parsers"""
    
    # Create the main import parser
    import_parser = subparsers.add_parser(
        'import', 
        help='Import data from various sources', 
        usage='catocli import <operation> [options]',
        description='''Import various types of data into Terraform state for infrastructure management and automation.

Common Examples:
  # Import firewall rules to Terraform
  catocli import if_rules_to_tf rules.json --module-name module.if_rules
  catocli import wf_rules_to_tf rules.json --module-name module.wf_rules
  
  # Import socket sites from JSON
  catocli import socket_sites_to_tf --data-type json --json-file sites.json --module-name module.sites
  
  # Import socket sites from CSV with network ranges
  catocli import socket_sites_to_tf --data-type csv --csv-file sites.csv --csv-folder ranges/ --module-name module.sites
  
  # Import with batch processing and verbose output
  catocli import if_rules_to_tf rules.json --module-name module.rules --batch-size 5 --delay 3 -v''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )
    import_subparsers = import_parser.add_subparsers(description='valid import operations', help='additional help')
    
    # Add if_rules_to_tf command
    if_rules_parser = import_subparsers.add_parser(
        'if_rules_to_tf', 
        help='Import Internet Firewall rules to Terraform state',
        usage='catocli import if_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import if_rules_to_tf config_data/all_ifw_rules_and_sections.json --module-name module.if_rules'
    )
    
    if_rules_parser.add_argument('json_file', help='Path to the JSON file containing IFW rules and sections')
    if_rules_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    if_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    if_rules_parser.add_argument('--batch-size', type=int, default=10, 
                                help='Number of imports per batch (default: 10)')
    if_rules_parser.add_argument('--delay', type=int, default=2, 
                                help='Delay between batches in seconds (default: 2)')
    if_rules_parser.add_argument('--rules-only', action='store_true', 
                                help='Import only rules, skip sections')
    if_rules_parser.add_argument('--sections-only', action='store_true', 
                                help='Import only sections, skip rules')
    if_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    if_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')
    
    if_rules_parser.set_defaults(func=import_rules_to_tf.import_if_rules_to_tf)

    lan_fw_rules_parser = import_subparsers.add_parser(
        'lan_fw_rules_to_tf',
        help='Import LAN Firewall (socketLan) rules to Terraform state',
        usage='catocli import lan_fw_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import lan_fw_rules_to_tf config_data/all_lan_fw_rules_and_sections.json --module-name module.lan_fw_rules'
    )

    lan_fw_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export lan_fw_rules`')
    lan_fw_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    lan_fw_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    lan_fw_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    lan_fw_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    lan_fw_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    lan_fw_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    lan_fw_rules_parser.set_defaults(func=import_rules_to_tf.import_lan_fw_rules_to_tf)

    ao_rules_parser = import_subparsers.add_parser(
        'ao_rules_to_tf',
        help='Import ZTNA Always-On rules to Terraform state',
        usage='catocli import ao_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import ao_rules_to_tf config_data/all_ao_rules_and_sections.json --module-name module.ao_rules'
    )

    ao_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export ao_rules`')
    ao_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    ao_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    ao_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    ao_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    ao_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ao_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    ao_rules_parser.set_defaults(func=import_rules_to_tf.import_ao_rules_to_tf)

    pa_rules_parser = import_subparsers.add_parser(
        'pa_rules_to_tf',
        help='Import Private Access rules to Terraform state',
        usage='catocli import pa_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import pa_rules_to_tf config_data/all_pa_rules.json --module-name module.pa_rules'
    )

    pa_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export pa_rules`')
    pa_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    pa_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    pa_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    pa_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    pa_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    pa_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    pa_rules_parser.set_defaults(func=import_rules_to_tf.import_pa_rules_to_tf)
    apc_rules_parser = import_subparsers.add_parser(
        'apc_rules_to_tf',
        help='Import Application Control rules to Terraform state',
        usage='catocli import apc_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import apc_rules_to_tf config_data/all_apc_rules_and_sections.json --module-name module.apc_rules'
    )

    apc_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export apc_rules`')
    apc_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    apc_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    apc_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    apc_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    apc_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    apc_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    apc_rules_parser.set_defaults(func=import_rules_to_tf.import_apc_rules_to_tf)

    atr_rules_parser = import_subparsers.add_parser(
        'atr_rules_to_tf',
        help='Import App Tenant Restriction rules to Terraform state',
        usage='catocli import atr_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import atr_rules_to_tf config_data/all_atr_rules_and_sections.json --module-name module.atr_rules'
    )

    atr_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export atr_rules`')
    atr_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    atr_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    atr_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    atr_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    atr_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    atr_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    atr_rules_parser.set_defaults(func=import_rules_to_tf.import_atr_rules_to_tf)

    

    # Add ts_rules_to_tf command
    ts_rules_parser = import_subparsers.add_parser(
        'ts_rules_to_tf',
        help='Import Terminal Server rules to Terraform state',
        usage='catocli import ts_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import ts_rules_to_tf config_data/all_ts_rules_and_sections.json --module-name module.ts_rules'
    )

    ts_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export ts_rules`')
    ts_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    ts_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    ts_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    ts_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    ts_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ts_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    ts_rules_parser.set_defaults(func=import_rules_to_tf.import_ts_rules_to_tf)

    # Add amfh_rules_to_tf command
    amfh_rules_parser = import_subparsers.add_parser(
        'amfh_rules_to_tf',
        help='Import Anti-Malware File Hash rules to Terraform state',
        usage='catocli import amfh_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import amfh_rules_to_tf config_data/all_amfh_rules_and_sections.json --module-name module.amfh_rules'
    )

    amfh_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export amfh_rules`')
    amfh_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    amfh_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    amfh_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    amfh_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    amfh_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    amfh_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    amfh_rules_parser.set_defaults(func=import_rules_to_tf.import_amfh_rules_to_tf)

    # Add ssia_rules_to_tf command
    ssia_rules_parser = import_subparsers.add_parser(
        'ssia_rules_to_tf',
        help='Import SDP Static IP Allocation rules to Terraform state',
        usage='catocli import ssia_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import ssia_rules_to_tf config_data/all_ssia_rules_and_sections.json --module-name module.ssia_rules'
    )

    ssia_rules_parser.add_argument('json_file', help='Path to the JSON file produced by `catocli export ssia_rules`')
    ssia_rules_parser.add_argument('--module-name', required=True,
                                help='Terraform module name to import resources into')
    ssia_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    ssia_rules_parser.add_argument('--batch-size', type=int, default=10,
                                help='Number of imports per batch (default: 10)')
    ssia_rules_parser.add_argument('--delay', type=int, default=2,
                                help='Delay between batches in seconds (default: 2)')
    ssia_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ssia_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    ssia_rules_parser.set_defaults(func=import_rules_to_tf.import_ssia_rules_to_tf)

    # Add wf_rules_to_tf command
    wf_rules_parser = import_subparsers.add_parser(
        'wf_rules_to_tf', 
        help='Import WAN Firewall rules to Terraform state',
        usage='catocli import wf_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import wf_rules_to_tf config_data/all_wf_rules_and_sections.json --module-name module.wf_rules'
    )
    
    wf_rules_parser.add_argument('json_file', help='Path to the JSON file containing WF rules and sections')
    wf_rules_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    wf_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    wf_rules_parser.add_argument('--batch-size', type=int, default=10, 
                                help='Number of imports per batch (default: 10)')
    wf_rules_parser.add_argument('--delay', type=int, default=2, 
                                help='Delay between batches in seconds (default: 2)')
    wf_rules_parser.add_argument('--rules-only', action='store_true', 
                                help='Import only rules, skip sections')
    wf_rules_parser.add_argument('--sections-only', action='store_true', 
                                help='Import only sections, skip rules')
    wf_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    wf_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')
    
    wf_rules_parser.set_defaults(func=import_rules_to_tf.import_wf_rules_to_tf)
    
    # Add tls_rules_to_tf command
    tls_rules_parser = import_subparsers.add_parser(
        'tls_rules_to_tf', 
        help='Import TLS Inspectiom rules to Terraform state',
        usage='catocli import tls_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import tls_rules_to_tf config_data/all_tls_rules_and_sections.json --module-name module.tls_rules'
    )
    
    tls_rules_parser.add_argument('json_file', help='Path to the JSON file containing TLS rules and sections')
    tls_rules_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    tls_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    tls_rules_parser.add_argument('--batch-size', type=int, default=10, 
                                help='Number of imports per batch (default: 10)')
    tls_rules_parser.add_argument('--delay', type=int, default=2, 
                                help='Delay between batches in seconds (default: 2)')
    tls_rules_parser.add_argument('--rules-only', action='store_true', 
                                help='Import only rules, skip sections')
    tls_rules_parser.add_argument('--sections-only', action='store_true', 
                                help='Import only sections, skip rules')
    tls_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    tls_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    tls_rules_parser.set_defaults(func=import_rules_to_tf.import_tls_rules_to_tf)

    # Add wnw_rules_to_tf command
    wnw_rules_parser = import_subparsers.add_parser(
        'wnw_rules_to_tf', 
        help='Import WAN Network rules to Terraform state',
        usage='catocli import wnw_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import wnw_rules_to_tf config_data/all_wnw_rules_and_sections.json --module-name module.wnw_rules'
    )
    
    wnw_rules_parser.add_argument('json_file', help='Path to the JSON file containing WNW rules and sections')
    wnw_rules_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    wnw_rules_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    wnw_rules_parser.add_argument('--batch-size', type=int, default=10, 
                                help='Number of imports per batch (default: 10)')
    wnw_rules_parser.add_argument('--delay', type=int, default=2, 
                                help='Delay between batches in seconds (default: 2)')
    wnw_rules_parser.add_argument('--rules-only', action='store_true', 
                                help='Import only rules, skip sections')
    wnw_rules_parser.add_argument('--sections-only', action='store_true', 
                                help='Import only sections, skip rules')
    wnw_rules_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    wnw_rules_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')

    wnw_rules_parser.set_defaults(func=import_rules_to_tf.import_wnw_rules_to_tf)    

    return import_parser
