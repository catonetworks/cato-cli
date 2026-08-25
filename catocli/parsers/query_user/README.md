
## CATO-CLI - query.user:
[Click here](https://api.catonetworks.com/documentation/#query-query.user) for documentation on this operation.

### Usage for query.user:

```bash
catocli query user -h

catocli query user <json>

catocli query user --json-file query.user.json

catocli query user '{"userListInput":{"pagingInput":{"from":1,"limit":1},"userFilterInput":{"department":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"directoryId":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"email":{"eq":"example_value","in":["example1","example2"],"neq":"example_value","nin":["example1","example2"]},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"jobTitle":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"remoteAccessEligibility":{"eq":true,"neq":true},"riskScore":{"eq":"LOW","in":"LOW","neq":"LOW","nin":"LOW"},"searchTerm":{"search":"string"},"userImportType":{"eq":"MANUAL","in":"MANUAL","neq":"MANUAL","nin":"MANUAL"},"userStatus":{"eq":"DISABLED","in":"DISABLED","neq":"DISABLED","nin":"DISABLED"}},"userSortInput":{"creationDate":{"direction":"ASC","priority":1},"department":{"direction":"ASC","priority":1},"email":{"direction":"ASC","priority":1},"jobTitle":{"direction":"ASC","priority":1},"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"remoteAccessEligibility":{"direction":"ASC","priority":1},"riskScore":{"direction":"ASC","priority":1},"userId":{"direction":"ASC","priority":1},"userImportType":{"direction":"ASC","priority":1},"userPrincipalName":{"direction":"ASC","priority":1},"userStatus":{"direction":"ASC","priority":1}}}}'

catocli query user '{
    "userListInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "userFilterInput": {
            "department": {
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
            "directoryId": {
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
            "email": {
                "eq": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ]
            },
            "id": {
                "eq": "id",
                "in": [
                    "id1",
                    "id2"
                ],
                "neq": "id",
                "nin": [
                    "id1",
                    "id2"
                ]
            },
            "jobTitle": {
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
            "remoteAccessEligibility": {
                "eq": true,
                "neq": true
            },
            "riskScore": {
                "eq": "LOW",
                "in": "LOW",
                "neq": "LOW",
                "nin": "LOW"
            },
            "searchTerm": {
                "search": "string"
            },
            "userImportType": {
                "eq": "MANUAL",
                "in": "MANUAL",
                "neq": "MANUAL",
                "nin": "MANUAL"
            },
            "userStatus": {
                "eq": "DISABLED",
                "in": "DISABLED",
                "neq": "DISABLED",
                "nin": "DISABLED"
            }
        },
        "userSortInput": {
            "creationDate": {
                "direction": "ASC",
                "priority": 1
            },
            "department": {
                "direction": "ASC",
                "priority": 1
            },
            "email": {
                "direction": "ASC",
                "priority": 1
            },
            "jobTitle": {
                "direction": "ASC",
                "priority": 1
            },
            "lastModified": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "remoteAccessEligibility": {
                "direction": "ASC",
                "priority": 1
            },
            "riskScore": {
                "direction": "ASC",
                "priority": 1
            },
            "userId": {
                "direction": "ASC",
                "priority": 1
            },
            "userImportType": {
                "direction": "ASC",
                "priority": 1
            },
            "userPrincipalName": {
                "direction": "ASC",
                "priority": 1
            },
            "userStatus": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.user ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`userListInput` [UserListInput] - (required) N/A    
