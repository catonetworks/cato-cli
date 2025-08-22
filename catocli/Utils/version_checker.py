#!/usr/bin/env python3
"""
Version checking utility for Cato CLI
Checks for newer versions available on GitHub releases and PyPI
"""

import json
import urllib.request
import urllib.error
import ssl
import os
import time
from .. import __version__

# Cache settings
CACHE_FILE = os.path.expanduser("~/.catocli_version_cache")
CACHE_DURATION = 3600 * 4  # 4 hours in seconds

def get_cached_version_info():
    """Get cached version information if still valid"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'r') as f:
                cache_data = json.load(f)
            
            # Check if cache is still valid
            if time.time() - cache_data.get('timestamp', 0) < CACHE_DURATION:
                return cache_data.get('latest_version'), cache_data.get('source')
    except (json.JSONDecodeError, OSError):
        pass
    return None, None

def cache_version_info(latest_version, source):
    """Cache version information"""
    try:
        cache_data = {
            'latest_version': latest_version,
            'source': source,
            'timestamp': time.time()
        }
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache_data, f)
    except OSError:
        pass  # Fail silently if we can't write cache

def get_latest_github_version():
    """Get the latest version from GitHub releases"""
    try:
        # Create SSL context that doesn't verify certificates (for corporate networks)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        url = "https://api.github.com/repos/catonetworks/cato-cli/releases/latest"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', f'catocli/{__version__}')
        
        with urllib.request.urlopen(req, context=context, timeout=5) as response:
            data = json.loads(response.read().decode())
            tag_name = data.get('tag_name', '')
            # Remove 'v' prefix if present
            if tag_name.startswith('v'):
                tag_name = tag_name[1:]
            return tag_name
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, KeyError):
        return None

def get_latest_pypi_version():
    """Get the latest version from PyPI"""
    try:
        # Create SSL context that doesn't verify certificates (for corporate networks)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        url = "https://pypi.org/pypi/catocli/json"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', f'catocli/{__version__}')
        
        with urllib.request.urlopen(req, context=context, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data['info']['version']
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, KeyError):
        return None

def get_latest_version():
    """Get the latest version available from GitHub or PyPI"""
    # Check cache first
    cached_version, cached_source = get_cached_version_info()
    if cached_version:
        return cached_version, cached_source
    
    # Try GitHub first (usually more up-to-date for development releases)
    github_version = get_latest_github_version()
    if github_version:
        cache_version_info(github_version, 'GitHub')
        return github_version, 'GitHub'
    
    # Fall back to PyPI
    pypi_version = get_latest_pypi_version()
    if pypi_version:
        cache_version_info(pypi_version, 'PyPI')
        return pypi_version, 'PyPI'
    
    return None, None

def compare_versions(version1, version2):
    """Compare two version strings. Returns 1 if version1 > version2, -1 if version1 < version2, 0 if equal"""
    def version_tuple(v):
        # Convert version string to tuple of integers for comparison
        # Handle versions like "1.0.20", "1.0.20-beta", etc.
        parts = v.split('-')[0].split('.')  # Remove pre-release suffixes
        return tuple(int(x) for x in parts if x.isdigit())
    
    try:
        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)
        
        # Pad shorter version with zeros
        max_len = max(len(v1_tuple), len(v2_tuple))
        v1_tuple += (0,) * (max_len - len(v1_tuple))
        v2_tuple += (0,) * (max_len - len(v2_tuple))
        
        if v1_tuple > v2_tuple:
            return 1
        elif v1_tuple < v2_tuple:
            return -1
        else:
            return 0
    except (ValueError, AttributeError):
        return 0  # If we can't parse, assume they're equal

def is_newer_version_available():
    """Check if a newer version is available"""
    try:
        latest_version, source = get_latest_version()
        if latest_version:
            comparison = compare_versions(latest_version, __version__)
            return comparison > 0, latest_version, source
    except Exception:
        pass  # Fail silently for any version parsing errors
    
    return False, None, None

def show_upgrade_message(latest_version, source):
    """Display upgrade message to user"""
    print()
    print("─" * 60)
    print(f"🚀 A newer version of catocli is available!")
    print(f"   Current version: {__version__}")
    print(f"   Latest version:  {latest_version} (from {source})")
    print()
    if source == 'PyPI':
        print("   To upgrade, run:")
        print("   pip install --upgrade catocli")
    else:
        print("   To upgrade, run:")
        print("   pip install --upgrade catocli")
        print("   (or check GitHub releases for pre-release versions)")
    print("─" * 60)
    print()

def check_for_updates(show_if_available=True):
    """
    Check for updates and optionally show upgrade message
    
    Args:
        show_if_available (bool): Whether to show the upgrade message if update is available
    
    Returns:
        tuple: (is_newer_available, latest_version, source)
    """
    try:
        is_newer, latest_version, source = is_newer_version_available()
        
        if is_newer and show_if_available:
            show_upgrade_message(latest_version, source)
        
        return is_newer, latest_version, source
    except Exception:
        # Fail silently - don't interrupt the user's workflow
        return False, None, None

def force_check_updates():
    """Force check for updates by clearing cache"""
    try:
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
    except OSError:
        pass
    
    return check_for_updates(show_if_available=True)
