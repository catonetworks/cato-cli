
## CATO-CLI - mutation.xdr.addStoryComment:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.xdr.addStoryComment) for documentation on this operation.

### Usage for mutation.xdr.addStoryComment:

```bash
catocli mutation xdr addStoryComment -h

catocli mutation xdr addStoryComment <json>

catocli mutation xdr addStoryComment --json-file mutation.xdr.addStoryComment.json

catocli mutation xdr addStoryComment '{"addStoryCommentInput":{"author":"string","storyId":"id","text":"string","type":"USER"}}'

catocli mutation xdr addStoryComment '{
    "addStoryCommentInput": {
        "author": "string",
        "storyId": "id",
        "text": "string",
        "type": "USER"
    }
}'
```

#### Operation Arguments for mutation.xdr.addStoryComment ####

`accountId` [ID] - (required) N/A    
`addStoryCommentInput` [AddStoryCommentInput] - (required) N/A    
