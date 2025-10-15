#!/usr/bin/env python3
"""
Socket Port Metrics Formatter for Cato CLI

This module provides functions to format socketPortMetrics API responses
into JSON and CSV formats, with special handling for field data
and unit conversions.
"""

import csv
import io
import json
from typing import Dict, List, Any

# Import shared utility functions
try:
    from .formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure
except ImportError:
    try:
        from catocli.Utils.formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure
    except ImportError:
        from formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure


def format_socket_port_metrics(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert socketPortMetrics JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from socketPortMetrics query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format, or None if no processable data
    """
    if output_format.lower() == 'csv':
        return _format_socket_port_metrics_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_socket_port_metrics_to_json(response_data)


def _format_socket_port_metrics_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetrics JSON response to organized JSON format
    
    Args:
        response_data: JSON response from socketPortMetrics query
        
    Returns:
        JSON formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'socketPortMetrics' not in response_data['data']:
        return None
    
    socket_metrics = response_data['data']['socketPortMetrics']
    if not socket_metrics or not isinstance(socket_metrics, dict):
        return None
    
    records = socket_metrics.get('records', [])
    
    if not records:
        return None
    
    # Organize data in a more structured format
    organized_data = {
        "socketPortMetrics": {
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
            # Get unit type for this field
            unit_type = record_unit_types[i] if i < len(record_unit_types) else "unknown"
            
            # Add unit type information for bytes fields using shared utility
            if is_bytes_measure(field, unit_type):
                formatted_mb = convert_bytes_to_mb(value)
                if formatted_mb and formatted_mb != str(value):
                    record_data[field] = {
                        "value": value,
                        "formatted_mb": formatted_mb,
                        "unit_type": "bytes"
                    }
                else:
                    record_data[field] = {
                        "value": value,
                        "unit_type": "bytes"
                    }
            else:
                record_data[field] = {
                    "value": value,
                    "unit_type": unit_type
                }
        
        organized_data["socketPortMetrics"]["records"].append(record_data)
    
    return json.dumps(organized_data, indent=2)


def _format_socket_port_metrics_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetrics JSON response to CSV format
    
    Args:
        response_data: JSON response from socketPortMetrics query
        
    Returns:
        CSV formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'socketPortMetrics' not in response_data['data']:
        return None
    
    socket_metrics = response_data['data']['socketPortMetrics']
    if not socket_metrics or not isinstance(socket_metrics, dict):
        return None
    
    records = socket_metrics.get('records', [])
    
    if not records:
        return None
    
    # Get all possible field names from the first record's fieldsMap
    first_record = records[0]
    field_names = list(first_record.get('fieldsMap', {}).keys())
    field_unit_types = first_record.get('fieldsUnitTypes', [])
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Create headers with _mb suffix for bytes fields using shared utility
    headers = []
    for i, field_name in enumerate(field_names):
        unit_type = field_unit_types[i] if i < len(field_unit_types) else "unknown"
        if is_bytes_measure(field_name, unit_type):
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
            unit_type = record_unit_types[i] if i < len(record_unit_types) else "unknown"
            
            # Convert bytes to MB using shared utility function
            if is_bytes_measure(field, unit_type):
                formatted_value = convert_bytes_to_mb(value)
                row.append(formatted_value if formatted_value else value)
            else:
                row.append(value)
        
        writer.writerow(row)
    
    return output.getvalue()
