
from ..parserApiClient import createRequest, get_help

def mutation_sites_parse(mutation_subparsers):
	mutation_sites_parser = mutation_subparsers.add_parser('sites', 
			help='sites() mutation operation', 
			usage=get_help("mutation_sites"))

	mutation_sites_subparsers = mutation_sites_parser.add_subparsers()

	mutation_sites_addBgpPeer_parser = mutation_sites_subparsers.add_parser('addBgpPeer', 
			help='addBgpPeer() sites operation', 
			usage=get_help("mutation_sites_addBgpPeer"))

	mutation_sites_addBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addBgpPeer_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addBgpPeer')

	mutation_sites_addCloudInterconnectPhysicalConnection_parser = mutation_sites_subparsers.add_parser('addCloudInterconnectPhysicalConnection', 
			help='addCloudInterconnectPhysicalConnection() sites operation', 
			usage=get_help("mutation_sites_addCloudInterconnectPhysicalConnection"))

	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addCloudInterconnectPhysicalConnection')

	mutation_sites_addCloudInterconnectSite_parser = mutation_sites_subparsers.add_parser('addCloudInterconnectSite', 
			help='addCloudInterconnectSite() sites operation', 
			usage=get_help("mutation_sites_addCloudInterconnectSite"))

	mutation_sites_addCloudInterconnectSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addCloudInterconnectSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addCloudInterconnectSite_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addCloudInterconnectSite')

	mutation_sites_addIpsecIkeV2Site_parser = mutation_sites_subparsers.add_parser('addIpsecIkeV2Site', 
			help='addIpsecIkeV2Site() sites operation', 
			usage=get_help("mutation_sites_addIpsecIkeV2Site"))

	mutation_sites_addIpsecIkeV2Site_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addIpsecIkeV2Site_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addIpsecIkeV2Site_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addIpsecIkeV2Site')

	mutation_sites_addIpsecIkeV2SiteTunnels_parser = mutation_sites_subparsers.add_parser('addIpsecIkeV2SiteTunnels', 
			help='addIpsecIkeV2SiteTunnels() sites operation', 
			usage=get_help("mutation_sites_addIpsecIkeV2SiteTunnels"))

	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addIpsecIkeV2SiteTunnels')

	mutation_sites_addNetworkRange_parser = mutation_sites_subparsers.add_parser('addNetworkRange', 
			help='addNetworkRange() sites operation', 
			usage=get_help("mutation_sites_addNetworkRange"))

	mutation_sites_addNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addNetworkRange_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addNetworkRange')

	mutation_sites_addSecondaryAwsVSocket_parser = mutation_sites_subparsers.add_parser('addSecondaryAwsVSocket', 
			help='addSecondaryAwsVSocket() sites operation', 
			usage=get_help("mutation_sites_addSecondaryAwsVSocket"))

	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addSecondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addSecondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addSecondaryAwsVSocket')

	mutation_sites_addSecondaryAzureVSocket_parser = mutation_sites_subparsers.add_parser('addSecondaryAzureVSocket', 
			help='addSecondaryAzureVSocket() sites operation', 
			usage=get_help("mutation_sites_addSecondaryAzureVSocket"))

	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addSecondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addSecondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addSecondaryAzureVSocket')

	mutation_sites_addSocketAddOnCard_parser = mutation_sites_subparsers.add_parser('addSocketAddOnCard', 
			help='addSocketAddOnCard() sites operation', 
			usage=get_help("mutation_sites_addSocketAddOnCard"))

	mutation_sites_addSocketAddOnCard_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addSocketAddOnCard_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addSocketAddOnCard_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addSocketAddOnCard_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addSocketAddOnCard_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addSocketAddOnCard_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addSocketAddOnCard_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addSocketAddOnCard_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addSocketAddOnCard')

	mutation_sites_addSocketSite_parser = mutation_sites_subparsers.add_parser('addSocketSite', 
			help='addSocketSite() sites operation', 
			usage=get_help("mutation_sites_addSocketSite"))

	mutation_sites_addSocketSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addSocketSite_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addSocketSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addSocketSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addSocketSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addSocketSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addSocketSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addSocketSite_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addSocketSite')

	mutation_sites_addStaticHost_parser = mutation_sites_subparsers.add_parser('addStaticHost', 
			help='addStaticHost() sites operation', 
			usage=get_help("mutation_sites_addStaticHost"))

	mutation_sites_addStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_addStaticHost_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_addStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_addStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_addStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_addStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_addStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_addStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.sites.addStaticHost')

	mutation_sites_removeBgpPeer_parser = mutation_sites_subparsers.add_parser('removeBgpPeer', 
			help='removeBgpPeer() sites operation', 
			usage=get_help("mutation_sites_removeBgpPeer"))

	mutation_sites_removeBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeBgpPeer_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeBgpPeer')

	mutation_sites_removeCloudInterconnectPhysicalConnection_parser = mutation_sites_subparsers.add_parser('removeCloudInterconnectPhysicalConnection', 
			help='removeCloudInterconnectPhysicalConnection() sites operation', 
			usage=get_help("mutation_sites_removeCloudInterconnectPhysicalConnection"))

	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeCloudInterconnectPhysicalConnection')

	mutation_sites_removeIpsecIkeV2SiteTunnels_parser = mutation_sites_subparsers.add_parser('removeIpsecIkeV2SiteTunnels', 
			help='removeIpsecIkeV2SiteTunnels() sites operation', 
			usage=get_help("mutation_sites_removeIpsecIkeV2SiteTunnels"))

	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeIpsecIkeV2SiteTunnels')

	mutation_sites_removeNetworkRange_parser = mutation_sites_subparsers.add_parser('removeNetworkRange', 
			help='removeNetworkRange() sites operation', 
			usage=get_help("mutation_sites_removeNetworkRange"))

	mutation_sites_removeNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeNetworkRange_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeNetworkRange')

	mutation_sites_removeSite_parser = mutation_sites_subparsers.add_parser('removeSite', 
			help='removeSite() sites operation', 
			usage=get_help("mutation_sites_removeSite"))

	mutation_sites_removeSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeSite_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeSite_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeSite')

	mutation_sites_removeSocketAddOnCard_parser = mutation_sites_subparsers.add_parser('removeSocketAddOnCard', 
			help='removeSocketAddOnCard() sites operation', 
			usage=get_help("mutation_sites_removeSocketAddOnCard"))

	mutation_sites_removeSocketAddOnCard_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeSocketAddOnCard_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeSocketAddOnCard_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeSocketAddOnCard')

	mutation_sites_removeStaticHost_parser = mutation_sites_subparsers.add_parser('removeStaticHost', 
			help='removeStaticHost() sites operation', 
			usage=get_help("mutation_sites_removeStaticHost"))

	mutation_sites_removeStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_removeStaticHost_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_removeStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_removeStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_removeStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_removeStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_removeStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_removeStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.sites.removeStaticHost')

	mutation_sites_startSiteUpgrade_parser = mutation_sites_subparsers.add_parser('startSiteUpgrade', 
			help='startSiteUpgrade() sites operation', 
			usage=get_help("mutation_sites_startSiteUpgrade"))

	mutation_sites_startSiteUpgrade_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_startSiteUpgrade_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_startSiteUpgrade_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_startSiteUpgrade_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_startSiteUpgrade_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_startSiteUpgrade_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_startSiteUpgrade_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_startSiteUpgrade_parser.set_defaults(func=createRequest,operation_name='mutation.sites.startSiteUpgrade')

	mutation_sites_updateBgpPeer_parser = mutation_sites_subparsers.add_parser('updateBgpPeer', 
			help='updateBgpPeer() sites operation', 
			usage=get_help("mutation_sites_updateBgpPeer"))

	mutation_sites_updateBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateBgpPeer_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateBgpPeer')

	mutation_sites_updateCloudInterconnectPhysicalConnection_parser = mutation_sites_subparsers.add_parser('updateCloudInterconnectPhysicalConnection', 
			help='updateCloudInterconnectPhysicalConnection() sites operation', 
			usage=get_help("mutation_sites_updateCloudInterconnectPhysicalConnection"))

	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateCloudInterconnectPhysicalConnection')

	mutation_sites_updateHa_parser = mutation_sites_subparsers.add_parser('updateHa', 
			help='updateHa() sites operation', 
			usage=get_help("mutation_sites_updateHa"))

	mutation_sites_updateHa_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateHa_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateHa_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateHa_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateHa_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateHa_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateHa_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateHa_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateHa')

	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser = mutation_sites_subparsers.add_parser('updateIpsecIkeV2SiteGeneralDetails', 
			help='updateIpsecIkeV2SiteGeneralDetails() sites operation', 
			usage=get_help("mutation_sites_updateIpsecIkeV2SiteGeneralDetails"))

	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateIpsecIkeV2SiteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateIpsecIkeV2SiteGeneralDetails')

	mutation_sites_updateIpsecIkeV2SiteTunnels_parser = mutation_sites_subparsers.add_parser('updateIpsecIkeV2SiteTunnels', 
			help='updateIpsecIkeV2SiteTunnels() sites operation', 
			usage=get_help("mutation_sites_updateIpsecIkeV2SiteTunnels"))

	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateIpsecIkeV2SiteTunnels')

	mutation_sites_updateNetworkRange_parser = mutation_sites_subparsers.add_parser('updateNetworkRange', 
			help='updateNetworkRange() sites operation', 
			usage=get_help("mutation_sites_updateNetworkRange"))

	mutation_sites_updateNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateNetworkRange_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateNetworkRange')

	mutation_sites_updateSiteGeneralDetails_parser = mutation_sites_subparsers.add_parser('updateSiteGeneralDetails', 
			help='updateSiteGeneralDetails() sites operation', 
			usage=get_help("mutation_sites_updateSiteGeneralDetails"))

	mutation_sites_updateSiteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateSiteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateSiteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateSiteGeneralDetails')

	mutation_sites_updateSocketInterface_parser = mutation_sites_subparsers.add_parser('updateSocketInterface', 
			help='updateSocketInterface() sites operation', 
			usage=get_help("mutation_sites_updateSocketInterface"))

	mutation_sites_updateSocketInterface_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateSocketInterface_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateSocketInterface_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateSocketInterface_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateSocketInterface_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateSocketInterface_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateSocketInterface_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateSocketInterface_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateSocketInterface')

	mutation_sites_updateStaticHost_parser = mutation_sites_subparsers.add_parser('updateStaticHost', 
			help='updateStaticHost() sites operation', 
			usage=get_help("mutation_sites_updateStaticHost"))

	mutation_sites_updateStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_sites_updateStaticHost_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sites_updateStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_sites_updateStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_sites_updateStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_sites_updateStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_sites_updateStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_sites_updateStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.sites.updateStaticHost')
