# BadRequestErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `invalid_request`: A parameter is invalid. `message` says which one.
- `validation_failed`: The request body does not match the schema. `issues` lists each problem with its `path`.

## Example Usage

```python
from moderation_api.models import BadRequestErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BadRequestErrorCode = "invalid_request"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_request"`
- `"validation_failed"`
