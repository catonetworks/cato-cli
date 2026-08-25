
## CATO-CLI - mutation.user.updateDynamicUserGroupsConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.updateDynamicUserGroupsConfiguration) for documentation on this operation.

### Usage for mutation.user.updateDynamicUserGroupsConfiguration:

```bash
catocli mutation user updateDynamicUserGroupsConfiguration -h

catocli mutation user updateDynamicUserGroupsConfiguration <json>

catocli mutation user updateDynamicUserGroupsConfiguration --json-file mutation.user.updateDynamicUserGroupsConfiguration.json

catocli mutation user updateDynamicUserGroupsConfiguration '{"updateDynamicUserGroupsConfigurationInput":{"dynamicUserGroupAttributeSettingsInput":{"enabled":true}}}'

catocli mutation user updateDynamicUserGroupsConfiguration '{
    "updateDynamicUserGroupsConfigurationInput": {
        "dynamicUserGroupAttributeSettingsInput": {
            "enabled": true
        }
    }
}'
```

#### Operation Arguments for mutation.user.updateDynamicUserGroupsConfiguration ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`updateDynamicUserGroupsConfigurationInput` [UpdateDynamicUserGroupsConfigurationInput] - (required) N/A    
