# AuthenticationErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `unauthorized`: Authentication failed.
- `missing_api_key`: No API key in the `Authorization` header.
- `malformed_api_key`: The `Authorization` header does not contain a valid key format.
- `invalid_api_key`: The API key does not exist or was revoked.

## Example Usage

```python
from moderation_api.models import AuthenticationErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuthenticationErrorCode = "unauthorized"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"unauthorized"`
- `"missing_api_key"`
- `"malformed_api_key"`
- `"invalid_api_key"`
