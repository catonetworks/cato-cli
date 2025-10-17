#!/usr/bin/env python3
"""
Shared utilities for export operations across all catocli export commands
Provides common functionality for filename handling, timestamp appending, and output path resolution
"""

import os
import json
import csv
from datetime import datetime
from typing import Optional, Dict, Any, Union


def generate_export_filename(
    args,
    base_name: str,
    format_type: str,
    account_id: Optional[str] = None,
    default_template: Optional[str] = None
) -> str:
    """
    Generate export filename based on command arguments and options.
    
    Args:
        args: Command line arguments containing filename options
        base_name: Base name for the file (e.g., 'scim_users', 'socket_sites')
        format_type: File format ('json', 'csv')
        account_id: Optional account ID for filename template
        default_template: Optional default template (e.g., '{base_name}_{account_id}.{ext}')
    
    Returns:
        str: Generated filename
    """
    # Priority order:
    # 1. -o/--output-file (highest priority)
    # 2. Format-specific filename (--json-filename, --csv-filename)
    # 3. Default template with account_id
    # 4. Simple base name with format
    
    output_filename = None
    
    # Check for direct output file specification
    if hasattr(args, 'output_file') and args.output_file:
        output_filename = args.output_file
    
    # Check for format-specific filename
    elif format_type == 'json' and hasattr(args, 'json_filename') and args.json_filename:
        output_filename = args.json_filename
        # Add .json extension if not present
        if not output_filename.endswith('.json'):
            output_filename += '.json'
    
    elif format_type == 'csv' and hasattr(args, 'csv_filename') and args.csv_filename:
        output_filename = args.csv_filename
        # Add .csv extension if not present
        if not output_filename.endswith('.csv'):
            output_filename += '.csv'
    
    # Use default template if provided and account_id available
    elif default_template and account_id:
        output_filename = default_template.format(
            base_name=base_name,
            account_id=account_id,
            ext=format_type
        )
    
    # Fall back to simple base name
    else:
        output_filename = f"{base_name}.{format_type}"
    
    # Handle timestamp appending
    if hasattr(args, 'append_timestamp') and args.append_timestamp:
        output_filename = append_timestamp_to_filename(output_filename)
    
    return output_filename


def append_timestamp_to_filename(filename: str) -> str:
    """
    Append timestamp to filename before the extension.
    
    Args:
        filename: Original filename
        
    Returns:
        str: Filename with timestamp appended
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name, ext = os.path.splitext(filename)
    return f"{name}_{timestamp}{ext}"


def resolve_export_path(
    args,
    filename: str,
    default_directory: str = "config_data"
) -> str:
    """
    Resolve the full export file path based on arguments and filename.
    
    Args:
        args: Command line arguments
        filename: The filename to use
        default_directory: Default output directory if none specified
        
    Returns:
        str: Full resolved file path
    """
    # Check if filename is already an absolute path
    if os.path.isabs(filename):
        return filename
    
    # Determine output directory
    output_dir = None
    if hasattr(args, 'output_directory') and args.output_directory:
        output_dir = args.output_directory
    else:
        output_dir = default_directory
    
    # Make output directory absolute if it's not
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(os.getcwd(), output_dir)
    
    return os.path.join(output_dir, filename)


def ensure_output_directory(filepath: str, verbose: bool = False) -> str:
    """
    Ensure the output directory exists for the given filepath.
    
    Args:
        filepath: Full path to the output file
        verbose: Whether to print verbose output
        
    Returns:
        str: The directory path that was created/verified
        
    Raises:
        Exception: If directory creation fails
    """
    output_dir = os.path.dirname(filepath)
    
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            if verbose:
                print(f"Created output directory: {output_dir}")
        except Exception as e:
            raise Exception(f"Failed to create output directory {output_dir}: {e}")
    
    return output_dir


def write_json_export(
    data: Any,
    filepath: str,
    verbose: bool = False,
    indent: int = 2
) -> Dict[str, Any]:
    """
    Write data to JSON file with proper formatting.
    
    Args:
        data: Data to export
        filepath: Full path to output file
        verbose: Whether to print verbose output
        indent: JSON indentation level
        
    Returns:
        dict: Result dictionary with success status and metadata
        
    Raises:
        Exception: If writing fails
    """
    try:
        # Ensure output directory exists
        ensure_output_directory(filepath, verbose)
        
        # Write JSON file
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=indent, ensure_ascii=False)
        
        if verbose:
            print(f"Successfully exported data to JSON: {filepath}")
        
        # Normalize path separators for better cross-platform display
        display_path = filepath.replace(os.sep, '/')
        return {
            'success': True,
            'output_file': display_path,
            'format': 'json',
            'record_count': len(data) if isinstance(data, (list, dict)) else 1
        }
        
    except Exception as e:
        raise Exception(f"Error writing JSON file {filepath}: {e}")


def write_csv_export(
    data: list,
    filepath: str,
    fieldnames: list,
    verbose: bool = False
) -> Dict[str, Any]:
    """
    Write data to CSV file with proper formatting.
    
    Args:
        data: List of dictionaries to export
        filepath: Full path to output file
        fieldnames: List of field names for CSV headers
        verbose: Whether to print verbose output
        
    Returns:
        dict: Result dictionary with success status and metadata
        
    Raises:
        Exception: If writing fails
    """
    try:
        # Ensure output directory exists
        ensure_output_directory(filepath, verbose)
        
        # Write CSV file
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in data:
                # Only include fields that are in fieldnames
                filtered_row = {k: v for k, v in row.items() if k in fieldnames}
                writer.writerow(filtered_row)
        
        if verbose:
            print(f"Successfully exported {len(data)} records to CSV: {filepath}")
        
        # Normalize path separators for better cross-platform display
        display_path = filepath.replace(os.sep, '/')
        return {
            'success': True,
            'output_file': display_path,
            'format': 'csv',
            'record_count': len(data)
        }
        
    except Exception as e:
        raise Exception(f"Error writing CSV file {filepath}: {e}")


def generate_template_data(format_type: str, template_data: Union[Dict, list]) -> Dict[str, Any]:
    """
    Generate template file with sample data.
    
    Args:
        format_type: 'json' or 'csv'
        template_data: Sample data structure for the template
        
    Returns:
        dict: Template data ready for export
    """
    if format_type == 'json':
        return template_data
    elif format_type == 'csv':
        # If template_data is a dict, wrap it in a list for CSV
        if isinstance(template_data, dict):
            return [template_data]
        return template_data
    else:
        raise ValueError(f"Unsupported template format: {format_type}")


def add_common_export_arguments(parser):
    """
    Add common export arguments to an argument parser.
    
    Args:
        parser: ArgumentParser instance to add arguments to
    """
    # Format selection
    parser.add_argument(
        '-f', '--format',
        choices=['csv', 'json'],
        default='json',
        help='Export format (default: json)'
    )
    
    # Output file options
    parser.add_argument(
        '-o', '--output-file',
        dest='output_file',
        help='Output file path (overrides format-specific filenames)'
    )
    
    parser.add_argument(
        '--json-filename',
        dest='json_filename',
        help='Override JSON file name'
    )
    
    parser.add_argument(
        '--csv-filename',
        dest='csv_filename',
        help='Override CSV file name'
    )
    
    parser.add_argument(
        '--append-timestamp',
        dest='append_timestamp',
        action='store_true',
        help='Append timestamp to file names'
    )
    
    parser.add_argument(
        '--output-directory',
        dest='output_directory',
        help='Output directory for exported files (default: config_data)'
    )
    
    # Template generation
    parser.add_argument(
        '-gt', '--generate-template',
        dest='generate_template',
        action='store_true',
        help='Generate template file instead of exporting data'
    )
    
    # Common flags
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    parser.add_argument(
        '-p', '--pretty',
        action='store_true',
        help='Pretty print JSON output'
    )


def export_data_unified(
    data: Any,
    args,
    base_name: str,
    account_id: Optional[str] = None,
    default_template: Optional[str] = None,
    csv_fieldnames: Optional[list] = None,
    default_directory: str = "config_data"
) -> list:
    """
    Unified export function that handles both JSON and CSV formats.
    
    Args:
        data: Data to export (list for CSV, any for JSON)
        args: Command line arguments
        base_name: Base name for the export file
        account_id: Optional account ID for filename template
        default_template: Optional filename template
        csv_fieldnames: Field names for CSV export (required if format is CSV)
        default_directory: Default output directory
        
    Returns:
        list: Result list with success status and metadata
    """
    try:
        format_type = getattr(args, 'format', 'json')
        verbose = getattr(args, 'verbose', False)
        
        # Generate filename
        filename = generate_export_filename(
            args, base_name, format_type, account_id, default_template
        )
        
        # Resolve full path
        filepath = resolve_export_path(args, filename, default_directory)
        
        if verbose:
            print(f"Exporting data to {format_type.upper()}: {filepath}")
        
        # Export based on format
        if format_type == 'json':
            result = write_json_export(data, filepath, verbose)
        elif format_type == 'csv':
            if not csv_fieldnames:
                raise ValueError("CSV fieldnames are required for CSV export")
            if not isinstance(data, list):
                raise ValueError("Data must be a list for CSV export")
            result = write_csv_export(data, filepath, csv_fieldnames, verbose)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
        
        return [result]
        
    except Exception as e:
        return [{'success': False, 'error': str(e)}]