#!/usr/bin/env python3
"""
Account Metrics Formatter for Cato CLI

This module provides functions to format accountMetrics API responses
into JSON and CSV formats, with special handling for hierarchical
timeseries data.
"""

import csv
import io
import json
from datetime import datetime
from typing import Dict, List, Any, Optional, Set, Tuple

# Import shared utility functions
try:
    from .formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure
except ImportError:
    try:
        from catocli.Utils.formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure
    except ImportError:
        from formatter_utils import convert_bytes_to_mb, format_timestamp, is_bytes_measure


def format_account_metrics(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert accountMetrics JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from accountMetrics query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format
    """
    if output_format.lower() == 'csv':
        return _format_account_metrics_to_csv(response_data)
    else:
        # Default to JSON format with organized structure
        return _format_account_metrics_to_json(response_data)


def _format_account_metrics_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert accountMetrics JSON response to organized JSON format with hierarchical structure
    
    Args:
        response_data: JSON response from accountMetrics query
        
    Returns:
        JSON formatted string with organized sites, interfaces, and timeseries data
    """
    if not response_data or not isinstance(response_data, dict):
        return json.dumps({"error": "Invalid response data"}, indent=2)
    
    # Check for API errors
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'accountMetrics' not in response_data['data']:
        return json.dumps({"error": "Invalid accountMetrics response structure"}, indent=2)
    
    account_metrics = response_data['data']['accountMetrics']
    if account_metrics is None:
        return None
    if not isinstance(account_metrics, dict):
        return json.dumps({"error": "Invalid accountMetrics data"}, indent=2)
    
    # Start building organized structure
    organized_data = {
        "accountMetrics": {
            "metadata": {
                "total_sites": 0,
                "total_users": 0,
                "total_interfaces": 0,
                "has_sites": False,
                "has_users": False,
                "raw_structure": {
                    "available_keys": list(account_metrics.keys())
                }
            },
            "sites": [],
            "users": []
        }
    }
    
    # Extract sites and users, handling None cases
    sites = account_metrics.get('sites', []) or []  # Handle None case
    users = account_metrics.get('users', []) or []  # Handle None case
    
    # Update metadata
    organized_data["accountMetrics"]["metadata"]["total_sites"] = len(sites)
    organized_data["accountMetrics"]["metadata"]["total_users"] = len(users)
    organized_data["accountMetrics"]["metadata"]["has_sites"] = len(sites) > 0
    organized_data["accountMetrics"]["metadata"]["has_users"] = len(users) > 0
    
    total_interfaces = 0
    
    # Process sites if present
    for site in sites:
        site_id = site.get('id', '')
        site_info = site.get('info', {}) or {}  # Handle None case
        site_name = site_info.get('name', '')
        interfaces = site.get('interfaces', []) or []  # Handle None case
        total_interfaces += len(interfaces)
        
        site_data = {
            'site_id': site_id,
            'site_name': site_name,
            'site_info': site_info,
            'total_interfaces': len(interfaces),
            'interfaces': []
        }
        
        # Process interfaces for this site
        for interface in interfaces:
            interface_info = interface.get('interfaceInfo', {}) or {}
            interface_name = interface_info.get('name', '') or interface.get('name', '')
            timeseries_list = interface.get('timeseries', []) or []
            interface_metrics = interface.get('metrics', {}) or {}
            
            interface_data = {
                'interface_name': interface_name,
                'interface_info': interface_info,
                'total_timeseries': len(timeseries_list),
                'interface_metrics': interface_metrics,
                'timeseries_data': []
            }
            
            # Organize timeseries data by timestamp
            timestamp_data = {}
            info_fields = {}
            
            for timeseries in timeseries_list:
                label = timeseries.get('label', '')
                units = timeseries.get('units', '')
                data_points = timeseries.get('data', []) or []
                info = timeseries.get('info', []) or []
                
                # Store info fields
                if info and len(info) >= 2:
                    info_fields['info_site_id'] = str(info[0]) 
                    info_fields['info_interface'] = str(info[1])
                
                # Process each data point
                for point in data_points:
                    if isinstance(point, (list, tuple)) and len(point) >= 2:
                        timestamp = int(point[0])
                        value = point[1]
                        timestamp_str = format_timestamp(timestamp)
                        
                        if timestamp_str not in timestamp_data:
                            timestamp_data[timestamp_str] = {}
                        
                        # Convert bytes measures to MB and add appropriate suffix
                        if is_bytes_measure(label, units) and value:
                            try:
                                converted_value = convert_bytes_to_mb(value)
                                timestamp_data[timestamp_str][label] = {
                                    'value': value,
                                    'formatted_mb': converted_value,
                                    'unit_type': 'bytes'
                                }
                            except (ValueError, ZeroDivisionError):
                                timestamp_data[timestamp_str][label] = {
                                    'value': value,
                                    'unit_type': 'bytes'
                                }
                        else:
                            timestamp_data[timestamp_str][label] = {
                                'value': value,
                                'unit_type': units or 'unknown'
                            }
            
            # Add timestamp data to interface
            interface_data['info_fields'] = info_fields
            interface_data['time_range'] = {
                'start': min(timestamp_data.keys()) if timestamp_data else None,
                'end': max(timestamp_data.keys()) if timestamp_data else None,
                'total_timestamps': len(timestamp_data)
            }
            interface_data['metrics_by_timestamp'] = timestamp_data
            
            site_data['interfaces'].append(interface_data)
        
        organized_data["accountMetrics"]["sites"].append(site_data)
    
    # Process users if present
    for user in users:
        user_id = user.get('id', '')
        user_name = user.get('name', '')
        user_metrics = user.get('metrics', {}) or {}
        user_interfaces = user.get('interfaces', []) or []
        
        user_data = {
            'user_id': user_id,
            'user_name': user_name,
            'user_metrics': user_metrics,
            'total_interfaces': len(user_interfaces),
            'interfaces': []
        }
        
        # Process user interfaces if any
        for interface in user_interfaces:
            interface_name = interface.get('name', '')
            timeseries_list = interface.get('timeseries', []) or []
            interface_metrics = interface.get('metrics', {}) or {}
            
            interface_data = {
                'interface_name': interface_name,
                'total_timeseries': len(timeseries_list),
                'interface_metrics': interface_metrics,
                'timeseries_data': []
            }
            
            # Organize timeseries data by timestamp
            timestamp_data = {}
            info_fields = {}
            
            for timeseries in timeseries_list:
                label = timeseries.get('label', '')
                units = timeseries.get('units', '')
                data_points = timeseries.get('data', []) or []
                info = timeseries.get('info', []) or []
                
                # Store info fields
                if info and len(info) >= 2:
                    info_fields['info_user_id'] = str(info[0])
                    info_fields['info_interface'] = str(info[1])
                
                # Process each data point
                for point in data_points:
                    if isinstance(point, (list, tuple)) and len(point) >= 2:
                        timestamp = int(point[0])
                        value = point[1]
                        timestamp_str = format_timestamp(timestamp)
                        
                        if timestamp_str not in timestamp_data:
                            timestamp_data[timestamp_str] = {}
                        
                        # Convert bytes measures to MB and add appropriate suffix
                        if is_bytes_measure(label, units) and value:
                            try:
                                converted_value = convert_bytes_to_mb(value)
                                timestamp_data[timestamp_str][label] = {
                                    'value': value,
                                    'formatted_mb': converted_value,
                                    'unit_type': 'bytes'
                                }
                            except (ValueError, ZeroDivisionError):
                                timestamp_data[timestamp_str][label] = {
                                    'value': value,
                                    'unit_type': 'bytes'
                                }
                        else:
                            timestamp_data[timestamp_str][label] = {
                                'value': value,
                                'unit_type': units or 'unknown'
                            }
            
            # Add timestamp data to interface
            interface_data['info_fields'] = info_fields
            interface_data['time_range'] = {
                'start': min(timestamp_data.keys()) if timestamp_data else None,
                'end': max(timestamp_data.keys()) if timestamp_data else None,
                'total_timestamps': len(timestamp_data)
            }
            interface_data['metrics_by_timestamp'] = timestamp_data
            
            user_data['interfaces'].append(interface_data)
        
        organized_data["accountMetrics"]["users"].append(user_data)
    
    return json.dumps(organized_data, indent=2)


def _format_account_metrics_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert accountMetrics JSON response to CSV format
    
    Args:
        response_data: JSON response from accountMetrics query
        
    Returns:
        CSV formatted string with unique columns for each metric and bytes converted to MB
    """
    if not response_data or 'data' not in response_data or 'accountMetrics' not in response_data['data']:
        return None
    
    account_metrics = response_data['data']['accountMetrics']
    # Handle the case where accountMetrics is None
    if account_metrics is None:
        return None
        
    sites = account_metrics.get('sites', []) or []  # Handle None case
    users = account_metrics.get('users', []) or []  # Handle None case
    
    # Check if we have any data to process
    if not sites and not users:
        # Return None to indicate we should fall back to raw response
        return None
    
    # Define byte metrics that need conversion to MB
    byte_metrics = {
        'bytesDownstream', 'bytesTotal', 'bytesUpstream', 
        'bytesDownstreamMax', 'bytesUpstreamMax'
    }
    
    # First pass: collect all unique metric labels to create columns
    all_metric_labels = set()
    for site in sites:
        interfaces = site.get('interfaces', [])
        for interface in interfaces:
            # Collect timeseries labels
            timeseries_list = interface.get('timeseries', []) or []
            for timeseries in timeseries_list:
                metric_label = timeseries.get('label', '')
                if metric_label in byte_metrics:
                    all_metric_labels.add(f"{metric_label}_mb")
                else:
                    all_metric_labels.add(metric_label)
            
            # Collect interface-level metrics (totals)
            interface_metrics = interface.get('metrics', {})
            for metric_key in interface_metrics.keys():
                if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                    # Use consistent naming: {metric}_mb for both timeseries and interface totals
                    all_metric_labels.add(f'{metric_key}_mb')
                else:
                    all_metric_labels.add(f'{metric_key}_total')
    
    # Sort metric labels for consistent column ordering
    sorted_metric_labels = sorted(all_metric_labels)
    
    # Group data by timestamp and interface to create one row per timestamp
    data_by_timestamp = {}
    
    for site in sites:
        site_id = site.get('id', '')
        site_info = site.get('info', {}) or {}  # Handle None case
        interfaces = site.get('interfaces', [])
        
        for interface in interfaces:
            interface_info = interface.get('interfaceInfo', {}) or {}
            interface_name = interface_info.get('name', '') or interface.get('name', '')
            timeseries_list = interface.get('timeseries', []) or []
            
            # Extract interface-level metrics (totals for the entire period)
            interface_metrics = interface.get('metrics', {})
            
            # Process each timeseries for this interface
            if timeseries_list:
                for timeseries in timeseries_list:
                    metric_label = timeseries.get('label', '')
                    data_points = timeseries.get('data', [])
                    
                    # Determine the column name (with _mb suffix for byte metrics)
                    if metric_label in byte_metrics:
                        column_name = f"{metric_label}_mb"
                    else:
                        column_name = metric_label
                    
                    for timestamp, value in data_points:
                        # Create unique key for each timestamp/interface combination
                        key = (int(timestamp), interface_name, site_id)
                        
                        if key not in data_by_timestamp:
                            data_by_timestamp[key] = {
                                'timestamp_period': format_timestamp(int(timestamp)),
                                'site_id': site_id,
                                'site_name': site_info.get('name', ''),
                                'interface_name': interface_name
                            }
                            # Initialize all metric columns to empty string
                            for label in sorted_metric_labels:
                                data_by_timestamp[key][label] = ''
                            
                            # Add interface-level metrics with byte conversion
                            for metric_key, metric_value in interface_metrics.items():
                                if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                                    # Convert bytes to MB for these specific metrics
                                    mb_value = float(metric_value) / (1024 * 1024) if metric_value and metric_value != 0 else 0
                                    column_name = f'{metric_key}_mb'
                                    # If timeseries data exists for this metric, don't overwrite it
                                    if not data_by_timestamp[key][column_name]:
                                        data_by_timestamp[key][column_name] = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                                else:
                                    # Add other interface metrics as-is
                                    data_by_timestamp[key][f'{metric_key}_total'] = str(metric_value) if metric_value is not None else ''
                        
                        # Convert bytes to MB if it's a byte metric
                        if metric_label in byte_metrics:
                            # Convert bytes to MB (divide by 1,048,576 = 1024^2)
                            mb_value = float(value) / (1024 * 1024) if value != 0 else 0
                            data_by_timestamp[key][column_name] = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                        else:
                            data_by_timestamp[key][column_name] = str(value)
            else:
                # No timeseries data, but we still want to create a row with interface metrics if they exist
                if interface_metrics:
                    # Use current time as placeholder timestamp since we have no timeseries data
                    import time
                    current_timestamp = int(time.time() * 1000)
                    key = (current_timestamp, interface_name, site_id)
                    
                    data_by_timestamp[key] = {
                        'timestamp_period': 'No timeseries data',
                        'site_id': site_id,
                        'site_name': site_info.get('name', ''),
                        'interface_name': interface_name
                    }
                    # Initialize all metric columns to empty string
                    for label in sorted_metric_labels:
                        data_by_timestamp[key][label] = ''
                    
                    # Add interface-level metrics with byte conversion
                    for metric_key, metric_value in interface_metrics.items():
                        if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                            # Convert bytes to MB for these specific metrics
                            mb_value = float(metric_value) / (1024 * 1024) if metric_value and metric_value != 0 else 0
                            column_name = f'{metric_key}_mb'
                            data_by_timestamp[key][column_name] = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                        else:
                            # Add other interface metrics as-is
                            data_by_timestamp[key][f'{metric_key}_total'] = str(metric_value) if metric_value is not None else ''
    
    # Process user-level data if present
    for user in users:
        user_id = user.get('id', '')
        user_name = user.get('name', '')
        user_metrics = user.get('metrics', {})
        user_interfaces = user.get('interfaces', [])
        
        # Collect user-level metrics for the metric labels set
        for metric_key in user_metrics.keys():
            if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                all_metric_labels.add(f'{metric_key}_mb')
            else:
                all_metric_labels.add(metric_key)
        
        # Process user interfaces (if any)
        if user_interfaces:
            for interface in user_interfaces:
                interface_name = interface.get('name', '')
                timeseries_list = interface.get('timeseries', []) or []
                interface_metrics = interface.get('metrics', {})
                
                # Add interface metrics to labels
                for metric_key in interface_metrics.keys():
                    if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                        all_metric_labels.add(f'{metric_key}_mb')
                    else:
                        all_metric_labels.add(f'{metric_key}_total')
                
                # Process timeseries data if available
                for timeseries in timeseries_list:
                    metric_label = timeseries.get('label', '')
                    data_points = timeseries.get('data', [])
                    
                    # Add to labels
                    if metric_label in byte_metrics:
                        all_metric_labels.add(f"{metric_label}_mb")
                    else:
                        all_metric_labels.add(metric_label)
                    
                    # Process data points
                    for timestamp, value in data_points:
                        key = (int(timestamp), f"user_{user_id}_{interface_name}", user_id)
                        
                        if key not in data_by_timestamp:
                            data_by_timestamp[key] = {
                                'timestamp_period': format_timestamp(int(timestamp)),
                                'site_id': user_id,
                                'site_name': user_name,
                                'interface_name': f"user_{user_id}_{interface_name}"
                            }
                            # Initialize all metric columns
                            for label in all_metric_labels:
                                data_by_timestamp[key][label] = ''
                        
                        # Add the metric value
                        if metric_label in byte_metrics:
                            mb_value = float(value) / (1024 * 1024) if value != 0 else 0
                            data_by_timestamp[key][f"{metric_label}_mb"] = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                        else:
                            data_by_timestamp[key][metric_label] = str(value)
        else:
            # No interfaces, create a row with just user-level metrics
            import time
            current_timestamp = int(time.time() * 1000)
            key = (current_timestamp, f"user_{user_id}", user_id)
            
            data_by_timestamp[key] = {
                'timestamp_period': 'User summary',
                'site_id': user_id,
                'site_name': user_name,
                'interface_name': f"user_{user_id}"
            }
            
            # Re-sort metric labels after adding user metrics
            sorted_metric_labels = sorted(all_metric_labels)
            
            # Initialize all metric columns
            for label in sorted_metric_labels:
                data_by_timestamp[key][label] = ''
            
            # Add user-level metrics
            for metric_key, metric_value in user_metrics.items():
                if metric_key in ['bytesDownstream', 'bytesUpstream', 'bytesTotal']:
                    mb_value = float(metric_value) / (1024 * 1024) if metric_value and metric_value != 0 else 0
                    data_by_timestamp[key][f'{metric_key}_mb'] = f"{mb_value:.3f}".rstrip('0').rstrip('.')
                else:
                    data_by_timestamp[key][metric_key] = str(metric_value) if metric_value is not None else ''
    
    # Re-sort metric labels after processing all data
    sorted_metric_labels = sorted(all_metric_labels)
    
    # Convert to list and sort by timestamp
    rows = list(data_by_timestamp.values())
    rows.sort(key=lambda x: (x['timestamp_period'], x['interface_name'], x['site_id']))
    
    if not rows:
        # Return None to indicate we should fall back to raw response
        return None
    
    # Create CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Build header: basic columns first, then metric columns
    basic_columns = ['timestamp_period', 'site_id', 'site_name', 'interface_name']
    header = basic_columns + sorted_metric_labels
    writer.writerow(header)
    
    # Write data rows
    for row_data in rows:
        row = []
        for col in header:
            value = row_data.get(col, '')
            row.append(value)
        writer.writerow(row)
    
    return output.getvalue()