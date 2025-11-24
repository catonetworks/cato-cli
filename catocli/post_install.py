#!/usr/bin/env python
"""Post-install script to setup argcomplete for catocli."""

import os
import sys
import subprocess


def get_shell_config_file():
    """Detect the user's shell and return the appropriate config file."""
    shell = os.environ.get('SHELL', '')
    home = os.path.expanduser('~')
    
    if 'zsh' in shell:
        return os.path.join(home, '.zshrc'), 'zsh'
    elif 'bash' in shell:
        # Check for bash_profile first, then bashrc
        bash_profile = os.path.join(home, '.bash_profile')
        bashrc = os.path.join(home, '.bashrc')
        
        # On macOS, .bash_profile is typically used
        if sys.platform == 'darwin':
            if os.path.exists(bash_profile):
                return bash_profile, 'bash'
            return bash_profile, 'bash'  # Create it if it doesn't exist
        else:
            # On Linux, prefer .bashrc
            if os.path.exists(bashrc):
                return bashrc, 'bash'
            return bashrc, 'bash'
    elif 'fish' in shell:
        fish_dir = os.path.join(home, '.config', 'fish')
        return os.path.join(fish_dir, 'config.fish'), 'fish'
    
    return None, None


def is_already_configured(config_file):
    """Check if argcomplete is already configured in the shell config file."""
    if not os.path.exists(config_file):
        return False
    
    try:
        with open(config_file, 'r') as f:
            content = f.read()
            return 'register-python-argcomplete catocli' in content
    except IOError:
        return False


def add_to_shell_config(config_file, shell_type):
    """Add argcomplete configuration to the shell config file."""
    if shell_type == 'zsh':
        lines = [
            '\n# Enable catocli tab completion (added by catocli installer)',
            'autoload -U bashcompinit',
            'bashcompinit',
            'eval "$(register-python-argcomplete catocli)"',
            ''
        ]
    elif shell_type == 'fish':
        lines = [
            '\n# Enable catocli tab completion (added by catocli installer)',
            'register-python-argcomplete --shell fish catocli | source',
            ''
        ]
    else:  # bash
        lines = [
            '\n# Enable catocli tab completion (added by catocli installer)',
            'eval "$(register-python-argcomplete catocli)"',
            ''
        ]
    
    try:
        # Create directory if needed (for fish)
        config_dir = os.path.dirname(config_file)
        if config_dir and not os.path.exists(config_dir):
            os.makedirs(config_dir, exist_ok=True)
        
        with open(config_file, 'a') as f:
            f.write('\n'.join(lines))
        return True
    except IOError as e:
        print(f"Error writing to {config_file}: {e}")
        return False


def setup_argcomplete():
    """Main function to setup argcomplete after installation."""
    print("\n" + "=" * 70)
    print("catocli Tab Completion Setup")
    print("=" * 70)
    
    config_file, shell_type = get_shell_config_file()
    
    if not config_file or not shell_type:
        print("\nCouldn't detect your shell automatically.")
        print("\nTo enable tab completion manually, add this to your shell config:")
        print("  eval \"$(register-python-argcomplete catocli)\"")
        print("=" * 70 + "\n")
        return
    
    if is_already_configured(config_file):
        print(f"\nTab completion is already configured in {config_file}")
        print("=" * 70 + "\n")
        return
    
    print(f"\nDetected shell: {shell_type}")
    print(f"Config file: {config_file}")
    print("\nWould you like to enable tab completion for catocli?")
    print("This will add a line to your shell configuration file.")
    
    # Check if running in non-interactive mode
    if not sys.stdin.isatty():
        print("\nNon-interactive mode detected. Skipping automatic setup.")
        print("\nTo enable tab completion manually, run:")
        print(f"  echo 'eval \"$(register-python-argcomplete catocli)\"' >> {config_file}")
        print("=" * 70 + "\n")
        return
    
    try:
        response = input("\nEnable tab completion? [Y/n]: ").strip().lower()
        
        if response in ['', 'y', 'yes']:
            if add_to_shell_config(config_file, shell_type):
                print(f"\n✓ Tab completion configured in {config_file}")
                print("\nTo activate in your current shell, run:")
                if shell_type == 'zsh':
                    print("  autoload -U bashcompinit && bashcompinit")
                    print("  eval \"$(register-python-argcomplete catocli)\"")
                elif shell_type == 'fish':
                    print("  register-python-argcomplete --shell fish catocli | source")
                else:
                    print("  eval \"$(register-python-argcomplete catocli)\"")
                print("\nOr restart your shell for changes to take effect.")
            else:
                print("\n✗ Failed to configure tab completion automatically.")
                print("\nTo enable manually, add this to your shell config:")
                print("  eval \"$(register-python-argcomplete catocli)\"")
        else:
            print("\nSkipped tab completion setup.")
            print("\nTo enable later, add this to your shell config:")
            print("  eval \"$(register-python-argcomplete catocli)\"")
    
    except (KeyboardInterrupt, EOFError):
        print("\n\nSkipped tab completion setup.")
        print("\nTo enable later, add this to your shell config:")
        print("  eval \"$(register-python-argcomplete catocli)\"")
    
    print("=" * 70 + "\n")


if __name__ == '__main__':
    setup_argcomplete()
