
import cato.parsers.custom.customLib as customLib

def custom_parse(subparsers):
	site_parser = subparsers.add_parser('site', help='Site', usage='cato site <operationName> [options]')
	site_subparsers = site_parser.add_subparsers(description='valid subcommands', help='additional help')

	site_list_parser = site_subparsers.add_parser('list', 
			help='site list', 
			usage=get_help_custom("site_list"))

	site_list_parser.add_argument('accountID', help='The Account ID.')
	site_list_parser.add_argument('-s', help='Search string', default='', nargs='?')
	site_list_parser.add_argument('-f', default="csv", choices=["json","csv"], nargs='?', 
		help='Specify format for output')
	site_list_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	site_list_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	site_list_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	
	site_list_parser.set_defaults(func=customLib.entityTypeList,operation_name='site')

def get_help_custom(path):
	matchCmd = "cato "+path.replace("_"," ")
	import os
	pwd = os.path.dirname(__file__)
	# doc = path+"/README.md"
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
