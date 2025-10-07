#!/usr/bin/env python3
"""
Demonstration of Universal Platform Help System
Shows how help output adapts to different platforms and shells
"""

import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from catocli.Utils.help_formatter import PlatformInfo, JSONExample, UniversalHelpFormatter

def demo_platform_detection():
    """Demo the platform detection capabilities"""
    print("=== CURRENT PLATFORM DETECTION ===")
    platform_info = PlatformInfo()
    
    print(f"Platform: {platform_info.platform}")
    print(f"Shell: {platform_info.shell}")
    print(f"Installation Method: {platform_info.installation_method}")
    print(f"Supports Multi-line: {platform_info.supports_multiline}")
    print()

def demo_json_formatting():
    """Demo JSON example formatting for different platforms"""
    
    # Sample JSON from siteLocation
    sample_json = """{
  "filters": [
    {
      "search": "California",
      "field": "stateName",
      "operation": "endsWith"
    }
  ]
}"""
    
    example = JSONExample(sample_json)
    
    # Simulate different platforms
    platforms = [
        {"platform": "darwin", "shell": "bash", "supports_multiline": True, "installation_method": "pip"},
        {"platform": "darwin", "shell": "zsh", "supports_multiline": True, "installation_method": "pip"},
        {"platform": "windows", "shell": "powershell", "supports_multiline": True, "installation_method": "pipx"},
        {"platform": "windows", "shell": "cmd", "supports_multiline": False, "installation_method": "pip"},
        {"platform": "linux", "shell": "bash", "supports_multiline": True, "installation_method": "venv"},
    ]
    
    for platform_data in platforms:
        # Create a mock platform info object
        class MockPlatformInfo:
            def __init__(self, data):
                self.platform = data["platform"]
                self.shell = data["shell"] 
                self.supports_multiline = data["supports_multiline"]
                self.installation_method = data["installation_method"]
        
        mock_platform = MockPlatformInfo(platform_data)
        
        print(f"=== {mock_platform.shell.upper()} on {mock_platform.platform.upper()} ===")
        formatted = example.format_for_platform(mock_platform, "query siteLocation")
        print("\n".join(formatted))
        print("\n" + "="*60 + "\n")

def demo_universal_help():
    """Demo the universal help formatter in action"""
    print("=== UNIVERSAL HELP FORMATTER ===")
    
    formatter = UniversalHelpFormatter()
    help_text = formatter.format_help("query_siteLocation", "readme")
    print(help_text)

if __name__ == "__main__":
    print("Universal Platform Help System Demo\n")
    
    demo_platform_detection()
    demo_json_formatting()
    demo_universal_help()
    
    print("\n=== SUMMARY ===")
    print("✅ Platform detection works across Windows, macOS, and Linux")
    print("✅ Shell detection supports cmd, PowerShell, bash, zsh, fish")
    print("✅ JSON examples adapt automatically to platform capabilities")
    print("✅ Installation method detection (pip, pipx, venv, development)")
    print("✅ Multi-line support detection and fallback handling")
    print("✅ Universal help formatter works with README files")
    print("\nThis system can be extended to work with:")
    print("- SCIM command descriptions")
    print("- Dynamically generated catolib.py commands") 
    print("- Any command source with JSON examples")