# Terraform Rules Export and Import Guide

This guide covers exporting Cato Network policy rules and importing them into Terraform for Infrastructure as Code (IaC) management.

## Overview

CatoCLI provides functionality to:
- **Export** policy rules from your Cato account to JSON format
- **Import** policy rules into Terraform state for management

This enables you to migrate existing Cato configurations into Terraform, allowing version control, automated deployments, and IaC best practices.

## Supported Policy Types

| Policy Type | Export Command | Import Command | Resource Type | Bulk Terraform Module
|-------------|---------------|----------------|---------------|---------------|
| Internet Firewall | `export if_rules` | `if_rules_to_tf` | [cato_if_rule](https://registry.terraform.io/providers/catonetworks/cato/latest/docs/resources/if_rule) | [bulk-if-rules](https://registry.terraform.io/modules/catonetworks/bulk-if-rules/cato/latest) |
| WAN Firewall | `export wf_rules` | `wf_rules_to_tf` | [cato_wf_rule](https://registry.terraform.io/providers/catonetworks/cato/latest/docs/resources/wf_rule) | [bulk-wf-rules](https://registry.terraform.io/modules/catonetworks/bulk-wf-rules/cato/latest) |
| TLS Inspection | `export tls_rules` | `tls_rules_to_tf` | [cato_tls_rule](https://registry.terraform.io/providers/catonetworks/cato/latest/docs/resources/tls_rule) | [bulk-tls-rules](https://registry.terraform.io/modules/catonetworks/bulk-tls-rules/cato/latest) |
| WAN Network | `export wnw_rules` | `wnw_rules_to_tf` | [cato_wnw_rule](https://registry.terraform.io/providers/catonetworks/cato/latest/docs/resources/wnw_rule) | [bulk-wnw-rules](https://registry.terraform.io/modules/catonetworks/bulk-wnw-rules/cato/latest) |

## Prerequisites

- CatoCLI installed and configured (see main [README.md](../README.md))
- Valid Cato API token with appropriate permissions
- Terraform installed (for import operations)
- Cato Terraform provider configured

## Export Policy Rules

### Export Internet Firewall Rules

Export Internet Firewall policy to JSON:

```bash
catocli export if_rules -o internet_firewall_rules.json
```

### Export WAN Firewall Rules

Export WAN Firewall policy to JSON:

```bash
catocli export wf_rules -o wan_firewall_rules.json
```

### Export TLS Inspection Rules

Export TLS Inspection policy to JSON:

```bash
catocli export tls_rules -o tls_inspection_rules.json
```

### Export WAN Network Rules

Export WAN Network policy to JSON:

```bash
catocli export wnw_rules -o wan_network_rules.json
```

### Export Options

- `-o, --output` - Specify output JSON file path (required)
- `-p, --profile` - Use a specific CatoCLI profile
- `--account-id` - Override account ID from profile

### Example with Profile

```bash
# Use a specific profile for export
catocli export wnw_rules -o rules.json -p production

# Override account ID
catocli export wnw_rules -o rules.json --account-id 12345
```

## Import Rules to Terraform

Import operations require the exported JSON file and assume you have Terraform configured with the Cato provider.

### Import Internet Firewall Rules

```bash
catocli import if_rules_to_tf \
  -f internet_firewall_rules.json \
  -r cato-ztna_internet_firewall_policy.my_policy
```

### Import WAN Firewall Rules

```bash
catocli import wf_rules_to_tf \
  -f wan_firewall_rules.json \
  -r cato-ztna_wan_firewall_policy.my_policy
```

### Import WAN Network Rules

```bash
catocli import wnw_rules_to_tf \
  -f wan_network_rules.json \
  -r cato-ztna_wan_network_policy.my_policy
```

### Import Options

- `-f, --file` - Path to exported JSON file (required)
- `-r, --resource` - Terraform resource name in format `resource_type.resource_name` (required)
- `-p, --profile` - Use a specific CatoCLI profile
- `--account-id` - Override account ID from profile

### Import Process

The import process performs the following steps:

1. **Load JSON Data** - Reads the exported policy JSON file
2. **Import Sections** - Creates Terraform imports for policy sections
3. **Import Rules** - Batch imports individual rules (10 rules per batch for optimal performance)
4. **Verification** - Validates the import completed successfully

## Complete Workflow Example

### Step 1: Export Current Configuration

```bash
# Export all policy types
catocli export if_rules -o exports/internet_firewall.json
catocli export wf_rules -o exports/wan_firewall.json
catocli export tls_rules -o exports/tls_inspection.json
catocli export wnw_rules -o exports/wan_network.json
```

### Step 2: Review Exported JSON

```bash
# Review the exported structure
cat exports/wan_network.json | jq .
```

### Step 3: Create Terraform Configuration

Create a Terraform configuration file that defines the policy resources:

```hcl
# main.tf
terraform {
  required_providers {
    cato-ztna = {
      source  = "catonetworks/cato-ztna"
      version = "~> 1.0"
    }
  }
}

provider "cato-ztna" {
  baseurl    = "https://api.catonetworks.com/api/v1/graphql2"
  token      = var.cato_token
  account_id = var.account_id
}

resource "cato-ztna_wan_network_policy" "my_policy" {
  # Configuration will be imported
}
```

### Step 4: Initialize Terraform

```bash
terraform init
```

### Step 5: Import Policy State

```bash
# Import the WAN Network policy
catocli import wnw_rules_to_tf \
  -f exports/wan_network.json \
  -r cato-ztna_wan_network_policy.my_policy
```

### Step 6: Generate Terraform Configuration

```bash
# Generate configuration from imported state
terraform show -no-color > imported_config.tf
```

### Step 7: Verify Import

```bash
# Plan should show no changes if import successful
terraform plan
```

## Exported JSON Structure

### Internet Firewall & WAN Firewall

```json
{
  "policy": {
    "sections": [
      {
        "name": "Section Name",
        "rules": [
          {
            "name": "Rule Name",
            "enabled": true,
            "action": "ALLOW",
            "source": { ... },
            "destination": { ... },
            ...
          }
        ]
      }
    ]
  }
}
```

### WAN Network Policy

```json
{
  "policy": {
    "sections": [
      {
        "name": "Section Name",
        "rules": [
          {
            "name": "Rule Name",
            "enabled": true,
            "source": { ... },
            "destination": { ... },
            "connection": { ... },
            ...
          }
        ]
      }
    ]
  }
}
```

## Batch Import Performance

The import process uses batching to optimize performance:

- **Sections**: Imported individually
- **Rules**: Imported in batches of 10 rules
- **Progress Tracking**: Real-time feedback during import

### Example Output

```
Starting import for WAN Network rules...
Processing section: Corporate Network
  Importing rules batch 1/3 (10 rules)...
  Importing rules batch 2/3 (10 rules)...
  Importing rules batch 3/3 (5 rules)...
Processing section: Guest Network
  Importing rules batch 1/1 (8 rules)...
Import completed successfully!
```

## Troubleshooting

### Export Issues

**Problem**: Export returns empty policy
```bash
# Verify account access and permissions
catocli configure show
```

**Problem**: Authentication error
```bash
# Reconfigure profile
catocli configure set
```

### Import Issues

**Problem**: Terraform not found
```bash
# Verify Terraform installation
terraform version
```

**Problem**: Resource already managed
```bash
# Remove from state if needed
terraform state rm cato-ztna_wan_network_policy.my_policy
# Then retry import
```

**Problem**: Import fails on specific rules
```bash
# Check Terraform provider version
terraform version
# Review JSON structure for issues
jq . exports/wan_network.json
```

## Best Practices

### 1. Version Control
```bash
# Create a dedicated directory for exports
mkdir -p terraform/imports/$(date +%Y%m%d)
catocli export wnw_rules -o terraform/imports/$(date +%Y%m%d)/wan_network.json

# Commit to version control
git add terraform/imports/
git commit -m "Export WAN Network policy - $(date +%Y%m%d)"
```

### 2. Backup Before Import
```bash
# Backup Terraform state before import
cp terraform.tfstate terraform.tfstate.backup.$(date +%Y%m%d_%H%M%S)
```

### 3. Incremental Migration
```bash
# Import one policy type at a time
catocli import wnw_rules_to_tf -f wan_network.json -r cato-ztna_wan_network_policy.policy1
terraform plan  # Verify
terraform apply  # Apply if needed

# Then proceed to next policy type
catocli import wf_rules_to_tf -f wan_firewall.json -r cato-ztna_wan_firewall_policy.policy2
```

### 4. Use Separate Workspaces
```bash
# Create workspace for imports
terraform workspace new imports
terraform workspace select imports

# Perform imports
catocli import wnw_rules_to_tf -f wan_network.json -r cato-ztna_wan_network_policy.my_policy
```

### 5. Validate After Import
```bash
# After import, ensure plan shows no changes
terraform plan -detailed-exitcode
# Exit code 0 = no changes (success)
# Exit code 2 = changes detected (review needed)
```

## Advanced Usage

### Scripted Bulk Export

```bash
#!/bin/bash
# bulk_export.sh - Export all policy types

DATE=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="exports/${DATE}"

mkdir -p "${OUTPUT_DIR}"

echo "Exporting policies to ${OUTPUT_DIR}..."

catocli export if_rules -o "${OUTPUT_DIR}/internet_firewall.json"
catocli export wf_rules -o "${OUTPUT_DIR}/wan_firewall.json"
catocli export tls_rules -o "${OUTPUT_DIR}/tls_inspection.json"
catocli export wnw_rules -o "${OUTPUT_DIR}/wan_network.json"

echo "Export completed: ${OUTPUT_DIR}"
```

### Automated Import Pipeline

```bash
#!/bin/bash
# import_pipeline.sh - Import all policies

set -euo pipefail

EXPORT_DIR="exports/latest"
RESOURCES=(
  "internet_firewall.json:cato-ztna_internet_firewall_policy.main"
  "wan_firewall.json:cato-ztna_wan_firewall_policy.main"
  "wan_network.json:cato-ztna_wan_network_policy.main"
)

for item in "${RESOURCES[@]}"; do
  IFS=':' read -r file resource <<< "$item"
  echo "Importing ${file} to ${resource}..."
  
  case "${file}" in
    internet_firewall.json)
      catocli import if_rules_to_tf -f "${EXPORT_DIR}/${file}" -r "${resource}"
      ;;
    wan_firewall.json)
      catocli import wf_rules_to_tf -f "${EXPORT_DIR}/${file}" -r "${resource}"
      ;;
    wan_network.json)
      catocli import wnw_rules_to_tf -f "${EXPORT_DIR}/${file}" -r "${resource}"
      ;;
  esac
done

echo "Import pipeline completed"
terraform plan
```

### Environment-Specific Exports

```bash
#!/bin/bash
# Export from different environments

ENVIRONMENTS=("production" "staging" "development")

for env in "${ENVIRONMENTS[@]}"; do
  echo "Exporting ${env} environment..."
  OUTPUT_DIR="exports/${env}"
  mkdir -p "${OUTPUT_DIR}"
  
  catocli export wnw_rules \
    -o "${OUTPUT_DIR}/wan_network.json" \
    -p "${env}"
done
```

## Integration with CI/CD

### GitLab CI Example

```yaml
# .gitlab-ci.yml
export_policies:
  stage: export
  script:
    - pip install catocli
    - catocli configure set --cato-token ${CATO_TOKEN} --account-id ${ACCOUNT_ID}
    - mkdir -p exports
    - catocli export wnw_rules -o exports/wan_network.json
  artifacts:
    paths:
      - exports/
    expire_in: 30 days

import_to_terraform:
  stage: import
  dependencies:
    - export_policies
  script:
    - terraform init
    - catocli import wnw_rules_to_tf -f exports/wan_network.json -r cato-ztna_wan_network_policy.main
    - terraform plan
  only:
    - main
```

### GitHub Actions Example

```yaml
# .github/workflows/cato-export.yml
name: Export Cato Policies

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install CatoCLI
        run: pip install catocli
      
      - name: Configure CatoCLI
        env:
          CATO_TOKEN: ${{ secrets.CATO_TOKEN }}
          ACCOUNT_ID: ${{ secrets.ACCOUNT_ID }}
        run: |
          catocli configure set --cato-token ${CATO_TOKEN} --account-id ${ACCOUNT_ID}
      
      - name: Export Policies
        run: |
          mkdir -p exports
          catocli export wnw_rules -o exports/wan_network.json
          catocli export wf_rules -o exports/wan_firewall.json
      
      - name: Upload Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: policy-exports
          path: exports/
```

## Related Documentation

- [Main README](../README.md) - Installation and setup
- [PROFILES.md](../PROFILES.md) - Profile configuration
- [Common Patterns](./common-patterns.md) - CLI usage patterns

## Support

For issues or questions:
- Review the [Cato API Documentation](https://api.catonetworks.com/documentation/)
- Check the [Terraform Provider Documentation](https://registry.terraform.io/providers/catonetworks/cato-ztna/latest/docs)
- Contact Cato Networks support
