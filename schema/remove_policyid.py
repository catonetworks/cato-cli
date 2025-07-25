#!/usr/bin/env python3

import json
import glob
import os
import sys

def remove_policy_id_from_object(obj, path=""):
    """
    Recursively remove policyId fields from a JSON object.
    """
    if isinstance(obj, dict):
        # Remove policyId field if it exists
        if "policyId" in obj:
            print(f"Removing policyId field at path: {path}")
            del obj["policyId"]
        
        # Recursively process all other fields
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else key
            remove_policy_id_from_object(value, new_path)
    
    elif isinstance(obj, list):
        # Process each item in the list
        for i, item in enumerate(obj):
            new_path = f"{path}[{i}]" if path else f"[{i}]"
            remove_policy_id_from_object(item, new_path)

def process_file(file_path):
    """
    Process a single JSON file to remove policyId fields.
    """
    print(f"Processing file: {file_path}")
    
    try:
        # Read the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Remove policyId fields
        remove_policy_id_from_object(data, os.path.basename(file_path))
        
        # Write the modified JSON back to the file
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        
        print(f"Successfully processed: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False
    
    return True

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Go up one level to cato-cli directory
    
    # Find all query.policy*.json files in the models directory
    models_dir = os.path.join(base_dir, "models")
    pattern = os.path.join(models_dir, "query.policy*.json")
    
    files = glob.glob(pattern)
    
    if not files:
        print("No query.policy*.json files found!")
        return 1
    
    print(f"Found {len(files)} files to process:")
    for file in files:
        print(f"  - {os.path.basename(file)}")
    
    # Process each file
    success_count = 0
    for file_path in files:
        if process_file(file_path):
            success_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {success_count}/{len(files)} files")
    
    if success_count != len(files):
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
