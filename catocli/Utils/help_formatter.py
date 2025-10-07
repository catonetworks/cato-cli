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
                # For PowerShell, prefer multi-line
                return [self.command_template.format(command=command_name, json=self.json_data)]
            else:
                # For cmd, use single-line with double quotes
                single_line = json.dumps(self.parsed_json) if self.parsed_json else self.json_data.replace('\n', ' ')
                return [f'catocli {command_name} "{single_line}" -p']
        else:
            # For Unix-like systems, use multi-line
            return [self.command_template.format(command=command_name, json=self.json_data)]
    
    def _format_powershell(self, command_name: str) -> List[str]:
        """Format for PowerShell"""
        examples = [
            "# PowerShell (recommended)",
            self.command_template.format(command=command_name, json=self.json_data),
            "",
            "# PowerShell alternative using here-string:",
            "$json = @'",
            self.json_data,
            "'@",
            f"catocli {command_name} $json -p"
        ]
        return examples
    
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
        help_lines = [
            "\nEXAMPLES:"
        ]
        
        # Extract examples based on source type
        readme_examples = []
        if help_source == "readme" or help_source == "auto":
            readme_examples = self._extract_from_readme(command_path)
            if readme_examples:
                for example in readme_examples:
                    help_lines.extend(example.format_for_platform(self.platform_info, command_name))
                    help_lines.append("")  # Add spacing between examples
        
        description_examples = []
        if help_source == "description" or (help_source == "auto" and not readme_examples):
            description_examples = self._extract_from_description(command_path)
            if description_examples:
                for example in description_examples:
                    help_lines.extend(example.format_for_platform(self.platform_info, command_name))
                    help_lines.append("")
        
        # If no examples found and this looks like a catolib command, generate schema-based examples
        if not readme_examples and not description_examples and ('query_' in command_path or 'mutation_' in command_path):
            schema_examples = self._generate_schema_based_examples(command_path)
            if schema_examples:
                for example in schema_examples:
                    help_lines.extend(example.format_for_platform(self.platform_info, command_name))
                    help_lines.append("")
        
        # Add platform-specific hints
        help_lines.extend(self._get_platform_hints())
        
        return "\n".join(help_lines)
    
    def _extract_from_readme(self, command_path: str) -> List[JSONExample]:
        """Extract JSON examples from README.md files"""
        examples = []
        
        # Find README.md file
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up from Utils to catocli
        readme_path = os.path.join(base_dir, "parsers", command_path, "README.md")
        
        if not os.path.exists(readme_path):
            return examples
        
        try:
            with open(readme_path, "r", encoding='utf-8') as f:
                content = f.read()
            
            # Extract JSON from markdown code blocks
            code_block_pattern = r'```(?:bash|shell|json)?\n(.*?)```'
            matches = re.findall(code_block_pattern, content, re.DOTALL)
            
            for match in matches:
                if 'catocli' in match and command_path.replace('_', ' ') in match:
                    # Extract JSON from the command - handle multi-line JSON
                    json_match = re.search(r"'({.*?})'\s*-p", match, re.DOTALL)
                    if json_match:
                        json_content = json_match.group(1)
                        examples.append(JSONExample(json_content))
            
            # Also look for inline examples
            inline_pattern = r'catocli.*?\'({[^}]*})\'.*?-p'
            inline_matches = re.findall(inline_pattern, content, re.DOTALL)
            
            for json_content in inline_matches:
                if json_content not in [ex.json_data for ex in examples]:  # Avoid duplicates
                    examples.append(JSONExample(json_content))
                    
        except Exception as e:
            print(f"Warning: Could not parse README for {command_path}: {e}")
        
        return examples
    
    def _extract_from_description(self, command_path: str) -> List[JSONExample]:
        """Extract JSON examples from argparse description text (like SCIM)"""
        examples = []
        
        # This would need to be integrated with the parser definitions
        # For now, return empty list - this can be expanded later
        return examples
    
    def _generate_schema_based_examples(self, command_path: str) -> List[JSONExample]:
        """Generate examples for catolib.py generated commands based on GraphQL schema"""
        examples = []
        
        # Parse command path to get operation type and name
        parts = command_path.split('_')
        if len(parts) < 2:
            return examples
            
        operation_type = parts[0]  # 'query' or 'mutation'
        operation_name = '_'.join(parts[1:])  # e.g., 'xdr_stories'
        
        # Generate a basic example based on common patterns
        if operation_type == 'query':
            # Most queries need at least accountID
            basic_example = {
                "accountID": "<your_account_id>"
            }
            
            # Add common parameters based on operation name
            if 'events' in operation_name or 'stories' in operation_name:
                basic_example.update({
                    "timeFrame": "LAST_24_HOURS",
                    "first": 100
                })
            elif 'sites' in operation_name:
                basic_example.update({
                    "siteType": "BRANCH"
                })
            elif 'accounts' in operation_name:
                basic_example.update({
                    "first": 50
                })
        else:
            # Mutation example
            basic_example = {
                "accountID": "<your_account_id>",
                "input": {
                    "# Add required fields here": "<value>"
                }
            }
        
        # Create formatted JSON string
        json_str = json.dumps(basic_example, indent=2)
        examples.append(JSONExample(json_str))
        
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
                    "TIP: PowerShell supports multi-line commands and here-strings (@'...'@)."
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