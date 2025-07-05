

## CATO-CLI - query.siteLocation:

### Usage for query.siteLocation:

`catocli query siteLocation -h`

`catocli query siteLocation <json>`

`catocli query siteLocation "$(cat < siteLocation.json)"`

`catocli query siteLocation '{"filters":[{"search": "Your city here","field":"city","operation":"exact"}]}'`

`catocli query siteLocation '{"filters":[{"search": "Your Country here","field":"countryName","operation":"startsWith"}]}'`

`catocli query siteLocation '{"filters":[{"search": "Your stateName here","field":"stateName","operation":"endsWith"}]}'`

`catocli query siteLocation '{"filters":[{"search": "Your City here","field":"city","operation":"startsWith"},{"search": "Your StateName here","field":"stateName","operation":"endsWith"},{"search": "Your Country here","field":"countryName","operation":"contains"}]}'`

#### Operation Arguments for query.siteLocation ####
`accountID` [ID] - (required) Unique Identifier of Account. 
`filters[]` [Array] - (optional) Array of objects consisting of `search`, `field` and `operation` attributes.
`filters[].search` [String] - (required) String to match countryName, stateName, or city specificed in `filters[].field`.
`filters[].field` [String] - (required) Specify field to match query against, defaults to look for any.  Possible values: `countryName`, `stateName`, or `city`.
`filters[].operation` [string] - (required) If a field is specified, operation to match the field value.  Possible values: `startsWith`,`endsWith`,`exact`, `contains`.
