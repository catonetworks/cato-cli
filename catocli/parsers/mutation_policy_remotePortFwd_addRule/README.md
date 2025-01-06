
## CATO-CLI - mutation.policy.remotePortFwd.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-addRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.addRule:

`catocli mutation policy remotePortFwd addRule -h`

`catocli mutation policy remotePortFwd addRule <json>`

`catocli mutation policy remotePortFwd addRule "$(cat < addRule.json)"`

`catocli mutation policy remotePortFwd addRule '{"remotePortFwdAddRuleInput": {"policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "remotePortFwdAddRuleDataInput": {"description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "externalIp": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "externalPortRange": {"from": {"from": "Port"}, "to": {"to": "Port"}}, "forwardIcmp": {"forwardIcmp": "Boolean"}, "internalIp": {"internalIp": "IPAddress"}, "internalPortRange": {"from": {"from": "Port"}, "to": {"to": "Port"}}, "name": {"name": "String"}, "remoteIPs": {"globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "subnet": {"subnet": ["NetworkSubnet"]}}, "restrictionType": {"restrictionType": "enum(RemotePortFwdRestrictionType)"}, "tracking": {"enabled": {"enabled": "Boolean"}, "frequency": {"frequency": "enum(PolicyRuleTrackingFrequencyEnum)"}, "mailingList": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subscriptionGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "webhook": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.addRule ####
`accountId` [ID] - (required) N/A 
`remotePortFwdAddRuleInput` [RemotePortFwdAddRuleInput] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
