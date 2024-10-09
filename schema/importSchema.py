#!/usr/bin/python
import catolib
import logging
import json

############ ENV Settings ############
logging.basicConfig(filename="download-schema.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
options = catolib.initParser()

def run():
	# ########################## OPTION 1 ##############################
	# ## Uncomment this secion to build cli as one continuous job 
	# ##################################################################
	# query = {
	# 	'query':'query IntrospectionQuery { __schema { description } }',
	# 	'operationName':'IntrospectionQuery'
	# }
	# success,introspection = catolib.send(options.api_key,query)
	# catolib.parseSchema(introspection)
	# catolib.writeCliDriver(catolib.catoApiSchema)
	# catolib.writeOperationParsers(catolib.catoApiSchema)
	# catolib.writeReadmes(catolib.catoApiSchema)
	# ##################################################################

	######################### OPTION 2 ##############################
	## Uncomment to manually run each step manually writing files locally 
	######################### Step 1 ################################ 
	## Run intrpsection to pull down schema and write locally
	################################################################# 
	query = {
		'query':'query IntrospectionQuery { __schema { description } }',
		'operationName':'IntrospectionQuery'
	}
	success,resp = catolib.send(options.api_key,query)
	catolib.writeFile("introspection.json",json.dumps(resp, indent=4, sort_keys=True))
	# ################################################################# 
	
	######################### Step 2 ################################ 
	## Load from introsspeection from local file, and 
	## use catolib to parse the schema, write locally 
	## to catoApiIntrospection.json and catoApiSchema.json
	################################################################# 
	introspection = catolib.loadJSON("introspection.json")
	catolib.parseSchema(introspection)
	catolib.writeFile("catoApiIntrospection.json",json.dumps(catolib.catoApiIntrospection, indent=4, sort_keys=True))
	catolib.writeFile("catoApiSchema.json",json.dumps(catolib.catoApiSchema, indent=4, sort_keys=True))
	#################################################################      

	####################### Step 3 ################################ 
	## Load catoApiSchema from local file, and write cliDriver
	## operation parsers, and readmes locally
	#############################################################
	catolib.catoApiSchema = catolib.loadJSON("catoApiSchema.json")
	catolib.writeCliDriver(catolib.catoApiSchema)
	catolib.writeOperationParsers(catolib.catoApiSchema)
	catolib.writeReadmes(catolib.catoApiSchema)
	###############################################################

if __name__ == '__main__':
	run()