#!/usr/bin/env python3
"""
Formatter Utilities for Cato CLI

This module provides shared utility functions and CSV formatting capabilities
for converting JSON responses from Cato API into various formats.

Shared utilities:
- convert_bytes_to_mb(): Convert bytes values to megabytes with proper formatting
- format_timestamp(): Convert timestamps to readable format
- parse_label_for_dimensions_and_measure(): Parse timeseries labels
- is_bytes_measure(): Determine if a measure represents bytes data

CSV formatting support:
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

# Note: The specific formatter functions are imported dynamically 
# in the format_to_csv function to avoid circular imports


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
        'bytes_upstream', 'bytes_downstream', 'bytes_total',
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
        # Dynamic import to avoid circular imports
        try:
            from .formatter_app_stats import format_app_stats
        except ImportError:
            try:
                from catocli.Utils.formatter_app_stats import format_app_stats
            except ImportError:
                from formatter_app_stats import format_app_stats
        return format_app_stats(response_data, output_format='csv')
    elif operation_name == 'query.appStatsTimeSeries':
        # Dynamic import to avoid circular imports
        try:
            from .formatter_app_stats_timeseries import format_app_stats_timeseries
        except ImportError:
            try:
                from catocli.Utils.formatter_app_stats_timeseries import format_app_stats_timeseries
            except ImportError:
                from formatter_app_stats_timeseries import format_app_stats_timeseries
        return format_app_stats_timeseries(response_data, output_format='csv')
    elif operation_name == 'query.socketPortMetricsTimeSeries':
        # Dynamic import to avoid circular imports
        try:
            from .formatter_socket_port_metrics_timeseries import format_socket_port_metrics_timeseries
        except ImportError:
            try:
                from catocli.Utils.formatter_socket_port_metrics_timeseries import format_socket_port_metrics_timeseries
            except ImportError:
                from formatter_socket_port_metrics_timeseries import format_socket_port_metrics_timeseries
        return format_socket_port_metrics_timeseries(response_data, output_format='csv')
    elif operation_name == 'query.accountMetrics':
        # Dynamic import to avoid circular imports
        try:
            from .formatter_account_metrics import format_account_metrics
        except ImportError:
            try:
                from catocli.Utils.formatter_account_metrics import format_account_metrics
            except ImportError:
                from formatter_account_metrics import format_account_metrics
        return format_account_metrics(response_data, output_format='csv')
    elif operation_name == 'query.eventsTimeSeries':
        # Dynamic import to avoid circular imports
        try:
            from .formatter_events_timeseries import format_events_timeseries
        except ImportError:
            try:
                from catocli.Utils.formatter_events_timeseries import format_events_timeseries
            except ImportError:
                from formatter_events_timeseries import format_events_timeseries
        return format_events_timeseries(response_data, output_format='csv')
    elif operation_name == 'query.socketPortMetrics':
        # Dynamic import to avoid circular imports
        try:
            from .formatter_socket_port_metrics import format_socket_port_metrics
        except ImportError:
            try:
                from catocli.Utils.formatter_socket_port_metrics import format_socket_port_metrics
            except ImportError:
                from formatter_socket_port_metrics import format_socket_port_metrics
        return format_socket_port_metrics(response_data, output_format='csv')
    else:
        # Default: try to convert any JSON response to simple CSV
        return json.dumps(response_data, indent=2)
