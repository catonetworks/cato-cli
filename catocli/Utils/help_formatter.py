#!/usr/bin/env python3
"""
Custom help formatter for catocli to improve subparser display
"""

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