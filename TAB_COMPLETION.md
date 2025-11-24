# Tab Completion for catocli

Starting with version 3.0.42, catocli includes support for intelligent tab completion using `argcomplete`.

## What is Tab Completion?

Tab completion allows you to press the `Tab` key to:
- Auto-complete commands and subcommands
- See available options and arguments
- Speed up command entry and reduce typos

## Automatic Setup (Recommended)

When you install or upgrade catocli, the installer will automatically prompt you to enable tab completion:

```bash
pip install --upgrade catocli
```

You'll see a prompt like:

```
======================================================================
catocli Tab Completion Setup
======================================================================

Detected shell: bash
Config file: /Users/yourusername/.bash_profile

Would you like to enable tab completion for catocli?
This will add a line to your shell configuration file.

Enable tab completion? [Y/n]: 
```

Simply press Enter or type `y` to enable tab completion automatically.

## Manual Setup

If you skipped the automatic setup or want to configure it later, you can run:

```bash
python -m catocli.post_install
```

Or manually add the following to your shell configuration file:

### Bash (~/.bashrc or ~/.bash_profile)

```bash
eval "$(register-python-argcomplete catocli)"
```

### Zsh (~/.zshrc)

```bash
autoload -U bashcompinit
bashcompinit
eval "$(register-python-argcomplete catocli)"
```

### Fish (~/.config/fish/config.fish)

```bash
register-python-argcomplete --shell fish catocli | source
```

## Activating Tab Completion

After configuration:

1. **Restart your shell** or run:
   ```bash
   source ~/.bashrc  # or ~/.bash_profile, ~/.zshrc, etc.
   ```

2. **Test it** by typing:
   ```bash
   catocli <Tab>
   ```
   You should see available commands like `query`, `mutation`, `configure`, etc.

## Usage Examples

Once enabled, you can use tab completion like this:

```bash
# Complete main commands
catocli <Tab>
# Shows: configure  mutation  query  raw  version

# Complete subcommands
catocli query <Tab>
# Shows: accountMetrics  admins  appStats  entityLookup  events  ...

# Complete operation names
catocli query ent<Tab>
# Completes to: catocli query entityLookup
```

## Troubleshooting

### Tab completion not working?

1. **Check argcomplete is installed:**
   ```bash
   pip show argcomplete
   ```

2. **Verify the configuration line is in your shell config:**
   ```bash
   grep "register-python-argcomplete catocli" ~/.bashrc
   ```

3. **Make sure you've sourced your shell config:**
   ```bash
   source ~/.bashrc  # or your shell's config file
   ```

4. **Test argcomplete directly:**
   ```bash
   eval "$(register-python-argcomplete catocli)"
   catocli <Tab>
   ```

### Still having issues?

- Ensure you're using a supported shell (bash, zsh, or fish)
- Check that `catocli` is in your PATH: `which catocli`
- Try running the post-install script manually: `python -m catocli.post_install`

## Benefits

- **Faster command entry**: Type less, do more
- **Discover features**: See available commands without consulting documentation
- **Reduce errors**: Auto-completion prevents typos
- **Learn the CLI**: Tab completion shows you what's available at each level

## Disabling Tab Completion

If you want to disable tab completion, simply remove or comment out the line in your shell configuration file:

```bash
# eval "$(register-python-argcomplete catocli)"
```

Then restart your shell or source the config file.
