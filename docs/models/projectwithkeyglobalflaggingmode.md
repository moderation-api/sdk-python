# ProjectWithKeyGlobalFlaggingMode

`ACTIVE` flags content. `DRY_RUN` evaluates content without flagging it, for testing a setup.

## Example Usage

```python
from moderation_api.models import ProjectWithKeyGlobalFlaggingMode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProjectWithKeyGlobalFlaggingMode = "DRY_RUN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DRY_RUN"`
- `"ACTIVE"`
