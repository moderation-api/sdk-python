# IsFlagged

## Example Usage

```python
from moderation_api.models import IsFlagged

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IsFlagged = "ALL"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ALL"`
- `"FLAGGED"`
- `"NOT_FLAGGED"`
- `"SHADOW_FLAGGED"`
