
## CATO-CLI - mutation.policy.terminalServer.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.updateRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.updateRule:

`catocli mutation policy terminalServer updateRule -h`

`catocli mutation policy terminalServer updateRule <json>`

`catocli mutation policy terminalServer updateRule "$(cat < mutation.policy.terminalServer.updateRule.json)"`

`catocli mutation policy terminalServer updateRule '{"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"terminalServerUpdateRuleInput":{"id":"id","terminalServerUpdateRuleDataInput":{"allowedHostIP":{"by":"ID","input":"string"},"description":"string","enabled":true,"excludeTraffic":{"by":"ID","input":"string"},"name":"string"}}}'`

`catocli mutation policy terminalServer updateRule -p '{
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "terminalServerUpdateRuleInput": {
        "id": "id",
        "terminalServerUpdateRuleDataInput": {
            "allowedHostIP": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "enabled": true,
            "excludeTraffic": {
                "by": "ID",
                "input": "string"
            },
            "name": "string"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.updateRule ####

`accountId` [ID] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
`terminalServerUpdateRuleInput` [TerminalServerUpdateRuleInput] - (required) N/A    
