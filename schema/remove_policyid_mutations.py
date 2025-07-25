#!/usr/bin/env python3

import json
import os
import glob

def remove_policy_id_recursive(obj, path=""):
    """
    Recursively remove all 'policyId' keys from a JSON object.
    Returns the number of removals made.
    """
    removals = 0
    
    if isinstance(obj, dict):
        # Create a list of keys to remove to avoid modifying dict during iteration
        keys_to_remove = []
        for key in obj.keys():
            if key == "policyId":
                keys_to_remove.append(key)
                current_path = f"{path}.{key}" if path else key
                print(f"  Removing policyId at: {current_path}")
                removals += 1
        
        # Remove the policyId keys
        for key in keys_to_remove:
            del obj[key]
        
        # Recursively process remaining values
        for key, value in obj.items():
            current_path = f"{path}.{key}" if path else key
            removals += remove_policy_id_recursive(value, current_path)
    
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            current_path = f"{path}[{i}]" if path else f"[{i}]"
            removals += remove_policy_id_recursive(item, current_path)
    
    return removals

def process_mutation_policy_files():
    """
    Find and process all mutation.policy*.json files in the models directory.
    """
    models_dir = "/Users/briananderson/Documents/Dev/github.com/catonetworks/cato-cli/models"
    pattern = os.path.join(models_dir, "mutation.policy*.json")
    
    files = glob.glob(pattern)
    
    if not files:
        print("No mutation.policy*.json files found!")
        return
    
    print(f"Found {len(files)} mutation.policy*.json files to process:")
    
    total_removals = 0
    processed_files = 0
    
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        print(f"\nProcessing: {filename}")
        
        try:
            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Remove policyId fields
            removals = remove_policy_id_recursive(data, filename)
            
            if removals > 0:
                # Write back the modified JSON
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                
                print(f"  Removed {removals} policyId field(s)")
                total_removals += removals
                processed_files += 1
            else:
                print("  No policyId fields found")
                
        except Exception as e:
            print(f"  Error processing {filename}: {e}")
    
    print(f"\n=== Summary ===")
    print(f"Files processed: {processed_files}")
    print(f"Total policyId fields removed: {total_removals}")

if __name__ == "__main__":
    process_mutation_policy_files()
