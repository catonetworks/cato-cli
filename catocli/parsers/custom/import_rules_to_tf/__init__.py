import catocli.parsers.custom.import_rules_to_tf.import_rules_to_tf as import_rules_to_tf

def rule_import_parse(subparsers):
    """Create import command parsers"""
    
    # Create the main import parser
    import_parser = subparsers.add_parser('import', help='Import data from various sources', usage='catocli import <operation> [options]')
    import_subparsers = import_parser.add_subparsers(description='valid import operations', help='additional help')
    
    # Add if_rules_to_tf command
    if_rules_parser = import_subparsers.add_parser(
        'if_rules_to_tf', 
        help='Import Internet Firewall rules to Terraform state',
        usage='catocli import if_rules_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import if_rules_to_tf config_data/all_wf_rules_and_sections.json --module-name module.if_rules'
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
    
    return import_parser
