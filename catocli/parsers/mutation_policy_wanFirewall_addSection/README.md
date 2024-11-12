
## CATO-CLI - mutation.policy.wanFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.addSection:

`catocli mutation policy wanFirewall addSection -h`

`catocli mutation policy wanFirewall addSection <json>`

`catocli mutation policy wanFirewall addSection "$(cat < addSection.json)"`

`catocli mutation policy wanFirewall addSection '{"policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.addSection ####
`accountId` [ID] - (required) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
