# AuthorStatus

Current author status

## Example Usage

```python
from moderation_api.models import AuthorStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuthorStatus = "enabled"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"enabled"`
- `"suspended"`
- `"blocked"`
