
## CATO-CLI - mutation.xdr.analystFeedback:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.xdr.analystFeedback) for documentation on this operation.

### Usage for mutation.xdr.analystFeedback:

`catocli mutation xdr analystFeedback -h`

`catocli mutation xdr analystFeedback <json>`

`catocli mutation xdr analystFeedback "$(cat < mutation.xdr.analystFeedback.json)"`

`catocli mutation xdr analystFeedback '{"analystFeedbackInput":{"additionalInfo":"string","severity":"High","status":"Open","storyId":"id","storyThreatType":{"details":"string","name":"string","recommendedAction":"string"},"threatClassification":"string","verdict":"Suspicious"}}'`

`catocli mutation xdr analystFeedback -p '{
    "analystFeedbackInput": {
        "additionalInfo": "string",
        "severity": "High",
        "status": "Open",
        "storyId": "id",
        "storyThreatType": {
            "details": "string",
            "name": "string",
            "recommendedAction": "string"
        },
        "threatClassification": "string",
        "verdict": "Suspicious"
    }
}'`


#### Operation Arguments for mutation.xdr.analystFeedback ####

`accountId` [ID] - (required) N/A    
`analystFeedbackInput` [AnalystFeedbackInput] - (required) N/A    
