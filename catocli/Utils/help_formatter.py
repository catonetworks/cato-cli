#!/usr/bin/env python3
"""
Universal Help Formatter for Cato CLI
Handles dynamic help generation across all command types and platforms
"""

import json
import os
import platform
import re
import sys
import shutil
from typing import Dict, List, Optional, Tuple


class PlatformInfo:
    """Information about the current platform and environment"""
    
    def __init__(self):
        self.platform = platform.system().lower()  # 'windows', 'darwin', 'linux'
        self.shell = self._detect_shell()
        self.installation_method = self._detect_installation()
        self.supports_multiline = self._supports_multiline()
    
    def _detect_shell(self) -> str:
        """Detect the current shell environment"""
        if self.platform == 'windows':
            # Check if running in PowerShell vs cmd
            if os.environ.get('PSModulePath'):
                return 'powershell'
            else:
                return 'cmd'
        else:
            # Unix-like systems
            shell = os.environ.get('SHELL', '/bin/bash')
            if 'zsh' in shell:
                return 'zsh'
            elif 'bash' in shell:
                return 'bash'
            elif 'fish' in shell:
                return 'fish'
            else:
                return 'bash'  # default
    
    def _detect_installation(self) -> str:
        """Detect how the CLI was installed"""
        try:
            if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
                return 'venv'
            elif shutil.which('pipx') and 'pipx' in sys.executable:
                return 'pipx'
            elif 'site-packages' in __file__:
                return 'pip'
            else:
                return 'development'
        except:
            return 'unknown'
    
    def _supports_multiline(self) -> bool:
        """Check if the current shell supports multi-line commands well"""
        if self.platform == 'windows' and self.shell == 'cmd':
            return False
        return True


class JSONExample:
    """Represents a JSON example that can be formatted for different platforms"""
    
    def __init__(self, json_data: str, command_template: str = "catocli {command} '{json}' -p"):
        self.json_data = json_data.strip()
        self.command_template = command_template
        self.parsed_json = self._parse_json()
    
    def _parse_json(self) -> Optional[dict]:
        """Parse the JSON data, returning None if invalid"""
        try:
            return json.loads(self.json_data)
        except (json.JSONDecodeError, ValueError):
            return None
    
    def format_for_platform(self, platform_info: PlatformInfo, command_name: str) -> List[str]:
        """Format the JSON example for the specific platform - show only the best format"""
        if platform_info.platform == 'windows':
            if platform_info.shell == 'powershell':
                # For PowerShell, show here-string format
                return self._format_powershell_comprehensive(command_name)
            else:
                # For cmd, use single-line with escaped quotes
                single_line = json.dumps(self.parsed_json) if self.parsed_json else self.json_data.replace('\n', ' ')
                escaped_json = single_line.replace('"', '\\"')
                # Extract flags from command template
                flags = self._extract_flags_from_template()
                return [f'catocli {command_name} "{escaped_json}" {flags}'.strip()]
        else:
            # For Unix-like systems, use multi-line with proper formatting
            return [self.command_template.format(command=command_name, json=self.json_data)]
    
    def _extract_flags_from_template(self) -> str:
        """Extract flags from the command template (everything after {json})""" 
        # Extract everything after '{json}' in the template
        if "'{json}'" in self.command_template:
            parts = self.command_template.split("'{json}'")
            if len(parts) > 1:
                return parts[1].strip()
        return ""
    
    def _format_powershell_comprehensive(self, command_name: str) -> List[str]:
        """Format PowerShell here-string example with proper quote escaping"""
        # Extract flags from command template
        flags = self._extract_flags_from_template()
        
        # Escape double quotes in JSON for PowerShell compatibility
        escaped_json = self.json_data.replace('"', '\\"')
        
        # Use here-string format which handles quotes better in PowerShell
        examples = [
            "# PowerShell (using here-string):",
            f"catocli {command_name} @'",
            escaped_json,
            f"'@ {flags}".strip() if flags else "'@"
        ]
        
        return examples
    
    def _convert_to_powershell_object(self) -> str:
        """Convert JSON to PowerShell object syntax"""
        if not self.parsed_json:
            return "# Unable to convert to PowerShell object"
        
        return self._json_to_powershell_recursive(self.parsed_json, 0)
    
    def _json_to_powershell_recursive(self, obj, indent_level: int) -> str:
        """Recursively convert JSON object to PowerShell syntax"""
        indent = "    " * indent_level
        
        if isinstance(obj, dict):
            if not obj:
                return "@{}"
            
            lines = ["$queryObject = @{"]
            for i, (key, value) in enumerate(obj.items()):
                value_str = self._json_to_powershell_recursive(value, indent_level + 1)
                if isinstance(value, (dict, list)):
                    lines.append(f"{indent}    {key} = {value_str}")
                else:
                    lines.append(f"{indent}    {key} = {value_str}")
                if i < len(obj) - 1:
                    lines[-1] += ";"
            lines.append(f"{indent}}}")
            return "\n".join(lines)
            
        elif isinstance(obj, list):
            if not obj:
                return "@()"
            
            if len(obj) == 1:
                # Single item array
                item_str = self._json_to_powershell_recursive(obj[0], indent_level)
                return f"@({item_str})"
            else:
                # Multi-item array
                lines = ["@("]
                for i, item in enumerate(obj):
                    item_str = self._json_to_powershell_recursive(item, indent_level + 1)
                    if isinstance(item, (dict, list)):
                        lines.append(f"{indent}    {item_str}")
                    else:
                        lines.append(f"{indent}    {item_str}")
                    if i < len(obj) - 1:
                        lines[-1] += ","
                lines.append(f"{indent})")
                return "\n".join(lines)
                
        elif isinstance(obj, str):
            # Use double quotes and escape internal quotes
            escaped_str = obj.replace('"', '"')
            return f'"{escaped_str}"'
        elif isinstance(obj, bool):
            return "$true" if obj else "$false"
        elif obj is None:
            return "$null"
        else:
            return str(obj)
    
    def _format_powershell(self, command_name: str) -> List[str]:
        """Legacy format for PowerShell (kept for compatibility)"""
        return self._format_powershell_comprehensive(command_name)
    
    def _format_cmd(self, command_name: str) -> List[str]:
        """Format for Windows Command Prompt"""
        # Convert to single line and use double quotes for cmd
        single_line = json.dumps(self.parsed_json) if self.parsed_json else self.json_data.replace('\n', ' ')
        examples = [
            "# Windows Command Prompt",
            f'catocli {command_name} "{single_line}" -p',
            "",
            "# Note: Consider using PowerShell for better JSON handling"
        ]
        return examples
    
    def _format_unix(self, platform_info: PlatformInfo, command_name: str) -> List[str]:
        """Format for Unix-like systems (macOS, Linux)"""
        examples = [
            f"# {platform_info.shell.upper()} (multi-line supported)",
            self.command_template.format(command=command_name, json=self.json_data),
            "",
            "# Alternative using heredoc:",
            f"catocli {command_name} \"$(cat << 'EOF'",
            self.json_data,
            "EOF",
            ")\" -p"
        ]
        return examples


class UniversalHelpFormatter:
    """Universal help formatter that works across all command types"""
    
    def __init__(self):
        self.platform_info = PlatformInfo()

    def format_help(self, command_path: str, help_source: str = "readme") -> str:
        """
        Generate help text for a command
        
        Args:
            command_path: Path like "query_siteLocation" or "scim"
            help_source: "readme", "description", or "auto"
        
        Returns:
            Formatted help string
        """
        command_name = command_path.replace('_', ' ')
        
        # Start building help output
        help_lines = ["\n"]
        
        # Extract examples based on source type
        readme_examples = []
        if help_source == "readme" or help_source == "auto":
            readme_examples = self._extract_from_readme(command_path)
            if readme_examples:
                for example in readme_examples:
                    # Check if this is a header or description line (not a command)
                    if example.startswith('###') or (example.startswith('-') and 'catocli' not in example):
                        # This is a header or description - preserve as-is
                        help_lines.append(example)
                        continue
                    
                    # Check if this example starts with a comment followed by a command
                    if example.startswith('#') and '\n' in example and 'catocli' in example:
                        # This is a comment followed by a command - extract both parts
                        lines = example.split('\n', 1)
                        if len(lines) == 2:
                            comment_line = lines[0]
                            command_part = lines[1]
                            
                            # Check if command has multi-line JSON and format appropriately
                            if "'{" in command_part and "}'" in command_part:
                                json_match = self._extract_json_from_example(command_part)
                                if json_match:
                                    # Extract command flags (everything after }')
                                    flags = ""
                                    if "}'" in command_part:
                                        flags_match = re.search(r"}'\s*(.*)$", command_part, re.MULTILINE)
                                        if flags_match:
                                            flags = flags_match.group(1).strip()
                                    
                                    # Create command template with flags
                                    if flags:
                                        command_template = f"catocli {{command}} '{{json}}' {flags}"
                                    else:
                                        command_template = "catocli {command} '{json}'"
                                    
                                    # Create JSONExample and apply platform-specific formatting
                                    json_example = JSONExample(json_match, command_template)
                                    formatted_commands = json_example.format_for_platform(self.platform_info, command_name)
                                    # Add comment first, then formatted commands
                                    help_lines.append(comment_line)
                                    help_lines.extend(formatted_commands)
                                else:
                                    # JSON extraction failed, format as simple command
                                    formatted_command = self._format_simple_command_for_platform(command_part)
                                    help_lines.append(comment_line)
                                    help_lines.append(formatted_command)
                            else:
                                # Simple command - apply platform formatting
                                formatted_command = self._format_simple_command_for_platform(command_part)
                                help_lines.append(comment_line)
                                help_lines.append(formatted_command)
                        else:
                            # Fallback - preserve as-is
                            help_lines.append(example)
                    elif 'catocli' in example and '{' in example and '}' in example:
                        # This is a catocli command with JSON - check if multi-line
                        if '\n' in example and "'{" in example:
                            # Multi-line JSON command
                            json_match = self._extract_json_from_example(example)
                            if json_match:
                                # Extract command flags (everything after }')
                                flags = ""
                                if "}'" in example:
                                    flags_match = re.search(r"}'\s*(.*)$", example, re.MULTILINE)
                                    if flags_match:
                                        flags = flags_match.group(1).strip()
                                
                                # Create command template with flags
                                if flags:
                                    command_template = f"catocli {{command}} '{{json}}' {flags}"
                                else:
                                    command_template = "catocli {command} '{json}'"
                                
                                # Create JSONExample and apply platform-specific formatting
                                json_example = JSONExample(json_match, command_template)
                                formatted_examples = json_example.format_for_platform(self.platform_info, command_name)
                                help_lines.extend(formatted_examples)
                            else:
                                # Preserve as-is if JSON extraction fails
                                help_lines.append(example)
                        else:
                            # Single-line command with JSON - format as simple command
                            formatted_example = self._format_simple_command_for_platform(example)
                            help_lines.append(formatted_example)
                    else:
                        # Simple command examples without JSON or description text - apply platform formatting
                        if 'catocli' in example:
                            formatted_example = self._format_simple_command_for_platform(example)
                            help_lines.append(formatted_example)
                        else:
                            # Not a command - preserve as-is (likely description text)
                            help_lines.append(example)
                    help_lines.append("")  # Add spacing between examples
        
        description_examples = []
        if help_source == "description" or (help_source == "auto" and not readme_examples):
            description_examples = self._extract_from_description(command_path)
            if description_examples:
                for example in description_examples:
                    if hasattr(example, 'format_for_platform'):
                        # This is a JSONExample object
                        help_lines.extend(example.format_for_platform(self.platform_info, command_name))
                    else:
                        # This is a string
                        help_lines.append(example)
                    help_lines.append("")
        
        # # If no examples found and this looks like a catolib command, generate schema-based examples
        # if not readme_examples and not description_examples and ('query_' in command_path or 'mutation_' in command_path):
        #     schema_examples = self._generate_schema_based_examples(command_path)
        #     if schema_examples:
        #         for example in schema_examples:
        #             help_lines.extend(example.format_for_platform(self.platform_info, command_name))
        #             help_lines.append("")
        
        # Add additional sections (timeFrame examples and Operation Arguments) if present in README
        additional_sections = self._extract_additional_sections(command_path)
        if additional_sections:
            help_lines.extend([""] + additional_sections)
        
        # Add platform-specific hints
        help_lines.extend(self._get_platform_hints())
        
        return "\n".join(help_lines)

    def _extract_from_readme(self, command_path: str) -> List[str]:
        """Extract catocli examples from README.md files, prioritizing Additional Examples section"""
        examples = []
        
        # Find README.md file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up from Utils to catocli
        readme_path = os.path.join(base_dir, "parsers", command_path, "README.md")
        
        # If not found, try custom path (for commands like query_eventsFeed)
        if not os.path.exists(readme_path):
            custom_readme_path = os.path.join(base_dir, "parsers", "custom", command_path, "README.md")
            if os.path.exists(custom_readme_path):
                readme_path = custom_readme_path
            else:
                return examples
        
        try:
            with open(readme_path, "r", encoding='utf-8') as f:
                content = f.read()
            
            command_name = command_path.replace('_', ' ')
            
            # Check if "## Advanced Usage" or "### Additional Examples" section exists
            has_advanced_usage = "## Advanced Usage" in content
            has_additional_examples = "### Additional Examples" in content
            
            # Define content to parse
            content_to_parse = content
            if has_advanced_usage:
                # Extract the Advanced Usage section (up to #### which is next level heading)
                advanced_pattern = r'## Advanced Usage\n(.*?)(?=\n####|\Z)'
                advanced_match = re.search(advanced_pattern, content, re.DOTALL)
                if advanced_match:
                    content_to_parse = advanced_match.group(1)
                    # Add a header for the examples
                    examples.append("### Examples")
                    # Don't extract intro text - it's redundant with the actual command examples
                    examples.append("")  # Add spacing
            elif has_additional_examples:
                # Fallback: Extract only the Additional Examples section
                additional_pattern = r'### Additional Examples\n(.*?)(?=\n####|\n## |\Z)'
                additional_match = re.search(additional_pattern, content, re.DOTALL)
                if additional_match:
                    content_to_parse = additional_match.group(1)
                    examples.append("### Examples")
                    # Don't extract intro text - it's redundant with the actual command examples
                    examples.append("")  # Add spacing
            
            # Extract catocli commands from markdown code blocks
            code_block_pattern = r'```(?:bash|shell|json)?\n(.*?)```'
            matches = re.findall(code_block_pattern, content_to_parse, re.DOTALL)
            
            for match in matches:
                # Split the match into individual lines and extract catocli commands with comments
                lines = match.split('\n')
                current_command = None
                current_comment = None
                in_multiline_json = False
                
                for i, line in enumerate(lines):
                    stripped_line = line.strip()
                    
                    # Check for comments that precede catocli commands
                    if stripped_line.startswith('# ') and not current_command:
                        current_comment = stripped_line
                    elif stripped_line.startswith('catocli') and command_name in stripped_line:
                        if current_command:
                            # Save previous multi-line command
                            examples.append(current_command)
                        
                        # Include comment if it exists
                        if current_comment:
                            current_command = current_comment + '\n' + stripped_line
                            current_comment = None  # Reset comment
                        else:
                            current_command = stripped_line
                            
                        # Check if this starts a multi-line JSON command (ends with '{' with optional flags before it)
                        if stripped_line.endswith("'{"):
                            in_multiline_json = True
                            # Keep the full command line including the opening bracket
                    elif in_multiline_json and current_command:
                        # We're in a multi-line JSON block - preserve exact formatting
                        if "}'" in stripped_line:
                            # End of multi-line JSON - include any flags after }'
                            current_command += '\n' + line
                            in_multiline_json = False
                            # Append the completed command
                            examples.append(current_command)
                            current_command = None
                            current_comment = None
                        else:
                            # Continue multi-line JSON with exact indentation
                            current_command += '\n' + line
                    elif current_command and not in_multiline_json and stripped_line and not stripped_line.startswith('catocli') and not stripped_line.startswith('# '):
                        # This could be continuation of a single-line command
                        current_command += ' ' + stripped_line
                    elif current_command and (stripped_line.startswith('catocli') or stripped_line == '' or i == len(lines) - 1):
                        # End of current command, start new one or end of block
                        if not in_multiline_json:
                            examples.append(current_command)
                            current_command = stripped_line if stripped_line.startswith('catocli') and command_name in stripped_line else None
                            # Reset comment when starting a new command
                            if not current_command:
                                current_comment = None
                    elif stripped_line == '':
                        # Reset comment on empty lines if no command is being processed
                        if not current_command:
                            current_comment = None
                
                # Don't forget the last command
                if current_command and not in_multiline_json:
                    examples.append(current_command)
            
            # If no Additional Examples section was found, also look for inline catocli commands (in backticks)
            if not has_additional_examples:
                inline_pattern = r'`(catocli[^`]+)`'
                inline_matches = re.findall(inline_pattern, content)
                
                for cmd in inline_matches:
                    if command_name in cmd and cmd not in examples:
                        examples.append(cmd)
                    
        except Exception as e:
            print(f"Warning: Could not parse README for {command_path}: {e}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_examples = []
        for example in examples:
            if example not in seen:
                seen.add(example)
                unique_examples.append(example)
        
        return unique_examples
    
    def _format_simple_command_for_platform(self, example: str) -> str:
        """Format a simple command example for the current platform"""
        # If it's already a comment or doesn't contain catocli command, return as-is
        if example.startswith('#') or 'catocli' not in example:
            return example
        
        # For Windows, we need to adjust command syntax
        if self.platform_info.platform == 'windows':
            if self.platform_info.shell == 'powershell':
                # PowerShell-specific adjustments
                # Convert Unix-style command substitution to PowerShell equivalent
                if '$(cat' in example:
                    # Handle different $(cat) variations
                    import re
                    # Pattern for $(cat file.json) or $(cat < file.json)
                    cat_pattern = r'\$\(cat\s*<?\s*([^\)]+)\)'
                    def replace_cat(match):
                        filename = match.group(1).strip()
                        return f'(Get-Content {filename} -Raw)'
                    example = re.sub(cat_pattern, replace_cat, example)
                # Handle quotes - PowerShell prefers double quotes for JSON strings
                # But for simple parameter examples, keep single quotes for strings
                return example
            elif self.platform_info.shell == 'cmd':
                # CMD-specific adjustments - CMD has many limitations
                if '$(cat ' in example:
                    return "# CMD: Save JSON to file first, then use the file path"
                elif len(example) > 100:
                    return "# CMD: Use PowerShell for complex commands - CMD has line length limits"
                # For CMD, convert single quotes to double quotes for JSON
                if "'{" in example and "}'" in example:
                    example = example.replace("'{", '"{')
                    example = example.replace("}'", '}"')
                    # Escape internal double quotes
                    # This is complex, so provide a simplification
                    return "# CMD: " + example + " (escape internal quotes as needed)"
        
        return example
    
    def _extract_json_from_example(self, example: str) -> str:
        """Extract JSON data from a catocli command example"""
        try:
            # Look for multi-line JSON first (between '{ and }' with potential flags after)
            # This pattern captures everything between '{ and }' (non-greedy)
            multiline_pattern = r"'(\{[\s\S]*?\})'(?:\s+[-\w])*"
            match = re.search(multiline_pattern, example)
            if match:
                json_str = match.group(1)
                # Validate it's JSON by trying to parse it
                json.loads(json_str)
                return json_str
            
            # Fallback to simple single-line JSON in single quotes
            single_quote_pattern = r"catocli[^']*'([^']+)'"
            match = re.search(single_quote_pattern, example)
            if match:
                json_str = match.group(1)
                # Validate it's JSON by trying to parse it
                json.loads(json_str)
                return json_str
                
        except (json.JSONDecodeError, AttributeError):
            pass
        
        return None
    
    def _extract_additional_sections(self, command_path: str) -> List[str]:
        """Extract timeFrame examples and Operation Arguments sections from README"""
        sections = []
        
        # Find README.md file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up from Utils to catocli
        readme_path = os.path.join(base_dir, "parsers", command_path, "README.md")
        
        # If not found, try custom path (for commands like query_eventsFeed)
        if not os.path.exists(readme_path):
            custom_readme_path = os.path.join(base_dir, "parsers", "custom", command_path, "README.md")
            if os.path.exists(custom_readme_path):
                readme_path = custom_readme_path
            else:
                return sections
        
        try:
            with open(readme_path, "r", encoding='utf-8') as f:
                content = f.read()
            
            # Extract TimeFrame Parameter Examples section
            timeframe_section_pattern = r'#### TimeFrame Parameter Examples.*?(?=\n####|\Z)'
            timeframe_match = re.search(timeframe_section_pattern, content, re.DOTALL)
            if timeframe_match:
                sections.append(timeframe_match.group(0).strip())
            
            # Extract Operation Arguments section  
            op_args_section_pattern = r'#### Operation Arguments for [^\n]*####.*?(?=\n####|\Z)'
            op_args_match = re.search(op_args_section_pattern, content, re.DOTALL)
            if op_args_match:
                sections.append(op_args_match.group(0).strip())
                
        except Exception as e:
            # If anything fails, return what we have so far
            pass
        
        return sections
    
    def _extract_from_description(self, command_path: str) -> List[str]:
        """Extract command examples from argparse description text (like SCIM)"""
        examples = []
        
        # This would need to be integrated with the parser definitions
        # For now, return empty list - this can be expanded later
        return examples
    
    def _get_platform_hints(self) -> List[str]:
        """Get platform-specific hints and tips"""
        hints = []
        
        if self.platform_info.platform == 'windows':
            if self.platform_info.shell == 'cmd':
                hints.extend([
                    "",
                    "NOTE: Command Prompt doesn't support multi-line commands well.",
                    "Consider using PowerShell for better JSON handling."
                ])
            elif self.platform_info.shell == 'powershell':
                hints.extend([
                    "",
                    "POWERSHELL JSON TIPS:",
                    "• Here-strings preserve JSON formatting and automatically escape quotes",
                    "• If you get 'Invalid JSON' errors, ensure quotes within JSON are escaped"
                ])
        else:
            hints.extend([
                "",
                "TIP: Multi-line JSON is fully supported in Unix shells."
            ])
        
        if self.platform_info.installation_method == 'pipx':
            hints.extend([
                "",
                "Installed via pipx - ensure proper UTF-8 encoding for JSON with special characters."
            ])
        
        return hints


# Global instance for easy access
_formatter = None

def get_universal_help(command_path: str, help_source: str = "auto") -> str:
    """
    Get universal help for a command
    
    Args:
        command_path: Command path like "query_siteLocation"
        help_source: "readme", "description", or "auto"
    
    Returns:
        Formatted help string
    """
    global _formatter
    if _formatter is None:
        _formatter = UniversalHelpFormatter()
    
    return _formatter.format_help(command_path, help_source)


def format_json_examples_for_platform(examples: List[str], command_name: str) -> str:
    """
    Format a list of JSON examples for the current platform
    
    Args:
        examples: List of JSON strings
        command_name: Command name for the examples
    
    Returns:
        Formatted help string
    """
    global _formatter
    if _formatter is None:
        _formatter = UniversalHelpFormatter()
    
    formatted_examples = []
    for json_str in examples:
        example = JSONExample(json_str)
        formatted_examples.extend(example.format_for_platform(_formatter.platform_info, command_name))
        formatted_examples.append("")  # Spacing between examples
    
    return "\n".join(formatted_examples)

import argparse
import re


class CustomSubparserHelpFormatter(argparse.HelpFormatter):
    """
    Custom formatter that improves the display of subparser choices.
    
    Removes the redundant first list of commands and only shows commands with descriptions,
    alphabetically sorted.
    """
    
    def _format_action(self, action):
        """Override the action formatting to handle subparser choices better"""
        # Get the normal formatted action
        result = super()._format_action(action)
        
        # If this is a subparsers action with choices, improve the formatting
        if hasattr(action, 'choices') and action.choices:
            # Pattern to match and remove the first choices list (without descriptions)
            # This matches patterns like:
            #   {
            #     command1
            #     command2
            #     ...
            #   }
            # or inline {command1,command2,...}
            choices_pattern = r'\{[^}]*\}|\n\s+\n(\s{4}[^\s].*\n)*\s+\n'
            
            # Also match the more complex multi-line format that argparse generates
            multiline_choices_pattern = r'\n\s*\n(\s{4}[^\s][^\n]*\n)+\s*\n'
            
            # Remove the first occurrence of choices list (the one without descriptions)
            if re.search(multiline_choices_pattern, result):
                # Find the first multiline choices block and remove it
                result = re.sub(multiline_choices_pattern, '\n', result, count=1)
            elif re.search(choices_pattern, result):
                result = re.sub(choices_pattern, '', result, count=1)
            
            # Now alphabetize the commands with descriptions
            # Find all command entries with descriptions (lines starting with 4+ spaces and containing command names)
            command_lines_pattern = r'(    \w+\s+.*\n(?:\s{20,}.*\n)*)+'
            match = re.search(command_lines_pattern, result)
            if match:
                commands_section = match.group(0)
                
                # Split into individual command entries
                individual_commands = []
                current_command = ""
                
                for line in commands_section.split('\n'):
                    if line.strip() == "":
                        continue
                    # If line starts with exactly 4 spaces, it's a new command
                    if line.startswith('    ') and not line.startswith('     '):
                        if current_command:
                            individual_commands.append(current_command)
                        current_command = line
                    else:
                        # This is a continuation line for the current command
                        current_command += '\n' + line
                
                # Add the last command
                if current_command:
                    individual_commands.append(current_command)
                
                # Sort commands alphabetically by command name (first word after the spaces)
                def get_command_name(cmd_text):
                    # Extract command name from "    commandName    description"
                    match = re.match(r'\s+(\w+)', cmd_text)
                    return match.group(1) if match else ''
                
                individual_commands.sort(key=get_command_name)
                
                # Reconstruct the sorted commands section
                sorted_commands_section = '\n'.join(individual_commands) + '\n'
                
                # Replace the original commands section with the sorted one
                result = result.replace(commands_section, sorted_commands_section)
        
        return result


def get_custom_formatter():
    """
    Factory function to get the custom formatter class.
    This allows for easy import and use in generated code.
    """
    return CustomSubparserHelpFormatter