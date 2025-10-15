# XDR query with minimum fields

```bash
# Example with minimum required fields
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
        }
    }
}'
```