
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

```bash
catocli query accountMetrics -h

catocli query accountMetrics <json>

catocli query accountMetrics "$(cat < query.accountMetrics.json)"

catocli query accountMetrics '{"groupDevices":true,"groupInterfaces":true,"timeFrame":"example_value"}'

catocli query accountMetrics -p '{
    "groupDevices": true,
    "groupInterfaces": true,
    "timeFrame": "example_value"
}'
```

#### Operation Arguments for query.accountMetrics ####

`accountID` [ID] - (required) Unique Identifier of Account.    
`groupDevices` [Boolean] - (required) When the boolean argument groupDevices is set to __true__, then the analytics for all the
Sockets (usually two in high availability) are aggregated as one result.

For the best results for aggregated Sockets, we recommend that there is consistent
names and functionality (for example Destination) for the links on both Sockets.    
`groupInterfaces` [Boolean] - (required) When the boolean argument groupInterfaces is set to __true__, then the data for all the
interfaces are aggregated to a single interface.    
`timeFrame` [TimeFrame] - (required) The time frame for the data that the query returns. The argument is in the format type.time value. This argument is mandatory.    
