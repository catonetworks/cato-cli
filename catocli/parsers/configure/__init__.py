#!/usr/bin/env python3
"""
Configure command parser for Cato CLI
Handles profile creation, listing, and switching
"""

import argparse
from .configure import (
    configure_profile, 
    list_profiles, 
    set_profile, 
    delete_profile,
    show_profile
)


def configure_parse(subparsers):
    """Create configure command parsers"""
    
    # Create the main configure parser
    configure_parser = subparsers.add_parser(
        'configure', 
        help='Configure Cato CLI credentials and profiles',
        usage='catocli configure <subcommand> [options]'
    )
    configure_subparsers = configure_parser.add_subparsers(
        description='Configure operations', 
        help='Profile management operations'
    )
    
    # Configure profile command
    config_parser = configure_subparsers.add_parser(
        'set',
        help='Configure a profile with credentials',
        usage='catocli configure set [--profile PROFILE] [options]'
    )
    config_parser.add_argument(
        '--profile', 
        default='default',
        help='Profile name to configure (default: default)'
    )
    config_parser.add_argument(
        '--endpoint',
        help='Cato API endpoint URL (default: https://api.catonetworks.com/api/v1/graphql2)'
    )
    config_parser.add_argument(
        '--cato-token',
        help='Cato API token'
    )
    config_parser.add_argument(
        '--account-id',
        help='Cato account ID'
    )
    config_parser.add_argument(
        '--scim-url',
        help='SCIM service URL (e.g., https://scimservice.catonetworks.com:4443/scim/v2/{accountId}/{sourceId})'
    )
    config_parser.add_argument(
        '--scim-token',
        help='SCIM Bearer token'
    )
    config_parser.add_argument(
        '--interactive',
        action='store_true',
        help='Interactive configuration mode'
    )
    config_parser.add_argument(
        '--skip-validation',
        action='store_true',
        help='Skip credential validation (save without testing)'
    )
    config_parser.set_defaults(func=configure_profile)
    
    # List profiles command
    list_parser = configure_subparsers.add_parser(
        'list',
        help='List all configured profiles',
        usage='catocli configure list'
    )
    list_parser.set_defaults(func=list_profiles)
    
    # Use/switch profile command
    use_parser = configure_subparsers.add_parser(
        'use',
        help='Set the active profile',
        usage='catocli configure use <profile>'
    )
    use_parser.add_argument(
        'profile',
        help='Profile name to activate'
    )
    use_parser.set_defaults(func=set_profile)
    
    # Show current profile command
    show_parser = configure_subparsers.add_parser(
        'show',
        help='Show current profile configuration',
        usage='catocli configure show [--profile PROFILE]'
    )
    show_parser.add_argument(
        '--profile',
        help='Profile name to show (default: current active profile)'
    )
    show_parser.set_defaults(func=show_profile)
    
    # Delete profile command
    delete_parser = configure_subparsers.add_parser(
        'delete',
        help='Delete a profile',
        usage='catocli configure delete <profile>'
    )
    delete_parser.add_argument(
        'profile',
        help='Profile name to delete'
    )
    delete_parser.add_argument(
        '--force',
        action='store_true',
        help='Force deletion without confirmation'
    )
    delete_parser.set_defaults(func=delete_profile)
    
    return configure_parser
