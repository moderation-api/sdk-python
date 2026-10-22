# UpdateActionTypeResponse

## Example Usage

```python
from moderation_api.models import UpdateActionTypeResponse

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UpdateActionTypeResponse = "AUTHOR_BLOCK"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"AUTHOR_BLOCK"`
- `"AUTHOR_BLOCK_TEMP"`
- `"AUTHOR_UNBLOCK"`
- `"AUTHOR_DELETE"`
- `"AUTHOR_REPORT"`
- `"AUTHOR_WARN"`
- `"AUTHOR_CUSTOM"`
- `"ITEM_REJECT"`
- `"ITEM_ALLOW"`
- `"ITEM_CUSTOM"`
