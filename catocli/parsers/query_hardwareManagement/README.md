
## CATO-CLI - query.hardwareManagement:
[Click here](https://api.catonetworks.com/documentation/#query-query.hardwareManagement) for documentation on this operation.

### Usage for query.hardwareManagement:

```bash
catocli query hardwareManagement -h

catocli query hardwareManagement <json>

catocli query hardwareManagement --json-file query.hardwareManagement.json

catocli query hardwareManagement '{"socketInventoryDistributionInput":{"socketInventoryFilterInput":{"freeText":{"search":"string"},"hardwareVersion":"X1500A","orderType":"PURCHASE","socketType":"X1500","status":"ORDERED"}},"socketInventoryInput":{"pagingInput":{"from":1,"limit":1},"socketInventoryFilterInput":{"freeText":{"search":"string"},"hardwareVersion":"X1500A","orderType":"PURCHASE","socketType":"X1500","status":"ORDERED"},"socketInventoryOrderInput":{"accountName":{"direction":"ASC","priority":1},"deliverySiteName":{"direction":"ASC","priority":1},"description":{"direction":"ASC","priority":1},"hardwareVersion":{"direction":"ASC","priority":1},"installedSite":{"direction":"ASC","priority":1},"serialNumber":{"direction":"ASC","priority":1},"shippingCompany":{"direction":"ASC","priority":1},"shippingDate":{"direction":"ASC","priority":1},"socketType":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}}}}'

catocli query hardwareManagement '{
    "socketInventoryDistributionInput": {
        "socketInventoryFilterInput": {
            "freeText": {
                "search": "string"
            },
            "hardwareVersion": "X1500A",
            "orderType": "PURCHASE",
            "socketType": "X1500",
            "status": "ORDERED"
        }
    },
    "socketInventoryInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "socketInventoryFilterInput": {
            "freeText": {
                "search": "string"
            },
            "hardwareVersion": "X1500A",
            "orderType": "PURCHASE",
            "socketType": "X1500",
            "status": "ORDERED"
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
            "hardwareVersion": {
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
}'
```

#### Operation Arguments for query.hardwareManagement ####

`accountId` [ID] - (required) N/A    
`socketInventoryDistributionInput` [SocketInventoryDistributionInput] - (required) N/A    
`socketInventoryInput` [SocketInventoryInput] - (required) N/A    
