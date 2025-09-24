
## CATO-CLI - query.sandbox:
[Click here](https://api.catonetworks.com/documentation/#query-query.sandbox) for documentation on this operation.

### Usage for query.sandbox:

`catocli query sandbox -h`

`catocli query sandbox <json>`

`catocli query sandbox "$(cat < query.sandbox.json)"`

`catocli query sandbox '{"sandboxReportsInput":{"pagingInput":{"from":1,"limit":1},"sandboxReportsFilterInput":{"fileHash":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"fileName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"reportCreateDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]}},"sandboxReportsSortInput":{"fileName":{"direction":"ASC","priority":1},"reportCreateDate":{"direction":"ASC","priority":1}}}}'`

`catocli query sandbox -p '{
    "sandboxReportsInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "sandboxReportsFilterInput": {
            "fileHash": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "fileName": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "reportCreateDate": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ]
            }
        },
        "sandboxReportsSortInput": {
            "fileName": {
                "direction": "ASC",
                "priority": 1
            },
            "reportCreateDate": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'`


#### Operation Arguments for query.sandbox ####

`accountId` [ID] - (required) N/A    
`sandboxReportsInput` [SandboxReportsInput] - (required) N/A    
