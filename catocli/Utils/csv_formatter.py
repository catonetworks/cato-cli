#!/usr/bin/env python3
"""
CSV Formatter for Cato CLI

This module provides functions to convert JSON responses from Cato API
into CSV format, with special handling for timeseries data in wide format.

Supports multiple response patterns:
- Records grid (appStats): records[] with fieldsMap + fieldsUnitTypes  
- Flat timeseries (appStatsTimeSeries, socketPortMetricsTimeSeries): timeseries[] with labels
- Hierarchical timeseries (accountMetrics): sites[] → interfaces[] → timeseries[]
"""

import csv
import io
import json
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Set, Tuple


# Shared Helper Functions

def format_timestamp(timestamp_ms: int) -> str:
    """
    Convert timestamp from milliseconds to readable format
    
    Args:
        timestamp_ms: Timestamp in milliseconds
        
    Returns:
        Formatted timestamp string in UTC
    """
    try:
        # Convert milliseconds to seconds for datetime
        timestamp_sec = timestamp_ms / 1000
        dt = datetime.utcfromtimestamp(timestamp_sec)
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except (ValueError, OSError):
        return str(timestamp_ms)


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


def parse_label_for_dimensions_and_measure(label: str) -> Tuple[str, Dict[str, str]]:
    """
    Parse timeseries label to extract measure and dimensions
    
    Args:
        label: Label like "sum(traffic) for application_name='App', user_name='User'"
        
    Returns:
        Tuple of (measure, dimensions_dict)
    """
    measure = ""
    dimensions = {}
    
    if ' for ' in label:
        measure_part, dim_part = label.split(' for ', 1)
        # Extract measure (e.g., "sum(traffic)")
        if '(' in measure_part and ')' in measure_part:
            measure = measure_part.split('(')[1].split(')')[0]
        
        # Parse dimensions using regex for better handling of quoted values
        # Matches: key='value' or key="value" or key=value
        dim_pattern = r'(\w+)=[\'"]*([^,\'"]+)[\'"]*'
        matches = re.findall(dim_pattern, dim_part)
        for key, value in matches:
            dimensions[key.strip()] = value.strip()
    else:
        # Fallback: use the whole label as measure
        measure = label
    
    return measure, dimensions


def is_bytes_measure(measure: str, units: str = "") -> bool:
    """
    Determine if a measure represents bytes data that should be converted to MB
    
    Args:
        measure: The measure name
        units: The units field if available
        
    Returns:
        True if this measure should be converted to MB
    """
    bytes_measures = {
        'downstream', 'upstream', 'traffic', 'bytes', 'bytesDownstream', 
        'bytesUpstream', 'bytesTotal', 'throughput_downstream', 'throughput_upstream'
    }
    
    # Check if measure name indicates bytes
    if measure.lower() in bytes_measures:
        return True
        
    # Check if measure contains bytes-related keywords
    if any(keyword in measure.lower() for keyword in ['bytes', 'throughput']):
        return True
        
    # Check units field
    if units and 'bytes' in units.lower():
        return True
        
    return False


def build_wide_timeseries_header(dimension_names: List[str], measures: List[str], 
                                 sorted_timestamps: List[int], bytes_measures: Set[str]) -> List[str]:
    """
    Build header for wide-format timeseries CSV
    
    Args:
        dimension_names: List of dimension column names
        measures: List of measure names
        sorted_timestamps: List of timestamps in order
        bytes_measures: Set of measures that should have _mb suffix
        
    Returns:
        Complete header row as list of strings
    """
    header = dimension_names.copy()
    
    # Add timestamp and measure columns for each time period
    for i, timestamp in enumerate(sorted_timestamps, 1):
        header.append(f'timestamp_period_{i}')
        for measure in measures:
            if measure in bytes_measures:
                header.append(f'{measure}_period_{i}_mb')
            else:
                header.append(f'{measure}_period_{i}')
    
    return header


def format_app_stats_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert appStats JSON response to CSV format
    
    Args:
        response_data: JSON response from appStats query
        
    Returns:
        CSV formatted string
    """
    if not response_data or not isinstance(response_data, dict):
        return ""
    
    # Check for API errors
    if 'errors' in response_data:
        return ""
    
    if 'data' not in response_data or 'appStats' not in response_data['data']:
        return ""
    
    app_stats = response_data['data']['appStats']
    if not app_stats or not isinstance(app_stats, dict):
        return ""
    
    records = app_stats.get('records', [])
    
    if not records:
        return ""
    
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


def format_app_stats_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert appStatsTimeSeries JSON response to wide-format CSV
    Similar to the reference sccm_app_stats_wide_format.csv
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        
    Returns:
        CSV formatted string in wide format with timestamps as columns
    """
    if not response_data or 'data' not in response_data or 'appStatsTimeSeries' not in response_data['data']:
        return ""
    
    app_stats_ts = response_data['data']['appStatsTimeSeries']
    timeseries = app_stats_ts.get('timeseries', [])
    
    if not timeseries:
        return ""
    
    # Parse dimension information and measures from labels
    # Labels are like: "sum(traffic) for application_name='Google Applications', user_name='PM Analyst'"
    parsed_series = []
    all_timestamps = set()
    
    for series in timeseries:
        label = series.get('label', '')
        data_points = series.get('data', [])
        
        # Extract measure and dimensions from label
        # Example: "sum(traffic) for application_name='Google Applications', user_name='PM Analyst'"
        measure = ""
        dimensions = {}
        
        try:
            if ' for ' in label:
                measure_part, dim_part = label.split(' for ', 1)
                # Extract measure (e.g., "sum(traffic)")
                if '(' in measure_part and ')' in measure_part:
                    measure = measure_part.split('(')[1].split(')')[0]
                
                # Parse dimensions using regex for better handling of quoted values
                # Matches: key='value' or key="value" or key=value
                dim_pattern = r'(\w+)=[\'"]*([^,\'"]+)[\'"]*'
                matches = re.findall(dim_pattern, dim_part)
                for key, value in matches:
                    dimensions[key.strip()] = value.strip()
            else:
                # Fallback: use the whole label as measure
                measure = label
            
            # Create series entry with safe data parsing
            data_dict = {}
            for point in data_points:
                if isinstance(point, (list, tuple)) and len(point) >= 2:
                    data_dict[int(point[0])] = point[1]
            
            series_entry = {
                'measure': measure,
                'dimensions': dimensions,
                'data': data_dict
            }
            parsed_series.append(series_entry)
            
            # Collect all timestamps
            all_timestamps.update(series_entry['data'].keys())
        except Exception as e:
            print(f"DEBUG: Error processing series with label '{label}': {e}")
            continue
    
    # Sort timestamps
    sorted_timestamps = sorted(all_timestamps)
    
    # Get all unique dimension combinations
    dimension_combos = {}
    for series in parsed_series:
        try:
            dim_key = tuple(sorted(series['dimensions'].items()))
            if dim_key not in dimension_combos:
                dimension_combos[dim_key] = {}
            dimension_combos[dim_key][series['measure']] = series['data']
        except Exception as e:
            print(f"DEBUG: Error processing dimension combination for series: {e}")
            print(f"DEBUG: Series dimensions: {series.get('dimensions', {})}")  
            continue
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header
    dimension_names = set()
    measures = set()
    for series in parsed_series:
        dimension_names.update(series['dimensions'].keys())
        measures.add(series['measure'])
    
    dimension_names = sorted(dimension_names)
    measures = sorted(measures)
    
    header = dimension_names.copy()
    # Add timestamp and measure columns for each time period
    for i, timestamp in enumerate(sorted_timestamps, 1):
        formatted_ts = format_timestamp(timestamp)
        header.append(f'timestamp_period_{i}')
        for measure in measures:
            # Add _mb suffix for bytes measures
            if measure in ['downstream', 'upstream', 'traffic']:
                header.append(f'{measure}_period_{i}_mb')
            else:
                header.append(f'{measure}_period_{i}')
    
    writer.writerow(header)
    
    # Write data rows
    for dim_combo, measures_data in dimension_combos.items():
        row = []
        
        # Add dimension values
        dim_dict = dict(dim_combo)
        for dim_name in dimension_names:
            row.append(dim_dict.get(dim_name, ''))
        
        # Add timestamp and measure data for each period
        for timestamp in sorted_timestamps:
            formatted_ts = format_timestamp(timestamp)
            row.append(formatted_ts)
            
            for measure in measures:
                value = measures_data.get(measure, {}).get(timestamp, '')
                # Convert bytes measures to MB
                if measure in ['downstream', 'upstream', 'traffic'] and value and str(value).replace('.', '').replace('-', '').isdigit():
                    try:
                        # Convert bytes to megabytes
                        mb_value = float(value) / 1048576
                        formatted_value = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                        row.append(formatted_value)
                    except (ValueError, ZeroDivisionError):
                        row.append(value)
                else:
                    row.append(value)
        
        writer.writerow(row)
    
    return output.getvalue()


def format_socket_port_metrics_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to wide-format CSV
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        
    Returns:
        CSV formatted string in wide format with timestamps as columns
    """
    if not response_data or 'data' not in response_data or 'socketPortMetricsTimeSeries' not in response_data['data']:
        return ""
    
    socket_metrics_ts = response_data['data']['socketPortMetricsTimeSeries']
    timeseries = socket_metrics_ts.get('timeseries', [])
    
    if not timeseries:
        return ""
    
    # Parse measures from labels - these are simpler than appStatsTimeSeries
    # Labels are like: "sum(throughput_downstream)" with no dimensions
    parsed_series = []
    all_timestamps = set()
    
    for series in timeseries:
        label = series.get('label', '')
        data_points = series.get('data', [])
        units = series.get('unitsTimeseries', '')
        info = series.get('info', [])
        
        # Extract measure from label - usually just "sum(measure_name)"
        measure, dimensions = parse_label_for_dimensions_and_measure(label)
        
        # If no dimensions found in label, create default dimensions from info if available
        if not dimensions and info:
            # Info array might contain contextual data like socket/port identifiers
            for i, info_value in enumerate(info):
                dimensions[f'info_{i}'] = str(info_value)
        
        # If still no dimensions, create a single default dimension
        if not dimensions:
            dimensions = {'metric_source': 'socket_port'}
        
        series_entry = {
            'measure': measure,
            'dimensions': dimensions,
            'units': units,
            'data': {int(point[0]): point[1] for point in data_points if len(point) >= 2}
        }
        parsed_series.append(series_entry)
        
        # Collect all timestamps
        all_timestamps.update(series_entry['data'].keys())
    
    # Sort timestamps
    sorted_timestamps = sorted(all_timestamps)
    
    # Get all unique dimension combinations
    dimension_combos = {}
    for series in parsed_series:
        dim_key = tuple(sorted(series['dimensions'].items()))
        if dim_key not in dimension_combos:
            dimension_combos[dim_key] = {}
        dimension_combos[dim_key][series['measure']] = {
            'data': series['data'],
            'units': series['units']
        }
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header
    dimension_names = set()
    measures = set()
    bytes_measures = set()
    
    for series in parsed_series:
        dimension_names.update(series['dimensions'].keys())
        measures.add(series['measure'])
        
        # Check if this measure should be converted to MB
        if is_bytes_measure(series['measure'], series['units']):
            bytes_measures.add(series['measure'])
    
    dimension_names = sorted(dimension_names)
    measures = sorted(measures)
    
    # Build header using shared helper
    header = build_wide_timeseries_header(dimension_names, measures, sorted_timestamps, bytes_measures)
    writer.writerow(header)
    
    # Write data rows
    for dim_combo, measures_data in dimension_combos.items():
        row = []
        
        # Add dimension values
        dim_dict = dict(dim_combo)
        for dim_name in dimension_names:
            row.append(dim_dict.get(dim_name, ''))
        
        # Add timestamp and measure data for each period
        for timestamp in sorted_timestamps:
            formatted_ts = format_timestamp(timestamp)
            row.append(formatted_ts)
            
            for measure in measures:
                measure_info = measures_data.get(measure, {})
                value = measure_info.get('data', {}).get(timestamp, '')
                
                # Convert bytes measures to MB
                if measure in bytes_measures and value:
                    row.append(convert_bytes_to_mb(value))
                else:
                    row.append(value)
        
        writer.writerow(row)
    
    return output.getvalue()


def format_to_csv(response_data: Dict[str, Any], operation_name: str) -> str:
    """
    Main function to format response data to CSV based on operation type
    
    Args:
        response_data: JSON response data
        operation_name: Name of the operation (e.g., 'query.appStats')
        
    Returns:
        CSV formatted string
    """
    if operation_name == 'query.appStats':
        return format_app_stats_to_csv(response_data)
    elif operation_name == 'query.appStatsTimeSeries':
        return format_app_stats_timeseries_to_csv(response_data)
    elif operation_name == 'query.socketPortMetricsTimeSeries':
        return format_socket_port_metrics_timeseries_to_csv(response_data)
    else:
        # Default: try to convert any JSON response to simple CSV
        return json.dumps(response_data, indent=2)
