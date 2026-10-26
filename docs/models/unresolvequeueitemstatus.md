# UnresolveQueueItemStatus

`pending` waits for review. `resolved` is reviewed.

## Example Usage

```python
from moderation_api.models import UnresolveQueueItemStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UnresolveQueueItemStatus = "pending"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"pending"`
- `"resolved"`
