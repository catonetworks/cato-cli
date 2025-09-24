
## CATO-CLI - mutation.xdr.deleteStoryComment:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.xdr.deleteStoryComment) for documentation on this operation.

### Usage for mutation.xdr.deleteStoryComment:

`catocli mutation xdr deleteStoryComment -h`

`catocli mutation xdr deleteStoryComment <json>`

`catocli mutation xdr deleteStoryComment "$(cat < mutation.xdr.deleteStoryComment.json)"`

`catocli mutation xdr deleteStoryComment '{"deleteStoryCommentInput":{"commentId":"id","storyId":"id"}}'`

`catocli mutation xdr deleteStoryComment -p '{
    "deleteStoryCommentInput": {
        "commentId": "id",
        "storyId": "id"
    }
}'`


#### Operation Arguments for mutation.xdr.deleteStoryComment ####

`accountId` [ID] - (required) N/A    
`deleteStoryCommentInput` [DeleteStoryCommentInput] - (required) N/A    
