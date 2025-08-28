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
    
    # Step 1: Download schema with introspection query
    query = {
        'query': 'query IntrospectionQuery { __schema { description } }',
        'operationName': 'IntrospectionQuery'
    }
    
    success, introspection = catolib.send(options.api_key, query)
    if not success:
        print("ERROR: Failed to download schema")
        return
    
    print("• Schema downloaded successfully")
    
    # Step 2: Parse schema using multi-threading
    print("• Parsing schema with multi-threading...")
    catolib.parseSchema(introspection)
    print("• Schema parsed successfully")
    
    # Step 3: Generate all CLI components
    print("• Generating CLI components...")
    catolib.writeCliDriver(catolib.catoApiSchema)
    print("• CLI driver generated")
    
    catolib.writeOperationParsers(catolib.catoApiSchema)
    print("• Operation parsers generated")
    
    catolib.writeReadmes(catolib.catoApiSchema)
    print("• README files generated")
    
    # Save the processed schema files for reference
    catolib.writeFile("catoApiIntrospection.json", json.dumps(catolib.catoApiIntrospection, indent=4, sort_keys=True))
    catolib.writeFile("catoApiSchema.json", json.dumps(catolib.catoApiSchema, indent=4, sort_keys=True))
    catolib.writeFile("introspection.json", json.dumps(introspection, indent=4, sort_keys=True))
    print("• Schema files saved")
    
    total_operations = len(catolib.catoApiSchema["query"]) + len(catolib.catoApiSchema["mutation"])
    print(f"\n- Continuous build completed successfully!")
    print(f"   - Total operations generated: {total_operations}")
    print(f"   - Query operations: {len(catolib.catoApiSchema['query'])}")
    print(f"   - Mutation operations: {len(catolib.catoApiSchema['mutation'])}")

if __name__ == '__main__':
    run()
