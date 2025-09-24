
## CATO-CLI - query.hardwareManagement:
[Click here](https://api.catonetworks.com/documentation/#query-query.hardwareManagement) for documentation on this operation.

### Usage for query.hardwareManagement:

`catocli query hardwareManagement -h`

`catocli query hardwareManagement <json>`

`catocli query hardwareManagement "$(cat < query.hardwareManagement.json)"`

`catocli query hardwareManagement '{"socketInventoryInput":{"pagingInput":{"from":1,"limit":1},"socketInventoryFilterInput":{"freeText":{"search":"string"}},"socketInventoryOrderInput":{"accountName":{"direction":"ASC","priority":1},"deliverySiteName":{"direction":"ASC","priority":1},"description":{"direction":"ASC","priority":1},"installedSite":{"direction":"ASC","priority":1},"serialNumber":{"direction":"ASC","priority":1},"shippingCompany":{"direction":"ASC","priority":1},"shippingDate":{"direction":"ASC","priority":1},"socketType":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}}}}'`

`catocli query hardwareManagement -p '{
    "socketInventoryInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "socketInventoryFilterInput": {
            "freeText": {
                "search": "string"
            }
        },
        "socketInventoryOrderInput": {
            "accountName": {
                "direction": "ASC",
                "priority": 1
            },
            "deliverySiteName": {
                "direction": "ASC",
                "priority": 1
            },
            "description": {
                "direction": "ASC",
                "priority": 1
            },
            "installedSite": {
                "direction": "ASC",
                "priority": 1
            },
            "serialNumber": {
                "direction": "ASC",
                "priority": 1
            },
            "shippingCompany": {
                "direction": "ASC",
                "priority": 1
            },
            "shippingDate": {
                "direction": "ASC",
                "priority": 1
            },
            "socketType": {
                "direction": "ASC",
                "priority": 1
            },
            "status": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'`


#### Operation Arguments for query.hardwareManagement ####

`accountId` [ID] - (required) N/A    
`socketInventoryInput` [SocketInventoryInput] - (required) N/A    
