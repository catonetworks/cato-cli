
## CATO-CLI - mutation.policy.remotePortFwd.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updateRule:

`catocli mutation policy remotePortFwd updateRule -h`

`catocli mutation policy remotePortFwd updateRule <json>`

`catocli mutation policy remotePortFwd updateRule "$(cat < updateRule.json)"`

`catocli mutation policy remotePortFwd updateRule '{"remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "remotePortFwdUpdateRuleInput": {"id": {"id": "ID"}, "remotePortFwdUpdateRuleDataInput": {"description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "externalIp": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "externalPortRange": {"from": {"from": "Port"}, "to": {"to": "Port"}}, "forwardIcmp": {"forwardIcmp": "Boolean"}, "internalIp": {"internalIp": "IPAddress"}, "internalPortRange": {"from": {"from": "Port"}, "to": {"to": "Port"}}, "name": {"name": "String"}, "remoteIPs": {"globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "subnet": {"subnet": ["NetworkSubnet"]}}, "restrictionType": {"restrictionType": "enum(RemotePortFwdRestrictionType)"}, "tracking": {"enabled": {"enabled": "Boolean"}, "frequency": {"frequency": "enum(PolicyRuleTrackingFrequencyEnum)"}, "mailingList": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subscriptionGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "webhook": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.updateRule ####
`accountId` [ID] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
`remotePortFwdUpdateRuleInput` [RemotePortFwdUpdateRuleInput] - (required) N/A 
