#!/usr/bin/env python3
"""
App Stats Timeseries Formatter for Cato CLI

This module provides functions to format appStatsTimeSeries API responses
into JSON and CSV formats, with special handling for timeseries data
and unit conversions.
"""

import csv
import io
import json
import re
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Import shared utility functions
try:
    from .formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure, is_bytes_measure, convert_bytes_to_mb
except ImportError:
    try:
        from catocli.Utils.formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure, is_bytes_measure, convert_bytes_to_mb
    except ImportError:
        from formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure, is_bytes_measure, convert_bytes_to_mb


def format_app_stats_timeseries(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert appStatsTimeSeries JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format, or None if no processable data
    """
    if output_format.lower() == 'csv':
        return _format_app_stats_timeseries_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_app_stats_timeseries_to_json(response_data)


def _format_app_stats_timeseries_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert appStatsTimeSeries JSON response to organized JSON format
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        
    Returns:
        JSON formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'appStatsTimeSeries' not in response_data['data']:
        return None
    
    app_stats_ts = response_data['data']['appStatsTimeSeries']
    if app_stats_ts is None:
        return None
        
    timeseries = app_stats_ts.get('timeseries', [])
    
    if not timeseries:
        return None
    
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
                
                if is_bytes_measure(measure):
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
                            'unit_type': 'bytes_err'
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


def _format_app_stats_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert appStatsTimeSeries JSON response to CSV format
    
    Args:
        response_data: JSON response from appStatsTimeSeries query
        
    Returns:
        CSV formatted string in long format with one row per timestamp, or None if no processable data
    """
    if not response_data or 'data' not in response_data or 'appStatsTimeSeries' not in response_data['data']:
        return None
    
    app_stats_ts = response_data['data']['appStatsTimeSeries']
    if app_stats_ts is None:
        return None
        
    timeseries = app_stats_ts.get('timeseries', [])
    
    if not timeseries:
        return None
    
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
                if is_bytes_measure(measure):
                    try:
                        converted_value = convert_bytes_to_mb(value) if value != '' else ''
                        row_data[f'{measure}_mb'] = converted_value
                    except (ValueError, ZeroDivisionError):
                        row_data[f'{measure}_mb'] = str(value) if value != '' else ''
                else:
                    row_data[measure] = str(value) if value != '' else ''
            
            rows.append(row_data)
    
    if not rows:
        return None
    
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