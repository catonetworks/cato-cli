#!/usr/bin/python
import catolib
import logging
import json
import concurrent.futures
import threading
import sys

############ ENV Settings ############
logging.basicConfig(filename="download-schema.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
options = catolib.initParser()

# Increase recursion limit for complex schemas
sys.setrecursionlimit(5000)

def run():
    print("Starting continuous multi-threaded schema processing...")
    
    ######################### CONTINUOUS BUILD PROCESS ##############################
    ## Single continuous process - download, parse, and generate all in one flow
    print("Downloading and processing GraphQL schema...")
    query = {
        'query': 'query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } }  fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } }  fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue }  fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }',
        'operationName': 'IntrospectionQuery'
    }
    success, introspection = catolib.send(options.api_key, query)
    if not success:
        print("ERROR: Failed to download schema")
        return
    
    print("• Schema downloaded successfully")
    print("• Parsing schema with enhanced dynamic field expansion...")
    catolib.parseSchema(introspection)
    print("• Schema parsed successfully")
    print("• Generating CLI components...")
    catolib.writeCliDriver(catolib.catoApiSchema)
    print("• CLI driver generated")
    catolib.writeOperationParsers(catolib.catoApiSchema)
    print("• Operation parsers generated")
    catolib.writeReadmes(catolib.catoApiSchema)
    print("• README files generated")
        
    total_operations = len(catolib.catoApiSchema["query"]) + len(catolib.catoApiSchema["mutation"])
    print(f"\n Continuous build completed successfully!")
    print(f"   - Total operations generated: {total_operations}")
    print(f"   - Query operations: {len(catolib.catoApiSchema['query'])}")
    print(f"   - Mutation operations: {len(catolib.catoApiSchema['mutation'])}")
    print(f"   - Total types processed: {len(catolib.catoApiIntrospection['objects']) + len(catolib.catoApiIntrospection['enums']) + len(catolib.catoApiIntrospection['scalars'])}")

if __name__ == '__main__':
    run()
