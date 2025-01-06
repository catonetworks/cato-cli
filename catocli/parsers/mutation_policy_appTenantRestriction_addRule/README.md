
## CATO-CLI - mutation.policy.appTenantRestriction.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-addRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addRule:

`catocli mutation policy appTenantRestriction addRule -h`

`catocli mutation policy appTenantRestriction addRule <json>`

`catocli mutation policy appTenantRestriction addRule "$(cat < addRule.json)"`

`catocli mutation policy appTenantRestriction addRule '{"appTenantRestrictionAddRuleInput": {"appTenantRestrictionAddRuleDataInput": {"action": {"action": "enum(AppTenantRestrictionActionEnum)"}, "application": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "headers": {"name": {"name": "HttpHeaderName"}, "value": {"value": "HttpHeaderValue"}}, "name": {"name": "String"}, "schedule": {"activeOn": {"activeOn": "enum(PolicyActiveOnEnum)"}, "customRecurring": {"days": {"days": "enum(DayOfWeek)"}, "from": {"from": "Time"}, "to": {"to": "Time"}}, "customTimeframe": {"from": {"from": "DateTime"}, "to": {"to": "DateTime"}}}, "severity": {"severity": "enum(AppTenantRestrictionSeverityEnum)"}, "source": {"country": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "floatingSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "group": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "host": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "networkInterface": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "site": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "siteNetworkSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": ["NetworkSubnet"]}, "systemGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "user": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "usersGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.addRule ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionAddRuleInput` [AppTenantRestrictionAddRuleInput] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
