
## CATO-CLI - query.xdr.stories:
[Click here](https://api.catonetworks.com/documentation/#query-query.xdr.stories) for documentation on this operation.

### Usage for query.xdr.stories:

```bash
catocli query xdr stories -h

catocli query xdr stories <json>

catocli query xdr stories "$(cat < query.xdr.stories.json)"

## Advanced Usage
# XDR query with minimum fields

```bash
catocli query xdr stories '{
    "storyInput": {
        "filter": [
            {
                "timeFrame": {
                    "time": "last.P1M"
                }
            }
        ],
        "paging": {
            "from": 0,
            "limit": 100
        },
        "sort": []
    }
}'


#### Operation Arguments for query.xdr.stories ####

`accountID` [ID] - (required) N/A    
