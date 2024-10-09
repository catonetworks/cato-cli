

## CATO-CLI - query.siteLocation:

### Usage for query.siteLocation:

`cato query siteLocation -h`

`cato query siteLocation <accountID> <json>`

`cato query siteLocation 12345 "$(cat < siteLocation.json)"`

`cato query siteLocation 12345 '{"filters":[{"search": "Your city here","field":"city","operation":"exact"}]}'`

`cato query siteLocation 12345 '{"filters":[{"search": "Your Country here","field":"countryName","operation":"startsWith"}]}'`

`cato query siteLocation 12345 '{"filters":[{"search": "Your stateName here","field":"stateName","operation":"endsWith"}]}'`

`cato query siteLocation 12345 '{filters:[{"search": "Your City here","field":"city","operation":"startsWith"},{"search": "Your StateName here","field":"stateName","operation":"endsWith"},{"search": "Your Country here","field":"countryName","operation":"contains"}}'`

#### Operation Arguments for query.siteLocation ####
`accountID` [ID] - (optional) Unique Identifier of Account. 
`filters[]` [Array] - (optional) Array of objects consisting of `search`, `field` and `operation` attributes.
`filters[].search` [String] - (required) String to match countryName, stateName, or city specificed in `filters[].field`.
`filters[].field` [String] - (required) Specify field to match query against, defaults to look for any.  Possible values: `countryName`, `stateName`, or `city`.
`filters[].operation` [string] - (required) If a field is specified, operation to match the field value.  Possible values: `startsWith`,`endsWith`,`exact`, `contains`.
