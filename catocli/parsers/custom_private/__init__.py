#!/usr/bin/env python3
"""
Private commands parser for custom GraphQL payloads
Dynamically loads commands from ~/.cato/settings.json
"""

import argparse
from ..customParserApiClient import createPrivateRequest, get_private_help
from ...Utils.cliutils import load_private_settings


def private_parse(subparsers):
    """Check for private settings and create private parser if found"""
    private_commands = load_private_settings()
    
    if not private_commands:
        return None
    
    # Create the private subparser
    private_parser = subparsers.add_parser(
        'private', 
        help='Private custom commands (configured in ~/.cato/settings.json)',
        usage='catocli private <command> [options]'
    )
    
    private_subparsers = private_parser.add_subparsers(
        description='Available private commands',
        help='Private command help'
    )
    
    # Dynamically create subparsers for each private command
    for command_name, command_config in private_commands.items():
        create_private_command_parser(
            private_subparsers, 
            command_name, 
            command_config
        )
    
    return private_parser


def create_private_command_parser(subparsers, command_name, command_config):
    """Create a parser for a specific private command"""
    
    # Create the command parser
    cmd_parser = subparsers.add_parser(
        command_name,
        help=f'Execute private command: {command_name}',
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
    
    # Add standard accountID argument (like other commands)
    cmd_parser.add_argument(
        '-accountID', 
        help='Override the account ID from profile with this value.'
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
    
    # Add dynamic arguments based on command configuration (excluding accountId since it's handled above)
    if 'arguments' in command_config:
        for arg in command_config['arguments']:
            arg_name = arg.get('name')
            # Skip accountId since it's handled by the standard -accountID argument
            if arg_name and arg_name.lower() != 'accountid':
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
