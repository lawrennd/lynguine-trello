# lynguine-trello

Trello boards as a lynguine tabular source (`type: trello`).

Point at the plugin form in lynguine:

https://github.com/lawrennd/lynguine/blob/main/docs/getting_started/io_plugins.rst

## Authorisation

This package **declares** `credential_type="trello_api"`. It does not open the
credential store. lynguine (CIP-0005) fetches the secret named by `credential:`
and passes it as `credential_value`.

```yaml
input:
  type: trello
  board: BOARD_ID
  credential: my_trello
plugins:
  - lynguine_trello
```

Store `{api_key, token}` under CIP-0005 key `my_trello` with type `trello_api`.

## Status

Registration and the credential contract are in place. The Trello REST reader is
not implemented yet (`read_trello` raises `NotImplementedError` once the token
and board id are present).
