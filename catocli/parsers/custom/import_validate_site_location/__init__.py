import catocli.parsers.custom.import_validate_site_location.validate_site_location as validate_site_location

def validate_site_location_parse(subparsers, import_parser):
    """Add validate_site_location command to existing import parser"""
    
    if import_parser is None:
        raise ValueError("Import parser not found. Make sure rule_import_parse is called first.")
    
    # Get the existing subparsers from the import parser
    import_subparsers = None
    for action in import_parser._subparsers._group_actions:
        if hasattr(action, 'choices'):
            import_subparsers = action
            break
    
    if import_subparsers is None:
        raise ValueError("Import subparsers not found in existing import parser.")
    
    # Add validate_site_location command
    validate_parser = import_subparsers.add_parser(
        'validate_site_location', 
        help='Validate site location data against Cato location database',
        description='Validate site location entries (country, city, state, timezone) from JSON or CSV data sources against Cato\'s location database.',
        usage='''catocli import validate_site_location <file_path> -f=<format> [options]

Examples:
  catocli import validate_site_location path/to/file.csv -f=csv
  catocli import validate_site_location path/to/file.json -f=json
  catocli import validate_site_location sites.csv -f=csv -v
  catocli import validate_site_location sites.json -f=json -v''',
        formatter_class=validate_site_location.argparse.RawDescriptionHelpFormatter
    )
    
    # Required arguments
    validate_parser.add_argument('file_path', 
                                help='Path to CSV or JSON file containing site location data')
    validate_parser.add_argument('-f', '--format', 
                                choices=['json', 'csv'], 
                                required=True,
                                help='File format: json or csv')
    
    # Optional arguments
    validate_parser.add_argument('-accountID', 
                                help='Account ID (optional, for CLI framework compatibility)', 
                                required=False)
    validate_parser.add_argument('-v', '--verbose', 
                                action='store_true', 
                                help='Verbose output showing all validation details')
    validate_parser.add_argument('--show-valid', 
                                action='store_true', 
                                help='Show valid entries in addition to invalid ones')
    validate_parser.add_argument('--output', 
                                help='Output file path for validation results (CSV format)')
    
    validate_parser.set_defaults(func=validate_site_location.validate_site_location)
        
    return import_parser
