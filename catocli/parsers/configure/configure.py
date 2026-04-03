#!/usr/bin/env python3
"""
Configure command implementation for Cato CLI
Implements profile creation, listing, switching, and management
"""

import getpass
import sys
import json
from graphql_client import Configuration
from graphql_client.api_client import ApiException
from graphql_client.api.call_api import ApiClient, CallApi
from ...Utils.profile_manager import get_profile_manager
from ...Utils.cliutils import load_private_settings


def test_credentials(endpoint, cato_token, account_id):
    """Test credentials by making an entityLookup API call"""
    try:
        print("Testing credentials...")
        
        # Create a temporary configuration
        test_config = Configuration()
        test_config.verify_ssl = False
        test_config.debug = False
        test_config.version = "1.0.0"  # Required for API client
        test_config.api_key["x-api-key"] = cato_token
        test_config.host = endpoint
        test_config.accountID = account_id
        
        # Make a simple entityLookup call to test credentials
        instance = CallApi(ApiClient(test_config))
        response = instance.call_api({
            "query": "query entityLookup($accountID: ID!, $type: EntityType!) { entityLookup(accountID: $accountID, type: $type) { items { entity { id name } } } }",
            "variables": {"accountID": account_id, "type": "country"}
        }, {})
        result = response[0] if response else None
        
        # Check if the call was successful
        if result and result.get('data') is not None:
            print("✓ Credentials validated successfully")
            return True, "Credentials are valid"
        elif result and result.get('errors'):
            error_msg = result['errors'][0].get('message', 'Unknown API error')
            return False, f"API error: {error_msg}"
        elif result is None:
            return False, "No response from API"
        else:
            return False, f"Invalid API response: {result}"
            
    except ApiException as e:
        if e.status == 401:
            return False, "Invalid API token"
        elif e.status == 403:
            return False, "Access denied - check account ID and permissions"
        else:
            return False, f"API error (status {e.status}): {str(e)}"
    except Exception as e:
        return False, f"Connection error: {str(e)}"


def configure_profile(args, configuration=None):
    """Configure a profile with credentials"""
    pm = get_profile_manager()
    profile_name = args.profile
    
    # Check if private settings exist (for cookie and private_endpoint options)
    private_settings_exist = bool(load_private_settings())

    try:
        # Check if any credential arguments were provided
        has_credential_args = (
            args.cato_token or args.account_id or args.endpoint or
            args.scim_url or args.scim_token or
            (private_settings_exist and (getattr(args, 'cookie', None) or getattr(args, 'private_endpoint', None)))
        )

        # Interactive mode
        if args.interactive or not has_credential_args:
            print(f"Configuring profile '{profile_name}'")
            print("Leave blank to keep existing values (if any)")
            print()

            # Get current values if profile exists
            current_config = pm.get_profile_config(profile_name) or {}

            # Get endpoint
            current_endpoint = current_config.get('endpoint', pm.default_endpoint)
            endpoint_input = input(f"Cato API Endpoint [{current_endpoint}]: ").strip()
            endpoint = endpoint_input if endpoint_input else current_endpoint

            # Get token
            current_token = current_config.get('cato_token', '')
            if current_token:
                token_prompt = f"Cato API Token [****{current_token[-4:]}]: "
            else:
                token_prompt = "Cato API Token: "
            token_input = getpass.getpass(token_prompt).strip()
            cato_token = token_input if token_input else current_token

            # Get account ID
            current_account = current_config.get('account_id', '')
            account_input = input(f"Account ID [{current_account}]: ").strip()
            account_id = account_input if account_input else current_account

            # SCIM credentials (optional)
            print()
            print("SCIM Credentials (optional - for SCIM API operations):")
            print("For SCIM setup guide: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps")

            # Get SCIM URL
            current_scim_url = current_config.get('scim_url', '')
            if current_scim_url:
                scim_url_input = input(f"SCIM URL [****{current_scim_url[-20:]}]: ").strip()
            else:
                scim_url_input = input("SCIM URL (e.g., https://scimservice.catonetworks.com:4443/scim/v2/accountId/sourceId): ").strip()
            scim_url = scim_url_input if scim_url_input else current_scim_url

            # Get SCIM token
            current_scim_token = current_config.get('scim_token', '')
            if current_scim_token:
                scim_token_prompt = f"SCIM Bearer Token [****{current_scim_token[-4:]}]: "
            else:
                scim_token_prompt = "SCIM Bearer Token: "
            scim_token_input = getpass.getpass(scim_token_prompt).strip()
            scim_token = scim_token_input if scim_token_input else current_scim_token

            # Private API credentials (only if settings.json exists)
            cookie = None
            private_endpoint = None
            if private_settings_exist:
                print()
                print("Private API Credentials (optional - for private API operations):")

                # Get cookie
                current_cookie = current_config.get('cookie', '')
                if current_cookie:
                    cookie_input = input(f"Session Cookie [****{current_cookie[-20:]}]: ").strip()
                else:
                    cookie_input = input("Session Cookie (e.g., X-Cato-Session-Id=...): ").strip()
                cookie = cookie_input if cookie_input else current_cookie

                # Get private endpoint
                current_private_endpoint = current_config.get('private_endpoint', '')
                if current_private_endpoint:
                    pe_input = input(f"Private Endpoint [****{current_private_endpoint[-30:]}]: ").strip()
                else:
                    pe_input = input("Private Endpoint (e.g., https://yourcma.cc.catonetworks.com/api/v1/graphql): ").strip()
                private_endpoint = pe_input if pe_input else current_private_endpoint

        else:
            # Non-interactive mode
            endpoint = args.endpoint
            cato_token = getattr(args, 'cato_token', None)
            account_id = getattr(args, 'account_id', None)
            scim_url = getattr(args, 'scim_url', None)
            scim_token = getattr(args, 'scim_token', None)
            cookie = getattr(args, 'cookie', None) if private_settings_exist else None
            private_endpoint = getattr(args, 'private_endpoint', None) if private_settings_exist else None
        
        # Get current config to fill in missing values
        current_config = pm.get_profile_config(profile_name) or {}

        # Fill in missing values from current config
        if not cato_token:
            cato_token = current_config.get('cato_token')
        if not account_id:
            account_id = current_config.get('account_id')
        if not endpoint:
            endpoint = current_config.get('endpoint', pm.default_endpoint)
        if 'cookie' in locals() and not cookie:
            cookie = current_config.get('cookie')
        if 'private_endpoint' in locals() and not private_endpoint:
            private_endpoint = current_config.get('private_endpoint')

        # Check if we're only updating cookie/private_endpoint (no validation needed)
        only_updating_private = (
            private_settings_exist and
            (getattr(args, 'cookie', None) or getattr(args, 'private_endpoint', None)) and
            not args.cato_token and not args.account_id and not args.endpoint and
            not args.scim_url and not args.scim_token and not args.interactive
        )

        # Validate required fields for regular API operations (unless only updating private credentials)
        if not only_updating_private:
            if not cato_token:
                print("ERROR: Cato API token is required")
                return [{"success": False, "error": "Missing cato_token"}]

            if not account_id:
                print("ERROR: Account ID is required")
                return [{"success": False, "error": "Missing account_id"}]

            # Test credentials before saving (unless validation is skipped)
            if hasattr(args, 'skip_validation') and args.skip_validation:
                print("⚠️  Skipping credential validation")
            else:
                is_valid, error_message = test_credentials(endpoint, cato_token, account_id)
                if not is_valid:
                    print(f"ERROR: {error_message}")
                    print("Profile not saved. Please check your credentials and try again.")
                    print("(Use --skip-validation to save without testing)")
                    return [{"success": False, "error": f"Credential validation failed: {error_message}"}]

        # Create/update the profile
        success = pm.create_profile(
            profile_name=profile_name,
            endpoint=endpoint if endpoint else None,
            cato_token=cato_token if cato_token else None,
            account_id=account_id if account_id else None,
            scim_url=scim_url if 'scim_url' in locals() and scim_url else None,
            scim_token=scim_token if 'scim_token' in locals() and scim_token else None,
            cookie=cookie if 'cookie' in locals() and cookie else None,
            private_endpoint=private_endpoint if 'private_endpoint' in locals() and private_endpoint else None
        )
        
        if success:
            print(f"Profile '{profile_name}' configured successfully!")
            if profile_name == 'default' or len(pm.list_profiles()) == 1:
                pm.set_current_profile(profile_name)
                print(f"Set '{profile_name}' as the active profile")
        else:
            print(f"Failed to configure profile '{profile_name}'")
            return [{"success": False, "error": "Failed to create profile"}]
            
        return [{"success": True, "profile": profile_name}]
        
    except KeyboardInterrupt:
        print("\nOperation cancelled")
        return [{"success": False, "error": "Operation cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {e}")
        return [{"success": False, "error": str(e)}]


def list_profiles(args, configuration=None):
    """List all configured profiles"""
    pm = get_profile_manager()
    
    try:
        profiles = pm.list_profiles()
        current_profile = pm.get_current_profile()
        
        if not profiles:
            print("No profiles configured.")
            print("Run 'catocli configure set' to create your first profile.")
            return [{"success": True, "profiles": []}]
        
        print("Available profiles:")
        print()
        
        for profile in profiles:
            is_current = profile == current_profile
            status = " (current)" if is_current else ""
            
            config = pm.get_profile_config(profile)
            endpoint = config.get('endpoint', 'N/A')
            account_id = config.get('account_id', 'N/A')
            
            print(f"  {profile}{status}")
            print(f"    Endpoint:   {endpoint}")
            print(f"    Account ID: {account_id}")
            print()
        
        return [{"success": True, "profiles": profiles, "current": current_profile}]
        
    except Exception as e:
        print(f"ERROR: {e}")
        return [{"success": False, "error": str(e)}]


def set_profile(args, configuration=None):
    """Set the active profile"""
    pm = get_profile_manager()
    profile_name = args.profile
    
    try:
        # Check if profile exists
        if profile_name not in pm.list_profiles():
            print(f"ERROR: Profile '{profile_name}' does not exist.")
            print("Available profiles:")
            for p in pm.list_profiles():
                print(f"  {p}")
            return [{"success": False, "error": "Profile not found"}]
        
        # Validate profile has required credentials
        is_valid, message = pm.validate_profile(profile_name)
        if not is_valid:
            print(f"ERROR: {message}")
            print(f"Run 'catocli configure set --profile {profile_name}' to update the profile.")
            return [{"success": False, "error": message}]
        
        # Set as current profile
        pm.set_current_profile(profile_name)
        print(f"Switched to profile '{profile_name}'")
        
        return [{"success": True, "profile": profile_name}]
        
    except Exception as e:
        print(f"ERROR: {e}")
        return [{"success": False, "error": str(e)}]


def show_profile(args, configuration=None):
    """Show current profile configuration"""
    pm = get_profile_manager()
    
    try:
        profile_name = args.profile if hasattr(args, 'profile') and args.profile else pm.get_current_profile()
        
        # Check if profile exists
        config = pm.get_profile_config(profile_name)
        if not config:
            print(f"Profile '{profile_name}' not found.")
            return [{"success": False, "error": "Profile not found"}]
        
        print(f"Profile: {profile_name}")
        print(f"Endpoint:   {config.get('endpoint', 'N/A')}")
        print(f"Account ID: {config.get('account_id', 'N/A')}")
        
        # Show token status without revealing it
        token = config.get('cato_token', '')
        if token:
            print(f"Token:      ****{token[-4:]} (configured)")
        else:
            print("Token:      (not configured)")
            
        # Show SCIM credentials status
        print()
        print("SCIM Credentials:")
        scim_url = config.get('scim_url', '')
        if scim_url:
            print(f"SCIM URL:   ****{scim_url[-20:]} (configured)")
        else:
            print("SCIM URL:   (not configured)")

        scim_token = config.get('scim_token', '')
        if scim_token:
            print(f"SCIM Token: ****{scim_token[-4:]} (configured)")
        else:
            print("SCIM Token: (not configured)")

        # Show Private API credentials status
        print()
        print("Private API Credentials:")
        cookie = config.get('cookie', '')
        if cookie:
            print(f"Cookie:           ****{cookie[-20:]} (configured)")
        else:
            print("Cookie:           (not configured)")

        private_endpoint = config.get('private_endpoint', '')
        if private_endpoint:
            print(f"Private Endpoint: {private_endpoint}")
        else:
            print("Private Endpoint: (not configured)")

        # Show if this is the current profile
        current_profile = pm.get_current_profile()
        if profile_name == current_profile:
            print("Status:     Current active profile")
        else:
            print(f"Status:     Available (current: {current_profile})")
        
        # Create masked config for JSON output
        masked_config = config.copy()
        if masked_config.get('cato_token'):
            masked_config['cato_token'] = f"****{masked_config['cato_token'][-4:]}"
        
        return [{"success": True, "profile": profile_name, "config": masked_config}]
        
    except Exception as e:
        print(f"ERROR: {e}")
        return [{"success": False, "error": str(e)}]


def delete_profile(args, configuration=None):
    """Delete a profile"""
    pm = get_profile_manager()
    profile_name = args.profile
    
    try:
        # Check if profile exists
        if profile_name not in pm.list_profiles():
            print(f"Profile '{profile_name}' does not exist.")
            return [{"success": False, "error": "Profile not found"}]
        
        # Check if it's the current profile
        current_profile = pm.get_current_profile()
        if profile_name == current_profile:
            print(f"Cannot delete the current active profile '{profile_name}'.")
            print("Switch to another profile first using 'catocli configure use <profile>'")
            return [{"success": False, "error": "Cannot delete active profile"}]
        
        # Confirm deletion unless forced
        if not args.force:
            response = input(f"Are you sure you want to delete profile '{profile_name}'? (y/N): ").strip().lower()
            if response != 'y':
                print("Deletion cancelled.")
                return [{"success": False, "error": "Deletion cancelled by user"}]
        
        # Delete the profile
        success = pm.delete_profile(profile_name)
        if success:
            print(f"Profile '{profile_name}' deleted successfully.")
        else:
            print(f"Failed to delete profile '{profile_name}'.")
            return [{"success": False, "error": "Failed to delete profile"}]
        
        return [{"success": True, "deleted_profile": profile_name}]
        
    except Exception as e:
        print(f"ERROR: {e}")
        return [{"success": False, "error": str(e)}]
