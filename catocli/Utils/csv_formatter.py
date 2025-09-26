#!/usr/bin/env python3
"""
CSV Formatter for Cato CLI

This module provides functions to convert JSON responses from Cato API
into CSV format, with special handling for timeseries data in long format.

Supports multiple response patterns:
- Records grid (appStats): records[] with fieldsMap + fieldsUnitTypes  
- Long-format timeseries (appStatsTimeSeries, socketPortMetricsTimeSeries): timeseries[] with labels (one row per timestamp)
- Hierarchical timeseries (userMetrics): sites[] → interfaces[] → timeseries[] (one row per timestamp)

All timeseries formatters now use long format (timestamp_period column) for better readability.
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
    Convert appStatsTimeSeries JSON response to long-format CSV (one row per timestamp)
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        
    Returns:
        CSV formatted string in long format with one row per timestamp
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
    
    # Collect all data in long format (one row per timestamp and dimension combination)
    rows = []
    
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
    
    # Create rows for each timestamp and dimension combination
    for dim_combo, measures_data in dimension_combos.items():
        dim_dict = dict(dim_combo)
        
        for timestamp in sorted_timestamps:
            # Build row data for this timestamp
            row_data = {
                'timestamp_period': format_timestamp(timestamp)
            }
            
            # Add dimension values
            for key, value in dim_dict.items():
                row_data[key] = value
            
            # Add measure values for this timestamp
            for measure, data in measures_data.items():
                value = data.get(timestamp, '')
                
                # Convert bytes measures to MB and add appropriate suffix
                if measure in ['downstream', 'upstream', 'traffic']:
                    if value:
                        try:
                            mb_value = float(value) / 1048576
                            formatted_value = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                            row_data[f'{measure}_mb'] = formatted_value
                        except (ValueError, ZeroDivisionError):
                            row_data[f'{measure}_mb'] = value
                    else:
                        row_data[f'{measure}_mb'] = value
                else:
                    row_data[measure] = value
            
            rows.append(row_data)
    
    if not rows:
        return ""
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header dynamically from all available columns
    all_columns = set()
    for row_data in rows:
        all_columns.update(row_data.keys())
    
    # Sort columns with timestamp_period first, then dimensions, then measures
    dimension_columns = []
    measure_columns = []
    
    for col in sorted(all_columns):
        if col == 'timestamp_period':
            continue  # Will be added first
        elif col.endswith('_mb') or col in ['downstream', 'upstream', 'traffic']:
            measure_columns.append(col)
        else:
            dimension_columns.append(col)
    
    header = ['timestamp_period'] + sorted(dimension_columns) + sorted(measure_columns)
    writer.writerow(header)
    
    # Write data rows
    for row_data in rows:
        row = []
        for col in header:
            value = row_data.get(col, '')
            row.append(value)
        writer.writerow(row)
    
    return output.getvalue()


def format_socket_port_metrics_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to long-format CSV (one row per timestamp)
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        
    Returns:
        CSV formatted string in long format with one row per timestamp
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
    
    # Collect all data in long format (one row per timestamp and dimension combination)
    rows = []
    
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
    
    # Create rows for each timestamp and dimension combination
    for dim_combo, measures_data in dimension_combos.items():
        dim_dict = dict(dim_combo)
        
        for timestamp in sorted_timestamps:
            # Build row data for this timestamp
            row_data = {
                'timestamp_period': format_timestamp(timestamp)
            }
            
            # Add dimension values
            for key, value in dim_dict.items():
                row_data[key] = value
            
            # Add measure values for this timestamp
            for measure, measure_info in measures_data.items():
                value = measure_info['data'].get(timestamp, '')
                units = measure_info['units']
                
                # Convert bytes measures to MB and add appropriate suffix
                if is_bytes_measure(measure, units):
                    if value:
                        converted_value = convert_bytes_to_mb(value)
                        row_data[f'{measure}_mb'] = converted_value
                    else:
                        row_data[f'{measure}_mb'] = value
                else:
                    row_data[measure] = value
            
            rows.append(row_data)
    
    if not rows:
        return ""
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header dynamically from all available columns
    all_columns = set()
    for row_data in rows:
        all_columns.update(row_data.keys())
    
    # Sort columns with timestamp_period first, then dimensions, then measures
    dimension_columns = []
    measure_columns = []
    
    for col in sorted(all_columns):
        if col == 'timestamp_period':
            continue  # Will be added first
        elif col.endswith('_mb') or col in ['throughput_downstream', 'throughput_upstream']:
            measure_columns.append(col)
        else:
            dimension_columns.append(col)
    
    header = ['timestamp_period'] + sorted(dimension_columns) + sorted(measure_columns)
    writer.writerow(header)
    
    # Write data rows
    for row_data in rows:
        row = []
        for col in header:
            value = row_data.get(col, '')
            row.append(value)
        writer.writerow(row)
    
    return output.getvalue()


def format_user_metrics_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert userMetrics JSON response to long-format CSV (one row per timestamp)
    
    Args:
        response_data: JSON response from userMetrics query
        
    Returns:
        CSV formatted string in long format with one row per timestamp
    """
    if not response_data or 'data' not in response_data or 'accountMetrics' not in response_data['data']:
        return ""
    
    account_metrics = response_data['data']['accountMetrics']
    users = account_metrics.get('users', [])
    
    if not users:
        return ""
    
    # Collect all data in long format (one row per timestamp)
    rows = []
    
    for user in users:
        user_id = user.get('id', '')
        interfaces = user.get('interfaces', [])
        
        for interface in interfaces:
            interface_name = interface.get('name', '')
            timeseries_list = interface.get('timeseries', [])
            
            # Organize timeseries data by timestamp
            timestamp_data = {}
            info_fields = {}
            
            for timeseries in timeseries_list:
                label = timeseries.get('label', '')
                units = timeseries.get('units', '')
                data_points = timeseries.get('data', [])
                info = timeseries.get('info', [])
                
                # Store info fields (should be consistent across timeseries)
                if info and len(info) >= 2:
                    info_fields['info_user_id'] = str(info[0])
                    info_fields['info_interface'] = str(info[1])
                
                # Process each data point
                for point in data_points:
                    if isinstance(point, (list, tuple)) and len(point) >= 2:
                        timestamp = int(point[0])
                        value = point[1]
                        
                        if timestamp not in timestamp_data:
                            timestamp_data[timestamp] = {}
                        
                        # Convert bytes measures to MB and add appropriate suffix
                        if is_bytes_measure(label, units) and value:
                            converted_value = convert_bytes_to_mb(value)
                            timestamp_data[timestamp][f'{label}_mb'] = converted_value
                        else:
                            timestamp_data[timestamp][label] = value
            
            # Create rows for each timestamp
            for timestamp in sorted(timestamp_data.keys()):
                row_data = {
                    'info_interface': info_fields.get('info_interface', interface_name),
                    'info_user_id': info_fields.get('info_user_id', user_id),
                    'interface_name': interface_name,
                    'user_id': user_id,
                    'timestamp_period': format_timestamp(timestamp)
                }
                
                # Add all measures for this timestamp
                for measure, value in timestamp_data[timestamp].items():
                    row_data[measure] = value
                
                rows.append(row_data)
    
    if not rows:
        return ""
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header based on the expected format from the reference file
    expected_measures = [
        'bytesDownstream_mb', 'bytesDownstreamMax_mb', 'bytesUpstream_mb', 'bytesUpstreamMax_mb',
        'health', 'lostDownstreamPcnt', 'lostUpstreamPcnt', 
        'packetsDiscardedDownstreamPcnt', 'packetsDiscardedUpstreamPcnt', 
        'rtt', 'tunnelAge'
    ]
    
    header = ['info_interface', 'info_user_id', 'interface_name', 'user_id', 'timestamp_period'] + expected_measures
    writer.writerow(header)
    
    # Write data rows
    for row_data in rows:
        row = []
        for col in header:
            value = row_data.get(col, '')
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
    elif operation_name == 'query.userMetrics':
        return format_user_metrics_to_csv(response_data)
    else:
        # Default: try to convert any JSON response to simple CSV
        return json.dumps(response_data, indent=2)
