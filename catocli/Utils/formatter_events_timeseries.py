#!/usr/bin/env python3
"""
Events TimeSeries Formatter for Cato CLI

This module provides functions to format eventsTimeSeries API responses
into JSON and CSV formats, with special handling for granularity multiplication
when sum aggregation is used on appropriate fields.

Key functionality:
- Handles granularity multiplication for sum aggregations when appropriate
- Excludes rate, percentage, and normalized fields from multiplication
- Provides both JSON and CSV output formats
"""

import csv
import io
import json
import re
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Import shared utility functions
try:
    from .formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure
except ImportError:
    try:
        from catocli.Utils.formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure
    except ImportError:
        from formatter_utils import format_timestamp, parse_label_for_dimensions_and_measure


def should_multiply_by_granularity(field_name: str, agg_type: str) -> bool:
    """
    Determine if a field with sum aggregation should be multiplied by granularity
    
    Args:
        field_name: The name of the field being aggregated
        agg_type: The aggregation type (e.g., 'sum', 'avg', 'max')
        
    Returns:
        True if the field should be multiplied by granularity, False otherwise
    """
    # Only apply to sum aggregations
    if agg_type.lower() != 'sum':
        return False
    
    # Fields that should NOT be multiplied by granularity even with sum aggregation
    exclude_patterns = [
        # Rate fields (already per-time-unit)
        '_per_second', '_per_minute', '_per_hour', 'rate', 'bps', 'pps',
        'bytes_per_second', 'packets_per_second',
        
        # Percentage and ratio fields
        'percent', 'percentage', 'ratio', '_pct', 'utilization',
        'cpu_utilization', 'memory_usage_percent',
        
        # Score and normalized values
        'score', 'threat_score', 'confidence_level', 'risk_level',
        
        # Statistical measures (already calculated)
        'avg_', 'mean_', 'median_', 'p95_', 'p99_', 'percentile',
        'avg_response_time', 'p95_latency',
        
        # Unique/distinct counts
        'distinct_', 'unique_', 'cardinality',
        'distinct_users', 'unique_ips',
        
        # State/status values
        'status', 'state', 'health_score', 'connection_status'
    ]
    
    field_lower = field_name.lower()
    
    # Check if field matches any exclusion pattern
    for pattern in exclude_patterns:
        if pattern in field_lower:
            return False
    
    # Default: multiply sum aggregations by granularity
    return True


def format_events_timeseries(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert eventsTimeSeries JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from eventsTimeSeries query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format, or None if no processable data
    """
    if output_format.lower() == 'csv':
        return _format_events_timeseries_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_events_timeseries_to_json(response_data)


def _format_events_timeseries_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert eventsTimeSeries JSON response to organized JSON format with granularity multiplication
    
    Args:
        response_data: JSON response from eventsTimeSeries query
        
    Returns:
        JSON formatted string, or None if no processable data
    """
    if not response_data or not isinstance(response_data, dict):
        return None
    
    # Check for API errors
    if 'errors' in response_data:
        return None
    
    if 'data' not in response_data or 'eventsTimeSeries' not in response_data['data']:
        return None
    
    events_ts = response_data['data']['eventsTimeSeries']
    if events_ts is None:
        return None
        
    timeseries = events_ts.get('timeseries', [])
    granularity = events_ts.get('granularity', 1)
    
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
        
        # Get measure and aggregation type from key structure
        key_info = series.get('key', {})
        measure = key_info.get('measureFieldName', '')
        dimensions = {}
        
        # Extract aggregation type from label (e.g., "sum(event_count)")
        agg_type = ''
        if '(' in label and ')' in label:
            agg_match = re.match(r'(\w+)\(', label)
            if agg_match:
                agg_type = agg_match.group(1)
        
        # Extract dimensions from key.dimensions array
        key_dimensions = key_info.get('dimensions', [])
        for dim_info in key_dimensions:
            if isinstance(dim_info, dict) and 'fieldName' in dim_info and 'value' in dim_info:
                dimensions[dim_info['fieldName']] = dim_info['value']
        
        # Fallback to label parsing if key method fails
        if not measure and not dimensions:
            measure, dimensions = parse_label_for_dimensions_and_measure(label)
        
        # Determine if we should multiply by granularity
        should_multiply = should_multiply_by_granularity(measure, agg_type)
        
        # Create series entry with safe data parsing and granularity adjustment
        data_dict = {}
        for point in data_points:
            if isinstance(point, (list, tuple)) and len(point) >= 2:
                timestamp = int(point[0])
                value = point[1]
                
                # Apply granularity multiplication if appropriate
                if should_multiply and value is not None and granularity > 1:
                    try:
                        computed_value = round(float(value) * granularity, 3)
                        data_dict[timestamp] = {
                            'original_value': value,
                            'computed_value': computed_value,
                            'granularity': granularity,
                            'granularity_applied': True
                        }
                    except (ValueError, TypeError):
                        data_dict[timestamp] = {
                            'original_value': value,
                            'computed_value': value,
                            'granularity': granularity,
                            'granularity_applied': False,
                            'note': 'Could not convert to numeric for granularity adjustment'
                        }
                else:
                    data_dict[timestamp] = {
                        'original_value': value,
                        'computed_value': value,
                        'granularity': granularity,
                        'granularity_applied': False,
                        'note': 'Granularity not applied (field type or non-sum aggregation)'
                    }
                
                all_timestamps.add(timestamp)
        
        series_entry = {
            'label': label,
            'measure': measure,
            'aggregation_type': agg_type,
            'dimensions': dimensions,
            'granularity_multiplied': should_multiply,
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
    
    # Organize the response
    organized_data = {
        "eventsTimeSeries": {
            "summary": {
                "total_series": len(parsed_series),
                "total_timestamps": len(all_timestamps),
                "granularity": granularity,
                "time_range": {
                    "start": format_timestamp(min(all_timestamps)) if all_timestamps else None,
                    "end": format_timestamp(max(all_timestamps)) if all_timestamps else None
                },
                "measures": sorted(list(all_measures)),
                "dimensions": sorted(list(all_dimensions)),
                "granularity_note": "Sum aggregations on count fields are multiplied by granularity when appropriate"
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
            'aggregation_type': series['aggregation_type'],
            'granularity_multiplied': series['granularity_multiplied'],
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
        
        # Format each measure's data
        for measure, measure_data in group_data['measures'].items():
            formatted_data = {}
            for timestamp, value_info in measure_data['data'].items():
                timestamp_str = format_timestamp(timestamp)
                formatted_data[timestamp_str] = value_info
            
            series_data['measures'][measure] = {
                'label': measure_data['label'],
                'aggregation_type': measure_data['aggregation_type'],
                'granularity_multiplied': measure_data['granularity_multiplied'],
                'data_points': measure_data['data_points'],
                'data': formatted_data
            }
        
        organized_data["eventsTimeSeries"]["series"].append(series_data)
    
    return json.dumps(organized_data, indent=2)


def _format_events_timeseries_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert eventsTimeSeries JSON response to CSV format with granularity multiplication
    
    Args:
        response_data: JSON response from eventsTimeSeries query
        
    Returns:
        CSV formatted string in long format with one row per timestamp, or None if no processable data
    """
    if not response_data or 'data' not in response_data or 'eventsTimeSeries' not in response_data['data']:
        return None
    
    events_ts = response_data['data']['eventsTimeSeries']
    if events_ts is None:
        return None
        
    timeseries = events_ts.get('timeseries', [])
    granularity = events_ts.get('granularity', 1)
    
    if not timeseries:
        return None
    
    # Parse dimension information and measures from labels
    parsed_series = []
    all_timestamps = set()
    
    for series in timeseries:
        label = series.get('label', '')
        data_points = series.get('data', [])
        
        # Get measure and aggregation type from key structure
        key_info = series.get('key', {})
        measure = key_info.get('measureFieldName', '')
        dimensions = {}
        
        # Extract aggregation type from label
        agg_type = ''
        if '(' in label and ')' in label:
            agg_match = re.match(r'(\w+)\(', label)
            if agg_match:
                agg_type = agg_match.group(1)
        
        # Extract dimensions from key.dimensions array
        key_dimensions = key_info.get('dimensions', [])
        for dim_info in key_dimensions:
            if isinstance(dim_info, dict) and 'fieldName' in dim_info and 'value' in dim_info:
                dimensions[dim_info['fieldName']] = dim_info['value']
        
        # Fallback to label parsing if key method fails
        if not measure and not dimensions:
            measure, dimensions = parse_label_for_dimensions_and_measure(label)
        
        # Determine if we should multiply by granularity
        should_multiply = should_multiply_by_granularity(measure, agg_type)
        
        # Create series entry with safe data parsing
        data_dict = {}
        for point in data_points:
            if isinstance(point, (list, tuple)) and len(point) >= 2:
                timestamp = int(point[0])
                value = point[1]
                
                # Apply granularity multiplication if appropriate
                if should_multiply and value is not None and granularity > 1:
                    try:
                        computed_value = round(float(value) * granularity, 3)
                        data_dict[timestamp] = computed_value
                    except (ValueError, TypeError):
                        data_dict[timestamp] = value
                else:
                    data_dict[timestamp] = value
                
                all_timestamps.add(timestamp)
        
        series_entry = {
            'measure': measure,
            'aggregation_type': agg_type,
            'dimensions': dimensions,
            'granularity_multiplied': should_multiply,
            'data': data_dict
        }
        parsed_series.append(series_entry)
    
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
            'aggregation_type': series['aggregation_type'],
            'granularity_multiplied': series['granularity_multiplied']
        }
    
    # Create rows for each timestamp and dimension combination
    for dim_combo, measures_data in dimension_combos.items():
        dim_dict = dict(dim_combo)
        
        for timestamp in sorted_timestamps:
            # Build row data for this timestamp
            row_data = {
                'timestamp_period': format_timestamp(timestamp),
                'granularity': granularity
            }
            
            # Add dimension values
            for key, value in dim_dict.items():
                row_data[key] = value
            
            # Add measure values for this timestamp
            for measure, measure_info in measures_data.items():
                value = measure_info['data'].get(timestamp, '')
                agg_type = measure_info['aggregation_type']
                granularity_applied = measure_info['granularity_multiplied']
                
                # Add suffixes to indicate processing
                if granularity_applied and granularity > 1:
                    row_data[f'{measure}_computed'] = value
                    row_data[f'{measure}_notes'] = f'Multiplied by granularity ({granularity}s) for {agg_type} aggregation'
                else:
                    row_data[measure] = value
                    if agg_type == 'sum':
                        row_data[f'{measure}_notes'] = f'No granularity adjustment (field type exclusion)'
            
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
    
    # Sort columns with timestamp_period first, then granularity, then dimensions, then measures
    dimension_columns = []
    measure_columns = []
    note_columns = []
    
    for col in sorted(all_columns):
        if col in ['timestamp_period', 'granularity']:
            continue  # Will be added first
        elif col.endswith('_notes'):
            note_columns.append(col)
        elif col.endswith('_computed') or col in ['event_count', 'downstream', 'upstream', 'traffic']:
            measure_columns.append(col)
        else:
            dimension_columns.append(col)
    
    header = ['timestamp_period', 'granularity'] + sorted(dimension_columns) + sorted(measure_columns) + sorted(note_columns)
    writer.writerow(header)
    
    # Write data rows
    for row_data in rows:
        row = []
        for col in header:
            value = row_data.get(col, '')
            row.append(value)
        writer.writerow(row)
    
    return output.getvalue()