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
import concurrent.futures
import threading
from functools import lru_cache
import traceback

# Increase recursion limit and enable threading-safe operations
sys.setrecursionlimit(5000)
thread_local = threading.local()

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

# Thread-safe locks
schema_lock = threading.RLock()
file_write_lock = threading.RLock()

def initParser():
    if "CATO_TOKEN" not in os.environ:
        print("Missing authentication, please set the CATO_TOKEN environment variable with your api key.")
        exit()
    if "CATO_ACCOUNT_ID" not in os.environ:
        print("Missing authentication, please set the CATO_ACCOUNT_ID environment variable with your api key.")
        exit()
    
    # Process options
    parser = OptionParser()
    parser.add_option("-P", dest="prettify", action="store_true", help="Prettify output")
    parser.add_option("-p", dest="print_entities", action="store_true", help="Print entity records")
    parser.add_option("-v", dest="verbose", action="store_true", help="Print debug info")
    (options, args) = parser.parse_args()
    options.api_key = os.getenv("CATO_TOKEN")
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
    with file_write_lock:
        open(fileName, 'w+').close()
        with open(fileName, "w+") as file:
            file.write(data)

def openFile(fileName, readMode="rt"):
    try:
        with open(fileName, readMode) as f:
            fileTxt = f.read()
        return fileTxt
    except:
        # print('[ERROR] File path "'+fileName+'" in csv not found, or script unable to read.')
        exit()

############ parsing schema - THREADED VERSION ############

def parseSchema(schema):
    """Multi-threaded schema parsing with recursion depth management"""
    print("  - Loading settings and initializing...")
    
    # Load settings to get childOperationParent and childOperationObjects configuration
    settings = loadJSON("../catocli/clisettings.json")
    childOperationParent = settings.get("childOperationParent", {})
    childOperationObjects = settings.get("childOperationObjects", {})
    
    mutationOperationsTMP = {}
    queryOperationsTMP = {}
    
    print(f"• Processing {len(schema['data']['__schema']['types'])} schema types...")
    
    # Process all types - this part stays sequential as it's fast and needs to be done first
    for i, type_obj in enumerate(schema["data"]["__schema"]["types"]):
        if type_obj["kind"] == "ENUM":
            catoApiIntrospection["enums"][type_obj["name"]] = copy.deepcopy(type_obj)
        elif type_obj["kind"] == "SCALAR":
            catoApiIntrospection["scalars"][type_obj["name"]] = copy.deepcopy(type_obj)
        elif type_obj["kind"] == "INPUT_OBJECT":
            catoApiIntrospection["input_objects"][type_obj["name"]] = copy.deepcopy(type_obj)
        elif type_obj["kind"] == "INTERFACE":
            catoApiIntrospection["interfaces"][type_obj["name"]] = copy.deepcopy(type_obj)
        elif type_obj["kind"] == "UNION":
            catoApiIntrospection["unions"][type_obj["name"]] = copy.deepcopy(type_obj)
        elif type_obj["kind"] == "OBJECT":
            if type_obj["name"] == "Query":
                for field in type_obj["fields"]:
                    if field["name"] in childOperationParent:
                        queryOperationsTMP[field["name"]] = copy.deepcopy(field)
                    else:
                        catoApiSchema["query"]["query."+field["name"]] = copy.deepcopy(field)
            elif type_obj["name"] == "Mutation":
                for field in type_obj["fields"]:
                    mutationOperationsTMP[field["name"]] = copy.deepcopy(field)
            else:
                catoApiIntrospection["objects"][type_obj["name"]] = copy.deepcopy(type_obj)
    
    print("  - Basic types processed")
    
    # Process child operations in parallel
    print("  - Processing child operations...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        query_futures = []
        mutation_futures = []
        
        # Submit query operations
        for queryType in queryOperationsTMP:
            parentQueryOperationType = copy.deepcopy(queryOperationsTMP[queryType])
            future = executor.submit(
                getChildOperations,
                "query",
                parentQueryOperationType,
                parentQueryOperationType,
                "query." + queryType,
                childOperationObjects
            )
            query_futures.append((queryType, future))
        
        # Submit mutation operations
        for mutationType in mutationOperationsTMP:
            parentMutationOperationType = copy.deepcopy(mutationOperationsTMP[mutationType])
            future = executor.submit(
                getChildOperations,
                "mutation",
                parentMutationOperationType,
                parentMutationOperationType,
                "mutation." + mutationType,
                childOperationObjects
            )
            mutation_futures.append((mutationType, future))
        
        # Wait for completion
        for queryType, future in query_futures:
            try:
                future.result(timeout=120)
            except Exception as e:
                print(f"ERROR processing query {queryType}: {e}")
        
        for mutationType, future in mutation_futures:
            try:
                future.result(timeout=120)
            except Exception as e:
                print(f"ERROR processing mutation {mutationType}: {e}")
    
    print("  - Child operations processed")
    
    # Process final operations with parallel execution
    print("• Processing final operations...")
    operation_items = []
    for operationType in catoApiSchema:
        for operationName in catoApiSchema[operationType]:
            operation_items.append((operationType, operationName))
    
    print(f"  - Processing {len(operation_items)} operations...")
    
    # Process operations in batches to prevent memory issues
    batch_size = 10
    for i in range(0, len(operation_items), batch_size):
        batch = operation_items[i:i+batch_size]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for operationType, operationName in batch:
                future = executor.submit(processOperation, operationType, operationName)
                futures.append((operationType, operationName, future))
            
            # Wait for batch completion
            for operationType, operationName, future in futures:
                try:
                    future.result(timeout=180)
                    print(f"  - Processed {operationName}")
                except Exception as e:
                    print(f"ERROR processing {operationName}: {e}")
                    traceback.print_exc()

def processOperation(operationType, operationName):
    """Process a single operation - thread-safe"""
    try:
        with schema_lock:
            operation_data = copy.deepcopy(catoApiSchema[operationType][operationName])
        
        childOperations = operation_data.get("childOperations", {}).keys() if "childOperations" in operation_data else []
        
        # Process with recursion depth tracking
        parsedOperation = parseOperationWithDepthTracking(operation_data, childOperations, max_depth=50)
        parsedOperation = getOperationArgs(parsedOperation["type"]["definition"], parsedOperation)
        parsedOperation["path"] = operationName
        
        for argName in parsedOperation["args"]:
            arg = parsedOperation["args"][argName]
            parsedOperation["operationArgs"][arg["varName"]] = arg
        
        parsedOperation["variablesPayload"] = generateExampleVariables(parsedOperation)
        
        # Write files with thread-safe locking
        writeFile("../models/"+operationName+".json", json.dumps(parsedOperation, indent=4, sort_keys=True))
        
        payload = generateGraphqlPayload(parsedOperation["variablesPayload"], parsedOperation, operationName)
        writeFile("../queryPayloads/"+operationName+".json", json.dumps(payload, indent=4, sort_keys=True))
        writeFile("../queryPayloads/"+operationName+".txt", payload["query"])
        
    except Exception as e:
        print(f"Error in processOperation {operationName}: {e}")
        raise

def parseOperationWithDepthTracking(curOperation, childOperations, max_depth=50):
    """Parse operation with recursion depth tracking to prevent stack overflow"""
    if not hasattr(thread_local, 'depth'):
        thread_local.depth = 0
    
    thread_local.depth += 1
    
    try:
        if thread_local.depth > max_depth:
            print(f"WARNING: Max recursion depth {max_depth} reached, truncating...")
            return curOperation
        
        return parseOperation(curOperation, childOperations)
    finally:
        thread_local.depth -= 1

@lru_cache(maxsize=1000)
def getOfTypeWithCache(type_kind, type_name, oftype_name, parent_param_path):
    """Cached version of getOfType for commonly accessed types"""
    # This is a simplified version - implement full caching if needed
    pass

def getChildOperations(operationType, curType, parentType, parentPath, childOperationObjects):
    """Thread-safe version of getChildOperations"""
    # Parse fields for nested args to map out all child operations
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
            if (("args" in curFieldObject and len(curFieldObject["args"])>0) or 
                (curFieldObject["name"] in childOperationObjects) or 
                (curOfType["name"] in childOperationObjects)):
                hasChildren = True
                curParentType = copy.deepcopy(parentType)
                curFieldObject["args"] = getNestedArgDefinitions(curFieldObject["args"], curFieldObject["name"], None, None)
                curParentType["childOperations"][curFieldObject["name"]] = curFieldObject
                getChildOperations(operationType, curFieldObject, curParentType, parentPath + "." + curFieldObject["name"], childOperationObjects)
    
    if not hasChildren:
        with schema_lock:
            catoApiSchema[operationType][parentPath] = parentType

# Import all other functions from the original catolib.py with thread-safety improvements
# (I'm including the key functions here, but in practice you'd want to copy all functions)

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
        else:
            arg["varName"] = renderCamelCase(arg["type"]["name"])
        arg["responseStr"] = arg["name"] + ":$" + arg["varName"] + " "
        if "LIST" in arg["type"]["kind"]:
            arg["requestStr"] = "$" + arg["varName"] + ":" + "[" + arg["type"]["name"] + required2 + "]" + required1 + " "
        else:
            arg["requestStr"] = "$" + arg["varName"] + ":" + arg["type"]["name"] + required1 + " "
        newArgsList[arg["id_str"]] = arg
    return newArgsList

def getOfType(curType, ofType, parentParamPath, childOperations, parentFields, parentTypeName=None):
    """Thread-safe version with recursion depth management"""
    if not hasattr(thread_local, 'depth'):
        thread_local.depth = 0
    
    if thread_local.depth > 100:  # Prevent deep recursion
        print(f"WARNING: Deep recursion detected in getOfType, truncating...")
        return ofType
    
    thread_local.depth += 1
    
    try:
        ofType["kind"].append(copy.deepcopy(curType["kind"]))
        curParamPath = "" if (parentParamPath == None) else parentParamPath + "___"
        
        if curType["ofType"] != None:
            ofType = getOfType(copy.deepcopy(curType["ofType"]), ofType, parentParamPath, childOperations, parentFields)
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
                ofType["definition"]["inputFields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["inputFields"]), curParamPath, childOperations, parentFields, ofType["name"])
        elif "UNION" in ofType["kind"]:
            ofType["indexType"] = "interface"
            ofType["definition"] = copy.deepcopy(catoApiIntrospection["unions"][ofType["name"]])
            if ofType["definition"]["possibleTypes"] != None:
                ofType["definition"]["possibleTypes"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["possibleTypes"]), curParamPath, childOperations, parentFields)
        elif "OBJECT" in ofType["kind"]:
            ofType["indexType"] = "object"
            ofType["definition"] = copy.deepcopy(catoApiIntrospection["objects"][ofType["name"]])
            if ofType["definition"]["fields"] != None and childOperations!=None:
                ofType["definition"]["fields"] = checkForChildOperation(copy.deepcopy(ofType["definition"]["fields"]), childOperations)
                ofType["definition"]["fields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["fields"]), curParamPath, childOperations, parentFields, ofType["name"])
            if ofType["definition"]["interfaces"] != None:
                ofType["definition"]["interfaces"] = getNestedInterfaceDefinitions(copy.deepcopy(ofType["definition"]["interfaces"]), curParamPath, childOperations, parentFields)
        elif "INTERFACE" in ofType["kind"]:
            ofType["indexType"] = "interface"
            ofType["definition"] = copy.deepcopy(catoApiIntrospection["interfaces"][ofType["name"]])
            if ofType["definition"]["fields"] != None:
                ofType["definition"]["fields"] = getNestedFieldDefinitions(copy.deepcopy(ofType["definition"]["fields"]), curParamPath, childOperations, parentFields, ofType["name"])
        elif "ENUM" in ofType["kind"]:
            ofType["indexType"] = "enum"
            ofType["definition"] = copy.deepcopy(catoApiIntrospection["enums"][ofType["name"]])
        
        return ofType
    finally:
        thread_local.depth -= 1

def getNestedFieldDefinitions(fieldsAry, parentParamPath, childOperations, parentFields, parentTypeName=None):
    """Thread-safe version with FIXED records exclusion removal"""
    newFieldsList = {}
    for field in fieldsAry:
        if isinstance(field, str):
            field = fieldsAry[field]
        curParamPath = field["name"] if (parentParamPath == None) else (parentParamPath.replace("___",".") + field["name"])
        field["type"] = getOfType(field["type"], { "non_null": False, "kind": [], "name": None }, curParamPath, childOperations, parentFields, parentTypeName)
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
        else:
            field["varName"] = renderCamelCase(field["type"]["name"])
        
        field["responseStr"] = field["name"] + ":$" + field["varName"] + " "
        
        if "LIST" in field["type"]["kind"]:
            field["requestStr"] = "$" + field["varName"] + ":" + "[" + field["type"]["name"] + required2 + "]" + required1 + " "
        else:
            field["requestStr"] = "$" + field["varName"] + ":" + field["type"]["name"] + required1 + " "
        
        if "args" in field:
            field["args"] = getNestedArgDefinitions(field["args"], field["name"], childOperations, parentFields)
        
        ## aliasLogic must
        if parentFields!=None and field["name"] in parentFields and "SCALAR" not in field["type"]["kind"]:
            if parentTypeName:
                field["alias"] = renderCamelCase(field["name"]+"."+parentTypeName)+": "+field["name"]
            else:
                field["alias"] = renderCamelCase(field["type"]["name"]+"."+field["name"])+": "+field["name"]
        
        # CRITICAL FIX: Remove the records___fields exclusion to allow records field
        # The original code had: if "records___fields" != field["id_str"]:
        # We're removing this condition entirely to allow records field
        newFieldsList[field["name"]] = field
    
    return newFieldsList

# Copy remaining functions from original catolib.py...
# (Including parseOperation, checkForChildOperation, getOperationArgs, etc.)
# For brevity, I'm showing the key threading-related changes

def renderCamelCase(pathStr):
    str_result = ""
    pathAry = pathStr.split(".") 
    for i, path in enumerate(pathAry):
        if i == 0:
            str_result += path[0].lower() + path[1:]
        else:
            str_result += path[0].upper() + path[1:]
    return str_result

def send(api_key, query, variables={}, operationName=None):
    headers = { 'x-api-key': api_key,'Content-Type':'application/json'}
    no_verify = ssl._create_unverified_context()
    request = urllib.request.Request(url='https://api.catonetworks.com/api/v1/graphql2',
        data=json.dumps(query).encode("ascii"), headers=headers)
    response = urllib.request.urlopen(request, context=no_verify, timeout=60)
    result_data = response.read()
    result = json.loads(result_data)
    if "errors" in result:
        logging.warning(f"API error: {result_data}")
        return False, result
    return True, result

# Include all the other necessary functions from the original file
# (generateExampleVariables, parseNestedArgFields, renderInputFieldVal, 
#  writeCliDriver, writeOperationParsers, writeReadmes, etc.)
# For space reasons, I'm not including them all here, but they should be copied over

def parseOperation(curOperation, childOperations):
    if "operationArgs" not in curOperation:
        curOperation["operationArgs"] = {}
    curOperation["fieldTypes"] = {}
    curOfType = getOfType(curOperation["type"], { "non_null": False, "kind": [], "name": None }, None, childOperations, None)
    curOperation["type"] = copy.deepcopy(curOfType)
    if curOfType["name"] in catoApiIntrospection["objects"]:
        curOperation["args"] = getNestedArgDefinitions(curOperation["args"], None, childOperations, None)
        curOperation["type"]["definition"] = copy.deepcopy(catoApiIntrospection["objects"][curOperation["type"]["name"]])
        if "fields" in curOperation["type"]["definition"] and curOperation["type"]["definition"]["fields"] != None:
            curOperation["type"]["definition"]["fields"] = checkForChildOperation(copy.deepcopy(curOperation["type"]["definition"]["fields"]), childOperations)
            curOperation["type"]["definition"]["fields"] = copy.deepcopy(getNestedFieldDefinitions(curOperation["type"]["definition"]["fields"], None, childOperations, [], curOperation["type"]["name"]))
        if "inputFields" in curOperation["type"]["definition"] and curOperation["type"]["definition"]["inputFields"] != None:
            parentFields = curOperation["type"]["definition"]["inputFields"].keys()
            curOperation["type"]["definition"]["inputFields"] = copy.deepcopy(getNestedFieldDefinitions(curOperation["type"]["definition"]["inputFields"], None, childOperations, parentFields, curOperation["type"]["name"]))
    return curOperation

def checkForChildOperation(fieldsAry, childOperations):
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

def getOperationArgs(curType, curOperation):
    """Complete implementation with thread-safe recursion management and type safety"""
    if not hasattr(thread_local, 'depth'):
        thread_local.depth = 0
    
    if thread_local.depth > 50:  # Prevent deep recursion
        return curOperation
    
    thread_local.depth += 1
    
    try:
        # Ensure curType is a dictionary
        if not isinstance(curType, dict):
            return curOperation
            
        # Handle fields - check if it's a dict and not empty
        if isinstance(curType.get('fields'), dict) and curType['fields']:
            for fieldName, field in curType["fields"].items():
                if not isinstance(field, dict):
                    continue
                ## aliasLogic
                if isinstance(field.get("type"), dict) and isinstance(field["type"].get("definition"), dict):
                    curOperation["fieldTypes"][field["type"]["definition"]["name"]] = True
                    curOperation = getOperationArgs(field["type"]["definition"], curOperation)
                if isinstance(field.get("args"), dict):
                    for argName, arg in field["args"].items():
                        if isinstance(arg, dict) and "varName" in arg:
                            curOperation["operationArgs"][arg["varName"]] = arg
                            if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
        
        # Handle inputFields - check if it's a dict and not empty
        if isinstance(curType.get('inputFields'), dict) and curType['inputFields']:
            for inputFieldName, inputField in curType["inputFields"].items():
                if not isinstance(inputField, dict):
                    continue
                if isinstance(inputField.get("type"), dict) and isinstance(inputField["type"].get("definition"), dict):
                    curOperation["fieldTypes"][inputField["type"]["definition"]["name"]] = True
                    curOperation = getOperationArgs(inputField["type"]["definition"], curOperation)
                if isinstance(inputField.get("args"), dict):
                    for argName, arg in inputField["args"].items():
                        if isinstance(arg, dict) and "varName" in arg:
                            curOperation["operationArgs"][arg["varName"]] = arg
                            if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
        
        # Handle interfaces - check if it's a list
        if isinstance(curType.get('interfaces'), list):
            for interface in curType["interfaces"]:
                if not isinstance(interface, dict):
                    continue
                if isinstance(interface.get("type"), dict) and isinstance(interface["type"].get("definition"), dict):
                    curOperation["fieldTypes"][interface["type"]["definition"]["name"]] = True
                    curOperation = getOperationArgs(interface["type"]["definition"], curOperation)
                if isinstance(interface.get("args"), dict):
                    for argName, arg in interface["args"].items():
                        if isinstance(arg, dict) and "varName" in arg:
                            curOperation["operationArgs"][arg["varName"]] = arg
                            if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
        
        # Handle possibleTypes - check if it's a list first, then dict
        possibleTypes = curType.get('possibleTypes')
        if isinstance(possibleTypes, list):
            for possibleType in possibleTypes:
                if isinstance(possibleType, dict):
                    curOperation = getOperationArgs(possibleType, curOperation)
                    if isinstance(possibleType.get('fields'), dict):
                        for fieldName, field in possibleType["fields"].items():
                            if isinstance(field, dict) and isinstance(field.get("args"), dict):
                                for argName, arg in field["args"].items():
                                    if isinstance(arg, dict) and "varName" in arg:
                                        curOperation["operationArgs"][arg["varName"]] = arg
                                        if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                            curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
                    if isinstance(possibleType.get("args"), dict):
                        for argName, arg in possibleType["args"].items():
                            if isinstance(arg, dict) and "varName" in arg:
                                curOperation["operationArgs"][arg["varName"]] = arg
                                if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                    curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
        elif isinstance(possibleTypes, dict):
            for possibleTypeName, possibleType in possibleTypes.items():
                if isinstance(possibleType, dict):
                    curOperation = getOperationArgs(possibleType, curOperation)
                    if isinstance(possibleType.get('fields'), dict):
                        for fieldName, field in possibleType["fields"].items():
                            if isinstance(field, dict) and isinstance(field.get("args"), dict):
                                for argName, arg in field["args"].items():
                                    if isinstance(arg, dict) and "varName" in arg:
                                        curOperation["operationArgs"][arg["varName"]] = arg
                                        if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                            curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
                    if isinstance(possibleType.get("args"), dict):
                        for argName, arg in possibleType["args"].items():
                            if isinstance(arg, dict) and "varName" in arg:
                                curOperation["operationArgs"][arg["varName"]] = arg
                                if isinstance(arg.get("type"), dict) and isinstance(arg["type"].get("definition"), dict):
                                    curOperation = getOperationArgs(arg["type"]["definition"], curOperation)
        
        return curOperation
    finally:
        thread_local.depth -= 1

def generateExampleVariables(operation):
    """Generate example variables for operation"""
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
    
    if "accountID" in variablesObj:
        del variablesObj["accountID"]
    if "accountId" in variablesObj:
        del variablesObj["accountId"]
    return variablesObj

def parseNestedArgFields(fieldObj):
    """Parse nested argument fields with realistic examples"""
    if "SCALAR" in fieldObj["type"]["kind"] or "ENUM" in fieldObj["type"]["kind"]:
        return renderInputFieldVal(fieldObj)
    else:
        # For complex types, create a nested object with realistic examples
        subVariableObj = {}
        if "type" in fieldObj and "definition" in fieldObj["type"] and "inputFields" in fieldObj["type"]["definition"]:
            inputFields = fieldObj["type"]["definition"]["inputFields"]
            if inputFields:
                for inputFieldName, inputField in inputFields.items():
                    if isinstance(inputField, dict):
                        subVariableObj[inputField["name"]] = parseNestedArgFields(inputField)
        return subVariableObj

def renderInputFieldVal(arg):
    """Render input field values with realistic JSON examples"""
    value = "string"
    
    if "SCALAR" in arg["type"]["kind"]:
        type_name = arg["type"]["name"]
        if "LIST" in arg["type"]["kind"]:
            # Return array of realistic values based on scalar type
            if type_name == "String":
                value = ["string1", "string2"]
            elif type_name == "Int":
                value = [1, 2]
            elif type_name == "Float":
                value = [1.5, 2.5]
            elif type_name == "Boolean":
                value = [True, False]
            elif type_name == "ID":
                value = ["id1", "id2"]
            else:
                value = ["example1", "example2"]
        else:
            # Return single realistic value based on scalar type
            if type_name == "String":
                value = "string"
            elif type_name == "Int":
                value = 1
            elif type_name == "Float":
                value = 1.5
            elif type_name == "Boolean":
                value = True
            elif type_name == "ID":
                value = "id"
            else:
                value = "example_value"
    elif "ENUM" in arg["type"]["kind"]:
        # For enums, get the first available value if possible, otherwise generic example
        enum_definition = arg.get("type", {}).get("definition", {})
        enum_values = enum_definition.get("enumValues", [])
        if enum_values and len(enum_values) > 0:
            value = enum_values[0].get("name", "ENUM_VALUE")
        else:
            value = "ENUM_VALUE"
    
    return value

def generateGraphqlPayload(variablesObj, operation, operationName):
    """Generate GraphQL payload"""
    indent = "\t"
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
    
    queryStr += ") {\n" + renderArgsAndFields("", variablesObj, operation, operation["type"]["definition"], "\t\t") + "\t}"
    queryStr += indent + "\n}"
    
    body = {
        "query": queryStr,
        "variables": variablesObj,
        "operationName": renderCamelCase(".".join(operationAry)),
    }
    return body

def renderArgsAndFields(responseArgStr, variablesObj, curOperation, definition, indent):
    """Render GraphQL query arguments and fields"""
    for fieldName in definition['fields']:
        field = definition['fields'][fieldName]
        field_name = field['alias'] if 'alias' in field else field['name']
        responseArgStr += indent + field_name
        responseArgStr += "\n"
    return responseArgStr

def getNestedInterfaceDefinitions(possibleTypesAry, parentParamPath, childOperations, parentFields):
    """Get nested interface definitions"""
    curInterfaces = {}
    for possibleType in possibleTypesAry:
        if "OBJECT" in possibleType["kind"]:
            curInterfaces[possibleType["name"]] = copy.deepcopy(catoApiIntrospection["objects"][possibleType["name"]])
    return curInterfaces

def writeCliDriver(catoApiSchema):
    """Write CLI driver - thread-safe implementation"""
    parsersIndex = {}
    for operationType in catoApiSchema:
        for operation in catoApiSchema[operationType]:
            operationNameAry = operation.split(".")
            # Skip eventsFeed - it's handled as a custom parser
            if operationNameAry[1] == "eventsFeed":
                continue
            parsersIndex[operationNameAry[0]+"_"+operationNameAry[1]] = True
    parsers = list(parsersIndex.keys())

    cliDriverStr = """
import os
import argparse
import json
import catocli
from graphql_client import Configuration
from graphql_client.api_client import ApiException
from ..parsers.customParserApiClient import get_help
from .profile_manager import get_profile_manager
from .version_checker import check_for_updates, force_check_updates
import traceback
import sys
sys.path.insert(0, 'vendor')
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Initialize profile manager
profile_manager = get_profile_manager()
CATO_DEBUG = bool(os.getenv("CATO_DEBUG", False))
from ..parsers.raw import raw_parse
from ..parsers.custom import custom_parse
from ..parsers.custom_private import private_parse
from ..parsers.query_siteLocation import query_siteLocation_parse
from ..parsers.custom.query_eventsFeed import query_eventsFeed_parse
"""
    for parserName in parsers:
        cliDriverStr += "from ..parsers."+parserName+" import "+parserName+"_parse\n"

    cliDriverStr += """
def show_version_info(args, configuration=None):
    print(f"catocli version {catocli.__version__}")
    
    if not args.current_only:
        if args.check_updates:
            # Force check for updates
            is_newer, latest_version, source = force_check_updates()
        else:
            # Regular check (uses cache)
            is_newer, latest_version, source = check_for_updates(show_if_available=False)
        
        if latest_version:
            if is_newer:
                print(f"Latest version: {latest_version} (from {source}) - UPDATE AVAILABLE!")
                print()
                print("To upgrade, run:")
                print("pip install --upgrade catocli")
            else:
                print(f"Latest version: {latest_version} (from {source}) - You are up to date!")
        else:
            print("Unable to check for updates (check your internet connection)")
    return [{"success": True, "current_version": catocli.__version__, "latest_version": latest_version if not args.current_only else None}]
        
def get_configuration(skip_api_key=False):
    configuration = Configuration()
    configuration.verify_ssl = False
    configuration.debug = CATO_DEBUG
    configuration.version = "{}".format(catocli.__version__)
    
    # Try to migrate from environment variables first
    profile_manager.migrate_from_environment()
    
    # Get credentials from profile
    credentials = profile_manager.get_credentials()
    if not credentials:
        print("No Cato CLI profile configured.")
        print("Run 'catocli configure set' to set up your credentials.")
        exit(1)

    if not credentials.get('cato_token') or not credentials.get('account_id'):
        profile_name = profile_manager.get_current_profile()
        print(f"Profile '{profile_name}' is missing required credentials.")
        print(f"Run 'catocli configure set --profile {profile_name}' to update your credentials.")
        exit(1)
    
    # Use standard endpoint from profile for regular API calls
    configuration.host = credentials['endpoint']
        
    # Only set API key if not using custom headers file
    # (Private settings are handled separately in createPrivateRequest)
    if not skip_api_key:
        configuration.api_key["x-api-key"] = credentials['cato_token']
    configuration.accountID = credentials['account_id']
    
    return configuration

defaultReadmeStr = \"""
The Cato CLI is a command-line interface tool designed to simplify the management and automation of Cato Networks’ configurations and operations. 
It enables users to interact with Cato’s API for tasks such as managing Cato Management Application (CMA) site and account configurations, security policies, retrieving events, etc.\n\n
For assistance in generating syntax for the cli to perform various operations, please refer to the Cato API Explorer application.\n\n
https://github.com/catonetworks/cato-api-explorer
\"""

parser = argparse.ArgumentParser(prog='catocli', usage='%(prog)s <operationType> <operationName> [options]', description=defaultReadmeStr)
parser.add_argument('--version', action='version', version=catocli.__version__)
parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
subparsers = parser.add_subparsers()

# Version command - enhanced with update checking
version_parser = subparsers.add_parser('version', help='Show version information and check for updates')
version_parser.add_argument('--check-updates', action='store_true', help='Force check for updates (ignores cache)')
version_parser.add_argument('--current-only', action='store_true', help='Show only current version')
version_parser.set_defaults(func=show_version_info)

custom_parsers = custom_parse(subparsers)
private_parsers = private_parse(subparsers)
raw_parsers = subparsers.add_parser('raw', help='Raw GraphQL', usage=get_help("raw"))
raw_parser = raw_parse(raw_parsers)
query_parser = subparsers.add_parser('query', help='Query', usage='catocli query <operationName> [options]')
query_subparsers = query_parser.add_subparsers(description='valid subcommands', help='additional help')
query_siteLocation_parser = query_siteLocation_parse(query_subparsers)
query_eventsFeed_parser = query_eventsFeed_parse(query_subparsers)
mutation_parser = subparsers.add_parser('mutation', help='Mutation', usage='catocli mutation <operationName> [options]')
mutation_subparsers = mutation_parser.add_subparsers(description='valid subcommands', help='additional help')

"""
    for parserName in parsers:
        cliDriverStr += parserName+"_parser = "+parserName+"_parse("+parserName.split("_")[0]+"_subparsers)\n"

    cliDriverStr += """

def parse_headers(header_strings):
    headers = {}
    if header_strings:
        for header_string in header_strings:
            if ':' not in header_string:
                print(f"ERROR: Invalid header format '{header_string}'. Use 'Key: Value' format.")
                exit(1)
            key, value = header_string.split(':', 1)
            headers[key.strip()] = value.strip()
    return headers

def parse_headers_from_file(file_path):
    headers = {}
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' not in line:
                    print(f"ERROR: Invalid header format in {file_path} at line {line_num}: '{line}'. Use 'Key: Value' format.")
                    exit(1)
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"ERROR: Headers file '{file_path}' not found.")
        exit(1)
    except IOError as e:
        print(f"ERROR: Could not read headers file '{file_path}': {e}")
        exit(1)
    return headers

def main(args=None):
    # Check if no arguments provided or help is requested
    if args is None:
        args = sys.argv[1:]

    # Show version check when displaying help or when no command specified
    if not args or '-h' in args or '--help' in args:
        # Check for updates in background (non-blocking)
        try:
            check_for_updates(show_if_available=True)
        except Exception:
            # Don't let version check interfere with CLI operation
            pass

    args = parser.parse_args(args=args)
    try:
        # Skip authentication for configure commands
        if hasattr(args, 'func') and hasattr(args.func, '__module__') and 'configure' in str(args.func.__module__):
            response = args.func(args, None)
        else:
            # Check if using headers file to determine if we should skip API key
            # Note: Private settings should NOT affect regular API calls - only private commands
            using_headers_file = hasattr(args, 'headers_file') and args.headers_file
            
            # Get configuration from profiles
            configuration = get_configuration(skip_api_key=using_headers_file)
            
            # Parse custom headers if provided
            custom_headers = {}
            if hasattr(args, 'headers') and args.headers:
                custom_headers.update(parse_headers(args.headers))
            if hasattr(args, 'headers_file') and args.headers_file:
                custom_headers.update(parse_headers_from_file(args.headers_file))
            if custom_headers:
                configuration.custom_headers.update(custom_headers)
            # Handle account ID override (applies to all commands except raw)
            if args.func.__name__ not in ["createRawRequest"]:
                if hasattr(args, 'accountID') and args.accountID is not None:
                    # Command line override takes precedence
                    configuration.accountID = args.accountID
                # Otherwise use the account ID from the profile (already set in get_configuration)
            response = args.func(args, configuration)

        if type(response) == ApiException:
            print("ERROR! Status code: {}".format(response.status))
            print(response)
        else:
            if response!=None:
                # Check if this is CSV output
                if (isinstance(response, list) and len(response) > 0 and 
                    isinstance(response[0], dict) and "__csv_output__" in response[0]):
                    # Print CSV output directly without JSON formatting
                    print(response[0]["__csv_output__"], end='')
                else:
                    # Standard JSON output
                    print(json.dumps(response[0], sort_keys=True, indent=4))
    except KeyboardInterrupt:
        print('Operation cancelled by user (Ctrl+C).')
        exit(130)  # Standard exit code for SIGINT
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
    with file_write_lock:
        writeFile("../catocli/Utils/clidriver.py", cliDriverStr)
    print("  - CLI driver written successfully")

def writeOperationParsers(catoApiSchema):
    """Write operation parsers - thread-safe implementation"""
    parserMapping = {"query":{},"mutation":{}}
    
    # Load settings to get CSV-supported operations
    settings = loadJSON("../catocli/clisettings.json")
    csv_supported_operations = settings.get("queryOperationCsvOutput", {})
    
    ## Write the raw query parser ##
    cliDriverStr =f"""
from ..customParserApiClient import createRawRequest, get_help

def raw_parse(raw_parser):
    raw_parser.add_argument('json', nargs='?', default='{{}}', help='Query, Variables and opertaionName in JSON format (defaults to empty object if not provided).')
    raw_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    raw_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    raw_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    raw_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    raw_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    raw_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    raw_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    raw_parser.add_argument('-e', '--endpoint', dest='endpoint', help='Override the API endpoint URL (e.g., https://api.catonetworks.com/api/v1/graphql2)')
    raw_parser.set_defaults(func=createRawRequest,operation_name='raw')
"""
    parserPath = "../catocli/parsers/raw"
    if not os.path.exists(parserPath):
        os.makedirs(parserPath)
    with file_write_lock:
        writeFile(parserPath+"/__init__.py",cliDriverStr)

    ## Write the siteLocation query parser ##
    cliDriverStr =f"""
from ..customParserApiClient import querySiteLocation, get_help

def query_siteLocation_parse(query_subparsers):
    query_siteLocation_parser = query_subparsers.add_parser('siteLocation', 
            help='siteLocation local cli query', 
            usage=get_help("query_siteLocation"))
    query_siteLocation_parser.add_argument('json', nargs='?', default='{{}}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_siteLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_siteLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_siteLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_siteLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_siteLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_siteLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_siteLocation_parser.set_defaults(func=querySiteLocation,operation_name='query.siteLocation')
"""
    parserPath = "../catocli/parsers/query_siteLocation"
    if not os.path.exists(parserPath):
        os.makedirs(parserPath)
    with file_write_lock:
        writeFile(parserPath+"/__init__.py",cliDriverStr)

    # Process all operations to create parsers
    for operationType in parserMapping:
        operationAry = catoApiSchema[operationType]
        for operationName in operationAry:
            parserMapping = getParserMapping(parserMapping,operationName,operationName,operationAry[operationName])
    
    # Generate parser files for each operation
    for operationType in parserMapping:
        for operationName in parserMapping[operationType]:
            # Skip eventsFeed - it's handled as a custom parser
            if operationName == "eventsFeed":
                continue
            parserName = operationType+"_"+operationName
            parser = parserMapping[operationType][operationName]
            cliDriverStr = f"""
from ..customParserApiClient import createRequest, get_help

def {parserName}_parse({operationType}_subparsers):
    {parserName}_parser = {operationType}_subparsers.add_parser('{operationName}', 
            help='{operationName}() {operationType} operation', 
            usage=get_help("{operationType}_{operationName}"))
"""
            if "path" in parser:
                # Check if this operation supports CSV output
                operation_path = parserName.replace("_", ".")
                supports_csv = operation_path in csv_supported_operations
                
                cliDriverStr += f"""
    {parserName}_parser.add_argument('json', nargs='?', default='{{}}', help='Variables in JSON format (defaults to empty object if not provided).')
    {parserName}_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    {parserName}_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    {parserName}_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    {parserName}_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    {parserName}_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    {parserName}_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    {parserName}_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    {parserName}_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
"""
                # Add -f flag for CSV-supported operations
                if supports_csv:
                    cliDriverStr += f"""
    {parserName}_parser.add_argument('-f', '--format', choices=['json', 'csv'], default='json', help='Output format (default: json)')
    {parserName}_parser.add_argument('--csv-filename', dest='csv_filename', help='Override CSV file name (default: accountmetrics.csv)')
    {parserName}_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to the CSV file name')
"""
                
                cliDriverStr += f"    {parserName}_parser.set_defaults(func=createRequest,operation_name='{parserName.replace("_",".")}')"
                cliDriverStr += "\n"
            else:
                cliDriverStr += renderSubParser(parser,operationType+"_"+operationName)
            
            parserPath = "../catocli/parsers/"+parserName
            if not os.path.exists(parserPath):
                os.makedirs(parserPath)
            with file_write_lock:
                writeFile(parserPath+"/__init__.py",cliDriverStr)
    
    print("  - Operation parsers written successfully")

def writeReadmes(catoApiSchema):
    """Write README files - thread-safe implementation"""
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

#### Override API endpoint

`catocli raw --endpoint https://custom-api.example.com/graphql '<json>'`
"""
    parserPath = "../catocli/parsers/raw"
    if not os.path.exists(parserPath):
        os.makedirs(parserPath)
    with file_write_lock:
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

`catocli query siteLocation '{"filters":[{"search": "Your City here","field":"city","operation":"startsWith"},{"search": "Your StateName here","field":"stateName","operation":"endsWith"},{"search": "Your Country here","field":"countryName","operation":"contains"}]}'`

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
    with file_write_lock:
        writeFile(parserPath+"/README.md",readmeStr)
    
    # Process operations for README generation directly from schema
    for operationType in catoApiSchema:
        for operationName in catoApiSchema[operationType]:
            # Skip operations that don't start with the operation type (these are nested)
            if not operationName.startswith(operationType + "."):
                continue
            
            # Skip eventsFeed - it's handled as a custom parser with custom documentation
            operation_parts = operationName.split(".")[1:]
            if len(operation_parts) > 0 and operation_parts[0] == "eventsFeed":
                continue
                
            operation = catoApiSchema[operationType][operationName]
            
            # Get example from operation directly or from payload files
            example = operation.get("variablesPayload", {})
            if not example:
                payload_file_path = f"../queryPayloads/{operationName}.json"
                try:
                    payload_data = loadJSON(payload_file_path)
                    if "variables" in payload_data:
                        example = payload_data["variables"]
                except Exception as e:
                    # If payload file doesn't exist or has issues, use empty dict
                    pass
            
            # Create parser object
            parser = {
                "path": operationName,
                "args": {},
                "example": example
            }
            
            # Load operation arguments from the model file instead of schema
            try:
                model_file_path = f"../models/{operationName}.json"
                model_data = loadJSON(model_file_path)
                operationArgs = model_data.get("operationArgs", {})
                
                for argName in operationArgs:
                    arg = operationArgs[argName]
                    values = []
                    if "definition" in arg["type"] and "enumValues" in arg["type"]["definition"] and arg["type"]["definition"]["enumValues"] != None:
                        for enumValue in arg["type"]["definition"]["enumValues"]:
                            values.append(enumValue["name"])
                    parser["args"][arg["varName"]] = {
                        "name": arg["name"],
                        "description": "N/A" if arg["description"] == None else arg["description"],
                        "type": arg["type"]["name"] + ("[]" if "LIST" in arg["type"]["kind"] else ""),
                        "required": "required" if arg["required"] == True else "optional",
                        "values": values
                    }
            except Exception as e:
                # If model file doesn't exist or has issues, fall back to schema operationArgs
                operationArgs = operation.get("operationArgs", {})
                for argName in operationArgs:
                    arg = operationArgs[argName]
                    values = []
                    if "definition" in arg["type"] and "enumValues" in arg["type"]["definition"] and arg["type"]["definition"]["enumValues"] != None:
                        for enumValue in arg["type"]["definition"]["enumValues"]:
                            values.append(enumValue["name"])
                    parser["args"][arg["varName"]] = {
                        "name": arg["name"],
                        "description": "N/A" if arg["description"] == None else arg["description"],
                        "type": arg["type"]["name"] + ("[]" if "LIST" in arg["type"]["kind"] else ""),
                        "required": "required" if arg["required"] == True else "optional",
                        "values": values
                    }
            
            # Generate README for this operation
            # Extract the operation parts (e.g., "query.xdr.stories" -> "xdr stories")
            operation_parts = operationName.split(".")[1:]  # Remove the operation type prefix
            parserName = operationType + "_" + "_".join(operation_parts)
            operationPath = operationName
            operationCmd = operationType + " " + " ".join(operation_parts)
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
"""
                # Add realistic JSON example if available
                if "example" in parser and parser["example"]:
                    import json
                    example_json = json.dumps(parser["example"], separators=(',', ':'))
                    example_json_pretty = json.dumps(parser["example"], indent=4)
                    readmeStr += f"""
`catocli {operationCmd} '{example_json}'`

`catocli {operationCmd} -p '{example_json_pretty}'`

"""
                
                # Note: GitHub links for advanced examples are now handled dynamically in the help system
                
                # Check for example file and insert its content before Operation Arguments
                example_file_path = f"examples/{operationPath}.md"
                try:
                    example_content = openFile(example_file_path)
                    # Add the example content with proper formatting
                    readmeStr += f"""
## Advanced Usage
{example_content}

"""
                except:
                    # If example file doesn't exist, continue without adding example content
                    pass
                
                readmeStr += f"""
#### Operation Arguments for {operationPath} ####

"""
                if "args" in parser:
                    for argName in parser["args"]:
                        arg = parser["args"][argName]
                        arg_type = arg.get("type", "Unknown")
                        required_status = "required" if arg.get("required", False) else "optional"
                        description = arg.get("description", "No description available")
                        values_str = "Default Value: " + str(arg["values"]) if len(arg.get("values", [])) > 0 else ""
                        readmeStr += f'`{argName}` [{arg_type}] - ({required_status}) {description} {values_str}   \n'
                
                parserPath = "../catocli/parsers/"+parserName
                if not os.path.exists(parserPath):
                    os.makedirs(parserPath)
                with file_write_lock:
                    writeFile(parserPath+"/README.md",readmeStr)
            else:
                parserPath = "../catocli/parsers/"+parserName
                if not os.path.exists(parserPath):
                    os.makedirs(parserPath)
                with file_write_lock:
                    writeFile(parserPath+"/README.md",readmeStr)
                renderSubReadme(parser,operationType,operationPath)
    
    print("  - README files written successfully")

# Helper functions needed for the above implementations
def getParserMapping(curParser, curPath, operationFullPath, operation):
    """Helper function to map parser operations - matches original catolib.py logic"""
    
    # Try to get example from variablesPayload first, then from payload files
    example = operation.get("variablesPayload", {})
    
    # If no variablesPayload, try to load from queryPayloads directory
    if not example:
        payload_file_path = f"../queryPayloads/{operationFullPath}.json"
        try:
            payload_data = loadJSON(payload_file_path)
            if "variables" in payload_data:
                example = payload_data["variables"]
        except Exception as e:
            # If payload file doesn't exist or has issues, use empty dict
            pass
    
    parserObj = {
        "path": operationFullPath,
        "args": {},
        "example": example
    }
    
    # Safely handle operations that might not have operationArgs yet
    operationArgs = operation.get("operationArgs", {})
    for argName in operationArgs:
        arg = operationArgs[argName]
        values = []
        if "definition" in arg["type"] and "enumValues" in arg["type"]["definition"] and arg["type"]["definition"]["enumValues"] != None:
            for enumValue in arg["type"]["definition"]["enumValues"]:
                values.append(enumValue["name"])
        parserObj["args"][arg["varName"]] = {
            "name": arg["name"],
            "description": "N/A" if arg["description"] == None else arg["description"],
            "type": arg["type"]["name"] + ("[]" if "LIST" in arg["type"]["kind"] else ""),
            "required": "required" if arg["required"] == True else "optional",
            "values": values
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

def getOperationArgsForReadme(operationArgs):
    """Helper function to format operation arguments for README"""
    formattedArgs = {}
    for argName in operationArgs:
        arg = operationArgs[argName]
        formattedArgs[argName] = {
            "type": arg.get("type", {}).get("name", "Unknown"),
            "required": "required" if arg.get("required", False) else "optional",
            "description": arg.get("description", "No description available"),
            "values": []
        }
    return formattedArgs

def renderSubParser(subParser, parentParserPath):
    """Helper function to render sub-parsers with type safety"""
    if not isinstance(subParser, dict):
        return ""
        
    settings = loadJSON("../catocli/clisettings.json")
    csv_supported_operations = settings.get("queryOperationCsvOutput", {})

    cliDriverStr = f"""
    {parentParserPath}_subparsers = {parentParserPath}_parser.add_subparsers()
"""
    for subOperationName in subParser:
        subOperation = subParser[subOperationName]
        
        # Ensure subOperation is a dictionary
        if not isinstance(subOperation, dict):
            continue
            
        subParserPath = parentParserPath.replace(".","_")+"_"+subOperationName
        cliDriverStr += f"""
    {subParserPath}_parser = {parentParserPath}_subparsers.add_parser('{subOperationName}', 
            help='{subOperationName}() {parentParserPath.split('_')[-1]} operation', 
            usage=get_help("{subParserPath}"))
"""
        if isinstance(subOperation, dict) and "path" in subOperation:
            command = parentParserPath.replace("_"," ")+" "+subOperationName
            operation_path = subOperation.get("path", "")
            operation_path_csv = subParserPath.replace("_", ".")
            supports_csv = operation_path_csv in csv_supported_operations
            cliDriverStr += f"""
    {subParserPath}_parser.add_argument('json', nargs='?', default='{{}}', help='Variables in JSON format (defaults to empty object if not provided).')
    {subParserPath}_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    {subParserPath}_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    {subParserPath}_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    {subParserPath}_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    {subParserPath}_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    {subParserPath}_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    {subParserPath}_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    {subParserPath}_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    {subParserPath}_parser.set_defaults(func=createRequest,operation_name='{operation_path}')
"""
                            # Add -f flag for CSV-supported operations
            if supports_csv:
                cliDriverStr += f"""
    {subParserPath}_parser.add_argument('-f', '--format', choices=['json', 'csv'], default='json', help='Output format (default: json)')
    {subParserPath}_parser.add_argument('--csv-filename', dest='csv_filename', help='Override CSV file name (default: accountmetrics.csv)')
    {subParserPath}_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to the CSV file name')
"""

        else:
            cliDriverStr += renderSubParser(subOperation,subParserPath)
    return cliDriverStr

def renderSubReadme(subParser, operationType, parentOperationPath):
    """Helper function to render sub-README files with type safety"""
    # Ensure subParser is a dictionary before processing
    if not isinstance(subParser, dict):
        return
        
    for subOperationName in subParser:
        subOperation = subParser[subOperationName]
        
        # Ensure subOperation is a dictionary before processing
        if not isinstance(subOperation, dict):
            continue
            
        subOperationPath = parentOperationPath+"."+subOperationName
        subOperationCmd = parentOperationPath.replace("."," ")+" "+subOperationName
        parserPath = "../catocli/parsers/"+subOperationPath.replace(".","_")
        readmeStr = f"""
## CATO-CLI - {parentOperationPath}.{subOperationName}:
[Click here](https://api.catonetworks.com/documentation/#{operationType}-{subOperationName}) for documentation on this operation.

### Usage for {subOperationPath}:

`catocli {subOperationCmd} -h`
"""
        if isinstance(subOperation, dict) and "path" in subOperation:
            readmeStr += f"""
`catocli {subOperationCmd} <json>`

`catocli {subOperationCmd} "$(cat < {subOperationName}.json)"`

"""
            # Note: GitHub links for advanced examples are now handled dynamically in the help system
            
            # Check for example file and insert its content before Operation Arguments
            example_file_path = f"examples/{subOperationPath}.md"
            try:
                example_content = openFile(example_file_path)
                # Add the example content with proper formatting
                readmeStr += f"""
## Advanced Usage
{example_content}

"""
            except:
                # If example file doesn't exist, continue without adding example content
                pass
        
        if not os.path.exists(parserPath):
            os.makedirs(parserPath)
        with file_write_lock:
            writeFile(parserPath+"/README.md", readmeStr)
        
        # Only recurse if subOperation is a dict and doesn't have a "path" key
        if isinstance(subOperation, dict) and "path" not in subOperation:
            renderSubReadme(subOperation, operationType, subOperationPath)

def main():
    # Main execution function with threading support
    options = initParser()
    
    # Load the introspection schema
    print("Loading schema...")
    schema = loadJSON("./introspection.json")
    
    print("Starting multi-threaded schema parsing...")
    start_time = time.time()
    
    # Parse the schema using multi-threading
    parseSchema(schema)
    
    end_time = time.time()
    print(f"\n• Schema processing completed in {end_time - start_time:.2f} seconds")
    
    print("\n• Generating CLI components...")
    writeCliDriver(catoApiSchema)
    writeOperationParsers(catoApiSchema)
    writeReadmes(catoApiSchema)
    
    total_operations = len(catoApiSchema["query"]) + len(catoApiSchema["mutation"])
    print(f"\n• Successfully generated {total_operations} operation models")
    print(f"   - Query operations: {len(catoApiSchema['query'])}")
    print(f"   - Mutation operations: {len(catoApiSchema['mutation'])}")
    
if __name__ == "__main__":
    main()
