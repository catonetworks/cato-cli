#!/usr/bin/env python3
"""
Private commands parser for custom GraphQL payloads
Dynamically loads commands from ~/.cato/settings.json
"""

import argparse
from ..customParserApiClient import createPrivateRequest, get_private_help
from ...Utils.cliutils import load_private_settings


class PrivateCommandHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom formatter for private commands with wider spacing"""
    def __init__(self, prog):
        super().__init__(prog, max_help_position=35, width=100)


def _show_private_help(args, configuration=None):
    """Show formatted help when private is called without subcommand"""
    private_commands = load_private_settings()
    
    print("Usage: catocli private <command> [options]")
    print("\nNote: accountID is auto-loaded from ~/.cato/settings.json")
    print("\nAvailable private commands:")
    
    # Show commands with their descriptions
    for cmd_name, cmd_config in sorted(private_commands.items()):
        if cmd_name == 'version':
            continue  # Skip internal version command
        desc = cmd_config.get('description', 'No description available')
        # Truncate long descriptions
        if len(desc) > 70:
            desc = desc[:67] + '...'
        print(f"  {cmd_name:25} {desc}")
    
    print("\nFor detailed help on a specific command:")
    print("  catocli private <command> -h")
    print("\nNote: accountID is auto-loaded from ~/.cato/settings.json")
    print("      version is auto-fetched from API when needed")
    return None


def private_parse(subparsers):
    """Check for private settings and create private parser if found"""
    private_commands = load_private_settings()
    
    if not private_commands:
        return None
    
    # Create the private subparser
    private_parser = subparsers.add_parser(
        'private', 
        help='Private custom commands (configured in ~/.cato/settings.json)',
        usage='catocli private <command> [options]',
        formatter_class=PrivateCommandHelpFormatter
    )
    
    private_subparsers = private_parser.add_subparsers(
        title='Available private commands',
        description='Custom GraphQL operations defined in ~/.cato/settings.json',
        metavar='<command>',
        parser_class=argparse.ArgumentParser
    )
    
    # Set default help function
    private_parser.set_defaults(func=_show_private_help)
    
    # Dynamically create subparsers for each private command
    # Exclude 'version' command as it's auto-fetched internally for optimistic locking
    for command_name, command_config in private_commands.items():
        # Skip version command (used internally for auto-fetch)
        # if command_name == 'version':
        #     continue
            
        create_private_command_parser(
            private_subparsers, 
            command_name, 
            command_config
        )
    
    return private_parser


def create_private_command_parser(subparsers, command_name, command_config):
    """Create a parser for a specific private command"""
    
    # Get description from config, truncate if too long for help display
    description = command_config.get('description', f'{command_name} operation')
    help_text = description if len(description) <= 50 else description[:47] + '...'
    
    # Create the command parser
    cmd_parser = subparsers.add_parser(
        command_name,
        help=help_text,
        usage=get_private_help(command_name, command_config)
    )
    
    # Add standard arguments
    cmd_parser.add_argument(
        'json', 
        nargs='?', 
        default='{}', 
        help='Variables in JSON format (defaults to empty object if not provided).'
    )
    cmd_parser.add_argument(
        '--json-file',
        help='Path to a file containing JSON input variables.'
    )
    cmd_parser.add_argument(
        '-t', 
        const=True, 
        default=False, 
        nargs='?', 
        help='Print GraphQL query without sending API call'
    )
    cmd_parser.add_argument(
        '-v', 
        const=True, 
        default=False, 
        nargs='?', 
        help='Verbose output'
    )
    cmd_parser.add_argument(
        '-p', 
        const=True, 
        default=False, 
        nargs='?', 
        help='Pretty print'
    )
    cmd_parser.add_argument(
        '-H', '--header', 
        action='append', 
        dest='headers', 
        help='Add custom headers in "Key: Value" format. Can be used multiple times.'
    )
    cmd_parser.add_argument(
        '--headers-file', 
        dest='headers_file', 
        help='Load headers from a file. Each line should contain a header in "Key: Value" format.'
    )
    
    # Note: accountID is read from ~/.cato/settings.json automatically
    # This argument is kept for compatibility but the settings file value takes priority
    cmd_parser.add_argument(
        '-accountID',
        required=False,
        help='Account ID (auto-loaded from ~/.cato/settings.json)'
    )
    
    # Add CSV output arguments (if the command supports CSV)
    if 'csvOutputOperation' in command_config:
        cmd_parser.add_argument(
            '-f', '--format',
            choices=['json', 'csv'],
            default='json',
            help='Output format (default: json)'
        )
        cmd_parser.add_argument(
            '--csv-filename',
            help=f'Override CSV file name (default: {command_name}.csv)'
        )
        cmd_parser.add_argument(
            '--append-timestamp',
            action='store_true',
            help='Append timestamp to the CSV file name'
        )
    
    # Add dynamic arguments based on command configuration (excluding accountId and version)
    if 'arguments' in command_config:
        for arg in command_config['arguments']:
            arg_name = arg.get('name')
            # Skip accountId (from profile) and version (auto-fetched)
            if arg_name and arg_name.lower() not in ['accountid', 'version']:
                arg_type = arg.get('type', 'string')
                arg_default = arg.get('default')
                arg_help = f"Argument: {arg_name}"
                
                if arg_default:
                    arg_help += f" (default: {arg_default})"
                
                cmd_parser.add_argument(
                    f'--{arg_name}',
                    help=arg_help,
                    default=arg_default
                )
    
    # Set the function to handle this command
    cmd_parser.set_defaults(
        func=createPrivateRequest, 
        private_command=command_name,
        private_config=command_config
    )
