# eventsFeedEnhanced.py - Enhanced eventsFeed for catocli with advanced features
#
# This module provides an enhanced eventsFeed implementation that integrates with catocli
# while providing the advanced features from the original cato-toolbox eventsFeed.py.
# It leverages catocli's native authentication, API client, and compression features.
#

import datetime
import json
import os
import signal
import sys
import time
from ..customParserApiClient import createRequest


def enhanced_events_feed_handler(args, configuration):
    """Enhanced eventsFeed handler with advanced features like marker persistence, 
    continuous polling, and filtering."""
    
    # Store original function to restore later
    original_args = vars(args).copy()
    
    # Setup marker and config file handling
    marker, config_file = setup_marker_and_config(args)
    
    # Setup filters
    filter_obj = setup_filters(args)
    
    # Setup thresholds
    fetch_threshold = getattr(args, 'fetch_limit', 1)
    runtime_limit = getattr(args, 'runtime_limit', None)
    if runtime_limit is None:
        runtime_limit = sys.maxsize
    
    # Statistics tracking
    iteration = 1
    total_count = 0
    all_events = []
    start = datetime.datetime.now()
    
    log(f"Starting enhanced eventsFeed with marker: {marker}", args)
    log(f"Config file: {config_file}, fetch_limit: {fetch_threshold}, runtime_limit: {runtime_limit}", args)
    
    # Setup signal handling for graceful shutdown in enhanced mode
    interrupted = False
    def signal_handler(signum, frame):
        nonlocal interrupted
        interrupted = True
        log("Received interrupt signal, finishing current iteration...", args)
    
    if getattr(args, 'run', False):
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        log("Run continuous mode enabled. Press Ctrl+C to stop gracefully.", args)
    
    while True:
        # Build the JSON request for this iteration
        request_json = {
            "marker": marker
        }
        
        # Add account ID handling (catocli will handle this automatically)
        # Add filters if specified
        if filter_obj:
            request_json["filters"] = [filter_obj]
        
        # Set the JSON argument for the native catocli handler
        args.json = json.dumps(request_json)
        
        log(f"Iteration {iteration}: Requesting events with marker: {marker}", args)
        logd(f"Request JSON: {args.json}", args)
        
        # Use native catocli createRequest function 
        response = createRequest(args, configuration)
        
        if not response:
            log("No response received from API", args)
            break
        
        # Handle response format - catocli createRequest can return different formats
        response_data = None
        if isinstance(response, tuple):
            # If it's a tuple, the actual data is usually in the first element
            response_data = response[0] if len(response) > 0 else None
        elif isinstance(response, list):
            response_data = response[0] if len(response) > 0 else None
        else:
            response_data = response
        
        if not response_data or not isinstance(response_data, dict) or "data" not in response_data:
            log(f"Invalid response format: {type(response_data)} - {response_data}", args)
            break
            
        # Extract eventsFeed data
        try:
            events_feed_data = response_data["data"]["eventsFeed"]
            marker = events_feed_data.get("marker", "")
            fetched_count = int(events_feed_data.get("fetchedCount", 0))
            total_count += fetched_count
            
            # Process accounts and records
            events_list = []
            accounts = events_feed_data.get("accounts", [])
            if accounts and len(accounts) > 0:
                # The GraphQL response uses 'recordsEventsFeedAccountRecords' field name
                records = accounts[0].get("recordsEventsFeedAccountRecords", [])
                for record in records:
                    # Process fieldsMap format like original script
                    if "fieldsMap" in record:
                        event_data = record["fieldsMap"].copy()
                        event_data["event_timestamp"] = record.get("time", "")
                        # Reorder with timestamp first (for Splunk compatibility)
                        event_reorder = dict(sorted(event_data.items(), 
                                                   key=lambda i: i[0] == 'event_timestamp', reverse=True))
                        events_list.append(event_reorder)
                        all_events.append(event_reorder)
            
            # Build log line
            line = f"iteration:{iteration} fetched:{fetched_count} total_count:{total_count} marker:{marker}"
            if events_list:
                line += f" first_event:{events_list[0].get('event_timestamp', 'N/A')}"
                line += f" last_event:{events_list[-1].get('event_timestamp', 'N/A')}"
            log(line, args)
            
            # Print events if requested (use native catocli format)
            if getattr(args, 'print_events', False):
                for event in events_list:
                    if getattr(args, 'prettify', False):
                        print(json.dumps(event, indent=2, ensure_ascii=False))
                    else:
                        try:
                            print(json.dumps(event, ensure_ascii=False))
                        except Exception:
                            print(json.dumps(event))
            
            # Write marker back to config file
            if marker:
                try:
                    with open(config_file, "w") as f:
                        f.write(marker)
                    logd(f"Written marker to {config_file}: {marker}", args)
                except IOError as e:
                    log(f"Warning: Could not write marker to config file: {e}", args)
            
        except (KeyError, TypeError, ValueError) as e:
            log(f"Error processing response: {e}", args)
            break
        
        # Check stopping conditions
        iteration += 1
        
        # Check for interrupt signal
        if interrupted:
            log("Gracefully stopping due to interrupt signal", args)
            break
        
        # Only stop on fetch_limit if NOT in run continuous mode
        if not getattr(args, 'run', False) and fetched_count < fetch_threshold:
            log(f"Fetched count {fetched_count} less than threshold {fetch_threshold}, stopping", args)
            break
        
        # In run mode, continue polling even if no events, but respect runtime limit
        elapsed = datetime.datetime.now() - start
        if elapsed.total_seconds() > runtime_limit:
            log(f"Elapsed time {elapsed.total_seconds()} exceeds runtime limit {runtime_limit}, stopping", args)
            break
        
        # In run mode, add a small delay between iterations to avoid hammering the API
        if getattr(args, 'run', False):
            if fetched_count == 0:
                log("No events in this iteration, waiting 2 seconds before next poll...", args)
                time.sleep(2)  # Wait 2 seconds when no events
            else:
                time.sleep(0.1)  # Small delay when events are flowing
    
    # Final statistics
    end = datetime.datetime.now()
    log(f"Enhanced eventsFeed completed: {total_count} events in {end-start}", args)
    
    # Return in standard catocli format (the network streaming and sentinel 
    # integration are handled automatically by the native createRequest function)
    return [{
        "success": True,
        "total_events": total_count,
        "duration": str(end - start),
        "final_marker": marker,
        "iterations": iteration - 1
    }]


def setup_marker_and_config(args):
    """Setup marker and config file handling (similar to original eventsFeed.py)"""
    config_file = "./config.txt"
    
    if getattr(args, 'config_file', None):
        config_file = args.config_file
        log(f"Using config file from argument: {config_file}", args)
    else:
        log(f"Using default config file: {config_file}", args)
    
    marker = ""
    if getattr(args, 'marker', None):
        marker = args.marker
        log(f"Using marker from argument: {marker}", args)
    else:
        # Try to load marker from config file
        if os.path.isfile(config_file):
            try:
                with open(config_file, "r") as f:
                    marker = f.readlines()[0].strip()
                log(f"Read marker from config file: {marker}", args)
            except (IndexError, IOError) as e:
                log(f"Could not read marker from config file: {e}", args)
        else:
            log("Config file does not exist, starting with empty marker", args)
    
    return marker, config_file


def setup_filters(args):
    """Setup event filtering based on type and subtype"""
    filters = []
    
    # Process event_types filter
    if getattr(args, 'event_types', None):
        event_types = [t.strip() for t in args.event_types.split(',')]
        filters.append({
            "fieldName": "event_type",
            "operator": "in",
            "values": event_types
        })
        log(f"Added event_type filter: {event_types}", args)
    
    # Process event_sub_types filter
    if getattr(args, 'event_sub_types', None):
        event_sub_types = [t.strip() for t in args.event_sub_types.split(',')]
        filters.append({
            "fieldName": "event_sub_type", 
            "operator": "in",
            "values": event_sub_types
        })
        log(f"Added event_sub_type filter: {event_sub_types}", args)
    
    # Return single filter object if only one, None if none
    if len(filters) == 1:
        return filters[0]
    elif len(filters) > 1:
        # For multiple filters, we'd need to handle this differently
        # For now, just return the first one and warn
        log(f"Warning: Multiple filters specified, using first one only: {filters[0]}", args)
        return filters[0]
    
    return None


def log(text, args):
    """Log debug output"""
    # Handle catocli's -v argument which can be True or a string
    verbose = getattr(args, 'v', False)
    if verbose is True or (isinstance(verbose, str) and verbose.lower() in ['true', '1', 'yes']):
        print(f"LOG {datetime.datetime.now(datetime.UTC)}> {text}")


def logd(text, args):
    """Log detailed debug output"""
    if getattr(args, 'very_verbose', False):
        log(text, args)
