
## CATO-CLI - mutation.policy.siteWebProxy.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.moveRule) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.moveRule:

```bash
catocli mutation policy siteWebProxy moveRule -h

catocli mutation policy siteWebProxy moveRule <json>

catocli mutation policy siteWebProxy moveRule --json-file mutation.policy.siteWebProxy.moveRule.json

catocli mutation policy siteWebProxy moveRule '{"policyMoveRuleInput":{"id":"id","to":{"position":"AFTER_RULE","ref":"id"}},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "to": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.moveRule ####

