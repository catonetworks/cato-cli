#!/usr/bin/env python3
"""
Licensing Formatter for Cato CLI

Formats licensing API responses into JSON and CSV formats
"""

import csv
import io
import json
from datetime import datetime
from typing import Dict, List, Any, Optional


def format_licensing(response_data: Dict[str, Any], output_format: str = 'json') -> str:
    """
    Convert licensing JSON response to specified format (JSON or CSV)
    
    Args:
        response_data: JSON response from licensing query
        output_format: 'json' or 'csv'
        
    Returns:
        Formatted string in the requested format
    """
    if output_format.lower() == 'csv':
        return format_licensing_to_csv(response_data)
    else:
        return _format_licensing_to_json(response_data)


def _format_licensing_to_json(response_data: Dict[str, Any]) -> str:
    """
    Convert licensing JSON response to organized JSON format
    
    Args:
        response_data: JSON response from licensing query
        
    Returns:
        JSON formatted string with organized license data
    """
    if not response_data or not isinstance(response_data, dict):
        return json.dumps({"error": "Invalid response data"}, indent=2)
    
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'licensing' not in response_data['data']:
        return json.dumps({"error": "Invalid licensing response structure"}, indent=2)
    
    return json.dumps(response_data, indent=2)


def format_licensing_to_csv(response_data: Dict[str, Any]) -> str:
    """
    Convert licensing JSON response to CSV format with all license entries flattened
    
    Args:
        response_data: JSON response from licensing query
        
    Returns:
        CSV formatted string
    """
    if not response_data or not isinstance(response_data, dict):
        return "ERROR: Invalid response data"
    
    if 'errors' in response_data:
        return json.dumps(response_data, indent=2)
    
    if 'data' not in response_data or 'licensing' not in response_data['data']:
        return "ERROR: Invalid licensing response structure"
    
    licensing_info = response_data['data']['licensing'].get('licensingInfo', {})
    if not licensing_info:
        return "ERROR: No licensing info found"
    
    # CSV output
    output = io.StringIO()
    
    # Define CSV columns
    fieldnames = [
        'sku', 'total', 'plan', 'status', 'startDate', 'expirationDate',
        'siteLicenseType', 'siteLicenseGroup', 'allocatedBandwidth',
        'site_id', 'site_name', 'site_bandwidth',
        'description', 'dpaVersion', 'retentionPeriod', 'lastUpdated', 'id'
    ]
    
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    
    # Process all license entries from licensing_info.licenses array
    licenses = licensing_info.get('licenses', [])
    
    for license_entry in licenses:
        # Check if this is a pooled bandwidth license with sites
        if 'sites' in license_entry and license_entry['sites']:
            # Create a row for each site in the pooled license
            for site_info in license_entry['sites']:
                row = {
                    'sku': license_entry.get('sku'),
                    'total': license_entry.get('total'),
                    'plan': license_entry.get('plan'),
                    'status': license_entry.get('status'),
                    'startDate': license_entry.get('startDate', '').split('T')[0] if license_entry.get('startDate') else '',
                    'expirationDate': license_entry.get('expirationDate', '').split('T')[0] if license_entry.get('expirationDate') else '',
                    'siteLicenseType': license_entry.get('siteLicenseType'),
                    'siteLicenseGroup': license_entry.get('siteLicenseGroup'),
                    'allocatedBandwidth': license_entry.get('allocatedBandwidth'),
                    'site_id': site_info.get('sitePooledBandwidthLicenseSite', {}).get('id'),
                    'site_name': site_info.get('sitePooledBandwidthLicenseSite', {}).get('name'),
                    'site_bandwidth': site_info.get('allocatedBandwidth'),
                    'description': license_entry.get('description'),
                    'dpaVersion': license_entry.get('dpaVersion'),
                    'retentionPeriod': license_entry.get('retentionPeriod'),
                    'lastUpdated': license_entry.get('lastUpdated', '').split('T')[0] if license_entry.get('lastUpdated') else '',
                    'id': license_entry.get('id')
                }
                writer.writerow(row)
        else:
            # Regular license entry (no sites)
            row = {
                'sku': license_entry.get('sku'),
                'total': license_entry.get('total'),
                'plan': license_entry.get('plan'),
                'status': license_entry.get('status'),
                'startDate': license_entry.get('startDate', '').split('T')[0] if license_entry.get('startDate') else '',
                'expirationDate': license_entry.get('expirationDate', '').split('T')[0] if license_entry.get('expirationDate') else '',
                'siteLicenseType': license_entry.get('siteLicenseType'),
                'siteLicenseGroup': license_entry.get('siteLicenseGroup'),
                'allocatedBandwidth': license_entry.get('allocatedBandwidth'),
                'site_id': license_entry.get('site', {}).get('id') if isinstance(license_entry.get('site'), dict) else '',
                'site_name': license_entry.get('site', {}).get('name') if isinstance(license_entry.get('site'), dict) else '',
                'site_bandwidth': '',
                'description': license_entry.get('description'),
                'dpaVersion': license_entry.get('dpaVersion'),
                'retentionPeriod': license_entry.get('retentionPeriod'),
                'lastUpdated': license_entry.get('lastUpdated', '').split('T')[0] if license_entry.get('lastUpdated') else '',
                'id': license_entry.get('id')
            }
            writer.writerow(row)
    
    csv_content = output.getvalue()
    output.close()
    
    return csv_content
