#!/usr/bin/env python3
"""
PoP Locations Formatter for Cato CLI

Formats popLocations API responses into JSON and CSV formats
"""

import csv
import io
import json
from typing import Dict, List, Any


def format_pop_locations(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert popLocations JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from popLocations query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format
    """
    if output_format.lower() == 'csv':
        return format_pop_locations_to_csv(response_data)
    else:
        return _format_pop_locations_to_json(response_data)


def _format_pop_locations_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert popLocations JSON response to organized JSON format
    
    Args:
        response_data: JSON response from popLocations query
        
    Returns:
        JSON formatted string with organized PoP location data
    """
    if not response_data or not isinstance(response_data, dict):
        return json.dumps({"error": "Invalid response data"}, indent=2)
    
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'popLocations' not in response_data['data']:
        return json.dumps({"error": "Invalid popLocations response structure"}, indent=2)
    
    return json.dumps(response_data, indent=2)


def format_pop_locations_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert popLocations JSON response to CSV format with all PoP locations flattened
    
    Args:
        response_data: JSON response from popLocations query
        
    Returns:
        CSV formatted string
    """
    if not response_data or not isinstance(response_data, dict):
        return "ERROR: Invalid response data"
    
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'popLocations' not in response_data['data']:
        return "ERROR: Invalid popLocations response structure"
    
    pop_location_list = response_data['data']['popLocations'].get('popLocationList', {})
    if not pop_location_list:
        return "ERROR: No popLocations found"
    
    items = pop_location_list.get('items', [])
    if not items:
        return "ERROR: No PoP location items found"
    
    # CSV output
    output = io.StringIO()
    
    # Define CSV columns
    fieldnames = [
        'id', 'name', 'displayName', 'country_id', 'country_name', 
        'isPrivate', 'cloud_providers', 'tagging_methods'
    ]
    
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    
    # Process each PoP location
    for pop in items:
        # Extract cloud interconnect providers and tagging methods
        cloud_interconnects = pop.get('cloudInterconnect', []) or []
        providers = []
        tagging_methods = []
        
        for interconnect in cloud_interconnects:
            if interconnect.get('providerName'):
                providers.append(interconnect['providerName'])
            if interconnect.get('taggingMethod'):
                tagging_methods.append(interconnect['taggingMethod'])
        
        row = {
            'id': pop.get('id'),
            'name': pop.get('name'),
            'displayName': pop.get('displayName'),
            'country_id': pop.get('country', {}).get('id') if pop.get('country') else '',
            'country_name': pop.get('country', {}).get('name') if pop.get('country') else '',
            'isPrivate': pop.get('isPrivate', False),
            'cloud_providers': ', '.join(providers) if providers else '',
            'tagging_methods': ', '.join(tagging_methods) if tagging_methods else ''
        }
        writer.writerow(row)
    
    csv_content = output.getvalue()
    output.close()
    
    return csv_content
