#!/usr/bin/env python3
"""
App Stats Formatter for Cato CLI

This module provides functions to format appStats API responses
into JSON and CSV formats, with special handling for field data
and unit conversions.
"""

import csv
import io
import json
from typing import Dict, List, Any

# Helper functions
def convert_bytes_to_mb(value: Any) -> str:
    """
    Convert bytes value to megabytes with proper formatting

    Args:
        value: The value to convert (should be numeric)
        
    Returns:
        Formatted MB value as string
    """
    if not value or not str(value).replace('.', '').replace('-', '').isdigit():
        return str(value) if value is not None else ''
    
    try:
        # Convert bytes to megabytes (divide by 1,048,576)
        mb_value = float(value) / 1048576
        # Format to 3 decimal places, but remove trailing zeros
        return f"{mb_value:.3f}".rstrip('0').rstrip('.')
    except (ValueError, ZeroDivisionError):
        return str(value) if value is not None else ''


def format_app_stats(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert appStats JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from appStats query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format, or None if no processable data
    """
    if output_format.lower() == 'csv':
        return _format_app_stats_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_app_stats_to_json(response_data)


def _format_app_stats_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert appStats JSON response to organized JSON format
    
    Args:
        response_data: JSON response from appStats query
        
    Returns:
        JSON formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'appStats' not in response_data['data']:
        return None
    
    app_stats = response_data['data']['appStats']
    if not app_stats or not isinstance(app_stats, dict):
        return None
    
    records = app_stats.get('records', [])
    
    if not records:
        return None
    
    # Organize data in a more structured format
    organized_data = {
        "appStats": {
            "summary": {
                "total_records": len(records),
                "field_names": list(records[0].get('fieldsMap', {}).keys()) if records else [],
                "data_types": records[0].get('fieldsUnitTypes', []) if records else []
            },
            "records": []
        }
    }
    
    # Process each record
    for record in records:
        fields_map = record.get('fieldsMap', {})
        record_unit_types = record.get('fieldsUnitTypes', [])
        
        record_data = {}
        
        for i, (field, value) in enumerate(fields_map.items()):
            # Add unit type information for bytes fields
            if (i < len(record_unit_types) and 
                record_unit_types[i] == 'bytes' and 
                value and str(value).replace('.', '').replace('-', '').isdigit()):
                try:
                    # Convert bytes to megabytes for display
                    mb_value = float(value) / 1048576
                    formatted_value = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                    record_data[field] = {
                        "value": value,
                        "formatted_mb": formatted_value,
                        "unit_type": "bytes"
                    }
                except (ValueError, ZeroDivisionError):
                    record_data[field] = {
                        "value": value,
                        "unit_type": "bytes"
                    }
            else:
                record_data[field] = {
                    "value": value,
                    "unit_type": record_unit_types[i] if i < len(record_unit_types) else "unknown"
                }
        
        organized_data["appStats"]["records"].append(record_data)
    
    return json.dumps(organized_data, indent=2)


def _format_app_stats_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert appStats JSON response to CSV format
    
    Args:
        response_data: JSON response from appStats query
        
    Returns:
        CSV formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'appStats' not in response_data['data']:
        return None
    
    app_stats = response_data['data']['appStats']
    if not app_stats or not isinstance(app_stats, dict):
        return None
    
    records = app_stats.get('records', [])
    
    if not records:
        return None
    
    # Get all possible field names from the first record's fieldsMap
    first_record = records[0]
    field_names = list(first_record.get('fieldsMap', {}).keys())
    field_unit_types = first_record.get('fieldsUnitTypes', [])
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Create headers with _mb suffix for bytes fields
    headers = []
    for i, field_name in enumerate(field_names):
        if i < len(field_unit_types) and field_unit_types[i] == 'bytes':
            headers.append(f'{field_name}_mb')
        else:
            headers.append(field_name)
    
    # Write header
    writer.writerow(headers)
    
    # Write data rows
    for record in records:
        fields_map = record.get('fieldsMap', {})
        record_unit_types = record.get('fieldsUnitTypes', [])
        row = []
        
        for i, field in enumerate(field_names):
            value = fields_map.get(field, '')
            
            # Convert bytes to MB if the field type is bytes
            if (i < len(record_unit_types) and 
                record_unit_types[i] == 'bytes' and 
                value and str(value).replace('.', '').replace('-', '').isdigit()):
                try:
                    # Convert bytes to megabytes (divide by 1,048,576)
                    mb_value = float(value) / 1048576
                    # Format to 3 decimal places, but remove trailing zeros
                    formatted_value = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                    row.append(formatted_value)
                except (ValueError, ZeroDivisionError):
                    row.append(value)
            else:
                row.append(value)
        
        writer.writerow(row)
    
    return output.getvalue()