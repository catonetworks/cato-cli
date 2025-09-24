
## CATO-CLI - mutation.policy.terminalServer.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.addRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.addRule:

`catocli mutation policy terminalServer addRule -h`

`catocli mutation policy terminalServer addRule <json>`

`catocli mutation policy terminalServer addRule "$(cat < mutation.policy.terminalServer.addRule.json)"`

`catocli mutation policy terminalServer addRule '{"terminalServerAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"terminalServerAddRuleDataInput":{"allowedHostIP":{"by":"ID","input":"string"},"description":"string","enabled":true,"excludeTraffic":{"by":"ID","input":"string"},"name":"string"}},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer addRule -p '{
    "terminalServerAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "terminalServerAddRuleDataInput": {
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
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.addRule ####

`accountId` [ID] - (required) N/A    
`terminalServerAddRuleInput` [TerminalServerAddRuleInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
