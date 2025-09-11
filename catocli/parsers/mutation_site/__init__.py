
from ..customParserApiClient import createRequest, get_help

def mutation_site_parse(mutation_subparsers):
    mutation_site_parser = mutation_subparsers.add_parser('site', 
            help='site() mutation operation', 
            usage=get_help("mutation_site"))

    mutation_site_subparsers = mutation_site_parser.add_subparsers()

    mutation_site_addSecondaryAwsVSocket_parser = mutation_site_subparsers.add_parser('addSecondaryAwsVSocket', 
            help='addSecondaryAwsVSocket() site operation', 
            usage=get_help("mutation_site_addSecondaryAwsVSocket"))

    mutation_site_addSecondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addSecondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addSecondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.addSecondaryAwsVSocket')

    mutation_site_addSecondaryAzureVSocket_parser = mutation_site_subparsers.add_parser('addSecondaryAzureVSocket', 
            help='addSecondaryAzureVSocket() site operation', 
            usage=get_help("mutation_site_addSecondaryAzureVSocket"))

    mutation_site_addSecondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addSecondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addSecondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.addSecondaryAzureVSocket')

    mutation_site_removeSecondaryAzureVSocket_parser = mutation_site_subparsers.add_parser('removeSecondaryAzureVSocket', 
            help='removeSecondaryAzureVSocket() site operation', 
            usage=get_help("mutation_site_removeSecondaryAzureVSocket"))

    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeSecondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeSecondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSecondaryAzureVSocket')

    mutation_site_removeSecondaryAwsVSocket_parser = mutation_site_subparsers.add_parser('removeSecondaryAwsVSocket', 
            help='removeSecondaryAwsVSocket() site operation', 
            usage=get_help("mutation_site_removeSecondaryAwsVSocket"))

    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeSecondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeSecondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSecondaryAwsVSocket')

    mutation_site_updateSecondaryAzureVSocket_parser = mutation_site_subparsers.add_parser('updateSecondaryAzureVSocket', 
            help='updateSecondaryAzureVSocket() site operation', 
            usage=get_help("mutation_site_updateSecondaryAzureVSocket"))

    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateSecondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateSecondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSecondaryAzureVSocket')

    mutation_site_updateSecondaryAwsVSocket_parser = mutation_site_subparsers.add_parser('updateSecondaryAwsVSocket', 
            help='updateSecondaryAwsVSocket() site operation', 
            usage=get_help("mutation_site_updateSecondaryAwsVSocket"))

    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateSecondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateSecondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSecondaryAwsVSocket')

    mutation_site_addSocketSite_parser = mutation_site_subparsers.add_parser('addSocketSite', 
            help='addSocketSite() site operation', 
            usage=get_help("mutation_site_addSocketSite"))

    mutation_site_addSocketSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addSocketSite_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addSocketSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addSocketSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addSocketSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addSocketSite_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addSocketSite_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addSocketSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addSocketSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addSocketSite_parser.set_defaults(func=createRequest,operation_name='mutation.site.addSocketSite')

    mutation_site_updateSiteGeneralDetails_parser = mutation_site_subparsers.add_parser('updateSiteGeneralDetails', 
            help='updateSiteGeneralDetails() site operation', 
            usage=get_help("mutation_site_updateSiteGeneralDetails"))

    mutation_site_updateSiteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateSiteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateSiteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSiteGeneralDetails')

    mutation_site_removeSite_parser = mutation_site_subparsers.add_parser('removeSite', 
            help='removeSite() site operation', 
            usage=get_help("mutation_site_removeSite"))

    mutation_site_removeSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeSite_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeSite_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeSite_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeSite_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSite')

    mutation_site_updateSocketInterface_parser = mutation_site_subparsers.add_parser('updateSocketInterface', 
            help='updateSocketInterface() site operation', 
            usage=get_help("mutation_site_updateSocketInterface"))

    mutation_site_updateSocketInterface_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateSocketInterface_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateSocketInterface_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateSocketInterface_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateSocketInterface_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateSocketInterface_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateSocketInterface_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateSocketInterface_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateSocketInterface_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateSocketInterface_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSocketInterface')

    mutation_site_addNetworkRange_parser = mutation_site_subparsers.add_parser('addNetworkRange', 
            help='addNetworkRange() site operation', 
            usage=get_help("mutation_site_addNetworkRange"))

    mutation_site_addNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addNetworkRange_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addNetworkRange_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addNetworkRange_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.addNetworkRange')

    mutation_site_updateNetworkRange_parser = mutation_site_subparsers.add_parser('updateNetworkRange', 
            help='updateNetworkRange() site operation', 
            usage=get_help("mutation_site_updateNetworkRange"))

    mutation_site_updateNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateNetworkRange_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateNetworkRange_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateNetworkRange_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateNetworkRange')

    mutation_site_removeNetworkRange_parser = mutation_site_subparsers.add_parser('removeNetworkRange', 
            help='removeNetworkRange() site operation', 
            usage=get_help("mutation_site_removeNetworkRange"))

    mutation_site_removeNetworkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeNetworkRange_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeNetworkRange_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeNetworkRange_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeNetworkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeNetworkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeNetworkRange')

    mutation_site_updateHa_parser = mutation_site_subparsers.add_parser('updateHa', 
            help='updateHa() site operation', 
            usage=get_help("mutation_site_updateHa"))

    mutation_site_updateHa_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateHa_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateHa_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateHa_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateHa_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateHa_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateHa_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateHa_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateHa_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateHa_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateHa')

    mutation_site_addStaticHost_parser = mutation_site_subparsers.add_parser('addStaticHost', 
            help='addStaticHost() site operation', 
            usage=get_help("mutation_site_addStaticHost"))

    mutation_site_addStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addStaticHost_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addStaticHost_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addStaticHost_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.addStaticHost')

    mutation_site_updateStaticHost_parser = mutation_site_subparsers.add_parser('updateStaticHost', 
            help='updateStaticHost() site operation', 
            usage=get_help("mutation_site_updateStaticHost"))

    mutation_site_updateStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateStaticHost_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateStaticHost_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateStaticHost_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateStaticHost')

    mutation_site_removeStaticHost_parser = mutation_site_subparsers.add_parser('removeStaticHost', 
            help='removeStaticHost() site operation', 
            usage=get_help("mutation_site_removeStaticHost"))

    mutation_site_removeStaticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeStaticHost_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeStaticHost_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeStaticHost_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeStaticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeStaticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeStaticHost')

    mutation_site_addIpsecIkeV2Site_parser = mutation_site_subparsers.add_parser('addIpsecIkeV2Site', 
            help='addIpsecIkeV2Site() site operation', 
            usage=get_help("mutation_site_addIpsecIkeV2Site"))

    mutation_site_addIpsecIkeV2Site_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addIpsecIkeV2Site_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addIpsecIkeV2Site_parser.set_defaults(func=createRequest,operation_name='mutation.site.addIpsecIkeV2Site')

    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser = mutation_site_subparsers.add_parser('updateIpsecIkeV2SiteGeneralDetails', 
            help='updateIpsecIkeV2SiteGeneralDetails() site operation', 
            usage=get_help("mutation_site_updateIpsecIkeV2SiteGeneralDetails"))

    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateIpsecIkeV2SiteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateIpsecIkeV2SiteGeneralDetails')

    mutation_site_addIpsecIkeV2SiteTunnels_parser = mutation_site_subparsers.add_parser('addIpsecIkeV2SiteTunnels', 
            help='addIpsecIkeV2SiteTunnels() site operation', 
            usage=get_help("mutation_site_addIpsecIkeV2SiteTunnels"))

    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.site.addIpsecIkeV2SiteTunnels')

    mutation_site_updateIpsecIkeV2SiteTunnels_parser = mutation_site_subparsers.add_parser('updateIpsecIkeV2SiteTunnels', 
            help='updateIpsecIkeV2SiteTunnels() site operation', 
            usage=get_help("mutation_site_updateIpsecIkeV2SiteTunnels"))

    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateIpsecIkeV2SiteTunnels')

    mutation_site_removeIpsecIkeV2SiteTunnels_parser = mutation_site_subparsers.add_parser('removeIpsecIkeV2SiteTunnels', 
            help='removeIpsecIkeV2SiteTunnels() site operation', 
            usage=get_help("mutation_site_removeIpsecIkeV2SiteTunnels"))

    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeIpsecIkeV2SiteTunnels_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeIpsecIkeV2SiteTunnels')

    mutation_site_addCloudInterconnectSite_parser = mutation_site_subparsers.add_parser('addCloudInterconnectSite', 
            help='addCloudInterconnectSite() site operation', 
            usage=get_help("mutation_site_addCloudInterconnectSite"))

    mutation_site_addCloudInterconnectSite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addCloudInterconnectSite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addCloudInterconnectSite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addCloudInterconnectSite_parser.set_defaults(func=createRequest,operation_name='mutation.site.addCloudInterconnectSite')

    mutation_site_addCloudInterconnectPhysicalConnection_parser = mutation_site_subparsers.add_parser('addCloudInterconnectPhysicalConnection', 
            help='addCloudInterconnectPhysicalConnection() site operation', 
            usage=get_help("mutation_site_addCloudInterconnectPhysicalConnection"))

    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.site.addCloudInterconnectPhysicalConnection')

    mutation_site_updateCloudInterconnectPhysicalConnection_parser = mutation_site_subparsers.add_parser('updateCloudInterconnectPhysicalConnection', 
            help='updateCloudInterconnectPhysicalConnection() site operation', 
            usage=get_help("mutation_site_updateCloudInterconnectPhysicalConnection"))

    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateCloudInterconnectPhysicalConnection')

    mutation_site_removeCloudInterconnectPhysicalConnection_parser = mutation_site_subparsers.add_parser('removeCloudInterconnectPhysicalConnection', 
            help='removeCloudInterconnectPhysicalConnection() site operation', 
            usage=get_help("mutation_site_removeCloudInterconnectPhysicalConnection"))

    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeCloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeCloudInterconnectPhysicalConnection')

    mutation_site_addBgpPeer_parser = mutation_site_subparsers.add_parser('addBgpPeer', 
            help='addBgpPeer() site operation', 
            usage=get_help("mutation_site_addBgpPeer"))

    mutation_site_addBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addBgpPeer_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addBgpPeer_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addBgpPeer_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.site.addBgpPeer')

    mutation_site_updateBgpPeer_parser = mutation_site_subparsers.add_parser('updateBgpPeer', 
            help='updateBgpPeer() site operation', 
            usage=get_help("mutation_site_updateBgpPeer"))

    mutation_site_updateBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateBgpPeer_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateBgpPeer_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateBgpPeer_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateBgpPeer')

    mutation_site_removeBgpPeer_parser = mutation_site_subparsers.add_parser('removeBgpPeer', 
            help='removeBgpPeer() site operation', 
            usage=get_help("mutation_site_removeBgpPeer"))

    mutation_site_removeBgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeBgpPeer_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeBgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeBgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeBgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeBgpPeer_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeBgpPeer_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeBgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeBgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeBgpPeer_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeBgpPeer')

    mutation_site_startSiteUpgrade_parser = mutation_site_subparsers.add_parser('startSiteUpgrade', 
            help='startSiteUpgrade() site operation', 
            usage=get_help("mutation_site_startSiteUpgrade"))

    mutation_site_startSiteUpgrade_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_startSiteUpgrade_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_startSiteUpgrade_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_startSiteUpgrade_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_startSiteUpgrade_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_startSiteUpgrade_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_startSiteUpgrade_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_startSiteUpgrade_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_startSiteUpgrade_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_startSiteUpgrade_parser.set_defaults(func=createRequest,operation_name='mutation.site.startSiteUpgrade')

    mutation_site_assignSiteBwLicense_parser = mutation_site_subparsers.add_parser('assignSiteBwLicense', 
            help='assignSiteBwLicense() site operation', 
            usage=get_help("mutation_site_assignSiteBwLicense"))

    mutation_site_assignSiteBwLicense_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_assignSiteBwLicense_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_assignSiteBwLicense_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_assignSiteBwLicense_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_assignSiteBwLicense_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_assignSiteBwLicense_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_assignSiteBwLicense_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_assignSiteBwLicense_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_assignSiteBwLicense_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_assignSiteBwLicense_parser.set_defaults(func=createRequest,operation_name='mutation.site.assignSiteBwLicense')

    mutation_site_updateSiteBwLicense_parser = mutation_site_subparsers.add_parser('updateSiteBwLicense', 
            help='updateSiteBwLicense() site operation', 
            usage=get_help("mutation_site_updateSiteBwLicense"))

    mutation_site_updateSiteBwLicense_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_updateSiteBwLicense_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_updateSiteBwLicense_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_updateSiteBwLicense_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_updateSiteBwLicense_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_updateSiteBwLicense_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_updateSiteBwLicense_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_updateSiteBwLicense_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_updateSiteBwLicense_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_updateSiteBwLicense_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSiteBwLicense')

    mutation_site_replaceSiteBwLicense_parser = mutation_site_subparsers.add_parser('replaceSiteBwLicense', 
            help='replaceSiteBwLicense() site operation', 
            usage=get_help("mutation_site_replaceSiteBwLicense"))

    mutation_site_replaceSiteBwLicense_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_replaceSiteBwLicense_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_replaceSiteBwLicense_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_replaceSiteBwLicense_parser.set_defaults(func=createRequest,operation_name='mutation.site.replaceSiteBwLicense')

    mutation_site_removeSiteBwLicense_parser = mutation_site_subparsers.add_parser('removeSiteBwLicense', 
            help='removeSiteBwLicense() site operation', 
            usage=get_help("mutation_site_removeSiteBwLicense"))

    mutation_site_removeSiteBwLicense_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeSiteBwLicense_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeSiteBwLicense_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeSiteBwLicense_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeSiteBwLicense_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeSiteBwLicense_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeSiteBwLicense_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeSiteBwLicense_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeSiteBwLicense_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeSiteBwLicense_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSiteBwLicense')

    mutation_site_addSocketAddOnCard_parser = mutation_site_subparsers.add_parser('addSocketAddOnCard', 
            help='addSocketAddOnCard() site operation', 
            usage=get_help("mutation_site_addSocketAddOnCard"))

    mutation_site_addSocketAddOnCard_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_addSocketAddOnCard_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_addSocketAddOnCard_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_addSocketAddOnCard_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_addSocketAddOnCard_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_addSocketAddOnCard_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_addSocketAddOnCard_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_addSocketAddOnCard_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_addSocketAddOnCard_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_addSocketAddOnCard_parser.set_defaults(func=createRequest,operation_name='mutation.site.addSocketAddOnCard')

    mutation_site_removeSocketAddOnCard_parser = mutation_site_subparsers.add_parser('removeSocketAddOnCard', 
            help='removeSocketAddOnCard() site operation', 
            usage=get_help("mutation_site_removeSocketAddOnCard"))

    mutation_site_removeSocketAddOnCard_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_site_removeSocketAddOnCard_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_site_removeSocketAddOnCard_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_site_removeSocketAddOnCard_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSocketAddOnCard')
