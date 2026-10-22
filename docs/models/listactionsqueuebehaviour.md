# ListActionsQueueBehaviour

Whether the action resolves and removes the item, unresolves and re-add it to the queue, or does not change the resolve status.

## Example Usage

```python
from moderation_api.models import ListActionsQueueBehaviour

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ListActionsQueueBehaviour = "REMOVE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"REMOVE"`
- `"ADD"`
- `"NO_CHANGE"`
