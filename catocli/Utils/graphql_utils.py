#!/usr/bin/env python3
"""
GraphQL Utilities Library for Cato CLI

This module contains shared utility functions for GraphQL operations,
JSON handling, and string manipulations used across the Cato CLI components.

This consolidates duplicate functions from:
- catocli/parsers/customParserApiClient.py  
- schema/catolib.py

Functions included:
- JSON file loading with proper path resolution
- String manipulation (camelCase conversion)
- GraphQL introspection utilities
- Common validation utilities
"""

import json
import logging
import os
import sys


def loadJSON(file, calling_module_path=None):
    """
    Enhanced JSON loading with better error handling and path resolution
    
    This function handles loading JSON files from various locations in the CLI,
    with intelligent path resolution based on the calling module's location.
    
    Args:
        file: Filename to load (e.g., "clisettings.json", "models/query.xdr.stories.json")
        calling_module_path: Optional path of the calling module for better path resolution
        
    Returns:
        Parsed JSON data as dictionary
        
    Raises:
        FileNotFoundError: If file cannot be found
        json.JSONDecodeError: If JSON is invalid
    """
    # If calling module path is provided, use it for path resolution
    if calling_module_path:
        module_dir = os.path.dirname(calling_module_path)
    else:
        # Fallback: use current module's directory
        module_dir = os.path.dirname(__file__)
    
    # Special handling for different file types
    if file == "clisettings.json":
        # clisettings.json is in catocli/ directory
        # Navigate from Utils/ to catocli/
        catocli_dir = os.path.dirname(module_dir)
        file_path = os.path.join(catocli_dir, file)
    elif file.startswith("models/"):
        # Models are in the root directory
        # Navigate from catocli/Utils/ to root
        root_dir = os.path.dirname(os.path.dirname(module_dir))
        file_path = os.path.join(root_dir, file)
    elif file.startswith("queryPayloads/"):
        # Query payloads are in the root directory  
        root_dir = os.path.dirname(os.path.dirname(module_dir))
        file_path = os.path.join(root_dir, file)
    elif os.path.isabs(file):
        # Absolute path - use as is
        file_path = file
    else:
        # Relative path - try multiple locations
        possible_paths = [
            os.path.join(module_dir, file),  # Same directory as calling module
            os.path.join(os.path.dirname(module_dir), file),  # Parent directory
            os.path.join(os.path.dirname(os.path.dirname(module_dir)), file),  # Root directory
        ]
        
        file_path = None
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break
        
        if not file_path:
            raise FileNotFoundError(f"Could not find {file} in any of the expected locations")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as data:
            config = json.load(data)
            logging.debug(f"Successfully loaded {file} from {file_path}")
            return config
    except FileNotFoundError:
        logging.error(f"File \"{file_path}\" not found.")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in file \"{file_path}\": {e}")
        raise
    except Exception as e:
        logging.error(f"Error loading file \"{file_path}\": {e}")
        raise


def renderCamelCase(path_str):
    """
    Convert dot-separated path to camelCase
    
    Examples:
        'app.stats' -> 'appStats'
        'query.xdr.stories' -> 'queryXdrStories'
        'site.location' -> 'siteLocation'
    
    Args:
        path_str: Dot-separated string
        
    Returns:
        camelCase string
    """
    if not path_str:
        return ""
        
    result = ""
    path_ary = path_str.split(".")
    
    for i, path in enumerate(path_ary):
        if not path:  # Skip empty parts
            continue
            
        if i == 0:
            # First part: lowercase
            result += path[0].lower() + path[1:] if len(path) > 1 else path.lower()
        else:
            # Subsequent parts: capitalize first letter
            result += path[0].upper() + path[1:] if len(path) > 1 else path.upper()
            
    return result


def validateArgs(variables_obj, operation):
    """
    Basic argument validation for GraphQL operations
    
    Args:
        variables_obj: Dictionary of variables to validate
        operation: Operation definition containing argument specifications
        
    Returns:
        Tuple of (is_valid: bool, invalid_vars: list, message: str)
    """
    if not isinstance(variables_obj, dict):
        return False, [], "Variables must be a dictionary"
    
    if not operation or not isinstance(operation, dict):
        return False, [], "Operation definition is required"
    
    # For now, basic validation - can be enhanced based on operation requirements
    invalid_vars = []
    
    # Check for required arguments in operation
    operation_args = operation.get('operationArgs', {})
    for arg_name, arg_def in operation_args.items():
        if arg_def.get('required', False):
            var_name = arg_def.get('varName', arg_name)
            if var_name not in variables_obj or variables_obj[var_name] is None:
                invalid_vars.append(var_name)
    
    if invalid_vars:
        message = f"Missing required arguments: {', '.join(invalid_vars)}"
        return False, invalid_vars, message
    
    return True, [], "Valid"


def loadIntrospectionTypes():
    """
    Load GraphQL introspection type data
    
    This function loads the GraphQL schema introspection data used for 
    dynamic field expansion and query generation.
    
    Returns:
        Dictionary containing introspection type definitions
        
    Raises:
        Exception: If introspection data cannot be loaded
    """
    try:
        # Try to import from the catolib module where it's defined
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)  # catocli/
        root_dir = os.path.dirname(parent_dir)     # root/
        schema_dir = os.path.join(root_dir, 'schema')
        
        # Add schema directory to Python path temporarily
        if schema_dir not in sys.path:
            sys.path.insert(0, schema_dir)
        
        try:
            from catolib import catoApiIntrospection
            
            # Convert the introspection data to a more usable format
            introspection_types = {}
            
            # Add all type categories
            for category in ['objects', 'interfaces', 'unions', 'input_objects', 'enums', 'scalars']:
                if category in catoApiIntrospection:
                    introspection_types.update(catoApiIntrospection[category])
            
            return introspection_types
            
        finally:
            # Remove schema directory from path
            if schema_dir in sys.path:
                sys.path.remove(schema_dir)
                
    except Exception as e:
        logging.warning(f"Could not load introspection types: {e}")
        return {}


def getOfTypeNormalized(type_info):
    """
    Normalize GraphQL type information by unwrapping type wrappers
    
    GraphQL types can be wrapped in NonNull, List, etc. This function
    unwraps them to get the core type information.
    
    Args:
        type_info: GraphQL type information object
        
    Returns:
        Dictionary with normalized type info including:
        - name: Core type name
        - kind: Core type kind  
        - is_list: Whether the type is wrapped in a List
        - is_non_null: Whether the type is wrapped in NonNull
    """
    if not type_info:
        return {'name': None, 'kind': None, 'is_list': False, 'is_non_null': False}
    
    current_type = type_info
    is_list = False
    is_non_null = False
    
    # Unwrap type wrappers
    while current_type and current_type.get('ofType'):
        if current_type.get('kind') == 'NON_NULL':
            is_non_null = True
        elif current_type.get('kind') == 'LIST':
            is_list = True
        current_type = current_type.get('ofType')
    
    # Final type check
    if current_type and current_type.get('kind') == 'NON_NULL':
        is_non_null = True
        current_type = current_type.get('ofType')
    elif current_type and current_type.get('kind') == 'LIST':
        is_list = True  
        current_type = current_type.get('ofType')
    
    return {
        'name': current_type.get('name') if current_type else None,
        'kind': current_type.get('kind') if current_type else None,
        'is_list': is_list,
        'is_non_null': is_non_null
    }


def isComplexType(type_info):
    """
    Check if a GraphQL type is complex (requires subfield selection)
    
    Args:
        type_info: GraphQL type information
        
    Returns:
        Boolean indicating if the type needs subfield selection
    """
    normalized = getOfTypeNormalized(type_info)
    return normalized['kind'] in ['OBJECT', 'INTERFACE', 'UNION']


def sanitizeFieldName(field_name):
    """
    Sanitize field names for use in GraphQL queries
    
    Args:
        field_name: Original field name
        
    Returns:
        Sanitized field name safe for GraphQL
    """
    if not field_name:
        return ""
    
    # Remove any characters that aren't valid in GraphQL field names
    import re
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '', field_name)
    
    # Ensure it starts with a letter or underscore
    if sanitized and sanitized[0].isdigit():
        sanitized = '_' + sanitized
        
    return sanitized or "field"


def generateGraphqlPayload(variables_obj, operation, operation_name, renderArgsAndFields_func=None):
    """
    Enhanced GraphQL payload generation with dynamic argument discovery and improved field expansion
    
    This implementation includes several critical improvements:
    1. Full introspection-based field expansion for complex types
    2. Dynamic argument discovery during field rendering 
    3. Proper aliasing for fields with the same name in different fragments
    4. Complete handling of union types and inline fragments
    5. Automatic detection and expansion of fields that need subfield selections
    
    Args:
        variables_obj: Variables for the GraphQL query
        operation: Operation definition from schema
        operation_name: Name of the operation (e.g., 'query.appStats')
        
    Returns:
        Complete GraphQL request payload
    """
    indent = "\t"
    query_str = ""
    
    # Pre-process variables - handle cases like XDR stories where we need field name mappings
    # This could be expanded for other operations as needed
    if operation_name == "query.xdr.stories" and "storyInput" in variables_obj:
        story_input = variables_obj["storyInput"]
        # Map storyFilterInput to filter if needed 
        if "storyFilterInput" in story_input:
            story_input["filter"] = story_input.pop("storyFilterInput")
        # Map pagingInput to paging if needed
        if "pagingInput" in story_input:
            story_input["paging"] = story_input.pop("pagingInput")
    
    # Initialize dynamic operationArgs collection (like JavaScript curOperation.operationArgs)
    dynamic_operation_args = operation.get("operationArgs", {}).copy()
    
    # Build query structure first
    operation_ary = operation_name.split(".")
    operation_type = operation_ary.pop(0)
    query_str = f"{operation_type} "
    query_str += renderCamelCase(".".join(operation_ary))
    
    # We'll build variable_str after field rendering to include dynamically discovered arguments
    query_str += f" ( VARIABLES_PLACEHOLDER) {{\n"
    query_str += f"{indent}{operation['name']} ( "
    
    # Add main operation arguments - only include arguments that belong to the root operation field
    # Arguments for nested fields (like updateRule.input) will be handled in the field rendering process
    # Use args (not operationArgs) to only get main-level arguments for the root operation field
    main_args = operation.get("args", {})
    for arg_name in main_args:
        arg = main_args[arg_name]
        # Include required arguments always, and optional arguments only when they have meaningful values
        var_name = arg["varName"]
        is_required = arg.get("required", False)
        has_value = (var_name in variables_obj and 
                    variables_obj[var_name] is not None and 
                    variables_obj[var_name] != "" and 
                    variables_obj[var_name] != [] and 
                    variables_obj[var_name] != {})
        
        if is_required or has_value:
            query_str += arg["responseStr"]
    
    # Generate field selection with enhanced rendering and dynamic argument collection
    if renderArgsAndFields_func is None:
        # Try to import from the calling context
        try:
            import inspect
            frame = inspect.currentframe().f_back
            if 'renderArgsAndFields' in frame.f_globals:
                renderArgsAndFields_func = frame.f_globals['renderArgsAndFields']
            else:
                raise ImportError("renderArgsAndFields not found in calling context")
        except:
            # Fallback - this will need to be implemented or imported
            raise NotImplementedError("renderArgsAndFields function must be provided or available in calling context")
    
    field_selection = renderArgsAndFields_func("", variables_obj, operation, operation["type"]["definition"], operation_name, "\t\t", dynamic_operation_args)
    
    # CRITICAL FIX: Post-process the field selection to expand any remaining bare complex fields
    # This ensures all fields that need subfield selections are properly expanded
    field_selection = postProcessBareComplexFields(field_selection, "\t\t")
    
    query_str += ") {\n" + field_selection + "\t}"
    query_str += f"{indent}\n}}"
    
    # Now build variable declarations from dynamically collected arguments
    variable_str = ""
    for arg_name in dynamic_operation_args:
        arg = dynamic_operation_args[arg_name]
        # Include required arguments always, and optional arguments only when they have meaningful values
        var_name = arg["varName"]
        is_required = arg.get("required", False)
        has_value = (var_name in variables_obj and 
                    variables_obj[var_name] is not None and 
                    variables_obj[var_name] != "" and 
                    variables_obj[var_name] != [] and 
                    variables_obj[var_name] != {})
        
        if is_required or has_value:
            variable_str += arg["requestStr"]
    
    # Replace the placeholder with actual variables
    query_str = query_str.replace("VARIABLES_PLACEHOLDER", variable_str.strip())
    
    body = {
        "query": query_str,
        "variables": variables_obj,
        "operationName": renderCamelCase(".".join(operation_ary)),
    }
    return body


def postProcessBareComplexFields(field_selection_str, base_indent):
    """Post-process the generated field selection to expand any bare complex fields.
    
    ENHANCED VERSION: Uses dynamic introspection discovery instead of hardcoded field lists.
    This function scans the field selection string for fields that appear as bare fields
    but actually need subfield selections based on introspection data.
    
    This new approach:
    1. Dynamically discovers all available GraphQL types from introspection
    2. Attempts to match bare fields to their corresponding types
    3. Expands any fields that need subfield selections
    4. Works like the JavaScript version without hardcoded limitations
    
    Args:
        field_selection_str: The generated field selection string
        base_indent: The base indentation level
    
    Returns:
        Field selection string with all complex fields properly expanded
    """
    try:
        introspection_types = loadIntrospectionTypes()
    except:
        return field_selection_str  # Return unchanged if introspection fails
    
    if not introspection_types:
        return field_selection_str
    
    lines = field_selection_str.split('\n')
    processed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        line_expanded = False
        
        # Extract the field name from the line (handle aliases too)
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#') and not stripped_line.startswith('...') and '{' not in stripped_line and '}' not in stripped_line:
            # Extract field name (handle aliases like "fieldAlias: fieldName")
            field_name = stripped_line
            if ':' in stripped_line:
                # This is an alias, get the actual field name after the colon
                field_name = stripped_line.split(':', 1)[1].strip()
            
            # Only process if this looks like a bare field (no opening brace)
            if field_name and not field_name.endswith(':'):
                # Try to find a matching type in introspection data
                candidate_types = findCandidateTypesForField(field_name, introspection_types)
                
                # Determine indentation
                indent_match = len(line) - len(line.lstrip())
                current_indent = '\t' * (indent_match // 4)  # Convert spaces to tabs
                
                # Try each candidate type
                expansion = ""
                for candidate_type in candidate_types:
                    if candidate_type in introspection_types:
                        type_def = introspection_types[candidate_type]
                        if type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                            expansion = expandFieldWithIntrospection(field_name, candidate_type, current_indent)
                            if expansion:
                                break
                
                # If we found an expansion, replace the bare field
                if expansion:
                    # Create the expanded field (preserve any alias)
                    if ':' in stripped_line:
                        # Preserve the alias format
                        alias_part = stripped_line.split(':', 1)[0].strip()
                        expanded_field = f"{current_indent}{alias_part}: {field_name} {{\n{expansion}{current_indent}}}\n"
                    else:
                        expanded_field = f"{current_indent}{field_name} {{\n{expansion}{current_indent}}}\n"
                    processed_lines.append(expanded_field)
                    line_expanded = True
        
        # If line wasn't expanded, keep it as is
        if not line_expanded:
            processed_lines.append(line + '\n' if not line.endswith('\n') else line)
        
        i += 1
    
    return ''.join(processed_lines).rstrip() + ('\n' if field_selection_str.endswith('\n') else '')


def findCandidateTypesForField(field_name, introspection_types):
    """Dynamically find candidate GraphQL types for a given field name.
    
    This function searches through all available GraphQL types to find potential
    matches for a field name, using various heuristics similar to how the JavaScript
    version dynamically discovers types.
    
    Args:
        field_name: The field name to find types for
        introspection_types: Dictionary of all GraphQL types from introspection
    
    Returns:
        List of candidate type names that could match this field
    """
    candidates = []
    
    # Strategy 1: Exact type name match (e.g., field "user" -> type "User")
    exact_match = field_name.capitalize()
    if exact_match in introspection_types:
        candidates.append(exact_match)
    
    # Strategy 2: Common suffixes for field-to-type mapping
    suffixes = ['Ref', 'Details', 'Data', 'Info', 'Type', 'Event', 'Alert', 'Connection']
    for suffix in suffixes:
        candidate = field_name.capitalize() + suffix
        if candidate in introspection_types:
            candidates.append(candidate)
    
    # Strategy 3: Search for types that contain the field name
    for type_name in introspection_types:
        if field_name.lower() in type_name.lower() and type_name not in candidates:
            # Check if this type actually makes sense (has fields)
            type_def = introspection_types[type_name]
            if type_def.get('kind') in ['OBJECT', 'INTERFACE'] and type_def.get('fields'):
                candidates.append(type_name)
    
    # Strategy 4: Handle plurals (e.g., "events" -> "Event")
    if field_name.endswith('s') and len(field_name) > 1:
        singular = field_name[:-1]
        singular_candidates = findCandidateTypesForField(singular, introspection_types)
        candidates.extend(singular_candidates)
    
    # Strategy 5: Handle camelCase to PascalCase (e.g., "osDetails" -> "OsDetails")
    if any(c.isupper() for c in field_name[1:]):
        pascal_case = field_name[0].upper() + field_name[1:]
        if pascal_case in introspection_types:
            candidates.append(pascal_case)
    
    # Strategy 6: Advanced pattern matching based on field name structure
    # Handle compound field names (e.g., "incidentTimeline" -> "IncidentTimeline", "TimelineEvent", etc.)
    if len(field_name) > 3:  # Only for meaningful field names
        # Try breaking compound words and creating type names
        import re
        # Split on capital letters to handle camelCase
        words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\b)', field_name)
        if len(words) > 1:
            # Try different combinations
            # Full compound (e.g., "incidentTimeline" -> "IncidentTimeline")
            compound = ''.join(word.capitalize() for word in words)
            if compound not in candidates and compound in introspection_types:
                candidates.append(compound)
            
            # Last word as type (e.g., "networkTimeline" -> "Timeline")
            last_word = words[-1].capitalize()
            if last_word not in candidates and last_word in introspection_types:
                candidates.append(last_word)
            
            # First word as type (e.g., "incidentFlow" -> "Incident")
            first_word = words[0].capitalize()
            if first_word not in candidates and first_word in introspection_types:
                candidates.append(first_word)
    
    # Strategy 7: JavaScript-like dynamic discovery - search all types for fields that return this field name
    # This mimics how the JavaScript version dynamically discovers field relationships
    for type_name, type_def in introspection_types.items():
        if type_def.get('kind') in ['OBJECT', 'INTERFACE'] and type_def.get('fields'):
            for field_def in type_def['fields']:
                if field_def['name'] == field_name:
                    # Found a type that has a field with this name, get the field's type
                    field_type = field_def.get('type', {})
                    
                    # Navigate through type wrappers to find the core type
                    current_type = field_type
                    while current_type and current_type.get('ofType'):
                        current_type = current_type['ofType']
                    
                    if current_type and current_type.get('name'):
                        candidate_type = current_type['name']
                        if candidate_type not in candidates and candidate_type in introspection_types:
                            # Verify this type has complex fields (like JavaScript logic)
                            candidate_def = introspection_types[candidate_type]
                            if candidate_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                                candidates.append(candidate_type)
    
    # Remove duplicates while preserving order
    unique_candidates = []
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    
    return unique_candidates


def expandFieldWithIntrospection(field_name, field_type_name, indent, already_expanded_fields=None, max_depth=4):
    """Use introspection data to expand a field that needs subfield selections.
    
    ENHANCED VERSION: More comprehensive expansion that works like the JavaScript renderArgsAndFields.
    This version provides better handling of nested objects, unions, interfaces, and recursive expansion.
    
    Key improvements:
    1. Better handling of union types with proper inline fragments
    2. More comprehensive field selection (like JavaScript version)
    3. Improved recursion control and depth limiting
    4. Better field prioritization and selection
    
    Args:
        field_name: The name of the field to expand
        field_type_name: The GraphQL type name for this field
        indent: Current indentation level
        already_expanded_fields: Set of field names already expanded to prevent cycles
        max_depth: Maximum recursion depth
    
    Returns:
        String containing the expanded field with its subfields, or empty string if not expandable
    """
    if already_expanded_fields is None:
        already_expanded_fields = set()
    
    if field_name in already_expanded_fields or max_depth <= 0:
        return ""  # Prevent infinite recursion
    
    already_expanded_fields.add(field_name)
    
    try:
        # Load introspection data
        introspection_types = loadIntrospectionTypes()
        if field_type_name not in introspection_types:
            already_expanded_fields.remove(field_name)
            return ""  # Can't expand without introspection data
        
        type_def = introspection_types[field_type_name]
        
        # Only expand complex types
        if type_def.get('kind') not in ['OBJECT', 'INTERFACE', 'UNION']:
            already_expanded_fields.remove(field_name)
            return ""  # Simple types don't need expansion
        
        result = ""
        
        if type_def.get('kind') == 'OBJECT' and type_def.get('fields'):
            # Expand object fields - prioritize important fields first
            simple_fields = []
            complex_fields = []
            priority_fields = []  # High-priority fields to include first
            
            # Define fields that should be prioritized (commonly requested)
            high_priority_field_names = ['id', 'name', 'type', 'status', 'description', 'value', 'timestamp', 'createdAt', 'updatedAt']
            
            for introspection_field in type_def['fields']:
                field_name_inner = introspection_field['name']
                field_type_info = introspection_field.get('type', {})
                
                # Navigate through type wrappers to find the core type
                current_type = field_type_info
                while current_type and current_type.get('ofType'):
                    current_type = current_type['ofType']
                
                if current_type and current_type.get('kind'):
                    if current_type['kind'] in ['SCALAR', 'ENUM']:
                        # Simple field - prioritize if it's important
                        if field_name_inner in high_priority_field_names:
                            priority_fields.append(field_name_inner)
                        else:
                            simple_fields.append(field_name_inner)
                    elif current_type.get('name'):
                        # Complex field - check if it needs expansion
                        inner_type_name = current_type['name']
                        if inner_type_name in introspection_types:
                            inner_type_def = introspection_types[inner_type_name]
                            if inner_type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                                # This is a complex field that needs expansion
                                complex_fields.append((field_name_inner, inner_type_name))
                            else:
                                # It's a complex type but scalar-like (e.g., custom scalars)
                                simple_fields.append(field_name_inner)
                        else:
                            simple_fields.append(field_name_inner)
                else:
                    simple_fields.append(field_name_inner)
            
            # Add priority fields first
            for priority_field in priority_fields:
                result += f"{indent}\t{priority_field}\n"
            
            # Add simple fields (but limit them to prevent overly large queries)
            for simple_field in simple_fields[:15]:  # Limit to prevent massive queries
                result += f"{indent}\t{simple_field}\n"
            
            # Add complex fields with recursive expansion
            for complex_field_name, complex_type_name in complex_fields[:8]:  # Limit complex fields
                if complex_field_name not in already_expanded_fields and max_depth > 1:
                    expansion = expandFieldWithIntrospection(
                        complex_field_name, 
                        complex_type_name, 
                        indent + "\t", 
                        already_expanded_fields.copy(), 
                        max_depth - 1
                    )
                    if expansion:
                        result += f"{indent}\t{complex_field_name} {{\n{expansion}{indent}\t}}\n"
                    else:
                        # Fallback: add minimal expansion for known complex types
                        result += f"{indent}\t{complex_field_name}\n"
                else:
                    result += f"{indent}\t{complex_field_name}\n"
        
        elif type_def.get('kind') in ['INTERFACE', 'UNION'] and type_def.get('possibleTypes'):
            # Add __typename for interface/union types (essential for GraphQL)
            result += f"{indent}\t__typename\n"
            
            # Add inline fragments for each possible type
            for possible_type in type_def['possibleTypes'][:5]:  # Limit to prevent huge queries
                possible_type_name = possible_type.get('name')
                if possible_type_name and possible_type_name in introspection_types:
                    possible_type_def = introspection_types[possible_type_name]
                    if possible_type_def.get('fields'):
                        result += f"{indent}\t... on {possible_type_name} {{\n"
                        
                        # Add key fields from this type (limited depth to prevent recursion issues)
                        if max_depth > 1:
                            for poss_field in possible_type_def['fields'][:10]:  # Limit fields per fragment
                                poss_field_name = poss_field['name']
                                poss_field_type_info = poss_field.get('type', {})
                                
                                # Get the core type
                                current_type = poss_field_type_info
                                while current_type and current_type.get('ofType'):
                                    current_type = current_type['ofType']
                                
                                if current_type and current_type.get('kind'):
                                    if current_type['kind'] in ['SCALAR', 'ENUM']:
                                        result += f"{indent}\t\t{poss_field_name}\n"
                                    elif current_type.get('name') and current_type['name'] in introspection_types:
                                        # Check if this field needs further expansion
                                        inner_type_def = introspection_types[current_type['name']]
                                        if inner_type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION'] and max_depth > 2:
                                            # Recursively expand, but with reduced depth
                                            inner_expansion = expandFieldWithIntrospection(
                                                poss_field_name, 
                                                current_type['name'], 
                                                indent + "\t\t", 
                                                already_expanded_fields.copy(), 
                                                max_depth - 2
                                            )
                                            if inner_expansion:
                                                result += f"{indent}\t\t{poss_field_name} {{\n{inner_expansion}{indent}\t\t}}\n"
                                            else:
                                                result += f"{indent}\t\t{poss_field_name}\n"
                                        else:
                                            result += f"{indent}\t\t{poss_field_name}\n"
                                    else:
                                        result += f"{indent}\t\t{poss_field_name}\n"
                                else:
                                    result += f"{indent}\t\t{poss_field_name}\n"
                        
                        result += f"{indent}\t}}\n"
        
        already_expanded_fields.remove(field_name)
        return result
        
    except Exception as e:
        # If anything goes wrong, remove from expanded fields and return empty
        if field_name in already_expanded_fields:
            already_expanded_fields.remove(field_name)
        return ""


def renderArgsAndFields(response_arg_str, variables_obj, cur_operation, definition, operation_name, indent, dynamic_operation_args=None, custom_client=None):
    """
    ENHANCED field rendering with custom field expansion support, introspection-based field expansion,
    and dynamic argument collection.
    
    This is the key function that generates the GraphQL field selection.
    Key improvements:
    1. Uses introspection to fully expand complex types at all levels of nesting
    2. Properly handles union types and inline fragments
    3. Implements aliasing for fields to avoid naming conflicts
    4. Supports dynamic argument collection
    5. Automatically detects and expands fields with complex types
    
    Args:
        response_arg_str: Current field string being built
        variables_obj: Variables for the query
        cur_operation: Current operation definition  
        definition: Field definitions
        operation_name: Name of the operation (for custom mappings)
        indent: Current indentation level
        dynamic_operation_args: Dictionary to collect operation arguments dynamically (like JavaScript)
        custom_client: Custom client instance for custom field expansions (optional)
        
    Returns:
        Complete field selection string
    """
    if not definition or not isinstance(definition, dict) or 'fields' not in definition:
        return response_arg_str
    
    # For debugging severe issues
    # import sys
    # print(f"DEBUG: renderArgsAndFields - operation_name={operation_name}, fields={list(definition['fields'].keys())}", file=sys.stderr)
        
    for field_name in definition['fields']:
        field = definition['fields'][field_name]
        # Force use of plain field name instead of alias to match API response structure
        # The API returns simple field names like "audit" not "auditWanFirewallRulePayload: audit"
        field_display_name = field['name']
        
        # JAVASCRIPT COMPATIBILITY: Field inclusion logic will be handled at the subfield level
        # The JavaScript implementation strategically excludes certain subfields for specific operations
        
        # DISABLED: Field conflict resolution for fields with different types across union fragments
        # The original aliasing logic was creating aliases that don't match the API response structure
        # For example: auditWanFirewallRulePayload: audit instead of just audit
        # Since the API returns simple field names without aliases, we'll use the simple field name
        # 
        # if definition.get('name'):  # We're inside a union/interface fragment
        #     field_type_info = field.get('type', {})
        #     
        #     # Check for fields that commonly conflict across fragments
        #     if field['name'] in ['siteName', 'name', 'id', 'type', 'status']:
        #         # Create unique alias using the fragment type name
        #         field_display_name = f"{field['name']}{definition['name']}: {field['name']}"
        #     # Also handle fields where the type signature might differ
        #     elif field_type_info and field_type_info.get('kind'):
        #         kinds = field_type_info.get('kind', [])
        #         # Check if this is a nullable vs non-nullable conflict
        #         if isinstance(kinds, list):
        #             if ('NON_NULL' in kinds) != ('NON_NULL' in str(definition.get('fields', {}).get(field['name'], {}).get('type', {}))):
        #                 # Different nullability - create alias
        #                 field_display_name = f"{field['name']}{definition['name']}: {field['name']}"
        
        # Field inclusion logic: Skip fields that are known to cause issues
        # This matches the JavaScript implementation approach of being selective about fields
        
        # Check if field has arguments and whether they are present in variables
        should_include_field = True
        args_present = False
        arg_str = ""
        
        if field.get("args") and not isinstance(field['args'], list):
            if len(list(field['args'].keys())) > 0:
                # Field has arguments - check if any are required or present
                arg_str = " ( "
                required_args_missing = False
                
                for arg_name in field['args']:
                    arg = field['args'][arg_name]
                    
                    # NEW: Dynamic argument collection like JavaScript (line 874: curOperation.operationArgs[arg.varName] = arg)
                    if dynamic_operation_args is not None and isinstance(dynamic_operation_args, dict):
                        dynamic_operation_args[arg["varName"]] = arg
                    
                    # CRITICAL FIX: Match JavaScript logic exactly - regenerate responseStr here
                    # JavaScript line 868: arg.responseStr = arg.name + ":$" + arg.varName + " ";
                    arg['responseStr'] = arg['name'] + ":$" + arg['varName'] + " "
                    
                    # Only include arguments that are present in variables_obj and have values
                    # This matches the JavaScript implementation behavior
                    if arg["varName"] in variables_obj and variables_obj[arg["varName"]] is not None and variables_obj[arg["varName"]] != "" and variables_obj[arg["varName"]] != [] and variables_obj[arg["varName"]] != {}:
                        arg_str += arg['responseStr'] + " "
                        args_present = True
                    elif arg.get("required", False):
                        # Required argument is missing
                        required_args_missing = True
                        break
                        
                arg_str += ") "
                
                # Only exclude field if required arguments are missing
                # If all arguments are optional, include the field even without arguments
                should_include_field = not required_args_missing
        
        # ALWAYS process field (no exclusion logic like cato-api-explorer)
        response_arg_str += f"{indent}{field_display_name}"
        if args_present:
            response_arg_str += arg_str
        
        # Check if this field needs introspection expansion BEFORE checking for existing definitions
        field_needs_introspection_expansion = False
        field_type_name_for_expansion = None
        
        if field.get('type'):
            field_type = field['type']
            if field_type.get('name'):
                field_type_name_for_expansion = field_type['name']
            # Drill through wrapped types
            while field_type and field_type.get('ofType'):
                field_type = field_type['ofType']
                if field_type and field_type.get('name'):
                    field_type_name_for_expansion = field_type['name']
        
        # Check if this field type exists in introspection and needs expansion
        if field_type_name_for_expansion:
            introspection_types = loadIntrospectionTypes()
            if field_type_name_for_expansion in introspection_types:
                type_def = introspection_types[field_type_name_for_expansion]
                if type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                    # This field represents a complex type that needs subfield selections
                    # Check if we already have proper definitions for it
                    has_proper_definition = (
                        field.get("type") and field['type'].get('definition') and 
                        (field['type']['definition'].get('fields') is not None or 
                         field['type']['definition'].get('inputFields') is not None)
                    )
                    if not has_proper_definition:
                        field_needs_introspection_expansion = True
        
        # ENHANCED: Check for introspection expansion first if field needs it
        if field_needs_introspection_expansion:
            expansion = expandFieldWithIntrospection(field['name'], field_type_name_for_expansion, indent)
            if expansion:
                response_arg_str += " {\n"
                response_arg_str += expansion
                response_arg_str += f"{indent}}}\n"
            else:
                # Fallback - just add newline if expansion failed
                response_arg_str += "\n"
        
        # ENHANCED: Check for custom field expansions (only if not already expanded by introspection)
        elif custom_client and hasattr(custom_client, 'get_custom_fields') and custom_client.get_custom_fields(operation_name, field['name']):
            custom_fields = custom_client.get_custom_fields(operation_name, field['name'])
            response_arg_str += "  {\n"
            for custom_field in custom_fields:
                response_arg_str += f"{indent}\t{custom_field}\n"
            response_arg_str += f"{indent}}}\n"
        
        # Standard nested field processing - CRITICAL: Match JavaScript logic exactly
        # JavaScript: if (field.type && field.type.definition && field.type.definition.fields != null)
        elif field.get("type") and field['type'].get('definition') and field['type']['definition'].get('fields') is not None:
            response_arg_str += " {\n"
            for subfield_index in field['type']['definition']['fields']:
                subfield = field['type']['definition']['fields'][subfield_index]
                # Force use of plain field name instead of alias to match API response structure
                # The API returns simple field names like "audit" not "auditWanFirewallRulePayload: audit"
                subfield_name = subfield['name']
                
                # JAVASCRIPT COMPATIBILITY: Skip problematic 'fields' subfield in 'records' for socketPortMetrics
                # The JavaScript implementation strategically excludes the 'fields' object within 'records'
                # because it contains union types that cause GraphQL validation errors
                if (operation_name and 'socketPortMetrics' in operation_name and 
                    field_display_name == 'records' and subfield_name == 'fields'):
                    continue  # Skip the fields subfield that contains the problematic Value union type
                
                response_arg_str += f"{indent}\t{subfield_name}"
                
                if subfield.get("args") and len(list(subfield["args"].keys())) > 0:
                    sub_args_present = False
                    sub_arg_str = " ( "
                    for arg_name in subfield['args']:
                        arg = subfield['args'][arg_name]
                        
                        # CRITICAL: Match JavaScript logic exactly - DO NOT regenerate responseStr for subfield arguments
                        # JavaScript implementation (lines 901, 904) uses the existing arg.responseStr without modification
                        # The responseStr should have been set correctly during schema generation
                        # We only regenerate for NEW arguments discovered dynamically
                        
                        # NEW: Dynamic argument collection for subfield arguments too
                        if dynamic_operation_args is not None and isinstance(dynamic_operation_args, dict):
                            dynamic_operation_args[arg["varName"]] = arg
                        
                        # Only include arguments that are present in variables_obj and have values
                        if arg["varName"] in variables_obj and variables_obj[arg["varName"]] is not None and variables_obj[arg["varName"]] != "" and variables_obj[arg["varName"]] != [] and variables_obj[arg["varName"]] != {}:
                            sub_args_present = True
                            sub_arg_str += arg['responseStr'] + " "
                    sub_arg_str += " )"
                    if sub_args_present:
                        response_arg_str += sub_arg_str
                
                if subfield.get("type") and subfield['type'].get("definition") and (subfield['type']['definition'].get("fields") or subfield['type']['definition'].get('inputFields')):
                    response_arg_str += " {\n"
                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, subfield['type']['definition'], operation_name, indent + "\t\t", dynamic_operation_args, custom_client)
                    if subfield['type']['definition'].get('possibleTypes'):
                        possible_types = subfield['type']['definition']['possibleTypes']
                        # Handle both list and dict formats for possibleTypes
                        if isinstance(possible_types, list):
                            for possible_type in possible_types:
                                if isinstance(possible_type, dict) and 'name' in possible_type:
                                    # Only create fragment if there are actually fields to render
                                    if possible_type.get('fields') or possible_type.get('inputFields'):
                                        response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                        response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t", dynamic_operation_args, custom_client)
                                        
                                        # ENHANCED: Apply introspection expansion within fragments for fields without definitions
                                        if possible_type.get('fields'):
                                            for poss_field_name, poss_field in possible_type['fields'].items():
                                                if not poss_field.get('type', {}).get('definition'):
                                                    # This field might need introspection expansion
                                                    poss_field_type_name = None
                                                    if poss_field.get('type'):
                                                        poss_field_type = poss_field['type']
                                                        if poss_field_type.get('name'):
                                                            poss_field_type_name = poss_field_type['name']
                                                        # Drill through wrapped types
                                                        while poss_field_type and poss_field_type.get('ofType'):
                                                            poss_field_type = poss_field_type['ofType']
                                                            if poss_field_type and poss_field_type.get('name'):
                                                                poss_field_type_name = poss_field_type['name']
                                                    
                                                    if poss_field_type_name:
                                                        expansion = expandFieldWithIntrospection(poss_field['name'], poss_field_type_name, indent + "\t\t\t")
                                                        if expansion:
                                                            # Check if field was already added as bare field and remove it
                                                            lines = response_arg_str.split('\n')
                                                            filtered_lines = []
                                                            field_pattern = f"{indent}\t\t\t{poss_field['name']}"
                                                            for line in lines:
                                                                if not line.strip() == field_pattern.strip():
                                                                    filtered_lines.append(line)
                                                            response_arg_str = '\n'.join(filtered_lines)
                                                            # Add the expanded version
                                                            response_arg_str += f"{indent}\t\t\t{poss_field['name']} {{\n{expansion}{indent}\t\t\t}}\n"
                                        
                                        response_arg_str += f"{indent}\t\t}}\n"
                        elif isinstance(possible_types, dict):
                            for possible_type_name in possible_types:
                                possible_type = possible_types[possible_type_name]
                                # Only create fragment if there are actually fields to render
                                if possible_type.get('fields') or possible_type.get('inputFields'):
                                    response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t", dynamic_operation_args, custom_client)
                                    response_arg_str += f"{indent}\t\t}}\n"
                    response_arg_str += f"{indent}\t}}"
                elif subfield.get('type') and subfield['type'].get('definition') and subfield['type']['definition'].get('possibleTypes'):
                    response_arg_str += " {\n"
                    response_arg_str += f"{indent}\t\t__typename\n"
                    possible_types = subfield['type']['definition']['possibleTypes']
                    # Handle both list and dict formats for possibleTypes
                    if isinstance(possible_types, list):
                        for possible_type in possible_types:
                            if isinstance(possible_type, dict) and 'name' in possible_type:
                                # Only create fragment if there are actually fields to render
                                if possible_type.get('fields') or possible_type.get('inputFields'):
                                    response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t", dynamic_operation_args, custom_client)
                                    response_arg_str += f"{indent}\t\t}}\n"
                    elif isinstance(possible_types, dict):
                        for possible_type_name in possible_types:
                            possible_type = possible_types[possible_type_name]
                            # Only create fragment if there are actually fields to render
                            if possible_type.get('fields') or possible_type.get('inputFields'):
                                response_arg_str += f"{indent}\t\t... on {possible_type['name']} {{\n"
                                response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t\t", dynamic_operation_args, custom_client)
                                response_arg_str += f"{indent}\t\t}}\n"
                    response_arg_str += f"{indent}\t}}\n"
                # ENHANCED: Check if subfield needs introspection expansion even if it has basic definition
                # This handles fields within fragments that need expansion but don't have complete definitions
                subfield_needs_expansion = False
                subfield_type_name = None
                
                if subfield.get('type'):
                    subfield_type = subfield['type']
                    if subfield_type.get('name'):
                        subfield_type_name = subfield_type['name']
                    # Drill through wrapped types
                    while subfield_type and subfield_type.get('ofType'):
                        subfield_type = subfield_type['ofType']
                        if subfield_type and subfield_type.get('name'):
                            subfield_type_name = subfield_type['name']
                    
                    # Check if this field needs expansion based on introspection
                    if subfield_type_name:
                        try:
                            introspection_types = loadIntrospectionTypes()
                            if subfield_type_name in introspection_types:
                                type_def = introspection_types[subfield_type_name]
                                if type_def.get('kind') in ['OBJECT', 'INTERFACE', 'UNION']:
                                    # This field needs expansion - check if definition is insufficient
                                    has_complete_definition = (
                                        subfield.get("type") and subfield['type'].get('definition') and 
                                        (subfield['type']['definition'].get("fields") is not None or 
                                         subfield['type']['definition'].get('inputFields') is not None)
                                    )
                                    if not has_complete_definition:
                                        subfield_needs_expansion = True
                        except:
                            pass
                
                if subfield_needs_expansion and subfield_type_name:
                    expansion = expandFieldWithIntrospection(subfield['name'], subfield_type_name, indent + "\t")
                    if expansion:
                        response_arg_str += " {\n"
                        response_arg_str += expansion
                        response_arg_str += f"{indent}\t}}\n"
                    else:
                        response_arg_str += "\n"
                else:
                    response_arg_str += "\n"
                
            if field['type']['definition'].get('possibleTypes'):
                # Load introspection data for comprehensive union expansion
                introspection_types = loadIntrospectionTypes()
                
                possible_types = field['type']['definition']['possibleTypes']
                # Handle both list and dict formats for possibleTypes
                if isinstance(possible_types, list):
                    for possible_type in possible_types:
                        if isinstance(possible_type, dict) and 'name' in possible_type:
                            type_name = possible_type['name']
                            # Use introspection data to generate full union fragments
                            if type_name in introspection_types:
                                response_arg_str += f"{indent}\t... on {type_name} {{\n"
                                expanded_fragment = expandUnionFragment(type_name, introspection_types, indent)
                                if expanded_fragment:
                                    response_arg_str += expanded_fragment
                                response_arg_str += f"{indent}\t}}\n"
                elif isinstance(possible_types, dict):
                    for possible_type_name in possible_types:
                        possible_type = possible_types[possible_type_name]
                        type_name = possible_type['name'] if 'name' in possible_type else possible_type_name
                        # Use introspection data to generate full union fragments
                        if type_name in introspection_types:
                            response_arg_str += f"{indent}\t... on {type_name} {{\n"
                            expanded_fragment = expandUnionFragment(type_name, introspection_types, indent)
                            if expanded_fragment:
                                response_arg_str += expanded_fragment
                            response_arg_str += f"{indent}\t}}\n"
            response_arg_str += f"{indent}}}\n"
        
        # Handle inputFields
        elif field.get('type') and field['type'].get('definition') and field['type']['definition'].get('inputFields'):
            response_arg_str += " {\n"
            for subfield_name in field['type']['definition'].get('inputFields'):
                subfield = field['type']['definition']['inputFields'][subfield_name]
                # Enhanced aliasing logic for inputFields
                if (subfield.get('type') and subfield['type'].get('name') and 
                    cur_operation.get('fieldTypes', {}).get(subfield['type']['name']) and 
                    subfield.get('type', {}).get('kind') and 
                    'SCALAR' not in str(subfield['type']['kind'])):
                    subfield_name = f"{subfield['name']}{field['type']['definition']['name']}: {subfield['name']}"
                else:
                    subfield_name = subfield['name']
                response_arg_str += f"{indent}\t{subfield_name}"
                if subfield.get('type') and subfield['type'].get('definition') and (subfield['type']['definition'].get('fields') or subfield['type']['definition'].get('inputFields')):
                    response_arg_str += " {\n"
                    response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, subfield['type']['definition'], operation_name, indent + "\t\t", dynamic_operation_args, custom_client)
                    response_arg_str += f"{indent}\t}}\n"
            if field['type']['definition'].get('possibleTypes'):
                possible_types = field['type']['definition']['possibleTypes']
                # Handle both list and dict formats for possibleTypes
                if isinstance(possible_types, list):
                    for possible_type in possible_types:
                        if isinstance(possible_type, dict) and 'name' in possible_type:
                            response_arg_str += f"{indent}... on {possible_type['name']} {{\n"
                            if possible_type.get('fields') or possible_type.get('inputFields'):
                                response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t", dynamic_operation_args, custom_client)
                            response_arg_str += f"{indent}\t}}\n"
                elif isinstance(possible_types, dict):
                    for possible_type_name in possible_types:
                        possible_type = possible_types[possible_type_name]
                        response_arg_str += f"{indent}... on {possible_type['name']} {{\n"
                        if possible_type.get('fields') or possible_type.get('inputFields'):
                            response_arg_str = renderArgsAndFields(response_arg_str, variables_obj, cur_operation, possible_type, operation_name, indent + "\t\t", dynamic_operation_args, custom_client)
                        response_arg_str += f"{indent}\t}}\n"
            response_arg_str += f"{indent}}}\n"
        
        # Final check: any field that represents a complex type should be expanded if not already handled
        else:
            # Check if this field still needs introspection expansion
            if field_type_name_for_expansion:
                expansion = expandFieldWithIntrospection(field['name'], field_type_name_for_expansion, indent)
                if expansion:
                    response_arg_str += " {\n"
                    response_arg_str += expansion
                    response_arg_str += f"{indent}}}\n"
                else:
                    response_arg_str += "\n"
            else:
                response_arg_str += "\n"
    
    return response_arg_str


def expandUnionFragment(type_name, introspection_types, indent):
    """
    Helper function to expand a union fragment based on introspection data
    
    Args:
        type_name: Name of the union type to expand
        introspection_types: Introspection type definitions
        indent: Current indentation level
    
    Returns:
        String containing expanded fragment fields
    """
    if type_name not in introspection_types:
        return ""
        
    type_def = introspection_types[type_name]
    if not type_def.get('fields'):
        return ""
    
    result = ""
    for field in type_def['fields']:
        field_name = field['name']
        field_type = field.get('type', {})
        
        # Get core type
        current_type = field_type
        while current_type and current_type.get('ofType'):
            current_type = current_type['ofType']
        
        if current_type and current_type.get('kind') in ['SCALAR', 'ENUM']:
            result += f"{indent}\t\t{field_name}\n"
        else:
            result += f"{indent}\t\t{field_name}\n"
    
    return result


# Export commonly used functions for easy importing
__all__ = [
    'loadJSON',
    'renderCamelCase', 
    'validateArgs',
    'loadIntrospectionTypes',
    'getOfTypeNormalized',
    'isComplexType',
    'sanitizeFieldName',
    'generateGraphqlPayload',
    'postProcessBareComplexFields',
    'expandFieldWithIntrospection',
    'renderArgsAndFields',
    'expandUnionFragment'
]
