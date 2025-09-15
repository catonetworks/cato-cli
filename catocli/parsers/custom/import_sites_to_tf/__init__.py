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
        description='Import Cato socket sites, WAN interfaces, and network ranges to Terraform state from JSON or CSV data sources.',
        usage='''catocli import socket_sites_to_tf [options]

JSON Import Examples:
  catocli import socket_sites_to_tf --data-type json --json-file sites.json --module-name module.sites
  catocli import socket_sites_to_tf sites.json --module-name module.sites  # Legacy format (auto-detects JSON)

CSV Import Examples:
  catocli import socket_sites_to_tf --data-type csv --csv-file sites.csv --module-name module.sites
  catocli import socket_sites_to_tf --data-type csv --csv-file sites.csv --csv-folder sites_config --module-name module.sites''',
        formatter_class=import_sites_to_tf.argparse.RawDescriptionHelpFormatter
    )
    
    # Data source arguments
    data_group = socket_sites_parser.add_argument_group('Data Source (choose one)')
    data_group.add_argument('--data-type', choices=['json', 'csv'], 
                           help='Specify data source type: json or csv')
    data_group.add_argument('--json-file', 
                           help='Path to JSON file containing socket sites data')
    data_group.add_argument('--csv-file', 
                           help='Path to main CSV file containing socket sites data')
    data_group.add_argument('--csv-folder', 
                           help='Path to folder containing per-site network ranges CSV files (optional for CSV import)')
    
    # Backward compatibility: positional JSON file argument
    socket_sites_parser.add_argument('json_file_legacy', nargs='?', 
                                     help='[LEGACY] Path to JSON file (for backward compatibility)')
    
    # Required arguments
    socket_sites_parser.add_argument('--module-name', required=True, 
                                help='Terraform module name to import resources into')
    socket_sites_parser.add_argument('-accountID', help='Account ID (required by CLI framework but not used for import)', required=False)
    
    # Import options
    import_group = socket_sites_parser.add_argument_group('Import Options')
    import_group.add_argument('--batch-size', type=int, default=10, 
                             help='Number of imports per batch (default: 10)')
    import_group.add_argument('--delay', type=int, default=2, 
                             help='Delay between batches in seconds (default: 2)')
    import_group.add_argument('--sites-only', action='store_true', 
                             help='Import only sites, skip interfaces and network ranges')
    import_group.add_argument('--wan-interfaces-only', action='store_true', 
                             help='Import only WAN interfaces, skip sites and network ranges')
    import_group.add_argument('--lan-interfaces-only', action='store_true', 
                             help='Import only LAN interfaces, skip sites and network ranges')
    import_group.add_argument('--network-ranges-only', action='store_true', 
                             help='Import only network ranges, skip sites and interfaces')
    import_group.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    import_group.add_argument('--auto-approve', action='store_true', help='Skip confirmation prompt and proceed automatically')
    
    socket_sites_parser.set_defaults(func=import_sites_to_tf.import_socket_sites_to_tf)
        
    return import_parser
