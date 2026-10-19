
## CATO-CLI - mutation.webProxyConfig.encryptKeytabFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.webProxyConfig.encryptKeytabFile) for documentation on this operation.

### Usage for mutation.webProxyConfig.encryptKeytabFile:

```bash
catocli mutation webProxyConfig encryptKeytabFile -h

catocli mutation webProxyConfig encryptKeytabFile <json>

catocli mutation webProxyConfig encryptKeytabFile --json-file mutation.webProxyConfig.encryptKeytabFile.json

catocli mutation webProxyConfig encryptKeytabFile '{"encryptKeytabFileInput":{"file":"path/to/file"}}'

catocli mutation webProxyConfig encryptKeytabFile '{
    "encryptKeytabFileInput": {
        "file": "path/to/file"
    }
}'
```

#### Operation Arguments for mutation.webProxyConfig.encryptKeytabFile ####

`accountId` [ID] - (required) The ID of the account whose Site Web Proxy configuration is being updated.
`encryptKeytabFileInput` [EncryptKeytabFileInput] - (required) The Kerberos keytab file to encrypt.
