
## CATO-CLI - mutation.policy.terminalServer.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.terminalServer.publishPolicyRevision:

`catocli mutation policy terminalServer publishPolicyRevision -h`

`catocli mutation policy terminalServer publishPolicyRevision <json>`

`catocli mutation policy terminalServer publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy terminalServer publishPolicyRevision '{"policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
