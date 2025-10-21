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

# Import shared utility functions
try:
    from .formatter_utils import convert_bytes_to_mb, is_bytes_measure
except ImportError:
    try:
        from catocli.Utils.formatter_utils import convert_bytes_to_mb, is_bytes_measure
    except ImportError:
        from formatter_utils import convert_bytes_to_mb, is_bytes_measure


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
            # Check if this is a bytes field using both unit type and field name
            unit_type = record_unit_types[i] if i < len(record_unit_types) else "unknown"
            is_bytes_field = (unit_type == 'bytes') or is_bytes_measure(field, unit_type)
            
            if is_bytes_field:
                try:
                    formatted_mb = convert_bytes_to_mb(value)
                    record_data[field] = {
                        "value": value,
                        "formatted_mb": formatted_mb,
                        "unit_type": "bytes"
                    }
                except (ValueError, ZeroDivisionError):
                    record_data[field] = {
                        "value": value,
                        "unit_type": "bytes_err"
                    }
            else:
                record_data[field] = {
                    "value": value,
                    "unit_type": unit_type
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
        unit_type = field_unit_types[i] if i < len(field_unit_types) else "unknown"
        is_bytes_field = (unit_type == 'bytes') or is_bytes_measure(field_name, unit_type)
        
        if is_bytes_field:
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
            
            # Check if this is a bytes field using both unit type and field name
            unit_type = record_unit_types[i] if i < len(record_unit_types) else "unknown"
            is_bytes_field = (unit_type == 'bytes') or is_bytes_measure(field, unit_type)
            
            # Convert bytes to MB if the field is a bytes field
            if is_bytes_field:
                try:
                    formatted_value = convert_bytes_to_mb(value) if value != '' else ''
                    row.append(formatted_value)
                except (ValueError, ZeroDivisionError):
                    row.append(str(value) if value != '' else '')
            else:
                row.append(str(value) if value != '' else '')
        
        writer.writerow(row)
    
    return output.getvalue()