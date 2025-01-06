
## CATO-CLI - mutation.policy.appTenantRestriction.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updateRule:

`catocli mutation policy appTenantRestriction updateRule -h`

`catocli mutation policy appTenantRestriction updateRule <json>`

`catocli mutation policy appTenantRestriction updateRule "$(cat < updateRule.json)"`

`catocli mutation policy appTenantRestriction updateRule '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "appTenantRestrictionUpdateRuleInput": {"appTenantRestrictionUpdateRuleDataInput": {"action": {"action": "enum(AppTenantRestrictionActionEnum)"}, "application": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "headers": {"name": {"name": "HttpHeaderName"}, "value": {"value": "HttpHeaderValue"}}, "name": {"name": "String"}, "schedule": {"activeOn": {"activeOn": "enum(PolicyActiveOnEnum)"}, "customRecurring": {"days": {"days": "enum(DayOfWeek)"}, "from": {"from": "Time"}, "to": {"to": "Time"}}, "customTimeframe": {"from": {"from": "DateTime"}, "to": {"to": "DateTime"}}}, "severity": {"severity": "enum(AppTenantRestrictionSeverityEnum)"}, "source": {"country": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "floatingSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "group": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "host": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "networkInterface": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "site": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "siteNetworkSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": ["NetworkSubnet"]}, "systemGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "user": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "usersGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.updateRule ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`appTenantRestrictionUpdateRuleInput` [AppTenantRestrictionUpdateRuleInput] - (required) N/A 
