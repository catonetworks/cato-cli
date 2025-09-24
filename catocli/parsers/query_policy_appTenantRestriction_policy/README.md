
## CATO-CLI - query.policy.appTenantRestriction.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.appTenantRestriction.policy) for documentation on this operation.

### Usage for query.policy.appTenantRestriction.policy:

`catocli query policy appTenantRestriction policy -h`

`catocli query policy appTenantRestriction policy <json>`

`catocli query policy appTenantRestriction policy "$(cat < query.policy.appTenantRestriction.policy.json)"`

`catocli query policy appTenantRestriction policy '{"appTenantRestrictionPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy appTenantRestriction policy -p '{
    "appTenantRestrictionPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.appTenantRestriction.policy ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyInput` [AppTenantRestrictionPolicyInput] - (required) N/A    
