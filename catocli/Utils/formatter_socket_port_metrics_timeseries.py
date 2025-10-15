#!/usr/bin/env python3
"""
Socket Port Metrics Timeseries Formatter for Cato CLI

This module provides functions to format socketPortMetricsTimeSeries API responses
into JSON and CSV formats, with special handling for timeseries data
and unit conversions.
"""

import csv
import io
import json
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Import shared utility functions
try:
    from .formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure
except ImportError:
    try:
        from catocli.Utils.formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure
    except ImportError:
        from formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure, parse_label_for_dimensions_and_measure


def format_socket_port_metrics_timeseries(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format, or None if no processable data
    """
    if output_format.lower() == 'csv':
        return _format_socket_port_metrics_timeseries_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_socket_port_metrics_timeseries_to_json(response_data)


def _format_socket_port_metrics_timeseries_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to organized JSON format
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        
    Returns:
        JSON formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'socketPortMetricsTimeSeries' not in response_data['data']:
        return None
    
    socket_metrics_ts = response_data['data']['socketPortMetricsTimeSeries']
    if socket_metrics_ts is None:
        return None
        
    timeseries = socket_metrics_ts.get('timeseries', [])
    
    if not timeseries:
        return None
    
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


def _format_socket_port_metrics_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert socketPortMetricsTimeSeries JSON response to CSV format
    
    Args:
        response_data: JSON response from socketPortMetricsTimeSeries query
        
    Returns:
        CSV formatted string in long format with one row per timestamp, or None if no processable data
    """
    if not response_data or 'data' not in response_data or 'socketPortMetricsTimeSeries' not in response_data['data']:
        return None
    
    socket_metrics_ts = response_data['data']['socketPortMetricsTimeSeries']
    if socket_metrics_ts is None:
        return None
        
    timeseries = socket_metrics_ts.get('timeseries', [])
    
    if not timeseries:
        return None
    
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