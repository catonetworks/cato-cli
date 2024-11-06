import json
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
from ..parserApiClient import validateArgs

def entityTypeList(args, configuration):
    params = vars(args)
    operation = { 
        "operationArgs": {
            "accountID": {
                "name": "accountID",
                "required": True,
            }
        }
    }
    variablesObj = { "accountID": (params.get("accountID") if params.get("accountID") else params.get("accountId"))}

    instance = CallApi(ApiClient(configuration))
    operationName = params["operation_name"]
    query = '''query entityLookup ( $type:EntityType! $accountID:ID! $search:String ) {
        entityLookup ( accountID:$accountID type:$type search:$search ) {
            '''+params["operation_name"]+'''s: items {
                description
                '''+params["operation_name"]+''': entity {
                    id
                    name
                    type
                }
            }
        }
    }'''
    body = {
        "query": query,
        "operationName": "entityLookup",
        "variables": {
            "accountID": configuration.accountID,
            "type": params["operation_name"],
            "search": (params.get("s") if params.get("s")!=None else "")
        }
    }
    
    isOk, invalidVars, message = validateArgs(variablesObj,operation)
    if isOk==True:        
        if params["t"]==True:
            if params["p"]==True:
                print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
            else:
                print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
            return None
        else:
            try:
                response = instance.call_api(body,params)
                if params["v"]==True:
                    print(json.dumps(response[0]))
                elif params["f"]=="json":
                    if params["p"]==True:
                        print(json.dumps(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"),indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
                    else:
                        print(json.dumps(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s")))
                else:
                    if len(response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"))==0:
                        print("No results found")
                    else:
                        print("id,name,type,description")
                        for site in response[0].get("data").get("entityLookup").get(params["operation_name"]+"s"):
                            print(site.get(params["operation_name"]).get('id')+","+site.get(params["operation_name"]).get('name')+","+site.get(params["operation_name"]).get('type')+","+site.get('description'))
            except ApiException as e:
                return e
    else:
        print("ERROR: "+message,", ".join(invalidVars))

