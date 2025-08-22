import codecs
import json
import os
import sys
from graphql_client import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
import pprint
import uuid
import string
from urllib3.filepost import encode_multipart_formdata

def createRequest(args, configuration):
	params = vars(args)
	instance = CallApi(ApiClient(configuration))
	operationName = params["operation_name"]
	operation = loadJSON("models/"+operationName+".json")
	variablesObj = {}
	if params["json"] and not params["t"]:
		try:
			variablesObj = json.loads(params["json"])
		except ValueError as e:
			print("ERROR: Query argument must be valid json in quotes. ",e,'\n\nExample: \'{"yourKey":"yourValue"}\'')
			exit()
	elif not params["t"] and params["json"] is None:
		# Default to empty object if no json provided and not using -t flag
		variablesObj = {}
	# Special handling for eventsFeed and auditFeed which use accountIDs array
	if operationName in ["query.eventsFeed", "query.auditFeed"]:
		# Only add accountIDs if not already provided in JSON
		if "accountIDs" not in variablesObj:
			variablesObj["accountIDs"] = [configuration.accountID]
	elif "accountId" in operation["args"]:
		variablesObj["accountId"] = configuration.accountID
	else:
		variablesObj["accountID"] = configuration.accountID
	if params["t"]==True:
		# Skip validation when using -t flag
		isOk = True
	else:
		isOk, invalidVars, message = validateArgs(variablesObj,operation)
	if isOk==True:
		body = generateGraphqlPayload(variablesObj,operation,operationName)
		if params["t"]==True:
			# Load query from queryPayloads file
			try:
				queryPayloadFile = "queryPayloads/" + operationName + ".json"
				queryPayload = loadJSON(queryPayloadFile)
				if queryPayload and "query" in queryPayload:
					print(queryPayload["query"])
				else:
					print("ERROR: Query not found in " + queryPayloadFile)
			except Exception as e:
				print("ERROR: Could not load query from " + queryPayloadFile + ": " + str(e))
			return None
		else:
			try:
				return instance.call_api(body,params)
			except ApiException as e:
				return e
	else:
		print("ERROR: "+message,", ".join(invalidVars))
		try:
			queryPayloadFile = "queryPayloads/" + operationName + ".json"
			queryPayload = loadJSON(queryPayloadFile)
			print("\nExample: catocli "+operationName.replace(".", " "), json.dumps(queryPayload['variables']))
		except Exception as e:
			print("ERROR: Could not load query from " + queryPayloadFile + ": " + str(e))
		
def querySiteLocation(args, configuration):
	params = vars(args)
	operationName = params["operation_name"]
	operation = loadJSON("models/"+operationName+".json")
	try:
		variablesObj = json.loads(params["json"])	
	except ValueError as e:
		print("ERROR: Query argument must be valid json in quotes. ",e,'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	if not variablesObj.get("filters"):
		print("ERROR: Missing argument, must include filters array. ",e,'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	if not isinstance(variablesObj.get("filters"), list):
		print("ERROR: Invalid argument, must include filters array. ",e,'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	requiredFields = ["search","field","operation"]
	for filter in variablesObj["filters"]:
		if not isinstance(filter, dict):
			print("ERROR: Invalid filter '"+str(filter)+"', filters must be valid json and include 'search', 'field', and 'operation'. ",'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'',type(filter))
			exit()	
		for param in filter:
			if param not in requiredFields:
				print("ERROR: Invalid field '"+param+"', filters must include 'search', 'field', and 'operation'. ",'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
				exit()	
	for filter in variablesObj["filters"]:
		for param in filter:
			val = filter.get(param)
			if param=="search" and (not isinstance(val, str) or len(val)<3):
				print("ERROR: Invalid search '"+val+"', must be a string value and at least 3 characters in lengh. ",'\n\nExample: \'{"filters":[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
				exit()
			if param=="field" and (not isinstance(val, str) or val not in [ 'countryName', 'stateName', 'city']):
				print("ERROR: Invalid field '"+val+"', must be one of the following: 'countryName', 'stateName', or 'city'.",'\n\nExample: \'{"search":"your query here","field":"city"}\'')
				exit()		
			if param=="operation" and (not isinstance(val, str) or val not in [ 'startsWith', 'endsWith', 'exact', 'contains' ]):
				print("ERROR: Invalid operation '"+val+"', must be one of the following: 'startsWith', 'endsWith', 'exact', 'contains'.",'\n\nExample: \'{"search": "Your search here","field":"city","operation":"exact"}\'')
				exit()
	response = {"data":[]}
	for key, siteObj in operation.items():
		isOk = True
		for filter in variablesObj["filters"]:
			search = filter.get("search")
			field = filter.get("field")
			operation = filter.get("operation")
			if field in siteObj:
				if operation=="startsWith" and not siteObj[field].startswith(search):
					isOk = False
					break
				elif operation=="endsWith" and not siteObj[field].endswith(search):
					isOk = False
					break
				elif operation=="exact" and not siteObj[field]==search:
					isOk = False
					break
				elif operation=="contains" and not search in siteObj[field]:
					isOk = False
					break
			else:
				isOk = False
				break
			if isOk==False:
				break
		if isOk==True:
			response["data"].append(siteObj)
	if params["p"]==True:
		responseStr = json.dumps(response,indent=2,sort_keys=True,ensure_ascii=False).encode('utf8')
		print(responseStr.decode())
	else:
		responseStr = json.dumps(response,ensure_ascii=False).encode('utf8')
		print(responseStr.decode())
		
def createRawRequest(args, configuration):
	params = vars(args)
	# Handle endpoint override
	if hasattr(args, 'endpoint') and args.endpoint:
		configuration.host = args.endpoint
	
	# Check if binary/multipart mode is enabled
	if hasattr(args, 'binary') and args.binary:
		return createRawBinaryRequest(args, configuration)
		
	instance = CallApi(ApiClient(configuration))
	isOk = False
	try:
		body = json.loads(params["json"])
		isOk = True
	except ValueError as e:
		print("ERROR: Argument must be valid json. ",e)
		isOk=False	
	except Exception as e:
		isOk=False
		print("ERROR: ",e)
	if isOk==True:
		if params["t"]==True:
			if params["p"]==True:
				print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "\t"))
			else:
				print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
			return None
		else:
			try:
				return instance.call_api(body,params)
			except ApiException as e:
				print(e)
				exit()

def generateGraphqlPayload(variablesObj,operation,operationName):
	indent = "	"
	queryStr = ""
	variableStr = ""
	for varName in variablesObj:
		if (varName in operation["operationArgs"]):
			variableStr += operation["operationArgs"][varName]["requestStr"]
	operationAry = operationName.split(".")
	operationType = operationAry.pop(0)
	queryStr = operationType + " "
	queryStr += renderCamelCase(".".join(operationAry))
	queryStr += " ( " + variableStr + ") {\n"
	queryStr += indent + operation["name"] + " ( "			
	for argName in operation["args"]:
		arg = operation["args"][argName]
		if arg["varName"] in variablesObj:
			queryStr += arg["responseStr"]
	queryStr += ") {\n" + renderArgsAndFields("", variablesObj, operation, operation["type"]["definition"], "		") + "	}"
	queryStr += indent + "\n}";
	body = {
		"query":queryStr,
		"variables":variablesObj,
		"operationName":renderCamelCase(".".join(operationAry)),
	}
	return body

def get_help(path):
	matchCmd = "catocli "+path.replace("_"," ")
	import os
	pwd = os.path.dirname(__file__)
	doc = path+"/README.md"
	abs_path = os.path.join(pwd, doc)
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

def validateArgs(variablesObj,operation):
	isOk = True
	invalidVars = []
	message = "Arguments are missing or have invalid values: "
	for varName in variablesObj:
		if varName not in operation["operationArgs"]:
			isOk = False
			invalidVars.append('"'+varName+'"')
			message = "Invalid argument names. Looking for: "+", ".join(list(operation["operationArgs"].keys()))

	if isOk==True:
		for varName in operation["operationArgs"]:
			if operation["operationArgs"][varName]["required"] and varName not in variablesObj:
				isOk = False
				invalidVars.append('"'+varName+'"')
			else:
				if varName in variablesObj:
					value = variablesObj[varName]
					if operation["operationArgs"][varName]["required"] and value=="":
						isOk = False
						invalidVars.append('"'+varName+'":"'+str(value)+'"')
	return isOk, invalidVars, message

def loadJSON(file):
	CONFIG = {}
	module_dir = os.path.dirname(__file__)
	# Navigate up two directory levels (from parsers/ to catocli/ to root)
	module_dir = os.path.dirname(module_dir)  # Go up from parsers/
	module_dir = os.path.dirname(module_dir)  # Go up from catocli/
	try:
		file_path = os.path.join(module_dir, file)
		with open(file_path, 'r') as data:
			CONFIG = json.load(data)
			return CONFIG
	except:
		logging.warning(f"File \"{os.path.join(module_dir, file)}\" not found.")
		exit()

def renderCamelCase(pathStr):
	str = ""
	pathAry = pathStr.split(".") 
	for i, path in enumerate(pathAry):
		if i == 0:
			str += path[0].lower() + path[1:]
		else:
			str += path[0].upper() + path[1:]
	return str	

def renderArgsAndFields(responseArgStr, variablesObj, curOperation, definition, indent):
	for fieldName in definition['fields']:
		field = definition['fields'][fieldName]
		field_name = field['alias'] if 'alias' in field else field['name']				
		
		# Check if field has arguments and whether they are present in variables
		should_include_field = True
		argsPresent = False
		argStr = ""
		
		if field.get("args") and not isinstance(field['args'], list):
			if (len(list(field['args'].keys()))>0):
				# Field has arguments - only include if arguments are present in variables
				argStr = " ( "
				for argName in field['args']:
					arg = field['args'][argName]
					if arg["varName"] in variablesObj:
						argStr += arg['responseStr'] + " "
						argsPresent = True
				argStr += ") "
				# Only include fields with arguments if the arguments are present
				should_include_field = argsPresent
		
		# Only process field if we should include it
		if should_include_field:
			responseArgStr += indent + field_name
			if argsPresent:
				responseArgStr += argStr
				
		if should_include_field and field.get("type") and field['type'].get('definition') and field['type']['definition']['fields'] is not None:
			responseArgStr += " {\n"
			for subfieldIndex in field['type']['definition']['fields']:
				subfield = field['type']['definition']['fields'][subfieldIndex]
				# Use the alias if it exists, otherwise use the field name
				subfield_name = subfield['alias'] if 'alias' in subfield else subfield['name']
				responseArgStr += indent + "	" + subfield_name
				if subfield.get("args") and len(list(subfield["args"].keys()))>0:
					argsPresent = False
					subArgStr = " ( "
					for argName in subfield['args']:
						arg = subfield['args'][argName]
						if arg["varName"] in variablesObj:
							argsPresent = True
							subArgStr += arg['responseStr'] + " "
					subArgStr += " )"
					if argsPresent==True:
						responseArgStr += subArgStr
				if subfield.get("type") and subfield['type'].get("definition") and (subfield['type']['definition'].get("fields") or subfield['type']['definition'].get('inputFields')):
					responseArgStr += " {\n"
					responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, subfield['type']['definition'], indent + "		")
					if subfield['type']['definition'].get('possibleTypes'):
						for possibleTypeName in subfield['type']['definition']['possibleTypes']:
							possibleType = subfield['type']['definition']['possibleTypes'][possibleTypeName]
							responseArgStr += indent + "		... on " + possibleType['name'] + " {\n"
							if possibleType.get('fields') or possibleType.get('inputFields'):
								responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "			")
							responseArgStr += indent + "		}\n"
					responseArgStr += indent + "	}"
				elif subfield.get('type') and subfield['type'].get('definition') and subfield['type']['definition'].get('possibleTypes'):
					responseArgStr += " {\n"
					responseArgStr += indent + "		__typename\n"
					for possibleTypeName in subfield['type']['definition']['possibleTypes']:
						possibleType = subfield['type']['definition']['possibleTypes'][possibleTypeName]						
						responseArgStr += indent + "		... on " + possibleType['name'] + " {\n"
						if possibleType.get('fields') or possibleType.get('inputFields'):
							responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "			")
						responseArgStr += indent + "		}\n"
					responseArgStr += indent + " 	}\n"
				responseArgStr += "\n"
			if field['type']['definition'].get('possibleTypes'):
				for possibleTypeName in field['type']['definition']['possibleTypes']:
					possibleType = field['type']['definition']['possibleTypes'][possibleTypeName]
					responseArgStr += indent + "	... on " + possibleType['name'] + " {\n"
					if possibleType.get('fields') or possibleType.get('inputFields'):
						responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "		")
					responseArgStr += indent + "	}\n"
			responseArgStr += indent + "}\n"
		if should_include_field and field.get('type') and field['type'].get('definition') and field['type']['definition'].get('inputFields'):
			responseArgStr += " {\n"
			for subfieldName in field['type']['definition'].get('inputFields'):
				subfield = field['type']['definition']['inputFields'][subfieldName]
				# Updated aliasing logic for inputFields
				if (subfield.get('type') and subfield['type'].get('name') and 
					curOperation.get('fieldTypes', {}).get(subfield['type']['name']) and 
					subfield.get('type', {}).get('kind') and 
					'SCALAR' not in str(subfield['type']['kind'])):
					subfield_name = f"{subfield['name']}{field['type']['definition']['name']}: {subfield['name']}"
				else:
					subfield_name = subfield['name']  # Always use the raw field name, not incorrect aliases
				responseArgStr += indent + "	" + subfield_name
				if subfield.get('type') and subfield['type'].get('definition') and (subfield['type']['definition'].get('fields') or subfield['type']['definition'].get('inputFields')):
					responseArgStr += " {\n"
					responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, subfield['type']['definition'], indent + "		")
					responseArgStr += indent + "	}\n"
			if field['type']['definition'].get('possibleTypes'):
				for possibleTypeName in field['type']['definition']['possibleTypes']:
					possibleType = field['type']['definition']['possibleTypes'][possibleTypeName]
					responseArgStr += indent + "... on " + possibleType['name'] + " {\n"
					if possibleType.get('fields') or possibleType.get('inputFields'):
						responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "		")
					responseArgStr += indent + "	}\n"
			responseArgStr += indent + "}\n"
		if should_include_field:
			responseArgStr += "\n"
	return responseArgStr

def createRawBinaryRequest(args, configuration):
	"""Handle multipart/form-data requests for file uploads and binary content"""
	params = vars(args)
	
	
	# Parse the JSON body
	try:
		body = json.loads(params["json"])
	except ValueError as e:
		print("ERROR: JSON argument must be valid json. ", e)
		return
	except Exception as e:
		print("ERROR: ", e)
		return
	
	# Build form data
	form_fields = {}
	files = []
	
	# Add the operations field containing the GraphQL payload
	form_fields['operations'] = json.dumps(body)
	
	# Handle file mappings if files are specified
	if hasattr(args, 'files') and args.files:
		# Build the map object for file uploads
		file_map = {}
		for i, (field_name, file_path) in enumerate(args.files):
			file_index = str(i + 1)
			file_map[file_index] = [field_name]
			
			# Read file content
			try:
				with open(file_path, 'rb') as f:
					file_content = f.read()
				files.append((file_index, (os.path.basename(file_path), file_content, 'application/octet-stream')))
			except IOError as e:
				print(f"ERROR: Could not read file {file_path}: {e}")
				return
				
		# Add the map field
		form_fields['map'] = json.dumps(file_map)
	
	# Test mode - just print the request structure
	if params.get("t") == True:
		print("Multipart form data request:")
		if params.get("p") == True:
			print(f"Operations: {json.dumps(json.loads(form_fields.get('operations')), indent=2)}")
		else:
			print(f"Operations: {form_fields.get('operations')}")
		if 'map' in form_fields:
			print(f"Map: {form_fields.get('map')}")
		if files:
			print(f"Files: {[f[0] + ': ' + f[1][0] for f in files]}")
		return None
	
	# Perform the multipart request
	try:
		return sendMultipartRequest(configuration, form_fields, files, params)
	except Exception as e:
		# Safely handle exception string conversion
		try:
			error_str = str(e)
		except Exception:
			error_str = f"Exception of type {type(e).__name__}"
		
		if params.get("v") == True:
			import traceback
			print(f"ERROR: Failed to send multipart request: {error_str}")
			traceback.print_exc()
		else:
			print(f"ERROR: Failed to send multipart request: {error_str}")
		return None

def get_private_help(command_name, command_config):
	"""Generate comprehensive help text for a private command"""
	usage = f"catocli private {command_name}"
	
	# Create comprehensive JSON example with all arguments (excluding accountId)
	if 'arguments' in command_config:
		json_example = {}
		for arg in command_config['arguments']:
			arg_name = arg.get('name')
			# Skip accountId since it's handled by standard -accountID CLI argument
			if arg_name and arg_name.lower() != 'accountid':
				if 'example' in arg:
					# Use explicit example if provided
					json_example[arg_name] = arg['example']
				elif 'default' in arg:
					# Use default value if available
					json_example[arg_name] = arg['default']
				else:
					# Generate placeholder based on type
					arg_type = arg.get('type', 'string')
					if arg_type == 'string':
						json_example[arg_name] = f"<{arg_name}>"
					elif arg_type == 'object':
						if 'struct' in arg:
							# Use struct definition
							json_example[arg_name] = arg['struct']
						else:
							json_example[arg_name] = {}
					else:
						json_example[arg_name] = f"<{arg_name}>"
					
		if json_example:
			# Format JSON nicely for readability in help
			json_str = json.dumps(json_example, indent=2)
			usage += f" '{json_str}'"
	
	# Add common options
	usage += " [-t] [-v] [-p]"
	
	# Add command-specific arguments with descriptions (excluding accountId)
	if 'arguments' in command_config:
		filtered_args = [arg for arg in command_config['arguments'] if arg.get('name', '').lower() != 'accountid']
		if filtered_args:
			usage += "\n\nArguments:"
			for arg in filtered_args:
				arg_name = arg.get('name')
				arg_type = arg.get('type', 'string')
				arg_default = arg.get('default')
				arg_example = arg.get('example')
				
				if arg_name:
					usage += f"\n  --{arg_name}: {arg_type}"
					if arg_default is not None:
						usage += f" (default: {arg_default})"
					if arg_example is not None and arg_example != arg_default:
						usage += f" (example: {json.dumps(arg_example) if isinstance(arg_example, (dict, list)) else arg_example})"
	
	# Add standard accountID information
	usage += "\n\nStandard Arguments:"
	usage += "\n  -accountID: Account ID (taken from profile, can be overridden)"
	
	# Add payload file info if available
	if 'payloadFilePath' in command_config:
		usage += f"\n\nPayload template: {command_config['payloadFilePath']}"
	
	# Add batch processing info if configured
	if 'batchSize' in command_config:
		usage += f"\nBatch size: {command_config['batchSize']}"
		if 'paginationParam' in command_config:
			usage += f" (pagination: {command_config['paginationParam']})"
	
	return usage


def load_payload_template(command_config):
	"""Load and return the GraphQL payload template for a private command"""
	try:
		payload_path = command_config.get('payloadFilePath')
		if not payload_path:
			raise ValueError(f"Missing payloadFilePath in command configuration")
		
		# Construct the full path relative to the settings directory
		settings_dir = os.path.expanduser("~/.cato")
		full_payload_path = os.path.join(settings_dir, payload_path)
		
		# Load the payload file using the standard JSON loading mechanism
		try:
			with open(full_payload_path, 'r') as f:
				return json.load(f)
		except FileNotFoundError:
			raise ValueError(f"Payload file not found: {full_payload_path}")
		except json.JSONDecodeError as e:
			raise ValueError(f"Invalid JSON in payload file {full_payload_path}: {e}")
	except Exception as e:
		raise ValueError(f"Failed to load payload template: {e}")


def set_nested_value(obj, path, value):
	"""Set a value at a nested path in an object using jQuery-style JSON path syntax
	
	Supports:
	- Simple dot notation: 'a.b.c'
	- Array access: 'a.b[0].c' or 'a.b[0]'
	- Mixed paths: 'variables.filters[0].search'
	- Deep nesting: 'data.results[0].items[1].properties.name'
	"""
	import re
	
	# Parse the path into components handling both dot notation and array indices
	# Split by dots first, then handle array indices
	path_parts = []
	for part in path.split('.'):
		# Check if this part contains array notation like 'items[0]'
		array_matches = re.findall(r'([^\[]+)(?:\[(\d+)\])?', part)
		for match in array_matches:
			key, index = match
			if key:  # Add the key part
				path_parts.append(key)
			if index:  # Add the array index part
				path_parts.append(int(index))
	
	current = obj
	
	# Navigate to the parent of the target location
	for i, part in enumerate(path_parts[:-1]):
		next_part = path_parts[i + 1]
		
		if isinstance(part, int):
			# Current part is an array index
			if not isinstance(current, list):
				raise ValueError(f"Expected array at path component {i}, got {type(current).__name__}")
			
			# Extend array if necessary
			while len(current) <= part:
				current.append(None)
			
			# Initialize the array element if it doesn't exist
			if current[part] is None:
				if isinstance(next_part, int):
					current[part] = []  # Next part is array index, so create array
				else:
					current[part] = {}  # Next part is object key, so create object
			
			current = current[part]
			
		else:
			# Current part is an object key
			if not isinstance(current, dict):
				raise ValueError(f"Expected object at path component {i}, got {type(current).__name__}")
			
			# Create the key if it doesn't exist
			if part not in current:
				if isinstance(next_part, int):
					current[part] = []  # Next part is array index, so create array
				else:
					current[part] = {}  # Next part is object key, so create object
			
			current = current[part]
	
	# Set the final value
	final_part = path_parts[-1]
	if isinstance(final_part, int):
		# Final part is an array index
		if not isinstance(current, list):
			raise ValueError(f"Expected array at final path component, got {type(current).__name__}")
		
		# Extend array if necessary
		while len(current) <= final_part:
			current.append(None)
		
		current[final_part] = value
	else:
		# Final part is an object key
		if not isinstance(current, dict):
			raise ValueError(f"Expected object at final path component, got {type(current).__name__}")
		
		current[final_part] = value


def apply_template_variables(template, variables, private_config):
	"""Apply variables to the template using path-based insertion and template replacement"""
	if not template or not isinstance(template, dict):
		return template
	
	# Make a deep copy to avoid modifying the original
	import copy
	result = copy.deepcopy(template)
	
	# First, handle path-based variable insertion from private_config
	if private_config and 'arguments' in private_config:
		for arg in private_config['arguments']:
			arg_name = arg.get('name')
			arg_paths = arg.get('path', [])
			
			if arg_name and arg_name in variables and arg_paths:
				# Insert the variable value at each specified path
				for path in arg_paths:
					try:
						set_nested_value(result, path, variables[arg_name])
					except Exception as e:
						# If path insertion fails, continue to template replacement
						pass
	
	# Second, handle traditional template variable replacement as fallback
	def traverse_and_replace(obj, path=""):
		if isinstance(obj, dict):
			for key, value in list(obj.items()):
				new_path = f"{path}.{key}" if path else key
				
				# Check if this is a template variable (string that starts with '{{')
				if isinstance(value, str) and value.startswith('{{') and value.endswith('}}'):
					# Extract variable name
					var_name = value[2:-2].strip()
					
					# Replace with actual value if available
					if var_name in variables:
						obj[key] = variables[var_name]
				
				# Recursively process nested objects
				else:
					traverse_and_replace(value, new_path)
					
		elif isinstance(obj, list):
			for i, item in enumerate(obj):
				traverse_and_replace(item, f"{path}[{i}]")
	
	traverse_and_replace(result)
	return result


def createPrivateRequest(args, configuration):
	"""Handle private command execution using GraphQL payload templates"""
	params = vars(args)
	
	# Get the private command configuration
	private_command = params.get('private_command')
	private_config = params.get('private_config')
	
	if not private_command or not private_config:
		print("ERROR: Missing private command configuration")
		return None
	
	# Load private settings and apply ONLY for private commands
	try:
		settings_file = os.path.expanduser("~/.cato/settings.json")
		with open(settings_file, 'r') as f:
			private_settings = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		private_settings = {}
	
	# Override endpoint if specified in private settings
	if 'baseUrl' in private_settings:
		configuration.host = private_settings['baseUrl']
	
	# Add custom headers from private settings
	if 'headers' in private_settings and isinstance(private_settings['headers'], dict):
		if not hasattr(configuration, 'custom_headers'):
			configuration.custom_headers = {}
		for key, value in private_settings['headers'].items():
			configuration.custom_headers[key] = value
	
	# Parse input JSON variables
	try:
		variables = json.loads(params.get('json', '{}'))
	except ValueError as e:
		print(f"ERROR: Invalid JSON input: {e}")
		return None
	
	# Apply default values from settings configuration first
	for arg in private_config.get('arguments', []):
		arg_name = arg.get('name')
		if arg_name and 'default' in arg:
			variables[arg_name] = arg['default']
	
	# Apply profile account ID as fallback (lower priority than settings defaults)
	# Only apply if accountId is not already set by settings defaults
	if configuration and hasattr(configuration, 'accountID'):
		if 'accountID' not in variables and 'accountId' not in variables:
			# Use both naming conventions to support different payload templates
			variables['accountID'] = configuration.accountID
			variables['accountId'] = configuration.accountID
		# If accountId/accountID exists but not the other variation, add both
		elif 'accountID' in variables and 'accountId' not in variables:
			variables['accountId'] = variables['accountID']
		elif 'accountId' in variables and 'accountID' not in variables:
			variables['accountID'] = variables['accountId']
	
	# Apply CLI argument values (highest priority - overrides everything)
	for arg in private_config.get('arguments', []):
		arg_name = arg.get('name')
		if arg_name:
			# Handle special case for accountId - CLI uses -accountID but config uses accountId
			if arg_name.lower() == 'accountid':
				if hasattr(args, 'accountID') and getattr(args, 'accountID') is not None:
					arg_value = getattr(args, 'accountID')
					variables['accountID'] = arg_value
					variables['accountId'] = arg_value
				elif hasattr(args, 'accountId') and getattr(args, 'accountId') is not None:
					arg_value = getattr(args, 'accountId')
					variables['accountID'] = arg_value
					variables['accountId'] = arg_value
			# Handle other arguments normally
			else:
				if hasattr(args, arg_name):
					arg_value = getattr(args, arg_name)
					if arg_value is not None:
						variables[arg_name] = arg_value
	
	# Load the payload template
	try:
		payload_template = load_payload_template(private_config)
	except ValueError as e:
		print(f"ERROR: {e}")
		return None
	
	# Apply variables to the template using path-based insertion
	body = apply_template_variables(payload_template, variables, private_config)
	
	# Test mode - just print the request
	if params.get('t'):
		if params.get('p'):
			print(json.dumps(body, indent=2, sort_keys=True))
		else:
			print(json.dumps(body))
		return None
	
	# Execute the GraphQL request using custom method (no User-Agent header)
	try:
		return sendPrivateGraphQLRequest(configuration, body, params)
	except Exception as e:
		return e


def sendMultipartRequest(configuration, form_fields, files, params):
	"""Send a multipart/form-data request directly using urllib3"""
	import urllib3
	
	# Create pool manager
	pool_manager = urllib3.PoolManager(
		cert_reqs='CERT_NONE' if not getattr(configuration, 'verify_ssl', False) else 'CERT_REQUIRED'
	)
	
	# Prepare form data
	fields = []
	for key, value in form_fields.items():
		fields.append((key, value))
	
	for file_key, (filename, content, content_type) in files:
		fields.append((file_key, (filename, content, content_type)))
	
	# Encode multipart data
	body_data, content_type = encode_multipart_formdata(fields)
	
	# Prepare headers
	headers = {
		'Content-Type': content_type,
		'User-Agent': f"Cato-CLI-v{getattr(configuration, 'version', 'unknown')}"
	}
	
	# Add API key if not using headers file or custom headers
	using_custom_headers = hasattr(configuration, 'custom_headers') and configuration.custom_headers
	if not using_custom_headers and hasattr(configuration, 'api_key') and hasattr(configuration, 'api_key') and configuration.api_key and 'x-api-key' in configuration.api_key:
		headers['x-api-key'] = configuration.api_key['x-api-key']
	
	# Add custom headers
	if using_custom_headers:
		headers.update(configuration.custom_headers)
	
	# Verbose output
	if params.get("v") == True:
		print(f"Host: {getattr(configuration, 'host', 'unknown')}")
		masked_headers = headers.copy()
		if 'x-api-key' in masked_headers:
			masked_headers['x-api-key'] = '***MASKED***'
		print(f"Request Headers: {json.dumps(masked_headers, indent=4, sort_keys=True)}")
		print(f"Content-Type: {content_type}")
		print(f"Form fields: {list(form_fields.keys())}")
		print(f"Files: {[f[0] for f in files]}\n")
	
	try:
		# Make the request
		resp = pool_manager.request(
			'POST',
			getattr(configuration, 'host', 'https://api.catonetworks.com/api/v1/graphql'),
			body=body_data,
			headers=headers
		)
		
		# Parse response
		if resp.status < 200 or resp.status >= 300:
			reason = resp.reason if resp.reason is not None else "Unknown Error"
			error_msg = f"HTTP {resp.status}: {reason}"
			if resp.data:
				try:
					error_msg += f"\n{resp.data.decode('utf-8')}"
				except Exception:
					error_msg += f"\n{resp.data}"
			print(f"ERROR: {error_msg}")
			return None
		
		try:
			response_data = json.loads(resp.data.decode('utf-8'))
		except json.JSONDecodeError:
			response_data = resp.data.decode('utf-8')
		
		return [response_data]
		
	except Exception as e:
		# Safely handle exception string conversion
		try:
			error_str = str(e)
		except Exception:
			error_str = f"Exception of type {type(e).__name__}"
		print(f"ERROR: Network/request error: {error_str}")
		return None


def sendPrivateGraphQLRequest(configuration, body, params):
	"""Send a GraphQL request for private commands without User-Agent header"""
	import urllib3
	
	# Create pool manager
	pool_manager = urllib3.PoolManager(
		cert_reqs='CERT_NONE' if not getattr(configuration, 'verify_ssl', False) else 'CERT_REQUIRED'
	)
	
	# Prepare headers WITHOUT User-Agent
	headers = {
		'Content-Type': 'application/json'
	}
	
	# Add API key if not using headers file or custom headers
	using_custom_headers = hasattr(configuration, 'custom_headers') and configuration.custom_headers
	if not using_custom_headers and hasattr(configuration, 'api_key') and configuration.api_key and 'x-api-key' in configuration.api_key:
		headers['x-api-key'] = configuration.api_key['x-api-key']
	
	# Add custom headers
	if using_custom_headers:
		headers.update(configuration.custom_headers)
	
	# Encode headers to handle Unicode characters properly
	encoded_headers = {}
	for key, value in headers.items():
		# Ensure header values are properly encoded as strings
		if isinstance(value, str):
			# Replace problematic Unicode characters that can't be encoded in latin-1
			value = value.encode('utf-8', errors='replace').decode('latin-1', errors='replace')
		encoded_headers[key] = value
	headers = encoded_headers
	
	# Verbose output
	if params.get("v") == True:
		print(f"Host: {getattr(configuration, 'host', 'unknown')}")
		masked_headers = headers.copy()
		if 'x-api-key' in masked_headers:
			masked_headers['x-api-key'] = '***MASKED***'
		# Also mask Cookie for privacy
		if 'Cookie' in masked_headers:
			masked_headers['Cookie'] = '***MASKED***'
		print(f"Request Headers: {json.dumps(masked_headers, indent=4, sort_keys=True)}")
		print(f"Request Data: {json.dumps(body, indent=4, sort_keys=True)}\n")
	
	# Prepare request body
	body_data = json.dumps(body).encode('utf-8')
	
	try:
		# Make the request
		resp = pool_manager.request(
			'POST',
			getattr(configuration, 'host', 'https://api.catonetworks.com/api/v1/graphql'),
			body=body_data,
			headers=headers
		)
		
		# Parse response
		if resp.status < 200 or resp.status >= 300:
			reason = resp.reason if resp.reason is not None else "Unknown Error"
			error_msg = f"HTTP {resp.status}: {reason}"
			if resp.data:
				try:
					error_msg += f"\n{resp.data.decode('utf-8')}"
				except Exception:
					error_msg += f"\n{resp.data}"
			print(f"ERROR: {error_msg}")
			return None
		
		try:
			response_data = json.loads(resp.data.decode('utf-8'))
		except json.JSONDecodeError:
			response_data = resp.data.decode('utf-8')
		
		# Return in the same format as the regular API client
		return [response_data]
		
	except Exception as e:
		# Safely handle exception string conversion
		try:
			error_str = str(e)
		except Exception:
			error_str = f"Exception of type {type(e).__name__}"
		print(f"ERROR: Network/request error: {error_str}")
		return None
