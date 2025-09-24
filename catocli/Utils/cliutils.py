#!/usr/bin/env python3
"""
General CLI utilities for catocli

This module contains general-purpose utility functions used across the catocli
package, including settings loading and configuration management.
"""

import os
import json


# Import for resource handling
try:
    # Python 3.9+
    from importlib.resources import files
    def get_package_resource(package, filename):
        return files(package).joinpath(filename).read_text(encoding='utf-8')
except ImportError:
    try:
        # Python 3.7-3.8
        from importlib.resources import read_text
        def get_package_resource(package, filename):
            return read_text(package, filename, encoding='utf-8')
    except ImportError:
        try:
            # Fallback to pkg_resources
            import pkg_resources
            def get_package_resource(package, filename):
                return pkg_resources.resource_string(package, filename).decode('utf-8')
        except ImportError:
            # Final fallback - no package resources available
            def get_package_resource(package, filename):
                raise ImportError("No resource handling module available")


def load_cli_settings():
    """
    Load clisettings.json from multiple possible locations:
    1. Package resource (for installed packages)
    2. Repository location (for development)
    3. Adjacent file location (for development)
    4. Embedded defaults as final fallback
    
    Returns:
        dict: The loaded settings or embedded default settings if all loading fails
    """
    # Embedded default settings as final fallback
    default_settings = {
        "export_by_socket_type": {
            "SOCKET_X1500": True,
            "SOCKET_X1600": True,
            "SOCKET_X1600_LTE": True,
            "SOCKET_X1700": True
        },
        "default_socket_interface_map": {
            "SOCKET_X1500": "LAN1",
            "SOCKET_X1600": "INT_5",
            "SOCKET_X1600_LTE": "INT_5",
            "SOCKET_X1700": "INT_3"
        },
        "childOperationParent": {
            "xdr": True,
            "policy": True,
            "groups": True,
            "newGroups": True,
            "site": True
        },
        "childOperationObjects": {
            "ipAddressRange": True,
            "fqdn": True,
            "PolicyQueries": True,
            "GroupsQueries": True,
            "ContainerQueries": True,
            "SiteQueries": True
        },
        "queryOperationCsvOutput": {
            "query.appStats": "format_app_stats_to_csv",
            "query.appStatsTimeSeries": "format_app_stats_timeseries_to_csv",
            "query.socketPortMetricsTimeSeries": "format_socket_port_metrics_timeseries_to_csv"
        }
    }
    
    settings_locations = [
        # Try package resource first (for installed packages)
        lambda: json.loads(get_package_resource('catocli', 'clisettings.json')),
        # Try adjacent file location (for development - new location)
        lambda: json.load(open(os.path.join(os.path.dirname(__file__), '../clisettings.json'), 'r', encoding='utf-8')),
        # Try repository location (for development - fallback)
        lambda: json.load(open(os.path.join(os.path.dirname(__file__), '../../clisettings.json'), 'r', encoding='utf-8'))
    ]
    
    for i, load_func in enumerate(settings_locations):
        try:
            settings = load_func()
            if settings:
                return settings
        except (FileNotFoundError, json.JSONDecodeError, ImportError, OSError, ModuleNotFoundError) as e:
            # Continue to next location
            continue
    
    # If all locations fail, return embedded default settings
    return default_settings


def get_cli_settings_path():
    """
    Get the path to the CLI settings file, trying different locations.
    
    Returns:
        str or None: Path to the settings file if found, None otherwise
    """
    possible_paths = [
        # Adjacent file location (for development - new location)
        os.path.join(os.path.dirname(__file__), '../clisettings.json'),
        # Repository location (for development - fallback)
        os.path.join(os.path.dirname(__file__), '../../clisettings.json'),
        # Current directory
        os.path.join(os.getcwd(), 'clisettings.json'),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def load_json_file(file_path, encoding='utf-8'):
    """
    Load a JSON file with error handling.
    
    Args:
        file_path (str): Path to the JSON file
        encoding (str): File encoding (default: utf-8)
    
    Returns:
        dict or None: The loaded JSON data, or None if loading fails
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        return None


def save_json_file(data, file_path, encoding='utf-8', indent=2):
    """
    Save data to a JSON file with error handling.
    
    Args:
        data: Data to save
        file_path (str): Path to save the JSON file
        encoding (str): File encoding (default: utf-8)
        indent (int): JSON indentation (default: 2)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except (OSError, TypeError, ValueError) as e:
        return False


def load_private_settings():
    """
    Load private settings from ~/.cato/settings.json in an OS-compatible way.
    
    This function constructs the path to ~/.cato/settings.json using os.path methods
    for cross-platform compatibility (Windows, Mac, Linux).
    
    Returns:
        dict: The privateCommands section from the settings file, or empty dict if not found
    """
    # Use os.path.join for OS-compatible path construction
    cato_dir = os.path.join(os.path.expanduser("~"), ".cato")
    settings_file = os.path.join(cato_dir, "settings.json")
    
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            return settings.get('privateCommands', {})
    except (FileNotFoundError, json.JSONDecodeError, KeyError, OSError):
        return {}


def ensure_directory_exists(directory_path):
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        directory_path (str): Path to the directory
        
    Returns:
        bool: True if directory exists or was created successfully
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return True
    except OSError:
        return False
