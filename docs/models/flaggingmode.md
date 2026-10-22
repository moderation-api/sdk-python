# FlaggingMode

`ACTIVE` flags content. `DRY_RUN` evaluates content without flagging it.

## Example Usage

```python
from moderation_api.models import FlaggingMode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FlaggingMode = "DRY_RUN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DRY_RUN"`
- `"ACTIVE"`
