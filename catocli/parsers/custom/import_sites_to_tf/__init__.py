import catocli.parsers.custom.import_sites_to_tf.import_sites_to_tf as import_sites_to_tf

def site_import_parse(subparsers, import_parser):
    """Add socket sites import command to existing import parser"""
    
    if import_parser is None:
        raise ValueError("Import parser not found. Make sure rule_import_parse is called before site_import_parse.")
    
    # Get the existing subparsers from the import parser
    import_subparsers = None
    for action in import_parser._subparsers._group_actions:
        if hasattr(action, 'choices'):
            import_subparsers = action
            break
    
    if import_subparsers is None:
        raise ValueError("Import subparsers not found in existing import parser.")
    
    # Add socket_sites_to_tf command
    socket_sites_parser = import_subparsers.add_parser(
        'socket_sites_to_tf', 
        help='Import socket sites to Terraform state',
        usage='catocli import socket_sites_to_tf <json_file> --module-name <module_name> [options]\n\nexample: catocli import socket_sites_to_tf config_data/socket_sites_11484.json --module-name module.sites'
    )
    
    socket_sites_parser.add_argument('json_file', help='Path to the JSON file containing socket sites data')
    socket_sites_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    socket_sites_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    socket_sites_parser.add_argument('--batch-size', type=int, default=10, 
                                help='Number of imports per batch (default: 10)')
    socket_sites_parser.add_argument('--delay', type=int, default=2, 
                                help='Delay between batches in seconds (default: 2)')
    socket_sites_parser.add_argument('--sites-only', action='store_true', 
                                help='Import only sites, skip interfaces and network ranges')
    socket_sites_parser.add_argument('--wan-interfaces-only', action='store_true', 
                                help='Import only WAN interfaces, skip sites and network ranges')
    socket_sites_parser.add_argument('--lan-interfaces-only', action='store_true', 
                                help='Import only LAN interfaces, skip sites and network ranges')
    socket_sites_parser.add_argument('--network-ranges-only', action='store_true', 
                                help='Import only network ranges, skip sites and interfaces')
    socket_sites_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    socket_sites_parser.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')
    
    socket_sites_parser.set_defaults(func=import_sites_to_tf.import_socket_sites_to_tf)
        
    return import_parser
