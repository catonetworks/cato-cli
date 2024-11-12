import codecs
import json
import os
import sys
from graphql_client import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
import pprint

def createRequest(args, configuration):
	params = vars(args)
	instance = CallApi(ApiClient(configuration))
	operationName = params["operation_name"]
	operation = loadJSON("models/"+operationName+".json")
	try:
		variablesObj = json.loads(params["json"])	
	except ValueError as e:
		print("ERROR: Query argument must be valid json in quotes. ",e,'\n\nExample: \'{"yourKey":"yourValue"}\'')
		exit()
	if "accountId" in operation["args"]:
		variablesObj["accountId"] = configuration.accountID
	else:
		variablesObj["accountID"] = configuration.accountID
	isOk, invalidVars, message = validateArgs(variablesObj,operation)
	if isOk==True:
		body = generateGraphqlPayload(variablesObj,operation,operationName)
		if params["t"]==True:
			if params["p"]==True:
				print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
			else:
				print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
			return None
		else:
			try:
				return instance.call_api(body,params)
			except ApiException as e:
				return e
	else:
		print("ERROR: "+message,", ".join(invalidVars))

def querySiteLocation(args, configuration):
	params = vars(args)
	operationName = params["operation_name"]
	operation = loadJSON("models/"+operationName+".json")
	try:
		variablesObj = json.loads(params["json"])	
	except ValueError as e:
		print("ERROR: Query argument must be valid json in quotes. ",e,'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	if not variablesObj.get("filters"):
		print("ERROR: Missing argument, must include filters array. ",e,'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	if not isinstance(variablesObj.get("filters"), list):
		print("ERROR: Invalid argument, must include filters array. ",e,'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
		exit()
	requiredFields = ["search","field","operation"]
	for filter in variablesObj["filters"]:
		if not isinstance(filter, dict):
			print("ERROR: Invalid filter '"+str(filter)+"', filters must be valid json and include 'search', 'field', and 'operation'. ",'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'',type(filter))
			exit()	
		for param in filter:
			if param not in requiredFields:
				print("ERROR: Invalid field '"+param+"', filters must include 'search', 'field', and 'operation'. ",'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
				exit()	
	for filter in variablesObj["filters"]:
		for param in filter:
			val = filter.get(param)
			if param=="search" and (not isinstance(val, str) or len(val)<3):
				print("ERROR: Invalid search '"+val+"', must be a string value and at least 3 characters in lengh. ",'\n\nExample: \'{filters:[{"search": "Your city here","field":"city","opeation":"exact"}}\'')
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
	module_dir_ary = os.path.dirname(__file__).split("/")
	del module_dir_ary[-1]
	del module_dir_ary[-1]
	module_dir = "/".join(module_dir_ary)
	try:
		with open(module_dir+'/'+file, 'r') as data:
			CONFIG = json.load(data)
			return CONFIG
	except:
		logging.warning("File \""+module_dir+'/'+file+"\" not found.")
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
		responseArgStr += indent + field_name
		if field.get("args") and not isinstance(field['args'], list):
			if (len(list(field['args'].keys()))>0):
				argsPresent = False
				argStr = " ( "
				for argName in field['args']:
					arg = field['args'][argName]
					if arg["varName"] in variablesObj:
						argStr += arg['responseStr'] + " "
						argsPresent = True
				argStr += ") "
				if argsPresent==True:
					responseArgStr += argStr
		if field.get("type") and field['type'].get('definition') and field['type']['definition']['fields'] is not None:
			responseArgStr += " {\n"
			for subfieldIndex in field['type']['definition']['fields']:
				subfield = field['type']['definition']['fields'][subfieldIndex]
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
		if field.get('type') and field['type'].get('definition') and field['type']['definition'].get('inputFields'):
			responseArgStr += " {\n"
			for subfieldName in field['type']['definition'].get('inputFields'):
				subfield = field['type']['definition']['inputFields'][subfieldName]
				subfield_name = subfield['alias'] if 'alias' in subfield else subfield['name']
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
		responseArgStr += "\n"
	return responseArgStr
