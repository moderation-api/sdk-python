# InternalServerErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `internal_error`: Something went wrong on our side. Retry with backoff.

## Example Usage

```python
from moderation_api.models import InternalServerErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InternalServerErrorCode = "internal_error"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"internal_error"`
