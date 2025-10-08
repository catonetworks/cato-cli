
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

```bash
catocli query accountMetrics -h

catocli query accountMetrics <json>

catocli query accountMetrics "$(cat < query.accountMetrics.json)"

catocli query accountMetrics '{"groupDevices":true,"groupInterfaces":true,"timeFrame":"example_value"}'

catocli query accountMetrics '{
    "groupDevices": true,
    "groupInterfaces": true,
    "timeFrame": "example_value"
}'
```


#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- `"last.PT5M"` = Previous 5 minutes
- `"last.PT1H"` = Previous 1 hour  
- `"last.P1D"` = Previous 1 day
- `"last.P14D"` = Previous 14 days
- `"last.P1M"` = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: `"utc.2023-02-{28/00:00:00--28/23:59:59}"`
- Multiple days: `"utc.2023-02-{25/00:00:00--28/23:59:59}"`  
- Specific hours: `"utc.2023-02-{28/09:00:00--28/17:00:00}"`
- Across months: `"utc.2023-{01-28/00:00:00--02-03/23:59:59}"`


#### Operation Arguments for query.accountMetrics ####

`accountID` [ID] - (required) Unique Identifier of Account.    
`groupDevices` [Boolean] - (required) When the boolean argument groupDevices is set to __true__, then the analytics for all the
Sockets (usually two in high availability) are aggregated as one result.

For the best results for aggregated Sockets, we recommend that there is consistent
names and functionality (for example Destination) for the links on both Sockets.    
`groupInterfaces` [Boolean] - (required) When the boolean argument groupInterfaces is set to __true__, then the data for all the
interfaces are aggregated to a single interface.    
`timeFrame` [TimeFrame] - (required) The time frame for the data that the query returns. The argument is in the format type.time value. This argument is mandatory.    
