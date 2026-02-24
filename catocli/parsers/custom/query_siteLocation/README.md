

## CATO-CLI - query.siteLocation:

### Usage for query.siteLocation:

```bash
catocli query siteLocation -h

catocli query siteLocation <json>`

catocli query siteLocation "$(cat < siteLocation.json)"`

catocli query siteLocation '{"filters":[{"search": "Your city here","field":"city","operation":"exact"}]}'

catocli query siteLocation '{
    "filters": [
        {
            "search": "Your Country here",
            "field": "countryName",
            "operation": "startsWith"
        }
    ]
}'

catocli query siteLocation '{
    "filters": [
        {
            "search": "Your stateName here",
            "field": "stateName",
            "operation": "endsWith"
        }
    ]
}'

catocli query siteLocation '{
    "filters": [
        {
            "search": "Your City here",
            "field": "city",
            "operation": "startsWith"
        },
        {
            "search": "Your StateName here",
            "field": "stateName",
            "operation": "endsWith"
        },
        {
            "search": "Your Country here",
            "field": "countryName",
            "operation": "contains"
        }
    ]
}'

catocli query siteLocation '{
    "filters": [
        {
            "search": "US",
            "field": "countryCode",
            "operation": "exact"
        },
        {
            "search": "US-CA",
            "field": "stateCode",
            "operation": "exact"
        }
    ]
}'
```

#### Operation Arguments for query.siteLocation ####
`accountID` [ID] - (required) Unique Identifier of Account.
`filters[]` [Array] - (optional) Array of objects consisting of `search`, `field` and `operation` attributes.
`filters[].search` [String] - (required) String to match the field specified in `filters[].field`.
`filters[].field` [String] - (required) Specify field to match query against.  Possible values: `countryCode`, `countryName`, `stateCode`, `stateName`, or `city`.
`filters[].operation` [string] - (required) If a field is specified, operation to match the field value.  Possible values: `startsWith`,`endsWith`,`exact`, `contains`.

#### Mutually Exclusive Fields ####
- `countryCode` and `countryName` cannot be used in the same query
- `stateCode` and `stateName` cannot be used in the same query

#### State Codes ####
State codes use ISO 3166-2 format (e.g., `US-CA` for California, `IN-KL` for Kerala).

#### Data Source ####
Location data is sourced from [GeoNames](https://www.geonames.org/) (cities with population > 1000) and stored in a SQLite database. The database is rebuilt when running `importSchema.py` from the schema directory.
