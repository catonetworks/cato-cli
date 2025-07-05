#!/usr/bin/env python3
import json
import os
import sys
import subprocess
from typing import Any, Dict, List, Union

def should_strip_id(obj: Dict[str, Any]) -> bool:
    if not isinstance(obj, dict):
        return False
    
    keys = set(obj.keys())
    return keys == {'name', 'id'}

def strip_ids_recursive(obj: Union[Dict, List, Any]) -> Union[Dict, List, Any, None]:
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            ## Ignoring sections to retain id and name pair
            if key == 'sections':
                new_obj[key] = value
            else:
                processed_value = strip_ids_recursive(value)
                # Skip keys where the value is an empty list
                if processed_value != []:
                    new_obj[key] = processed_value
            # Check if this object should have its id stripped
            if should_strip_id(new_obj):
                return {'name': new_obj['name']}
        return new_obj

    elif isinstance(obj, list):
        # Recursively process all items in the list
        processed_list = [strip_ids_recursive(item) for item in obj]
        # Remove None values from the list (if any were removed)
        processed_list = [item for item in processed_list if item is not None]
        return processed_list
    
    else:
        # For primitive types (str, int, bool, None), return as-is
        return obj

## General purpose functions
def exec_cli(command):
    result = None
    try:
        response = subprocess.run(command, shell=True, text=True, capture_output=True)
        if response.returncode != 0:
            print(f"Command failed with return code {response.returncode}")
            print(f"stderr: {response.stderr}")
            return None
        result = json.loads(response.stdout)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")
        print(f"stdout: {response.stdout}")
        print(f"stderr: {response.stderr}")
        return None
    except Exception as e:
        print(f"Failed to execute command: {e}")
        return None
    return result

