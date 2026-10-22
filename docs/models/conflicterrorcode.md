# ConflictErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `resource_conflict`: The request conflicts with an existing resource.

## Example Usage

```python
from moderation_api.models import ConflictErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConflictErrorCode = "resource_conflict"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"resource_conflict"`
