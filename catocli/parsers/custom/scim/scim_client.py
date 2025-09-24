#!/usr/bin/env python3
"""
SCIM client wrapper for Cato CLI integration
Wraps the CatoSCIM functionality and integrates with CLI credential management
"""

import csv
import datetime
import json
import logging
import os
import secrets
import ssl
import string
import sys
import time
import urllib.parse
import urllib.request
import warnings
from urllib.error import HTTPError, URLError
from ....Utils.profile_manager import get_profile_manager


# Set up module-level logger
logger = logging.getLogger(__name__)


class CatoSCIMClient:
    """
    CatoSCIM client wrapper for Cato CLI
    
    Wraps the original CatoSCIM functionality and integrates with the CLI's
    credential management system.
    """

    def __init__(self, scim_url=None, scim_token=None, log_level='WARNING', verify_ssl=True):
        """
        Initialize a Cato SCIM client object.

        Args:
            scim_url: The SCIM service URL (from profile or environment)
            scim_token: The Bearer token for SCIM authentication (from profile or environment)
            log_level: Logging level as string
            verify_ssl: Controls SSL certificate verification
        """
        
        # Get credentials from profile if not provided
        if not scim_url or not scim_token:
            pm = get_profile_manager()
            credentials = pm.get_credentials()
            if credentials:
                scim_url = scim_url or credentials.get('scim_url')
                scim_token = scim_token or credentials.get('scim_token')
        
        # Also check environment variables as fallback
        self.baseurl = scim_url or os.environ.get('CATO_SCIM_URL')
        self.token = scim_token or os.environ.get('CATO_SCIM_TOKEN')
        
        if not self.baseurl:
            raise ValueError(
                "SCIM URL must be provided in profile or via CATO_SCIM_URL environment variable.\n"
                "Run 'catocli configure set' to add SCIM credentials to your profile.\n"
                "For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps"
            )
        if not self.token:
            raise ValueError(
                "SCIM Bearer token must be provided in profile or via CATO_SCIM_TOKEN environment variable.\n"
                "Run 'catocli configure set' to add SCIM credentials to your profile.\n"
                "For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps"
            )
        
        self.verify_ssl = verify_ssl
        self.call_count = 0
        
        # Configure module logger
        if isinstance(log_level, int):
            # Backwards compatibility: 0=CRITICAL+1, 1=ERROR, 2=INFO, 3=DEBUG
            level_map = {0: logging.CRITICAL + 1, 1: logging.ERROR, 2: logging.INFO, 3: logging.DEBUG}
            logger.setLevel(level_map.get(log_level, logging.DEBUG))
        else:
            logger.setLevel(getattr(logging, log_level.upper(), logging.WARNING))
        
        # Issue security warning if SSL verification is disabled
        if not self.verify_ssl:
            warnings.warn(
                "SSL certificate verification is disabled. This is INSECURE and should "
                "only be used in development environments. Never disable SSL verification "
                "in production!",
                SecurityWarning,
                stacklevel=2
            )
            logger.warning("SSL certificate verification is disabled - this is insecure!")
        
        logger.debug(f"Initialized CatoSCIMClient with baseurl: {self.baseurl}")

    def send(self, method="GET", path="/", request_data=None):
        """
        Makes a REST request to the SCIM API.

        Args:
            method: HTTP method to use (GET, POST, PUT, PATCH, DELETE)
            path: Path to the REST command being called, e.g. "/Users"
            request_data: Optional JSON format message body for POST, PUT, PATCH

        Returns:
            Tuple where the first element is a Boolean success flag,
            and the second element is the response data or error information.
        """
        logger.info(f'Sending {method} request to {path}')
        body = None
        if request_data is not None:
            logger.debug(f'Request data: {request_data}')
            body = json.dumps(request_data).encode('ascii')

        # Construct the request headers
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        # Create and send the request
        try:
            request = urllib.request.Request(
                url=self.baseurl + path,
                headers=headers,
                method=method,
                data=body
            )
            self.call_count += 1
            
            # Handle SSL verification based on configuration
            if self.verify_ssl:
                # Use default SSL verification (secure)
                response = urllib.request.urlopen(request)
            else:
                # Disable SSL verification (development only)
                logger.warning("SSL verification disabled - this is insecure!")
                context = ssl._create_unverified_context()
                response = urllib.request.urlopen(request, context=context)
            
            result_data = response.read()
        except HTTPError as e:
            body = e.read().decode('utf-8', 'replace')
            return False, {"status": e.code, "error": body}
        except URLError as e:
            logger.error(f'Error sending request: {e}')
            return False, {"reason": e.reason, "error": str(e)}
        except Exception as e:
            logger.error(f'Error sending request: {e}')
            return False, {"error": str(e)}
        
        logger.debug(f'Response data: {result_data}')
        if result_data == b'':  # DELETE returns an empty response
            result_data = b'{}'
        return True, json.loads(result_data.decode('utf-8', 'replace'))

    def add_members(self, groupid, members):
        """
        Adds multiple members to an existing group.
        
        Args:
            groupid: SCIM group ID to add members to
            members: List of member dictionaries with 'value' field containing user IDs
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Adding members to group {groupid}')

        # Create the data object
        data = {
            "schemas": [
                "urn:ietf:params:scim:api:messages:2.0:PatchOp"
            ],
            "Operations": [
                {
                    "op": "add",
                    "path": "members",
                    "value": members
                }
            ]
        }
        
        # Send the request
        success, result = self.send("PATCH", f'/Groups/{groupid}', data)
        return success, result

    def create_group(self, displayName, externalId, members=None):
        """
        Creates a new group.
        
        Args:
            displayName: Display name for the group
            externalId: External ID for the group
            members: Optional list of member dictionaries
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Creating group: {displayName} (externalId: {externalId})')

        # Handle mutable default argument safely
        if members is None:
            members = []

        # Create the data object
        data = {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": displayName,
            "externalId": externalId,
            "members": members
        }

        # Send the request
        success, result = self.send("POST", "/Groups", data)
        return success, result

    def create_user(self, email, givenName, familyName, externalId, password=None, active=True):
        """
        Creates a new user.
        
        Args:
            email: Email address for the user
            givenName: Given name (first name)
            familyName: Family name (last name)
            externalId: External ID for the user
            password: Optional password (random one generated if not provided)
            active: Whether user should be active
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Creating user: {email}')

        # Generate a strong password if none supplied
        if password is None:
            new_password = ""
            for i in range(10):
                new_password += secrets.choice(string.ascii_letters + string.digits)
        else:
            new_password = password

        # Create the data object
        data = {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
            ],
            "userName": email,
            "name": {
                "givenName": givenName,
                "familyName": familyName
            },
            "emails": [
                {
                    "primary": True,
                    "value": email
                }
            ],
            "externalId": externalId,
            "password": new_password,
            "active": active
        }

        # Send the request
        success, result = self.send("POST", "/Users", data)
        return success, result

    def disable_group(self, groupid):
        """
        Disables the group matching the given groupid.
        
        Args:
            groupid: SCIM group ID to disable
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Disabling group: {groupid}')
        return self.send("DELETE", f'/Groups/{groupid}')

    def disable_user(self, userid):
        """
        Disables the user matching the given userid.
        
        Args:
            userid: SCIM user ID to disable
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Disabling user: {userid}')
        return self.send("DELETE", f'/Users/{userid}')

    def find_group(self, displayName):
        """
        Returns groups matching the given display name.
        
        Args:
            displayName: Display name to search for
        
        Returns:
            Tuple of (success_boolean, list_of_groups)
        """
        logger.info(f'Finding group by name: {displayName}')
        groups = []
        iteration = 0
        while True:
            # Send the query and bail if error
            iteration += 1
            filter_string = urllib.parse.quote(f'displayName eq "{displayName}"')
            success, response = self.send("GET", f'/Groups?filter={filter_string}&startIndex={len(groups)}')
            if not success:
                logger.error(f'Error retrieving groups: {response}')
                return False, response

            logger.debug(f'Group search iteration {iteration}: current={len(groups)}, received={len(response["Resources"])}, total={response["totalResults"]}')

            # Add new groups to the list
            for group in response["Resources"]:
                groups.append(group)

            # Check for stop condition
            if len(groups) >= response["totalResults"]:
                break

        return True, groups

    def find_users(self, field, value):
        """
        Returns users matching the given field and value.
        
        Args:
            field: Field to search (userName, email, givenName, familyName)
            value: Value to search for
        
        Returns:
            Tuple of (success_boolean, list_of_users)
        """
        logger.info(f'Finding users by {field}: {value}')
        users = []
        iteration = 0
        while True:
            # Send the query and bail if error
            iteration += 1
            filter_string = urllib.parse.quote(f'{field} eq "{value}"')
            success, response = self.send("GET", f'/Users?filter={filter_string}&startIndex={len(users)}')
            if not success:
                logger.error(f'Error retrieving users: {response}')
                return False, response

            logger.debug(f'User search iteration {iteration}: current={len(users)}, received={len(response["Resources"])}, total={response["totalResults"]}')

            # Add new users to the list
            for user in response["Resources"]:
                users.append(user)

            # Check for stop condition
            if len(users) >= response["totalResults"]:
                break

        return True, users

    def get_group(self, groupid):
        """
        Gets a group by their ID.
        
        Args:
            groupid: SCIM group ID to retrieve
        
        Returns:
            Tuple of (success_boolean, group_data)
        """
        logger.info(f'Getting group: {groupid}')
        return self.send("GET", f'/Groups/{groupid}')

    def get_groups(self):
        """
        Returns all groups.
        
        Returns:
            Tuple of (success_boolean, list_of_groups)
        """
        logger.info('Fetching all groups')
        groups = []
        iteration = 0
        while True:
            # Send the query and bail if error
            iteration += 1
            success, response = self.send("GET", f'/Groups?startIndex={len(groups)}')
            if not success:
                logger.error(f'Error retrieving groups: {response}')
                return False, response

            logger.debug(f'Groups fetch iteration {iteration}: current={len(groups)}, received={len(response["Resources"])}, total={response["totalResults"]}')

            # Add new groups to the list
            for group in response["Resources"]:
                groups.append(group)

            # Check for stop condition
            if len(groups) >= response["totalResults"]:
                break

        return True, groups

    def get_user(self, userid):
        """
        Gets a user by their ID.
        
        Args:
            userid: SCIM user ID to retrieve
        
        Returns:
            Tuple of (success_boolean, user_data)
        """
        logger.info(f'Getting user: {userid}')
        return self.send("GET", f'/Users/{userid}')

    def get_users(self):
        """
        Returns all users.
        
        Returns:
            Tuple of (success_boolean, list_of_users)
        """
        logger.info('Fetching all users')
        users = []
        iteration = 0
        while True:
            # Send the query and bail if error
            iteration += 1
            success, response = self.send("GET", f'/Users?startIndex={len(users)}')
            if not success:
                logger.error(f'Error retrieving users: {response}')
                return False, response

            logger.debug(f'Users fetch iteration {iteration}: current={len(users)}, received={len(response["Resources"])}, total={response["totalResults"]}')

            # Add new users to the list
            for user in response["Resources"]:
                users.append(user)

            # Check for stop condition
            if len(users) >= response["totalResults"]:
                break

        return True, users

    def remove_members(self, groupid, members):
        """
        Removes multiple members from an existing group.
        
        Args:
            groupid: SCIM group ID to remove members from
            members: List of member dictionaries with 'value' field containing user IDs
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Removing members from group {groupid}')

        # Create the data object
        data = {
            "schemas": [
                "urn:ietf:params:scim:api:messages:2.0:PatchOp"
            ],
            "Operations": [
                {
                    "op": "remove",
                    "path": "members",
                    "value": members
                }
            ]
        }
        
        # Send the request
        success, result = self.send("PATCH", f'/Groups/{groupid}', data)
        return success, result

    def rename_group(self, groupid, new_name):
        """
        Renames an existing group.
        
        Args:
            groupid: SCIM group ID to rename
            new_name: New display name for the group
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Renaming group {groupid}')

        # Create the data object
        data = {
            "schemas": [
                "urn:ietf:params:scim:api:messages:2.0:PatchOp"
            ],
            "Operations": [
                {
                    "op": "replace",
                    "path": "displayName",
                    "value": new_name
                }
            ]
        }
        
        # Send the request
        success, result = self.send("PATCH", f'/Groups/{groupid}', data)
        return success, result

    def update_group(self, groupid, group_data):
        """
        Updates an existing group with complete group data.
        
        Args:
            groupid: SCIM group ID to update
            group_data: Complete group JSON data as Python dictionary
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Updating group {groupid}')

        # Send the request
        success, result = self.send("PUT", f'/Groups/{groupid}', group_data)
        return success, result

    def update_user(self, userid, user_data):
        """
        Updates an existing user with complete user data.
        
        Args:
            userid: SCIM user ID to update
            user_data: Complete user JSON data as Python dictionary
        
        Returns:
            Tuple of (success_boolean, response_data)
        """
        logger.info(f'Updating user {userid}')

        # Send the request
        success, result = self.send("PUT", f'/Users/{userid}', user_data)
        return success, result


def get_scim_client(profile_name=None):
    """
    Get a configured SCIM client using credentials from the specified profile.
    
    Args:
        profile_name: Profile to use (defaults to current active profile)
    
    Returns:
        CatoSCIMClient instance
    
    Raises:
        ValueError: If SCIM credentials are missing from profile
    """
    pm = get_profile_manager()
    credentials = pm.get_credentials(profile_name)
    
    if not credentials:
        raise ValueError(f"Profile not found: {profile_name or pm.get_current_profile()}")
    
    scim_url = credentials.get('scim_url')
    scim_token = credentials.get('scim_token')
    
    if not scim_url or not scim_token:
        current_profile = profile_name or pm.get_current_profile()
        raise ValueError(
            f"Profile '{current_profile}' is missing SCIM credentials.\n"
            f"Run 'catocli configure set --profile {current_profile}' to add SCIM URL and Bearer token.\n"
            f"For more information, see: https://support.catonetworks.com/hc/en-us/articles/29492743031581-Using-the-Cato-SCIM-API-for-Custom-SCIM-Apps"
        )
    
    return CatoSCIMClient(scim_url=scim_url, scim_token=scim_token)
