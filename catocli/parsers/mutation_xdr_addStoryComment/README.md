
## CATO-CLI - mutation.xdr.addStoryComment:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.xdr.addStoryComment) for documentation on this operation.

### Usage for mutation.xdr.addStoryComment:

`catocli mutation xdr addStoryComment -h`

`catocli mutation xdr addStoryComment <json>`

`catocli mutation xdr addStoryComment "$(cat < mutation.xdr.addStoryComment.json)"`

`catocli mutation xdr addStoryComment '{"addStoryCommentInput":{"storyId":"id","text":"string"}}'`

`catocli mutation xdr addStoryComment -p '{
    "addStoryCommentInput": {
        "storyId": "id",
        "text": "string"
    }
}'`


#### Operation Arguments for mutation.xdr.addStoryComment ####

`accountId` [ID] - (required) N/A    
`addStoryCommentInput` [AddStoryCommentInput] - (required) N/A    
