
## CATO-CLI - query.container:
[Click here](https://api.catonetworks.com/documentation/#query-query.container) for documentation on this operation.

### Usage for query.container:

`catocli query container -h`

`catocli query container <json>`

`catocli query container "$(cat < query.container.json)"`

`catocli query container '{"containerSearchInput":{"containerRefInput":{"by":"ID","input":"string"},"types":"IP_RANGE"},"downloadFqdnContainerFileInput":{"by":"ID","input":"string"},"downloadIpAddressRangeContainerFileInput":{"by":"ID","input":"string"},"fqdnContainerSearchFqdnInput":{"fqdn":"example_value"},"fqdnContainerSearchInput":{"containerRefInput":{"by":"ID","input":"string"}},"ipAddressRangeContainerSearchInput":{"containerRefInput":{"by":"ID","input":"string"}},"ipAddressRangeContainerSearchIpAddressRangeInput":{"ipAddressRangeInput":{"from":"example_value","to":"example_value"}}}'`

`catocli query container -p '{
    "containerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "types": "IP_RANGE"
    },
    "downloadFqdnContainerFileInput": {
        "by": "ID",
        "input": "string"
    },
    "downloadIpAddressRangeContainerFileInput": {
        "by": "ID",
        "input": "string"
    },
    "fqdnContainerSearchFqdnInput": {
        "fqdn": "example_value"
    },
    "fqdnContainerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    },
    "ipAddressRangeContainerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    },
    "ipAddressRangeContainerSearchIpAddressRangeInput": {
        "ipAddressRangeInput": {
            "from": "example_value",
            "to": "example_value"
        }
    }
}'`


#### Operation Arguments for query.container ####

`accountId` [ID] - (required) N/A    
`containerSearchInput` [ContainerSearchInput] - (required) N/A    
`downloadFqdnContainerFileInput` [DownloadFqdnContainerFileInput] - (required) N/A    
`downloadIpAddressRangeContainerFileInput` [DownloadIpAddressRangeContainerFileInput] - (required) N/A    
`fqdnContainerSearchFqdnInput` [FqdnContainerSearchFqdnInput] - (required) N/A    
`fqdnContainerSearchInput` [FqdnContainerSearchInput] - (required) N/A    
`ipAddressRangeContainerSearchInput` [IpAddressRangeContainerSearchInput] - (required) N/A    
`ipAddressRangeContainerSearchIpAddressRangeInput` [IpAddressRangeContainerSearchIpAddressRangeInput] - (required) N/A    
