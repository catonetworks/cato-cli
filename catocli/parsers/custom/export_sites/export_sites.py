import os
import json
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID

def export_socket_site_to_json(args, configuration):
    """
    Export consolidated site and socket data to JSON format
    """
    processed_data = {'sites':{}}
    
    try:
        account_id = getAccountID(args, configuration)
        # Get account snapshot with siteIDs if provided
        # Get siteIDs from args if provided (comma-separated string)
        site_ids = []
        if hasattr(args, 'siteIDs') and args.siteIDs:
            # Parse comma-separated string into list, removing whitespace
            site_ids = [site_id.strip() for site_id in args.siteIDs.split(',') if site_id.strip()]
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Filtering snapshot for site IDs: {site_ids}")
        
        ###############################################################
        ## Call APIs to retrieve sites, interface and network ranges ##
        ###############################################################
        snapshot_sites = getAccountSnapshot(args, configuration, account_id, site_ids)
        entity_network_interfaces = getEntityLookup(args, configuration, account_id, "networkInterface")
        entity_network_ranges = getEntityLookup(args, configuration, account_id, "siteRange")
        entity_sites = getEntityLookup(args, configuration, account_id, "site")
        
        ##################################################################
        ## Create processed_data object indexed by siteId with location ##
        ##################################################################
        for site_data in snapshot_sites:
            cur_site = {
                'wan_interfaces': {},
                'lan_interfaces': {},
            }
            site_id = site_data.get('id')
            cur_site['id'] = site_id
            cur_site['name'] = site_data.get('infoSiteSnapshot', {}).get('name')
            cur_site['description'] = site_data.get('infoSiteSnapshot', {}).get('description')
            cur_site['connectionType'] = site_data.get('infoSiteSnapshot', {}).get('connType')
            cur_site['type'] = site_data.get('infoSiteSnapshot', {}).get('type')
            cur_site = populateSiteLocationData(args, site_data, cur_site)

            site_interfaces = site_data.get('infoSiteSnapshot', {}).get('interfaces', [])
            for wan_ni in site_interfaces:
                cur_wan_interface = {}
                id = wan_ni.get('wanRoleInterfaceInfo', "")
                if id[0:3] == "wan":
                    cur_wan_interface['id'] = id
                    cur_wan_interface['name'] = wan_ni.get('name', "")
                    cur_wan_interface['upstreamBandwidth'] = wan_ni.get('upstreamBandwidth', 0)
                    cur_wan_interface['downstreamBandwidth'] = wan_ni.get('downstreamBandwidth', 0)
                    cur_wan_interface['destType'] = wan_ni.get('destType', "")
                    cur_site['wan_interfaces'][id] = cur_wan_interface

            if site_id:
                processed_data['sites'][site_id] = cur_site

        ##################################################################################
        ## Process entity lookup LAN network interfaces adding to site object by site_id##
        ##################################################################################
        for lan_ni in entity_network_interfaces:
            cur_lan_interface = {
                'network_ranges': {},
            }
            site_id = lan_ni.get("helperFields","").get('siteId', "")
            id = lan_ni.get('entity', "").get('id', "")
            interfaceName = lan_ni.get('entity', "").get('interfaceName', "")
            cur_lan_interface['id'] = id
            cur_lan_interface['name'] = interfaceName
            cur_lan_interface['index'] = lan_ni.get("helperFields","").get('interfaceId', "")
            cur_lan_interface['upstreamBandwidth'] = lan_ni.get('upstreamBandwidth', 0)
            cur_lan_interface['downstreamBandwidth'] = lan_ni.get('downstreamBandwidth', 0)
            cur_lan_interface['destType'] = lan_ni.get('destType', "")
            processed_data['sites'][site_id]['lan_interfaces'][interfaceName] = cur_lan_interface

        #############################################################################
        ## Process entity lookup network ranges populating by network interface id ##
        #############################################################################
        for range in entity_network_ranges:
            cur_range = {}
            site_id = lan_ni.get("helperFields","").get('siteId', "")
            id = lan_ni.get('entity', "").get('id', "")
            interface_name = lan_ni.get('entity', "").get('interfaceName', "")
            cur_lan_interface['id'] = id
            cur_lan_interface['subnet'] = lan_ni.get("helperFields","").get('subnet', "")
            cur_lan_interface['vlanTag'] = lan_ni.get("helperFields","").get('vlanTag', "")
            cur_lan_interface['microsegmentation'] = lan_ni.get("helperFields","").get('microsegmentation', "")
            
            processed_data['sites'][site_id]['lan_interfaces'][interface_name] = cur_range


        # Write the processed data to file using the general-purpose function
        output_file = writeDataToFile(
            data=processed_data,
            args=args,
            account_id=account_id,
            default_filename_template="socket_sites_{account_id}.json",
            default_directory="config_data"
        )
        
        return [{"success": True, "output_file": output_file, "account_id": account_id}]
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


##########################################################################
########################### Helper functions #############################
##########################################################################

def populateSiteLocationData(args, site_data, cur_site):
    # Load site location data for timezone and state code lookups
    site_location_data = {}
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(script_dir, '..', '..', '..', '..', 'models')
        location_file = os.path.join(models_dir, 'query.siteLocation.json')
        
        if os.path.exists(location_file):
            with open(location_file, 'r', encoding='utf-8') as f:
                site_location_data = json.load(f)
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Loaded {len(site_location_data)} location entries from {location_file}")
        else:
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Warning: Site location file not found at {location_file}")
    except Exception as e:
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Warning: Could not load site location data: {e}")

    ## siteLocation attributes
    cur_site['address'] = site_data.get('infoSiteSnapshot', {}).get('address')
    cur_site['city'] = site_data.get('infoSiteSnapshot', {}).get('cityName')                
    cur_site['stateName'] = site_data.get('infoSiteSnapshot', {}).get('countryStateName')
    cur_site['countryCode'] = site_data.get('infoSiteSnapshot', {}).get('countryCode')
    cur_site['countryName'] = site_data.get('infoSiteSnapshot', {}).get('countryName')

    # Look up timezone and state code from location data
    country_name = cur_site['countryName']
    state_name = cur_site['stateName']
    city = cur_site['city']

    # Create lookup key based on available data
    if state_name:
        lookup_key = f"{country_name}___{state_name}___{city}"
    else:
        lookup_key = f"{country_name}___{city}"
    
    # Debug output for lookup
    if hasattr(args, 'verbose') and args.verbose:
        print(f"Site {cur_site['name']}: Looking up '{lookup_key}'")

    # Look up location details
    location_data = site_location_data.get(lookup_key, {})
    
    if hasattr(args, 'verbose') and args.verbose:
        if location_data:
            print(f"  Found location data: {location_data}")
        else:
            print(f"  No location data found for key: {lookup_key}")
            # Try to find similar keys for debugging
            similar_keys = [k for k in site_location_data.keys() if country_name in k and (not city or city in k)][:5]
            if similar_keys:
                print(f"  Similar keys found: {similar_keys}")

    cur_site['stateCode'] = location_data.get('stateCode', None)

    # Get timezone - always use the 0 element in the timezones array
    timezones = location_data.get('timezone', [])
    cur_site['timezone'] = timezones[0] if timezones else None
    return cur_site

def getEntityLookup(args, configuration, account_id, entity_type):
    """
    Helper function to get entity lookup data for a specific entity type
    """
    #################################
    ## Get entity lookup for sites ##
    #################################
    entity_query = {
        "query": "query entityLookup ( $accountID:ID! $type:EntityType! $sortInput:[SortInput] $lookupFilterInput:[LookupFilterInput] ) { entityLookup ( accountID:$accountID type:$type sort:$sortInput filters:$lookupFilterInput ) { items { entity { id name type } description helperFields } total } }",
        "variables": {
            "accountID": account_id,
            "type": entity_type
        },
        "operationName": "entityLookup"
    }
    response = makeCall(args, configuration, entity_query)

    # Check for GraphQL errors in snapshot response
    if 'errors' in response:
        error_messages = [error.get('message', 'Unknown error') for error in response['errors']]
        raise Exception(f"Snapshot API returned errors: {', '.join(error_messages)}")
    
    if not response or 'data' not in response or 'entityLookup' not in response['data']:
        raise ValueError("Failed to retrieve snapshot data from API")
    
    items = response['data']['entityLookup']['items']
    if items is None:
        items = []
        if hasattr(args, 'verbose') and args.verbose:
            print("No items found in entity lookup - "+ entity_type)
    return items

def getAccountSnapshot(args, configuration, account_id, site_ids=None):
    snapshot_query = {
        "query": "query accountSnapshot ( $siteIDs:[ID!] $accountID:ID ) { accountSnapshot ( accountID:$accountID ) { id sites ( siteIDs:$siteIDs ) { id protoId connectivityStatusSiteSnapshot: connectivityStatus haStatusSiteSnapshot: haStatus { readiness wanConnectivity keepalive socketVersion } operationalStatusSiteSnapshot: operationalStatus lastConnected connectedSince popName devices { id name identifier connected haRole interfaces { connected id name physicalPort naturalOrder popName previousPopID previousPopName tunnelConnectionReason tunnelUptime tunnelRemoteIP tunnelRemoteIPInfoInterfaceSnapshot: tunnelRemoteIPInfo { ip countryCode countryName city state provider latitude longitude } type infoInterfaceSnapshot: info { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRole } cellularInterfaceInfoInterfaceSnapshot: cellularInterfaceInfo { networkType simSlotId modemStatus isModemConnected iccid imei operatorName isModemSuspended apn apnSelectionMethod signalStrength isRoamingAllowed simNumber disconnectionReason isSimSlot1Detected isSimSlot2Detected } } lastConnected lastDuration connectedSince lastPopID lastPopName recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfoRecentConnection: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } type deviceUptime socketInfo { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } interfacesLinkState { id up mediaIn linkSpeed duplex hasAddress hasInternet hasTunnel } osType osVersion version versionNumber releaseGroup mfaExpirationTime mfaCreationTime internalIP } infoSiteSnapshot: info { name type description countryCode region countryName countryStateName cityName address isHA connType creationTime interfaces { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRoleInterfaceInfo: wanRole } sockets { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } ipsec { isPrimary catoIP remoteIP ikeVersion } } hostCount altWanStatus } users { id connectivityStatusUserSnapshot: connectivityStatus operationalStatusUserSnapshot: operationalStatus name deviceName uptime lastConnected version versionNumber popID popName remoteIP remoteIPInfoUserSnapshot: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } internalIP osType osVersion devices { id name identifier connected haRole interfaces { connected id name physicalPort naturalOrder popName previousPopID previousPopName tunnelConnectionReason tunnelUptime tunnelRemoteIP tunnelRemoteIPInfoInterfaceSnapshot: tunnelRemoteIPInfo { ip countryCode countryName city state provider latitude longitude } type infoInterfaceSnapshot: info { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRole } cellularInterfaceInfoInterfaceSnapshot: cellularInterfaceInfo { networkType simSlotId modemStatus isModemConnected iccid imei operatorName isModemSuspended apn apnSelectionMethod signalStrength isRoamingAllowed simNumber disconnectionReason isSimSlot1Detected isSimSlot2Detected } } lastConnected lastDuration connectedSince lastPopID lastPopName recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfoRecentConnection: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } type deviceUptime socketInfo { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } interfacesLinkState { id up mediaIn linkSpeed duplex hasAddress hasInternet hasTunnel } osType osVersion version versionNumber releaseGroup mfaExpirationTime mfaCreationTime internalIP } connectedInOffice infoUserSnapshot: info { name status email creationTime phoneNumber origin authMethod } recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } } timestamp }  }",
        "variables": {
            "accountID": account_id,
            "siteIDs": site_ids
        },
        "operationName": "accountSnapshot"
    }
    response = makeCall(args, configuration, snapshot_query)

    # Check for GraphQL errors in snapshot response
    if 'errors' in response:
        error_messages = [error.get('message', 'Unknown error') for error in response['errors']]
        raise Exception(f"Snapshot API returned errors: {', '.join(error_messages)}")
    
    if not response or 'data' not in response or 'accountSnapshot' not in response['data']:
        raise ValueError("Failed to retrieve snapshot data from API")
    
    if not response or 'sites' not in response['data']['accountSnapshot'] or response['data']['accountSnapshot']['sites'] is None:
        raise ValueError("No sites found in account snapshot data from API")

    return response