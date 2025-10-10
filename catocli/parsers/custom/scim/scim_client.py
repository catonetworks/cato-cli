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

    def __init__(self, scim_url=None, scim_token=None, log_level='WARNING', verify_ssl=True, verbose=False):
        """
        Initialize a Cato SCIM client object.

        Args:
            scim_url: The SCIM service URL (from profile or environment)
            scim_token: The Bearer token for SCIM authentication (from profile or environment)
            log_level: Logging level as string
            verify_ssl: Controls SSL certificate verification
            verbose: Whether to print detailed request/response information
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
        self.verbose = verbose
        self.call_count = 0
        
        # Parse accountId and sourceId from the SCIM URL
        self.account_id, self.source_id = self._parse_scim_url(self.baseurl)
        
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
                stacklevel=2
            )
            logger.warning("SSL certificate verification is disabled - this is insecure!")
        
        logger.debug(f"Initialized CatoSCIMClient with baseurl: {self.baseurl}")
        logger.debug(f"Parsed accountId: {self.account_id}, sourceId: {self.source_id}")

    def _parse_scim_url(self, scim_url):
        """
        Parse accountId and sourceId from SCIM URL.
        
        Args:
            scim_url: SCIM URL in format https://scimservice.catonetworks.com:4443/scim/v2/{accountId}/{sourceId}
        
        Returns:
            tuple: (account_id, source_id)
        
        Raises:
            ValueError: If URL format is invalid
        """
        if not scim_url:
            raise ValueError("SCIM URL is required")
        
        try:
            parsed = urllib.parse.urlparse(scim_url)
            path_parts = parsed.path.strip('/').split('/')
            
            # Expected path: ['scim', 'v2', 'accountId', 'sourceId']
            if len(path_parts) < 4 or path_parts[0] != 'scim' or path_parts[1] != 'v2':
                raise ValueError(
                    f"Invalid SCIM URL format. Expected: https://scimservice.catonetworks.com:4443/scim/v2/{{accountId}}/{{sourceId}}, "
                    f"got: {scim_url}"
                )
            
            account_id = path_parts[2]
            source_id = path_parts[3]
            
            # Validate that they are numeric (optional, but helpful for catching errors)
            try:
                int(account_id)
                int(source_id)
            except ValueError:
                logger.warning(f"Non-numeric accountId ({account_id}) or sourceId ({source_id}) in SCIM URL: {scim_url}")
            
            return account_id, source_id
            
        except (IndexError, AttributeError) as e:
            raise ValueError(
                f"Failed to parse SCIM URL: {scim_url}. "
                f"Expected format: https://scimservice.catonetworks.com:4443/scim/v2/{{accountId}}/{{sourceId}}"
            ) from e

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
        
        # Prepare request body
        body = None
        if request_data is not None:
            logger.debug(f'Request data: {request_data}')
            body = json.dumps(request_data).encode('ascii')

        # Construct the request headers
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        
        # Print verbose request information
        if self.verbose:
            print(f"\n SCIM API Request:", file=sys.stderr)
            print(f"   Method: {method}", file=sys.stderr)
            print(f"   URL: {self.baseurl + path}", file=sys.stderr)
            print(f"   Headers: Authorization: Bearer *****, Content-Type: application/json", file=sys.stderr)
            if request_data:
                print(f"   Request Payload:", file=sys.stderr)
                print(f"   {json.dumps(request_data, indent=2, ensure_ascii=False)}", file=sys.stderr)
            else:
                print(f"   Request Payload: (none)", file=sys.stderr)

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
            response_json = json.loads(result_data.decode('utf-8', 'replace')) if result_data != b'' else {}
            
            # Print verbose response information
            if self.verbose:
                print(f"\n SCIM API Response:", file=sys.stderr)
                print(f"   Status: {response.status} {response.reason}", file=sys.stderr)
                print(f"   Response Payload:", file=sys.stderr)
                print(f"   {json.dumps(response_json, indent=2, ensure_ascii=False)}", file=sys.stderr)
            
            return True, response_json
            
        except HTTPError as e:
            error_body = e.read().decode('utf-8', 'replace')
            error_response = {"status": e.code, "error": error_body}
            
            # Print verbose error response information
            if self.verbose:
                print(f"\n SCIM API Error Response:", file=sys.stderr)
                print(f"   Status: {e.code} {e.reason}", file=sys.stderr)
                print(f"   Error Response:", file=sys.stderr)
                try:
                    error_json = json.loads(error_body)
                    print(f"   {json.dumps(error_json, indent=2, ensure_ascii=False)}", file=sys.stderr)
                except json.JSONDecodeError:
                    print(f"   {error_body}", file=sys.stderr)
            
            return False, error_response
            
        except URLError as e:
            error_response = {"reason": e.reason, "error": str(e)}
            
            if self.verbose:
                print(f"\n SCIM API Connection Error:", file=sys.stderr)
                print(f"   Error: {str(e)}", file=sys.stderr)
            
            logger.error(f'Error sending request: {e}')
            return False, error_response
            
        except Exception as e:
            error_response = {"error": str(e)}
            
            if self.verbose:
                print(f"\n SCIM API Unexpected Error:", file=sys.stderr)
                print(f"   Error: {str(e)}", file=sys.stderr)
            
            logger.error(f'Error sending request: {e}')
            return False, error_response

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
            "externalId": externalId
        }
        
        # Cato SCIM API requires users to be created as active first
        # For inactive users, we create them as active then disable them
        data["active"] = True  # Always create as active initially
        if password is not None:
            data["password"] = new_password
        
        # Debug logging to see what we're sending
        logger.debug(f'Sending user data: {json.dumps(data, indent=2)}')
        logger.info(f'Creating user {email} (requested active: {active})')
        
        # Send the request to create the user
        success, result = self.send("POST", "/Users", data)
        
        # If user creation succeeded but should be inactive, disable them
        if success and not active:
            user_id = result.get('id')
            if user_id:
                logger.info(f'Disabling user {email} (id: {user_id}) as requested')
                disable_success, disable_result = self.disable_user(user_id)
                if not disable_success:
                    logger.warning(f'User {email} created but failed to disable: {disable_result}')
                    # Still return success for user creation, but add a warning to the result
                    result['warning'] = f'User created as active but could not be disabled: {disable_result}'
        
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
            field: Field to search (userName, email, givenName, familyName, externalId)
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
            api_url = f'/Users?filter={filter_string}&startIndex={len(users)}'
            logger.debug(f'SCIM API call: GET {api_url} (filter: {field} eq "{value}")')
            success, response = self.send("GET", api_url)
            if not success:
                logger.error(f'Error retrieving users: {response}')
                return False, response
            
            logger.debug(f'SCIM API response: success={success}, totalResults={response.get("totalResults", "unknown")}, resourcesCount={len(response.get("Resources", []))}')

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

    def get_user(self, userid, excluded_attributes=None):
        """
        Gets a user by their ID.
        
        Args:
            userid: SCIM user ID to retrieve
            excluded_attributes: Optional comma-separated list of attributes to exclude
        
        Returns:
            Tuple of (success_boolean, user_data)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Getting user: {userid}')
        
        # Build query parameters if excluded_attributes is provided
        path = f'/Users/{userid}'
        if excluded_attributes:
            path += f'?excludedAttributes={urllib.parse.quote(excluded_attributes)}'
        
        return self.send("GET", path)

    def get_users(self, count=None, start_index=None, params=None):
        """
        Returns users with optional pagination and filtering support.
        
        Args:
            count: Optional maximum number of users to return
            start_index: Optional starting index for pagination (1-based)
            params: Optional additional query parameters
        
        Returns:
            Tuple of (success_boolean, list_of_users_or_paginated_response)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info('Fetching users')
        
        # If specific pagination parameters are provided, return paginated response
        if count is not None or start_index is not None:
            # Build query parameters
            query_params = []
            if count is not None:
                query_params.append(f'count={count}')
            if start_index is not None:
                query_params.append(f'startIndex={start_index}')
            
            # Add any additional params
            if params and isinstance(params, dict):
                for key, value in params.items():
                    query_params.append(f'{key}={urllib.parse.quote(str(value))}')
            
            query_string = '&'.join(query_params)
            path = f'/Users?{query_string}' if query_string else '/Users'
            
            logger.debug(f'Sending paginated users request: {path}')
            success, response = self.send("GET", path)
            
            if success:
                # Return the full paginated response format
                return True, response
            else:
                logger.error(f'Error retrieving users: {response}')
                return False, response
        
        # Default behavior: fetch all users (backward compatibility)
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
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Updating user {userid}')

        if user_data is None:
            raise ValueError("user_data is required")

        # Send the request
        success, result = self.send("PUT", f'/Users/{userid}', user_data)
        return success, result

    def patch_user(self, user_id, patch_request):
        """
        Patch a SCIM user with partial updates (PATCH operation).
        
        Args:
            user_id: SCIM user ID to patch
            patch_request: PatchRequestDTO containing Operations array
        
        Returns:
            Tuple of (success_boolean, response_data)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Patching user {user_id} in account {self.account_id}, source {self.source_id}')

        # The SCIM API expects the full path format: /scim/v2/{accountId}/{sourceId}/Users/{id}
        # But our base URL already includes the /scim/v2/{accountId}/{sourceId} part,
        # so we just need to append /Users/{user_id}
        path = f'/Users/{user_id}'
        success, result = self.send("PATCH", path, patch_request)
        return success, result

    def delete_user(self, user_id):
        """
        Delete a SCIM user (DELETE operation).
        
        Args:
            user_id: SCIM user ID to delete
        
        Returns:
            Tuple of (success_boolean, response_data)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Deleting user {user_id} in account {self.account_id}, source {self.source_id}')

        # The SCIM API expects the full path format: /scim/v2/{accountId}/{sourceId}/Users/{id}
        # But our base URL already includes the /scim/v2/{accountId}/{sourceId} part,
        # so we just need to append /Users/{user_id}
        path = f'/Users/{user_id}'
        success, result = self.send("DELETE", path)
        return success, result

    def patch_group(self, group_id, patch_request):
        """
        Patch a SCIM group with partial updates (PATCH operation).
        
        Args:
            group_id: SCIM group ID to patch
            patch_request: PatchRequestDTO containing Operations array
        
        Returns:
            Tuple of (success_boolean, response_data)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Patching group {group_id} in account {self.account_id}, source {self.source_id}')

        # The SCIM API expects the full path format: /scim/v2/{accountId}/{sourceId}/Groups/{id}
        # But our base URL already includes the /scim/v2/{accountId}/{sourceId} part,
        # so we just need to append /Groups/{group_id}
        path = f'/Groups/{group_id}'
        success, result = self.send("PATCH", path, patch_request)
        return success, result

    def delete_group(self, group_id):
        """
        Delete a SCIM group (DELETE operation).
        
        Args:
            group_id: SCIM group ID to delete
        
        Returns:
            Tuple of (success_boolean, response_data)
        
        Note:
            accountId and sourceId are automatically extracted from the SCIM URL in credentials
        """
        logger.info(f'Deleting group {group_id} in account {self.account_id}, source {self.source_id}')

        # The SCIM API expects the full path format: /scim/v2/{accountId}/{sourceId}/Groups/{id}
        # But our base URL already includes the /scim/v2/{accountId}/{sourceId} part,
        # so we just need to append /Groups/{group_id}
        path = f'/Groups/{group_id}'
        success, result = self.send("DELETE", path)
        return success, result

    def find_users_by_external_ids(self, external_ids):
        """
        Find multiple users by their external IDs in bulk.
        
        Note: The Cato SCIM API does not support filtering by externalId field,
        so we get all users and filter locally by externalId.
        
        Args:
            external_ids: List of external IDs to search for
        
        Returns:
            Tuple of (success_boolean, dict mapping external_id to user_id)
        """
        if not external_ids:
            return True, {}
        
        logger.info(f'Finding users by external IDs: {external_ids}')
        
        # Since the SCIM API doesn't support externalId filtering,
        # get all users and filter locally
        try:
            success, all_users = self.get_users()
            if not success:
                logger.error(f'Failed to get all users: {all_users}')
                return False, all_users
            
            logger.debug(f'Retrieved {len(all_users)} total users for external ID matching')
            
            # Build mapping from external_id to user_id
            user_map = {}
            external_ids_set = set(external_ids)  # For faster lookup
            
            for user in all_users:
                user_external_id = user.get('externalId')
                if user_external_id and user_external_id in external_ids_set:
                    user_id = user.get('id')
                    if user_id:
                        user_map[user_external_id] = user_id
                        logger.debug(f'Mapped external_id "{user_external_id}" -> user_id "{user_id}"')
            
            # Log results for each requested external_id
            for external_id in external_ids:
                if external_id in user_map:
                    logger.info(f'Found user {external_id} -> {user_map[external_id]}')
                else:
                    logger.warning(f'User with external_id "{external_id}" not found')
            
            logger.info(f'User lookup complete: found {len(user_map)}/{len(external_ids)} users')
            return True, user_map
            
        except Exception as e:
            logger.error(f'Error in bulk external_id lookup: {e}')
            return False, str(e)


def get_scim_client(profile_name=None, verbose=False):
    """
    Get a configured SCIM client using credentials from the specified profile.
    
    Args:
        profile_name: Profile to use (defaults to current active profile)
        verbose: Whether to enable verbose request/response logging
    
    Returns:
        CatoSCIMClient instance or None if configuration is missing/invalid
    """
    try:
        pm = get_profile_manager()
        credentials = pm.get_credentials(profile_name)
        
        if not credentials:
            logger.error(f"Profile not found: {profile_name or pm.get_current_profile()}")
            return None
        
        scim_url = credentials.get('scim_url')
        scim_token = credentials.get('scim_token')
        
        if not scim_url or not scim_token:
            current_profile = profile_name or pm.get_current_profile()
            logger.error(
                f"Profile '{current_profile}' is missing SCIM credentials. "
                f"Run 'catocli configure set --profile {current_profile}' to add SCIM URL and Bearer token."
            )
            return None
        
        return CatoSCIMClient(scim_url=scim_url, scim_token=scim_token, verbose=verbose)
    
    except Exception as e:
        logger.error(f"Error initializing SCIM client: {e}")
        return None
