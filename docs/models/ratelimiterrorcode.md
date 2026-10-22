# RateLimitErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `rate_limit_exceeded`: Too many requests. Wait for the `Retry-After` seconds.

## Example Usage

```python
from moderation_api.models import RateLimitErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RateLimitErrorCode = "rate_limit_exceeded"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"rate_limit_exceeded"`
