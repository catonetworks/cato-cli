
import catocli.parsers.custom.customLib as customLib
from catocli.parsers.custom.export_rules import export_rules_parse
from catocli.parsers.custom.import_rules_to_tf import rule_import_parse
from catocli.parsers.custom.import_sites_to_tf import site_import_parse
from catocli.parsers.configure import configure_parse
from catocli.parsers.custom.export_sites import export_sites_parse
from catocli.parsers.custom.scim import scim_parse

def custom_parse(subparsers):
	entityTypes = ["account","admin","allocatedIP","any","availablePooledUsage","availableSiteUsage","dhcpRelayGroup","groupSubscription","host","lanFirewall","localRouting","location","mailingListSubscription","networkInterface","portProtocol","simpleService","site","siteRange","timezone","vpnUser","webhookSubscription"]
	entity_parser = subparsers.add_parser('entity', help='Entity Lookup', usage='catocli entity <operationName> [options]')
	entity_subparsers = entity_parser.add_subparsers(description='valid subcommands', help='additional help')

	for entity in entityTypes:
		item_parser = entity_subparsers.add_parser(entity, help="entityLookup() for type: "+entity, usage='catocli entity '+entity+' <operationName> [options]')
		item_subparsers = item_parser.add_subparsers(description='valid subcommands', help='additional help')

		item_list_parser = item_subparsers.add_parser('list', 
				help='entity'+entity+' list', 
				usage=get_help_custom("entity_"+entity+"_list"))

		item_list_parser.add_argument('-accountID', help='The Account ID.')
		item_list_parser.add_argument('-s', help='Search string', default='', nargs='?')
		item_list_parser.add_argument('-f', default="csv", choices=["json","csv"], nargs='?', 
			help='Specify format for output')
		item_list_parser.add_argument('-t', const=True, default=False, nargs='?', 
			help='Print test request preview without sending api call')
		item_list_parser.add_argument('-v', const=True, default=False, nargs='?', 
			help='Verbose output')
		item_list_parser.add_argument('-p', const=True, default=False, nargs='?', 
			help='Pretty print')
		
		item_list_parser.set_defaults(func=customLib.entityTypeList,operation_name=entity)

	# Add additional custom parsers here 
	export_rules_parse(subparsers)
	import_parser = rule_import_parse(subparsers)
	site_import_parse(subparsers, import_parser)
	configure_parse(subparsers)
	scim_parse(subparsers)

def get_help_custom(path):
	matchCmd = "catocli "+path.replace("_"," ")
	import os
	pwd = os.path.dirname(__file__)
	abs_path = os.path.join(pwd, "README.md")
	new_line = "\nEXAMPLES:\n"
	lines = open(abs_path, "r").readlines()
	for line in lines:
		if f"{matchCmd}" in line:
			clean_line = line.replace("<br /><br />", "").replace("`","")
			new_line += f"{clean_line}\n"
	# matchArg = path.replace("_",".")
	# for line in lines:
	# 	if f"`{matchArg}" in line:
	# 		clean_line = line.replace("<br /><br />", "").replace("`","")
	# 		new_line += f"{clean_line}\n"
	return new_line
