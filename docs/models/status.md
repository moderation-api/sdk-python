# Status

Current author status

## Example Usage

```python
from moderation_api.models import Status

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Status = "enabled"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"enabled"`
- `"suspended"`
- `"blocked"`
