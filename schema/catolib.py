#!/usr/bin/python
import datetime
import json
import ssl
import sys
import time
import urllib.parse
import urllib.request
import logging
from optparse import OptionParser
import os
import sys
import copy

api_call_count = 0
start = datetime.datetime.now()
catoApiIntrospection = {
	"enums": {},
	"scalars": {},
	"objects": {},
	"input_objects": {},
	"unions": {},
	"interfaces": {},
	"unknowns": {}
}
catoApiSchema = {
	"query": {},
	"mutation": {}
}

def initParser():
	if "CATO_TOKEN" not in os.environ:
		print("Missing authentication, please set the CATO_TOKEN environment variable with your api key.")
		exit()
	
	# Process options
	parser = OptionParser()
	parser.add_option("-I", dest="ID", help="Account ID")
	parser.add_option("-P", dest="prettify", action="store_true", help="Prettify output")
	parser.add_option("-p", dest="print_entities", action="store_true", help="Print entity records")
	parser.add_option("-v", dest="verbose", action="store_true", help="Print debug info")
	(options, args) = parser.parse_args()
	options.api_key = os.getenv("CATO_TOKEN")
	if options.ID is None is None:
		parser.print_help()
		sys.exit()
	if options.verbose:
		logging.getLogger().setLevel(logging.DEBUG)
	else:
		logging.getLogger().setLevel(logging.INFO)
	return options

def loadJSON(file):
	CONFIG = {}
	try:
		with open(file, 'r') as data:
			CONFIG = json.load(data)
			logging.warning("Loaded "+file+" data")
			return CONFIG
	except:
		logging.warning("File \""+file+"\" not found.")
		exit()

def writeFile(fileName, data):
	open(fileName, 'w+').close()
	file=open(fileName,"w+")
	file.write(data)

def openFile(fileName, readMode="rt"):
	try:
		with open(fileName, readMode) as f:
			fileTxt = f.read()
		f.closed
		return fileTxt
	except:
		print('[ERROR] File path "'+fileName+'" in csv not found, or script unable to read.')
		exit()

############ parsing schema ############

def parseSchema(schema):
	mutationOperationsTMP = {}
	queryOperationsTMP = {}
	for i, type in enumerate(schema["data"]["__schema"]["types"]):
		if type["kind"] == "ENUM":
			catoApiIntrospection["enums"][type["name"]] = copy.deepcopy(type)
		elif type["kind"] == "SCALAR":
			catoApiIntrospection["scalars"][type["name"]] = copy.deepcopy(type)
		elif type["kind"] == "INPUT_OBJECT":
			catoApiIntrospection["input_objects"][type["name"]] = copy.deepcopy(type)
		elif type["kind"] == "INTERFACE":
			catoApiIntrospection["interfaces"][type["name"]] = copy.deepcopy(type)
		elif type["kind"] == "UNION":
			catoApiIntrospection["unions"][type["name"]] = copy.deepcopy(type)
		elif type["kind"] == "OBJECT":
			if type["name"] == "Query":
				for field in type["fields"]:
					if field["name"] =="xdr":
						queryOperationsTMP[field["name"]] = copy.deepcopy(field)
					else:
						catoApiSchema["query"]["query."+field["name"]] = copy.deepcopy(field)
						# catoParserMapping["query"][field["name"]]
			elif type["name"] == "Mutation":
				for field in type["fields"]:
					mutationOperationsTMP[field["name"]] = copy.deepcopy(field)
			else:
				catoApiIntrospection["objects"][type["name"]] = copy.deepcopy(type)
	
	for queryType in queryOperationsTMP:
		parentQueryOperationType = copy.deepcopy(queryOperationsTMP[queryType])
		getChildOperations("query", parentQueryOperationType, parentQueryOperationType, "query." + queryType)
	
	for mutationType in mutationOperationsTMP:
		parentMutationOperationType = copy.deepcopy(mutationOperationsTMP[mutationType])
		getChildOperations("mutation", parentMutationOperationType, parentMutationOperationType, "mutation." + mutationType)

	for operationType in catoApiSchema:
		for operationName in catoApiSchema[operationType]:
			# if operationName=="query.xdr.stories":
			childOperations = catoApiSchema[operationType][operationName]["childOperations"].keys() if "childOperations" in catoApiSchema[operationType][operationName] and catoApiSchema[operationType][operationName]!=None else []
			parsedOperation = parseOperation(catoApiSchema[operationType][operationName],childOperations)
			parsedOperation = getOperationArgs(parsedOperation["type"]["definition"],parsedOperation)
			parsedOperation["path"] = operationName
			for argName in parsedOperation["args"]:
				arg = parsedOperation["args"][argName]
				parsedOperation["operationArgs"][arg["varName"]] = arg
			parsedOperation["variablesPayload"] = generateExampleVariables(parsedOperation)
			writeFile("../models/"+operationName+".json",json.dumps(parsedOperation, indent=4, sort_keys=True))
			writeFile("../queryPayloads/"+operationName+".json",json.dumps(generateGraphqlPayload(parsedOperation["variablesPayload"],parsedOperation,operationName),indent=4,sort_keys=True))
			payload = generateGraphqlPayload(parsedOperation["variablesPayload"],parsedOperation,operationName)
			writeFile("../queryPayloads/"+operationName+".txt",payload["query"])

def getChildOperations(operationType, curType, parentType, parentPath):
	# Parse fields for nested args to map out all child operations
	# This will separate fields like stories and story for query.xdr, 
	# and all fields which are actually sub operations from mutation.internetFirewall, etc 
	if "childOperations" not in parentType:
		parentType["childOperations"] = {}
	curOfType = None
	if "kind" in curType:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["kind"].lower() + "s"][curType["name"]])
	elif "type" in curType and curType["type"]["ofType"]==None:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["type"]["kind"].lower() + "s"][curType["type"]["name"]])
	elif "type" in curType and curType["type"]["ofType"]["ofType"]==None:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["type"]["ofType"]["kind"].lower() + "s"][curType["type"]["ofType"]["name"]])
	elif "type" in curType and curType["type"]["ofType"]["ofType"]["ofType"]==None:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["type"]["ofType"]["ofType"]["kind"].lower() + "s"][curType["type"]["ofType"]["ofType"]["name"]])
	elif "type" in curType and curType["type"]["ofType"]["ofType"]["ofType"]["ofType"]==None:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["type"]["ofType"]["ofType"]["ofType"]["kind"].lower() + "s"][curType["type"]["ofType"]["ofType"]["ofType"]["name"]])
	else:
		curOfType = copy.deepcopy(catoApiIntrospection[curType["type"]["ofType"]["ofType"]["ofType"]["ofType"]["kind"].lower() + "s"][curType["type"]["ofType"]["ofType"]["ofType"]["ofType"]["name"]])
	hasChildren = False

	if "fields" in curOfType and curOfType["fields"] != None:
		parentFields = []
		for field in curOfType["fields"]:
			curFieldObject = copy.deepcopy(field)
			if "args" in curFieldObject and len(curFieldObject["args"])>0:
				hasChildren = True
				curParentType = copy.deepcopy(parentType)
				curFieldObject["args"] = getNestedArgDefinitions(curFieldObject["args"], curFieldObject["name"],None,None)
				curParentType["childOperations"][curFieldObject["name"]] = curFieldObject
				getChildOperations(operationType, curFieldObject, curParentType, parentPath + "." + curFieldObject["name"])
	if not hasChildren:
		catoApiSchema[operationType][parentPath] = parentType

def getNestedArgDefinitions(argsAry, parentParamPath, childOperations, parentFields):
	newArgsList = {}
	for arg in argsAry:
		curParamPath = renderCamelCase(arg["name"]) if (parentParamPath == None or parentParamPath == "") else parentParamPath.replace("___",".") + "." + renderCamelCase(arg["name"])
		if "path" in arg and '.' not in arg["path"]:
			arg["child"] = True
			arg["parent"] = arg["path"]		
		arg["type"] = getOfType(arg["type"], { "non_null": False, "kind": [], "name": None }, curParamPath, childOperations, parentFields)
		arg["path"] = curParamPath
		arg["id_str"] = curParamPath.replace(".","___")
		if isinstance(arg["type"]["kind"], list):
			arg["required"] = True if arg["type"]["kind"][0] == "NON_NULL" else False
		else:
			arg["required"] = True if arg["type"]["kind"] == "NON_NULL" else False
		required1 = "!" if arg["required"] else ""
		required2 = "!" if "NON_NULL" in arg["type"]["kind"][1:] else ""
		if "SCALAR" in arg["type"]["kind"] or "ENUM" in arg["type"]["kind"]:
			arg["varName"] = renderCamelCase(arg["name"])
			# arg["id_str"] = arg["varName"]
		else:
			arg["varName"] = renderCamelCase(arg["type"]["name"])
		arg["responseStr"] = arg["name"] + ":$" + arg["varName"] + " "
		if "LIST" in arg["type"]["kind"]:
			arg["requestStr"] = "$" + arg["varName"] + ":" + "[" + arg["type"]["name"] + required2 + "]" + required1 + " "
		else:
			arg["requestStr"] = "$" + arg["varName"] + ":" + arg["type"]["name"] + required1 + " "
		newArgsList[arg["id_str"]] = arg
	# print("getNestedArgDefinitions()",newArgsList.keys())
	return newArgsList

def getOfType(curType, ofType, parentParamPath, childOperations, parentFields):
	ofType["kind"].append(copy.deepcopy(curType["kind"]))
	curParamPath = "" if (parentParamPath == None) else parentParamPath + "___"
	if curType["ofType"] != None:
		ofType = getOfType(copy.deepcopy(curType["ofType"]), ofType, parentParamPath,childOperations,parentFields)
	else:
		ofType["name"] = curType["name"]	
	parentFields = []
	if "definition" in ofType and "fields" in ofType["definition"] and ofType["definition"]["fields"]!=None:
		for fieldName in ofType["definition"]["fields"]:
			field = ofType["definition"]["fields"][fieldName]
			parentFields.append(field["name"])			
	if "INPUT_OBJECT" in ofType["kind"]:
		ofType["indexType"] = "input_object"
		ofType["definition"] = copy.deepcopy(catoApiIntrospection["input_objects"][ofType["name"]])
		if ofType["definition"]["inputFields"] != None:
			ofType["definition"]["inputFields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["inputFields"]), curParamPath, childOperations, parentFields)
	elif "UNION" in ofType["kind"]:
		ofType["indexType"] = "interface"
		ofType["definition"] = copy.deepcopy(catoApiIntrospection["unions"][ofType["name"]])
		if ofType["definition"]["possibleTypes"] != None:
			ofType["definition"]["possibleTypes"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["possibleTypes"]), curParamPath,childOperations, parentFields)
			# strip out each nested interface attribute from parent oftype fields, 
			# this is to prevent duplicate fields causing the query to fail
			for interfaceName in ofType["definition"]["possibleTypes"]:
				possibleType = ofType["definition"]["possibleTypes"][interfaceName]
				if ofType["definition"]["fields"]!=None:
					for fieldName in ofType["definition"]["fields"]:
						field = ofType["definition"]["fields"][fieldName]
						nestedFieldPath = parentParamPath + interfaceName + "___" + field["name"]
						# aliasLogic
						# if field["name"] in parentFields:
						# 	field["alias"] = renderCamelCase(interfaceName+"."+field["name"])+": "+field["name"]
						# 	if "SCALAR" in field["type"]["kind"] or "ENUM" in field["type"]["kind"]:
						# 		possibleType["fields"][nestedFieldPath]["alias"] = renderCamelCase(interfaceName+"."+field["name"])+": "+field["name"]
						# 	else: 
						# 		possibleType["fields"][nestedFieldPath]["alias"] = renderCamelCase(field["type"]["name"])+": "+field["name"]
				ofType["definition"]["possibleTypes"][interfaceName] = copy.deepcopy(possibleType)
	elif "OBJECT" in ofType["kind"]:
		ofType["indexType"] = "object"
		ofType["definition"] = copy.deepcopy(catoApiIntrospection["objects"][ofType["name"]])
		if ofType["definition"]["fields"] != None and childOperations!=None:
			ofType["definition"]["fields"] = checkForChildOperation(copy.deepcopy(ofType["definition"]["fields"]),childOperations)
			ofType["definition"]["fields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["fields"]), curParamPath,childOperations, parentFields)
		if ofType["definition"]["interfaces"] != None:
			ofType["definition"]["interfaces"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["interfaces"]), curParamPath,childOperations, parentFields)
	elif "INTERFACE" in ofType["kind"]:
		ofType["indexType"] = "interface"
		ofType["definition"] = copy.deepcopy(catoApiIntrospection["interfaces"][ofType["name"]])
		if ofType["definition"]["fields"] != None:
			ofType["definition"]["fields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["fields"]), curParamPath, childOperations, parentFields)
		if ofType["definition"]["possibleTypes"] != None:
			ofType["definition"]["possibleTypes"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["possibleTypes"]), curParamPath, childOperations, parentFields)
			for interfaceName in ofType["definition"]["possibleTypes"]:
				possibleType = copy.deepcopy(ofType["definition"]["possibleTypes"][interfaceName])
				for fieldName in ofType["definition"]["fields"]:
					field = ofType["definition"]["fields"][fieldName]
					nestedFieldPath = parentParamPath + interfaceName + "." + field["name"]
					nestedFieldPath = nestedFieldPath.replace(".","___")
					if "args" in field and len(field["args"])>0:
						field["args"] = getNestedArgDefinitions(copy.deepcopy(field["args"]), nestedFieldPath, curParamPath, parentFields)
					# aliasLogic MUST
					# CatoEndpointUser
					if field["name"] in possibleType["fields"] and possibleType["fields"][field["name"]] != None:
						# del possibleType["fields"][field["name"]]
						if "SCALAR" in field["type"]["kind"] or "ENUM" in field["type"]["kind"]:
							possibleType["fields"][field["name"]]["alias"] = renderCamelCase(interfaceName+"."+field["name"])+": "+field["name"]
						else: 
							possibleType["fields"][field["name"]]["alias"] = renderCamelCase(field["type"]["name"])+": "+field["name"]
				ofType["definition"]["possibleTypes"][interfaceName] = copy.deepcopy(possibleType)
		if ofType["definition"]["interfaces"] != None:
			ofType["definition"]["interfaces"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["interfaces"]), curParamPath,childOperations, parentFields)
	elif "ENUM" in ofType["kind"]:
		ofType["indexType"] = "enum"
		ofType["definition"] = copy.deepcopy(catoApiIntrospection["enums"][ofType["name"]])
	return ofType

def getNestedFieldDefinitions(fieldsAry, parentParamPath,childOperations, parentFields):
	newFieldsList = {}
	for field in fieldsAry:
		if isinstance(field,str):
			field = fieldsAry[field]
		curParamPath = field["name"] if (parentParamPath == None) else (parentParamPath.replace("___",".") + field["name"])
		# curParamPath = field["name"] if (parentParamPath == None) else (parentParamPath + "." + field["name"])
		field["type"] = getOfType(field["type"], { "non_null": False, "kind": [], "name": None }, curParamPath,childOperations, parentFields)
		field["path"] = curParamPath
		field["id_str"] = curParamPath.replace(".","___")
		if isinstance(field["type"]["kind"], list):
			field["required"] = True if field["type"]["kind"][0] == "NON_NULL" else False
		else:
			field["required"] = True if field["type"]["kind"] == "NON_NULL" else False
		required1 = "!" if field["required"] else ""
		required2 = "!" if field["type"]["kind"][1:] == "NON_NULL" else ""
		if "SCALAR" in field["type"]["kind"] or "ENUM" in field["type"]["kind"]:
			field["varName"] = renderCamelCase(field["name"])
			# field["id_str"] = field["varName"]
		else:
			field["varName"] = renderCamelCase(field["type"]["name"])
		field["responseStr"] = field["name"] + ":$" + field["varName"] + " "
		if "LIST" in field["type"]["kind"]:
			field["requestStr"] = "$" + field["varName"] + ":" + "[" + field["type"]["name"] + required2 + "]" + required1 + " "
		else:
			field["requestStr"] = "$" + field["varName"] + ":" + field["type"]["name"] + required1 + " "
		if "args" in field:
			field["args"] = getNestedArgDefinitions(field["args"], field["name"],childOperations, parentFields)
		## aliasLogic must
		if parentFields!=None and field["name"] in parentFields and "SCALAR" not in field["type"]["kind"]:
			# if field["name"]=="records":
			# 	raise ValueError('A very specific bad thing happened.')
				# print(json.dumps(field,indent=2,sort_keys=True))
				# print(field["path"],parentFields)
			# field["alias"] = renderCamelCase(field["type"]["name"]+"."+field["name"])+": "+field["name"]
			field["alias"] = renderCamelCase(field["type"]["name"]+"."+field["name"])+": "+field["name"]
		if "records.fields" not in field["path"]:
			newFieldsList[field["name"]] = field	
	# for (fieldPath in newFieldList) {
	# 	var field = newFieldList[fieldPath];
	# 	if (curOperationObj.fieldTypes && field.type.name != null) curOperationObj.fieldTypes[field.type.name] = true;
	# 	field.type = getOfType(field.type, { non_null: false, kind: [], name: null }, field.path);
	# }	
	return newFieldsList

def getNestedInterfaceDefinitions(possibleTypesAry, parentParamPath,childOperations, parentFields):
	curInterfaces = {}
	for possibleType in possibleTypesAry:
		if "OBJECT" in possibleType["kind"]:
			curInterfaces[possibleType["name"]] = copy.deepcopy(catoApiIntrospection["objects"][possibleType["name"]])
	# for curInterface in curInterfaces:
	# 	curParamPath = "" if parentParamPath == None else parentParamPath + curInterface["name"] + "___"
	for curInterfaceName in curInterfaces:
		curInterface = curInterfaces[curInterfaceName]
		curParamPath = "" if parentParamPath == None else parentParamPath + curInterface["name"] + "___"
		if "fields" in curInterface and curInterface["fields"] != None:
			curInterface["fields"] = getNestedFieldDefinitions(copy.deepcopy(curInterface["fields"]), curParamPath,childOperations, parentFields)
		if "inputFields" in curInterface and curInterface["inputFields"] != None:
			curInterface["inputFields"] = getNestedFieldDefinitions(copy.deepcopy(curInterface["inputFields"]), curParamPath,childOperations, parentFields)
		if "interfaces" in curInterface and curInterface["interfaces"] != None:
			curInterface["interfaces"] = getNestedInterfaceDefinitions(copy.deepcopy(curInterface["interfaces"]), curParamPath,childOperations, parentFields)
		if "possibleTypes" in curInterface and curInterface["possibleTypes"] != None:
			curInterface["possibleTypes"] = getNestedInterfaceDefinitions(copy.deepcopy(curInterface["possibleTypes"]), curParamPath,childOperations, parentFields)
	return curInterfaces

def parseOperation(curOperation,childOperations):
	if "operationArgs" not in curOperation:
		curOperation["operationArgs"] = {}
	curOperation["fieldTypes"] = {}
	curOfType = getOfType(curOperation["type"], { "non_null": False, "kind": [], "name": None }, None,childOperations,None)
	curOperation["type"] = copy.deepcopy(curOfType)
	if curOfType["name"] in catoApiIntrospection["objects"]:
		curOperation["args"] = getNestedArgDefinitions(curOperation["args"], None,childOperations,None)
		curOperation["type"]["definition"] = copy.deepcopy(catoApiIntrospection["objects"][curOperation["type"]["name"]])		
		if "fields" in curOperation["type"]["definition"] and curOperation["type"]["definition"]["fields"] != None:
			# aliasLogic
			# parentFields = []
			# for field in curOperation["type"]["definition"]["fields"]:
			# 	parentFields.append(field["name"])
			curOperation["type"]["definition"]["fields"] = checkForChildOperation(copy.deepcopy(curOperation["type"]["definition"]["fields"]),childOperations)
			curOperation["type"]["definition"]["fields"] = copy.deepcopy(getNestedFieldDefinitions(curOperation["type"]["definition"]["fields"], None,childOperations,[]))
		if "inputFields" in curOperation["type"]["definition"] and curOperation["type"]["definition"]["inputFields"] != None:
			parentFields = curOperation["type"]["definition"]["inputFields"].keys()
			curOperation["type"]["definition"]["inputFields"] = copy.deepcopy(getNestedFieldDefinitions(curOperation["type"]["definition"]["inputFields"], None,childOperations,parentFields))
	return curOperation

def checkForChildOperation(fieldsAry,childOperations):
	newFieldList = {}
	subOperation = False
	for i, field in enumerate(fieldsAry):
		if field["name"] in childOperations:
			subOperation = field
		newFieldList[field["name"]] = copy.deepcopy(field)
	if subOperation != False:
		newFieldList = {}
		newFieldList[subOperation["name"]] = subOperation
	return newFieldList

def getOperationArgs(curType,curOperation):
	if curType.get('fields'):
		for fieldName in curType["fields"]:
			field = curType["fields"][fieldName]
			## aliasLogic
			if "type" in field and "definition" in field["type"]:
				curOperation["fieldTypes"][field["type"]["definition"]["name"]] = True
				curOperation = getOperationArgs(field["type"]["definition"],curOperation)
			if "args" in field:
				for argName in field["args"]:
					arg = field["args"][argName]
					curOperation["operationArgs"][arg["varName"]] = arg
					if "type" in arg and "definition" in arg["type"]:
						curOperation = getOperationArgs(arg["type"]["definition"],curOperation)
	if curType.get('inputFields'):
		for inputFieldName in curType["inputFields"]:
			inputField = curType["inputFields"][inputFieldName]
			if "type" in inputField and "definition" in inputField["type"]:
				curOperation["fieldTypes"][inputField["type"]["definition"]["name"]] = True
				curOperation = getOperationArgs(inputField["type"]["definition"],curOperation)
			if "args" in inputField:
				for argName in inputField["args"]:
					arg = inputField["args"][argName]
					curOperation["operationArgs"][arg["varName"]] = arg
					if "type" in arg and "definition" in arg["type"]:
						curOperation = getOperationArgs(arg["type"]["definition"],curOperation)
	if curType.get('interfaces'):
		for interface in curType["interfaces"]:
			if "type" in interface and "definition" in interface["type"]:
				curOperation["fieldTypes"][interface["type"]["definition"]["name"]] = True
				curOperation = getOperationArgs(interface["type"]["definition"],curOperation)
			if "args" in interface:
				for argName in interface["args"]:
					arg = interface["args"][argName]
					curOperation["operationArgs"][arg["varName"]] = arg
					if "type" in arg and "definition" in arg["type"]:
						curOperation = getOperationArgs(arg["type"]["definition"],curOperation)
	if curType.get('possibleTypes'):
		for possibleTypeName in curType["possibleTypes"]:
			possibleType = curType["possibleTypes"][possibleTypeName]
			curOperation = getOperationArgs(possibleType,curOperation)
			if possibleType.get('fields'):
				for fieldName in possibleType["fields"]:
					field = possibleType["fields"][fieldName]
					## aliasLogic
					# if "type" in curOperation and "definition" in curOperation["type"] and "fields" in curOperation["type"]["definition"] and field["name"] in curOperation["type"]["definition"]["fields"]:
					# 	# if field["type"]["definition"]["fields"]==None or field["type"]["definition"]["inputFields"]:
					# 	# if "SCALAR" not in field["type"]["kind"] or "ENUM" not in field["type"]["kind"]:
					# 	field["alias"] = renderCamelCase(possibleTypeName+"."+field["name"])+": "+field["name"]
			if "args" in possibleType:
				for argName in possibleType["args"]:
					arg = possibleType["args"][argName]
					curOperation["operationArgs"][arg["varName"]] = arg
					if "type" in arg and "definition" in arg["type"]:
						curOperation = getOperationArgs(arg["type"]["definition"],curOperation)
	return curOperation

def renderCamelCase(pathStr):
	str = ""
	pathAry = pathStr.split(".") 
	for i, path in enumerate(pathAry):
		if i == 0:
			str += path[0].lower() + path[1:]
		else:
			str += path[0].upper() + path[1:]
	return str	

## Functions to create sample nested variable objects for cli arguments ##
def generateExampleVariables(operation):
	variablesObj = {}
	for argName in operation["operationArgs"]:
		arg = operation["operationArgs"][argName]
		if "SCALAR" in arg["type"]["kind"] or "ENUM" in arg["type"]["kind"]:
			variablesObj[arg["name"]] = renderInputFieldVal(arg)
		else:
			argTD = arg["type"]["definition"]
			variablesObj[arg["varName"]] = {}
			if "inputFields" in argTD and argTD["inputFields"] != None:
				for inputFieldName in argTD["inputFields"]:
					inputField = argTD["inputFields"][inputFieldName]
					variablesObj[arg["varName"]][inputField["varName"]] = parseNestedArgFields(inputField)
			if "fields" in argTD and argTD["fields"] != None:
				for fieldName in argTD["fields"]:
					field = argTD["fields"][fieldName]
					variablesObj[arg["varName"]][field["varName"]] = parseNestedArgFields(field)
			if "possibleTypes" in argTD and argTD["possibleTypes"] != None:
				for possibleTypeName in argTD["possibleTypes"]:
					possibleType = argTD["possibleTypes"][possibleTypeName]
					variablesObj[arg["varName"]][possibleType["varName"]] = parseNestedArgFields(possibleTypeName)
	if "accountID" in variablesObj:
		del variablesObj["accountID"]
	if "accountId" in variablesObj:
		del variablesObj["accountId"]
	return variablesObj

def parseNestedArgFields(fieldObj):
	subVariableObj = {}
	if "SCALAR" in fieldObj["type"]["kind"] or "ENUM" in fieldObj["type"]["kind"]:
		subVariableObj[fieldObj["name"]] = renderInputFieldVal(fieldObj)
	else:
		fieldTD = fieldObj["type"]["definition"]
		if "inputFields" in fieldTD and fieldTD["inputFields"] != None:
			for inputFieldName in fieldTD["inputFields"]:
				inputField = fieldTD["inputFields"][inputFieldName]
				subVariableObj[inputField["name"]] = parseNestedArgFields(inputField)
		if "fields" in fieldTD and fieldTD["fields"] != None:
			for fieldName in fieldTD["fields"]:
				field = fieldTD["fields"][fieldName]
				subVariableObj[field["name"]] = parseNestedArgFields(field)
		if "possibleTypes" in fieldTD and fieldTD["possibleTypes"] != None:
			for possibleTypeName in fieldTD["possibleTypes"]:
				possibleType = fieldTD["possibleTypes"][possibleTypeName]
				subVariableObj[possibleType["name"]] = parseNestedArgFields(possibleTypeName)
	return subVariableObj

def renderInputFieldVal(arg):
	value = "string"
	if "SCALAR" in arg["type"]["kind"]:
		if "LIST" in arg["type"]["kind"]:
			value = [arg["type"]["name"]]
		else:
			value = arg["type"]["name"]
	elif "ENUM" in arg["type"]["kind"]:
		value = "enum("+arg["type"]["name"]+")"
		# arg["type"]["definition"]["enumValues"][0]["name"]
	return value

def writeCliDriver(catoApiSchema):
	parsersIndex = {}
	for operationType in catoApiSchema:
		for operation in catoApiSchema[operationType]:
			operationNameAry = operation.split(".")
			parsersIndex[operationNameAry[0]+"_"+operationNameAry[1]] = True
	parsers = list(parsersIndex.keys())
	cliDriverStr = """
import os
import argparse
import json
import catocli
from graphql_client import Configuration
from graphql_client.api_client import ApiException
from ..parsers.parserApiClient import get_help
import traceback
import sys
sys.path.insert(0, 'vendor')
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if "CATO_TOKEN" not in os.environ:
	print("Missing authentication, please set the CATO_TOKEN environment variable with your api key.")
	exit()
CATO_TOKEN = os.getenv("CATO_TOKEN")
CATO_DEBUG = bool(os.getenv("CATO_DEBUG", False))
from ..parsers.raw import raw_parse
from ..parsers.custom import custom_parse
from ..parsers.query_siteLocation import query_siteLocation_parse
"""
	for parserName in parsers:
		cliDriverStr += "from ..parsers."+parserName+" import "+parserName+"_parse\n"

	cliDriverStr += """
configuration = Configuration()
configuration.verify_ssl = False
configuration.api_key["x-api-key"] = CATO_TOKEN
configuration.host = "{}".format(catocli.__cato_host__)
configuration.debug = CATO_DEBUG
configuration.version = "{}".format(catocli.__version__)

parser = argparse.ArgumentParser(prog='catocli', usage='%(prog)s <operationType> <operationName> [options]', description="CLI for query on CATO via API.")
parser.add_argument('--version', action='version', version=catocli.__version__)
subparsers = parser.add_subparsers()
custom_parsers = custom_parse(subparsers)
raw_parsers = subparsers.add_parser('raw', help='Raw GraphQL', usage=get_help("raw"))
raw_parser = raw_parse(raw_parsers)
query_parser = subparsers.add_parser('query', help='Query', usage='catocli query <operationName> [options]')
query_subparsers = query_parser.add_subparsers(description='valid subcommands', help='additional help')
query_siteLocation_parser = query_siteLocation_parse(query_subparsers)
mutation_parser = subparsers.add_parser('mutation', help='Mutation', usage='catocli mutation <operationName> [options]')
mutation_subparsers = mutation_parser.add_subparsers(description='valid subcommands', help='additional help')

"""
	for parserName in parsers:
		cliDriverStr += parserName+"_parser = "+parserName+"_parse("+parserName.split("_").pop(0)+"_subparsers)\n"

	cliDriverStr += """

def main(args=None):
	args = parser.parse_args(args=args)
	try:
		CATO_ACCOUNT_ID = os.getenv("CATO_ACCOUNT_ID")
		if args.func.__name__!="createRawRequest":
			if CATO_ACCOUNT_ID==None and args.accountID==None:
				print("Missing accountID, please specify an accountID:\\n")
				print('Option 1: Set the CATO_ACCOUNT_ID environment variable with the value of your account ID.')
				print('export CATO_ACCOUNT_ID="12345"\\n')
				print("Option 2: Override the accountID value as a cli argument, example:")
				print('catocli <operationType> <operationName> -accountID=12345 <json>')
				print("catocli query entityLookup -accountID=12345 '{\\\"type\\\":\\\"country\\\"}'\\n")
				exit()
			elif args.accountID!=None:
				configuration.accountID = args.accountID
			else:
				configuration.accountID = CATO_ACCOUNT_ID
		response = args.func(args, configuration)

		if type(response) == ApiException:
			print("ERROR! Status code: {}".format(response.status))
			print(response)
		else:
			if response!=None:
				print(json.dumps(response[0], sort_keys=True, indent=4))
	except Exception as e:
		if isinstance(e, AttributeError):
			print('Missing arguments. Usage: catocli <operation> -h')
			if args.v==True:
				print('ERROR: ',e)
				traceback.print_exc()
		else:
			print('ERROR: ',e)
			traceback.print_exc()
		exit(1)
"""
	writeFile("../catocli/Utils/clidriver.py",cliDriverStr)

def writeOperationParsers(catoApiSchema):
	parserMapping = {"query":{},"mutation":{}}
	## Write the raw query parser ##
	cliDriverStr =f"""
from ..parserApiClient import createRawRequest, get_help

def raw_parse(raw_parser):
	raw_parser.add_argument('json', help='Query, Variables and opertaionName in JSON format.')
	raw_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print test request preview without sending api call')
	raw_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	raw_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	raw_parser.set_defaults(func=createRawRequest,operation_name='raw')
"""
	parserPath = "../catocli/parsers/raw"
	if not os.path.exists(parserPath):
		os.makedirs(parserPath)
	writeFile(parserPath+"/__init__.py",cliDriverStr)

	## Write the siteLocation query parser ##
	cliDriverStr =f"""
from ..parserApiClient import querySiteLocation, get_help

def query_siteLocation_parse(query_subparsers):
	query_siteLocation_parser = query_subparsers.add_parser('siteLocation', 
			help='siteLocation local cli query', 
			usage=get_help("query_siteLocation"))

	query_siteLocation_parser.add_argument('json', help='Variables in JSON format.')
	query_siteLocation_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_siteLocation_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_siteLocation_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_siteLocation_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_siteLocation_parser.set_defaults(func=querySiteLocation,operation_name='query.siteLocation')
"""
	parserPath = "../catocli/parsers/query_siteLocation"
	if not os.path.exists(parserPath):
		os.makedirs(parserPath)
	writeFile(parserPath+"/__init__.py",cliDriverStr)

	for operationType in parserMapping:
		operationAry = catoApiSchema[operationType]
		for operationName in operationAry:
			parserMapping = getParserMapping(parserMapping,operationName,operationName,operationAry[operationName])
	for operationType in parserMapping:
		for operationName in parserMapping[operationType]:
			parserName = operationType+"_"+operationName
			parser = parserMapping[operationType][operationName]
			cliDriverStr = f"""
from ..parserApiClient import createRequest, get_help

def {parserName}_parse({operationType}_subparsers):
	{parserName}_parser = {operationType}_subparsers.add_parser('{operationName}', 
			help='{operationName}() {operationType} operation', 
			usage=get_help("{operationType}_{operationName}"))
"""
			if "path" in parser:
				cliDriverStr += f"""
	{parserName}_parser.add_argument('json', help='Variables in JSON format.')
	{parserName}_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	{parserName}_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	{parserName}_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	{parserName}_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	{parserName}_parser.set_defaults(func=createRequest,operation_name='{parserName.replace("_",".")}')
"""
			else:
				cliDriverStr += renderSubParser(parser,operationType+"_"+operationName)
			parserPath = "../catocli/parsers/"+parserName
			if not os.path.exists(parserPath):
				os.makedirs(parserPath)
			writeFile(parserPath+"/__init__.py",cliDriverStr)

def renderSubParser(subParser,parentParserPath):
	cliDriverStr = f"""
	{parentParserPath}_subparsers = {parentParserPath}_parser.add_subparsers()
"""
	for subOperationName in subParser:
		subOperation = subParser[subOperationName]
		subParserPath = parentParserPath.replace(".","_")+"_"+subOperationName
		cliDriverStr += f"""
	{subParserPath}_parser = {parentParserPath}_subparsers.add_parser('{subOperationName}', 
			help='{subOperationName}() {parentParserPath.split('_').pop()} operation', 
			usage=get_help("{subParserPath}"))
"""
		if "path" in subOperation:
			command = parentParserPath.replace("_"," ")+" "+subOperationName
			cliDriverStr += f"""
	{subParserPath}_parser.add_argument('json', help='Variables in JSON format.')
	{subParserPath}_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	{subParserPath}_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	{subParserPath}_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	{subParserPath}_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	{subParserPath}_parser.set_defaults(func=createRequest,operation_name='{subOperation["path"]}')
"""
		else:
			cliDriverStr += renderSubParser(subOperation,subParserPath)
	return cliDriverStr

def writeReadmes(catoApiSchema):
	parserMapping = {"query":{},"mutation":{}}
	
	## Write the raw query readme ##
	readmeStr = """
## CATO-CLI - raw.graphql
[Click here](https://api.catonetworks.com/documentation/) for documentation on this operation.

### Usage for raw.graphql

`catocli raw -h`

`catocli raw <json>`

`catocli raw "$(cat < rawGraphqQL.json)"`

`catocli raw '{ "query": "query operationNameHere($yourArgument:String!) { field1 field2 }", "variables": { "yourArgument": "string", "accountID": "10949" }, "operationName": "operationNameHere" } '`

`catocli raw '{ "query": "mutation operationNameHere($yourArgument:String!) { field1 field2 }", "variables": { "yourArgument": "string", "accountID": "10949" }, "operationName": "operationNameHere" } '`
"""
	parserPath = "../catocli/parsers/raw"
	if not os.path.exists(parserPath):
		os.makedirs(parserPath)
	writeFile(parserPath+"/README.md",readmeStr)
	
		## Write the query.siteLocation readme ##
	readmeStr = """

## CATO-CLI - query.siteLocation:

### Usage for query.siteLocation:

`catocli query siteLocation -h`

`catocli query siteLocation <json>`

`catocli query siteLocation "$(cat < siteLocation.json)"`

`catocli query siteLocation '{"filters":[{"search": "Your city here","field":"city","operation":"exact"}]}'`

`catocli query siteLocation '{"filters":[{"search": "Your Country here","field":"countryName","operation":"startsWith"}]}'`

`catocli query siteLocation '{"filters":[{"search": "Your stateName here","field":"stateName","operation":"endsWith"}]}'`

`catocli query siteLocation '{filters:[{"search": "Your City here","field":"city","operation":"startsWith"},{"search": "Your StateName here","field":"stateName","operation":"endsWith"},{"search": "Your Country here","field":"countryName","operation":"contains"}}'`

#### Operation Arguments for query.siteLocation ####
`accountID` [ID] - (required) Unique Identifier of Account. 
`filters[]` [Array] - (optional) Array of objects consisting of `search`, `field` and `operation` attributes.
`filters[].search` [String] - (required) String to match countryName, stateName, or city specificed in `filters[].field`.
`filters[].field` [String] - (required) Specify field to match query against, defaults to look for any.  Possible values: `countryName`, `stateName`, or `city`.
`filters[].operation` [string] - (required) If a field is specified, operation to match the field value.  Possible values: `startsWith`,`endsWith`,`exact`, `contains`.
"""
	parserPath = "../catocli/parsers/query_siteLocation"
	if not os.path.exists(parserPath):
		os.makedirs(parserPath)
	writeFile(parserPath+"/README.md",readmeStr)
	
	for operationType in parserMapping:
		operationAry = catoApiSchema[operationType]
		for operationName in operationAry:
			parserMapping = getParserMapping(parserMapping,operationName,operationName,operationAry[operationName])
	for operationType in parserMapping:
		for operationName in parserMapping[operationType]:
			parserName = operationType+"_"+operationName
			parser = parserMapping[operationType][operationName]
			operationPath = operationType+"."+operationName
			operationCmd = operationType+" "+operationName
			readmeStr = f"""
## CATO-CLI - {operationPath}:
[Click here](https://api.catonetworks.com/documentation/#{operationType}-{operationName}) for documentation on this operation.

### Usage for {operationPath}:

`catocli {operationCmd} -h`
"""
			if "path" in parser:
				readmeStr += f"""
`catocli {operationCmd} <json>`

`catocli {operationCmd} "$(cat < {operationName}.json)"`

`catocli {operationCmd} '{json.dumps(parser["example"])}'`

#### Operation Arguments for {operationPath} ####
"""
				for argName in parser["args"]:
					arg = parser["args"][argName]
					readmeStr += '`'+argName+'` ['+arg["type"]+'] - '
					readmeStr += '('+arg["required"]+') '+arg["description"]+' '
					readmeStr += 'Default Value: '+str(arg["values"]) if len(arg["values"])>0 else ""
					readmeStr += "\n"
				parserPath = "../catocli/parsers/"+parserName
				if not os.path.exists(parserPath):
					os.makedirs(parserPath)
				writeFile(parserPath+"/README.md",readmeStr)
			else:
				parserPath = "../catocli/parsers/"+parserName
				if not os.path.exists(parserPath):
					os.makedirs(parserPath)
				writeFile(parserPath+"/README.md",readmeStr)
				renderSubReadme(parser,operationType,operationType+"."+operationName)

def renderSubReadme(subParser,operationType,parentOperationPath):
	for subOperationName in subParser:
		subOperation = subParser[subOperationName]
		subOperationPath = parentOperationPath+"."+subOperationName
		subOperationCmd = parentOperationPath.replace("."," ")+" "+subOperationName
		parserPath = "../catocli/parsers/"+subOperationPath.replace(".","_")
		readmeStr = f"""
## CATO-CLI - {parentOperationPath}.{subOperationName}:
[Click here](https://api.catonetworks.com/documentation/#{operationType}-{subOperationName}) for documentation on this operation.

### Usage for {subOperationPath}:

`catocli {subOperationCmd} -h`
"""
		if "path" in subOperation:
			readmeStr += f"""
`catocli {subOperationCmd} <json>`

`catocli {subOperationCmd} "$(cat < {subOperationName}.json)"`

`catocli {subOperationCmd} '{json.dumps(subOperation["example"])}'`

#### Operation Arguments for {subOperationPath} ####
"""
			for argName in subOperation["args"]:
				arg = subOperation["args"][argName]
				readmeStr += '`'+argName+'` ['+arg["type"]+'] - '
				readmeStr += '('+arg["required"]+') '+arg["description"]+' '
				readmeStr += 'Default Value: '+str(arg["values"]) if len(arg["values"])>0 else ""
				readmeStr += "\n"
			if not os.path.exists(parserPath):
				os.makedirs(parserPath)
			writeFile(parserPath+"/README.md",readmeStr)
		else:
			if not os.path.exists(parserPath):
				os.makedirs(parserPath)
			writeFile(parserPath+"/README.md",readmeStr)
			renderSubReadme(subOperation,operationType,subOperationPath)

def getParserMapping(curParser,curPath,operationFullPath,operation):
	parserObj = {
		"path":operationFullPath,
		"args":{},
		# "example":"N/A",
		"example":operation["variablesPayload"]
	}
	for argName in operation["operationArgs"]:
		arg = operation["operationArgs"][argName]
		values = []
		if "definition" in arg["type"] and "enumValues" in arg["type"]["definition"] and arg["type"]["definition"]["enumValues"]!=None:
			for enumValue in arg["type"]["definition"]["enumValues"]:
				values.append(enumValue["name"])
		parserObj["args"][arg["varName"]] = {
			"name":arg["name"],
			"description":"N/A" if arg["description"]==None else arg["description"],
			"type":arg["type"]["name"]+("[]" if "LIST" in arg["type"]["kind"] else ""),
			"required": "required" if arg["required"]==True else "optional",
			"values":values
		}
	pAry = curPath.split(".")
	pathCount = len(curPath.split("."))
	if pAry[0] not in curParser:
		curParser[pAry[0]] = {}
	if pathCount == 2:
		curParser[pAry[0]][pAry[1]] = parserObj
	else:
		if pAry[1] not in curParser[pAry[0]]:
			curParser[pAry[0]][pAry[1]] = {}
		if pathCount == 3:
			curParser[pAry[0]][pAry[1]][pAry[2]] = parserObj
		else:
			if pAry[2] not in curParser[pAry[0]][pAry[1]]:
				curParser[pAry[0]][pAry[1]][pAry[2]] = {}
			if pathCount == 4:
				curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]] = parserObj
			else:
				if pAry[3] not in curParser[pAry[0]][pAry[1]][pAry[2]]:
					curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]] = {}
				if pathCount == 5:
					curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]][pAry[4]] = parserObj
				else:
					if pAry[4] not in curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]]:
						curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]][pAry[4]] = {}
					if pathCount == 6:
						curParser[pAry[0]][pAry[1]][pAry[2]][pAry[3]][pAry[4]][pAry[5]] = parserObj
	return curParser

def send(api_key,query,variables={},operationName=None):
	headers = { 'x-api-key': api_key,'Content-Type':'application/json'}
	no_verify = ssl._create_unverified_context()
	request = urllib.request.Request(url='https://api.catonetworks.com/api/v1/graphql2',
		data=json.dumps(query).encode("ascii"),headers=headers)
	response = urllib.request.urlopen(request, context=no_verify, timeout=60)
	result_data = response.read()
	result = json.loads(result_data)
	if "errors" in result:
		logging.warning(f"API error: {result_data}")
		return False,result
	return True,result


################### adding functions local to generate dynamic payloads ####################
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
		"query":queryStr.replace("\n", " ").replace("\t", " ").replace("    ", " ").replace("   ", " ").replace("  ", " "),
		"variables":variablesObj,
		"operationName":renderCamelCase(".".join(operationAry)),
	}
	return body

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
