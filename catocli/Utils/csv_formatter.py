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

# Universal import for pip, pipx, and local development
try:
    from .formatter_account_metrics import format_account_metrics
except ImportError:
    try:
        from catocli.Utils.formatter_account_metrics import format_account_metrics
    except ImportError:
        from formatter_account_metrics import format_account_metrics

try:
    from .formatter_app_stats import format_app_stats
except ImportError:
    try:
        from catocli.Utils.formatter_app_stats import format_app_stats
    except ImportError:
        from formatter_app_stats import format_app_stats


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





def format_app_stats_timeseries(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert appStatsTimeSeries JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format
    """
    if output_format.lower() == 'csv':
        return format_app_stats_timeseries_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_app_stats_timeseries_to_json(response_data)


def _format_app_stats_timeseries_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert appStatsTimeSeries JSON response to organized JSON format
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        
    Returns:
        JSON formatted string
    """
    if not response_data or not isinstance(response_data, dict):
        return json.dumps({"error": "Invalid response data"}, indent=2)
    
    # Check for API errors
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'appStatsTimeSeries' not in response_data['data']:
        return json.dumps({"error": "Invalid appStatsTimeSeries response structure"}, indent=2)
    
    app_stats_ts = response_data['data']['appStatsTimeSeries']
    timeseries = app_stats_ts.get('timeseries', [])
    
    if not timeseries:
        return json.dumps({"appStatsTimeSeries": {"timeseries": [], "summary": "No timeseries data found"}}, indent=2)
    
    # Parse dimension information and measures from labels
    parsed_series = []
    all_timestamps = set()
    all_dimensions = set()
    all_measures = set()
    
    for series in timeseries:
        label = series.get('label', '')
        data_points = series.get('data', [])
        units = series.get('units', '')
        
        # Get measure and dimensions from key structure (new API format)
        key_info = series.get('key', {})
        measure = key_info.get('measureFieldName', '')
        dimensions = {}
        
        # Extract dimensions from key.dimensions array
        key_dimensions = key_info.get('dimensions', [])
        for dim_info in key_dimensions:
            if isinstance(dim_info, dict) and 'fieldName' in dim_info and 'value' in dim_info:
                dimensions[dim_info['fieldName']] = dim_info['value']
        
        # Fallback to label parsing if key method fails
        if not measure and not dimensions:
            measure, dimensions = parse_label_for_dimensions_and_measure(label)
        
        # Create series entry with safe data parsing
        data_dict = {}
        for point in data_points:
            if isinstance(point, (list, tuple)) and len(point) >= 2:
                timestamp = int(point[0])
                value = point[1]
                data_dict[timestamp] = value
                all_timestamps.add(timestamp)
        
        series_entry = {
            'label': label,
            'measure': measure,
            'dimensions': dimensions,
            'data_points': len(data_dict),
            'time_range': {
                'start': format_timestamp(min(data_dict.keys())) if data_dict else None,
                'end': format_timestamp(max(data_dict.keys())) if data_dict else None
            },
            'data': data_dict
        }
        parsed_series.append(series_entry)
        
        # Collect metadata
        all_measures.add(measure)
        all_dimensions.update(dimensions.keys())
    
    # Organize timeseries data by dimension combinations and timestamps
    organized_data = {
        "appStatsTimeSeries": {
            "summary": {
                "total_series": len(parsed_series),
                "total_timestamps": len(all_timestamps),
                "time_range": {
                    "start": format_timestamp(min(all_timestamps)) if all_timestamps else None,
                    "end": format_timestamp(max(all_timestamps)) if all_timestamps else None
                },
                "measures": sorted(list(all_measures)),
                "dimensions": sorted(list(all_dimensions))
            },
            "series": []
        }
    }
    
    # Group series by dimension combinations for better organization
    dimension_groups = {}
    for series in parsed_series:
        dim_key = tuple(sorted(series['dimensions'].items()))
        if dim_key not in dimension_groups:
            dimension_groups[dim_key] = {
                'dimensions': series['dimensions'],
                'measures': {},
                'time_range': series['time_range']
            }
        dimension_groups[dim_key]['measures'][series['measure']] = {
            'label': series['label'],
            'data_points': series['data_points'],
            'data': series['data']
        }
    
    # Convert to organized format
    for dim_combo, group_data in dimension_groups.items():
        series_data = {
            'dimensions': group_data['dimensions'],
            'time_range': group_data['time_range'],
            'measures': {}
        }
        
        # Organize measures with unit conversion for bytes data
        for measure, measure_data in group_data['measures'].items():
            formatted_data = {}
            for timestamp, value in measure_data['data'].items():
                timestamp_str = format_timestamp(timestamp)
                
                if measure in ['downstream', 'upstream', 'traffic'] and value:
                    try:
                        mb_value = value
                        # mb_value = float(value) / 1048576
                        formatted_value = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                        formatted_data[timestamp_str] = {
                            'value': value,
                            'formatted_mb': formatted_value,
                            'unit_type': 'bytes'
                        }
                    except (ValueError, ZeroDivisionError):
                        formatted_data[timestamp_str] = {
                            'value': value,
                            'unit_type': 'bytes'
                        }
                else:
                    formatted_data[timestamp_str] = {
                        'value': value,
                        'unit_type': 'unknown'
                    }
            
            series_data['measures'][measure] = {
                'label': measure_data['label'],
                'data_points': measure_data['data_points'],
                'data': formatted_data
            }
        
        organized_data["appStatsTimeSeries"]["series"].append(series_data)
    
    return json.dumps(organized_data, indent=2)


def format_app_stats_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert appStatsTimeSeries JSON response to CSV format
    
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
        units = series.get('units', '')
        
        # Get measure and dimensions from key structure (new API format)
        key_info = series.get('key', {})
        measure = key_info.get('measureFieldName', '')
        dimensions = {}
        
        # Extract dimensions from key.dimensions array
        key_dimensions = key_info.get('dimensions', [])
        for dim_info in key_dimensions:
            if isinstance(dim_info, dict) and 'fieldName' in dim_info and 'value' in dim_info:
                dimensions[dim_info['fieldName']] = dim_info['value']
        
        # Fallback to label parsing if key method fails
        if not measure and not dimensions:
            try:
                if ' for ' in label:
                    measure_part, dim_part = label.split(' for ', 1)
                    # Extract measure (e.g., "sum(traffic)")
                    if '(' in measure_part and ')' in measure_part:
                        measure = measure_part.split('(')[1].split(')')[0]
                    
                    # Parse dimensions using regex for better handling of quoted values
                    dim_pattern = r'(\w+)=[\'"]*([^,\'"]+)[\'"]*'
                    matches = re.findall(dim_pattern, dim_part)
                    for key, value in matches:
                        dimensions[key.strip()] = value.strip()
                else:
                    # Fallback: use the whole label as measure
                    measure = label
            except Exception as e:
                print(f"DEBUG: Error processing series with label '{label}': {e}")
                continue
            
        # Create series entry with safe data parsing
        try:
            data_dict = {}
            for point in data_points:
                if isinstance(point, (list, tuple)) and len(point) >= 2:
                    data_dict[int(point[0])] = point[1]
                    all_timestamps.add(int(point[0]))
            
            series_entry = {
                'measure': measure,
                'dimensions': dimensions,
                'data': data_dict
            }
            parsed_series.append(series_entry)
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
                            # Current bug in appStatsTimeSeries returning mb indicating unit as bytes
                            # mb_value = float(value) / 1048576
                            mb_value = value
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




def format_socket_port_metrics_timeseries(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format
    """
    if output_format.lower() == 'csv':
        return format_socket_port_metrics_timeseries_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_socket_port_metrics_timeseries_to_json(response_data)


def _format_socket_port_metrics_timeseries_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to organized JSON format
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        
    Returns:
        JSON formatted string
    """
    if not response_data or not isinstance(response_data, dict):
        return json.dumps({"error": "Invalid response data"}, indent=2)
    
    # Check for API errors
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'socketPortMetricsTimeSeries' not in response_data['data']:
        return json.dumps({"error": "Invalid socketPortMetricsTimeSeries response structure"}, indent=2)
    
    socket_metrics_ts = response_data['data']['socketPortMetricsTimeSeries']
    timeseries = socket_metrics_ts.get('timeseries', [])
    
    if not timeseries:
        return json.dumps({"socketPortMetricsTimeSeries": {"timeseries": [], "summary": "No timeseries data found"}}, indent=2)
    
    # Parse measures from labels - these are simpler than appStatsTimeSeries
    parsed_series = []
    all_timestamps = set()
    all_measures = set()
    
    for series in timeseries:
        label = series.get('label', '')
        data_points = series.get('data', [])
        units = series.get('unitsTimeseries', '')
        info = series.get('info', [])
        
        # Extract measure from label - usually just "sum(measure_name)"
        measure, dimensions = parse_label_for_dimensions_and_measure(label)
        
        # If no dimensions found in label, create default dimensions from info if available
        if not dimensions and info:
            for i, info_value in enumerate(info):
                dimensions[f'info_{i}'] = str(info_value)
        
        # If still no dimensions, create a single default dimension
        if not dimensions:
            dimensions = {'metric_source': 'socket_port'}
        
        # Create series entry with safe data parsing
        data_dict = {}
        for point in data_points:
            if isinstance(point, (list, tuple)) and len(point) >= 2:
                timestamp = int(point[0])
                value = point[1]
                data_dict[timestamp] = value
                all_timestamps.add(timestamp)
        
        series_entry = {
            'label': label,
            'measure': measure,
            'dimensions': dimensions,
            'units': units,
            'data_points': len(data_dict),
            'time_range': {
                'start': format_timestamp(min(data_dict.keys())) if data_dict else None,
                'end': format_timestamp(max(data_dict.keys())) if data_dict else None
            },
            'data': data_dict
        }
        parsed_series.append(series_entry)
        
        # Collect metadata
        all_measures.add(measure)
    
    # Organize data
    organized_data = {
        "socketPortMetricsTimeSeries": {
            "summary": {
                "total_series": len(parsed_series),
                "total_timestamps": len(all_timestamps),
                "time_range": {
                    "start": format_timestamp(min(all_timestamps)) if all_timestamps else None,
                    "end": format_timestamp(max(all_timestamps)) if all_timestamps else None
                },
                "measures": sorted(list(all_measures))
            },
            "series": []
        }
    }
    
    # Group series by dimension combinations
    dimension_groups = {}
    for series in parsed_series:
        dim_key = tuple(sorted(series['dimensions'].items()))
        if dim_key not in dimension_groups:
            dimension_groups[dim_key] = {
                'dimensions': series['dimensions'],
                'measures': {},
                'time_range': series['time_range']
            }
        dimension_groups[dim_key]['measures'][series['measure']] = {
            'label': series['label'],
            'units': series['units'],
            'data_points': series['data_points'],
            'data': series['data']
        }
    
    # Convert to organized format with unit conversion
    for dim_combo, group_data in dimension_groups.items():
        series_data = {
            'dimensions': group_data['dimensions'],
            'time_range': group_data['time_range'],
            'measures': {}
        }
        
        for measure, measure_data in group_data['measures'].items():
            formatted_data = {}
            for timestamp, value in measure_data['data'].items():
                timestamp_str = format_timestamp(timestamp)
                
                if is_bytes_measure(measure, measure_data['units']) and value:
                    try:
                        converted_value = convert_bytes_to_mb(value)
                        formatted_data[timestamp_str] = {
                            'value': value,
                            'formatted_mb': converted_value,
                            'unit_type': 'bytes'
                        }
                    except (ValueError, ZeroDivisionError):
                        formatted_data[timestamp_str] = {
                            'value': value,
                            'unit_type': 'bytes'
                        }
                else:
                    formatted_data[timestamp_str] = {
                        'value': value,
                        'unit_type': measure_data['units'] or 'unknown'
                    }
            
            series_data['measures'][measure] = {
                'label': measure_data['label'],
                'units': measure_data['units'],
                'data_points': measure_data['data_points'],
                'data': formatted_data
            }
        
        organized_data["socketPortMetricsTimeSeries"]["series"].append(series_data)
    
    return json.dumps(organized_data, indent=2)


def format_socket_port_metrics_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to CSV format
    
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
        return format_app_stats(response_data, output_format='csv')
    elif operation_name == 'query.appStatsTimeSeries':
        return format_app_stats_timeseries_to_csv(response_data)
    elif operation_name == 'query.socketPortMetricsTimeSeries':
        return format_socket_port_metrics_timeseries_to_csv(response_data)
    elif operation_name == 'query.accountMetrics':
        return format_account_metrics(response_data, output_format='csv')
    else:
        # Default: try to convert any JSON response to simple CSV
        return json.dumps(response_data, indent=2)
