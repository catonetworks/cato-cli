
## CATO-CLI - mutation.policy.wanFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.addSection:

`cato mutation policy wanFirewall addSection -h`

`cato mutation policy wanFirewall addSection <accountID> <json>`

`cato mutation policy wanFirewall addSection 12345 "$(cat < addSection.json)"`

`cato mutation policy wanFirewall addSection 12345 '{"PolicyAddSectionInput": {"PolicyAddSectionInfoInput": {"name": {"name": "String"}}, "PolicySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.addSection ####
`PolicyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
