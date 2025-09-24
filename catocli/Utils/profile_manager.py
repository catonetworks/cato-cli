#!/usr/bin/env python3
"""
Profile management for Cato CLI authentication
Supports AWS CLI-style profiles with credentials stored in ~/.cato/credentials
"""

import os
import configparser
from pathlib import Path
import sys


class ProfileManager:
    """Manages Cato CLI profiles and credentials"""
    
    def __init__(self):
        self.cato_dir = Path.home() / '.cato'
        self.credentials_file = self.cato_dir / 'credentials'
        self.config_file = self.cato_dir / 'config'
        self.default_endpoint = "https://api.catonetworks.com/api/v1/graphql2"
        
    def ensure_cato_directory(self):
        """Ensure ~/.cato directory exists"""
        self.cato_dir.mkdir(mode=0o700, exist_ok=True)
        
    def get_profile_config(self, profile_name='default'):
        """Get configuration for a specific profile"""
        if not self.credentials_file.exists():
            return None
            
        config = configparser.ConfigParser()
        config.read(self.credentials_file)
        
        if profile_name not in config:
            return None
            
        profile_config = dict(config[profile_name])
        
        # Ensure required fields have defaults
        if 'endpoint' not in profile_config:
            profile_config['endpoint'] = self.default_endpoint
            
        return profile_config
    
    def list_profiles(self):
        """List all available profiles"""
        if not self.credentials_file.exists():
            return []
            
        config = configparser.ConfigParser()
        config.read(self.credentials_file)
        return list(config.sections())
    
    def create_profile(self, profile_name, endpoint=None, cato_token=None, account_id=None, scim_url=None, scim_token=None):
        """Create or update a profile"""
        self.ensure_cato_directory()
        
        config = configparser.ConfigParser()
        if self.credentials_file.exists():
            config.read(self.credentials_file)
        
        if profile_name not in config:
            config.add_section(profile_name)
        
        if endpoint:
            config[profile_name]['endpoint'] = endpoint
        elif 'endpoint' not in config[profile_name]:
            config[profile_name]['endpoint'] = self.default_endpoint
            
        if cato_token:
            config[profile_name]['cato_token'] = cato_token
            
        if account_id:
            config[profile_name]['account_id'] = account_id
        
        if scim_url:
            config[profile_name]['scim_url'] = scim_url
            
        if scim_token:
            config[profile_name]['scim_token'] = scim_token
        
        with open(self.credentials_file, 'w') as f:
            config.write(f)
        
        # Set secure permissions
        os.chmod(self.credentials_file, 0o600)
        
        return True
    
    def delete_profile(self, profile_name):
        """Delete a profile"""
        if not self.credentials_file.exists():
            return False
            
        config = configparser.ConfigParser()
        config.read(self.credentials_file)
        
        if profile_name not in config:
            return False
            
        config.remove_section(profile_name)
        
        with open(self.credentials_file, 'w') as f:
            config.write(f)
            
        return True
    
    def get_current_profile(self):
        """Get the current active profile name"""
        # Check environment variable first
        profile = os.getenv('CATO_PROFILE')
        if profile:
            return profile
            
        # Check config file
        if self.config_file.exists():
            config = configparser.ConfigParser()
            config.read(self.config_file)
            if 'default' in config and 'profile' in config['default']:
                return config['default']['profile']
        
        return 'default'
    
    def set_current_profile(self, profile_name):
        """Set the current active profile"""
        self.ensure_cato_directory()
        
        config = configparser.ConfigParser()
        if self.config_file.exists():
            config.read(self.config_file)
        
        if 'default' not in config:
            config.add_section('default')
            
        config['default']['profile'] = profile_name
        
        with open(self.config_file, 'w') as f:
            config.write(f)
            
        return True
    
    def get_credentials(self, profile_name=None):
        """Get credentials for the specified or current profile"""
        if profile_name is None:
            profile_name = self.get_current_profile()
            
        profile_config = self.get_profile_config(profile_name)
        if not profile_config:
            return None
            
        return {
            'endpoint': profile_config.get('endpoint', self.default_endpoint),
            'cato_token': profile_config.get('cato_token'),
            'account_id': profile_config.get('account_id'),
            'scim_url': profile_config.get('scim_url'),
            'scim_token': profile_config.get('scim_token')
        }
    
    def validate_profile(self, profile_name=None):
        """Validate that a profile has all required credentials"""
        credentials = self.get_credentials(profile_name)
        if not credentials:
            return False, f"Profile '{profile_name or self.get_current_profile()}' not found"
            
        missing = []
        if not credentials.get('cato_token'):
            missing.append('cato_token')
        if not credentials.get('account_id'):
            missing.append('account_id')
            
        if missing:
            return False, f"Profile missing required fields: {', '.join(missing)}"
            
        return True, "Profile is valid"
    
    def validate_scim_credentials(self, profile_name=None):
        """Validate that a profile has SCIM credentials"""
        credentials = self.get_credentials(profile_name)
        current_profile = profile_name or self.get_current_profile()
        
        if not credentials:
            return False, f"Profile '{current_profile}' not found"
            
        missing = []
        if not credentials.get('scim_url'):
            missing.append('scim_url')
        if not credentials.get('scim_token'):
            missing.append('scim_token')
            
        if missing:
            return False, (
                f"Profile '{current_profile}' is missing SCIM credentials: {', '.join(missing)}\n"
                f"Run 'catocli configure set --profile {current_profile}' to add SCIM credentials.\n"
                f"For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps"
            )
            
        return True, "SCIM credentials are valid"
    
    def migrate_from_environment(self):
        """Migrate from environment variables to default profile if needed"""
        cato_token = os.getenv('CATO_TOKEN')
        account_id = os.getenv('CATO_ACCOUNT_ID')
        
        if cato_token and account_id:
            # Check if default profile already exists
            default_config = self.get_profile_config('default')
            if not default_config:
                print("Migrating environment variables to default profile...")
                self.create_profile('default', 
                                 endpoint=self.default_endpoint,
                                 cato_token=cato_token, 
                                 account_id=account_id)
                return True
        return False


def get_profile_manager():
    """Get a ProfileManager instance"""
    return ProfileManager()
