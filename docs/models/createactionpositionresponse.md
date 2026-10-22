# CreateActionPositionResponse

Show the action in all queues, selected queues or no queues (to use via API only).

## Example Usage

```python
from moderation_api.models import CreateActionPositionResponse

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CreateActionPositionResponse = "ALL_QUEUES"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ALL_QUEUES"`
- `"SOME_QUEUES"`
- `"HIDDEN"`
