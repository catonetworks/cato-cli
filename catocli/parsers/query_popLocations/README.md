
## CATO-CLI - query.popLocations:
[Click here](https://api.catonetworks.com/documentation/#query-popLocations) for documentation on this operation.

### Usage for query.popLocations:

`catocli query popLocations -h`

`catocli query popLocations <json>`

`catocli query popLocations "$(cat < popLocations.json)"`

`catocli query popLocations '{"popLocationFilterInput": {"booleanFilterInput": {"eq": {"eq": "Boolean"}, "neq": {"neq": "Boolean"}}, "countryRefFilterInput": {"eq": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "in": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "neq": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "nin": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "idFilterInput": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "popLocationCloudInterconnectFilterInput": {"taggingMethod": {"eq": {"eq": "enum(TaggingMethod)"}, "in": {"in": "enum(TaggingMethod)"}, "neq": {"neq": "enum(TaggingMethod)"}, "nin": {"nin": "enum(TaggingMethod)"}}}, "stringFilterInput": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}}}'`

#### Operation Arguments for query.popLocations ####
`accountId` [ID] - (required) N/A 
`popLocationFilterInput` [PopLocationFilterInput] - (optional) N/A 
