import codecs
import json
import os
import sys
from graphql_client import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
import pprint
import uuid
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
	if "accountId" in operation["args"]:
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
