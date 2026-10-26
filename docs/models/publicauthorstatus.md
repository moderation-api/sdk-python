# PublicAuthorStatus

Current author status

## Example Usage

```python
from moderation_api.models import PublicAuthorStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PublicAuthorStatus = "enabled"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"enabled"`
- `"suspended"`
- `"blocked"`
