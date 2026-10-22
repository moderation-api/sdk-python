# UpdateActionQueueBehaviourRequest

Whether the action resolves and removes the item, unresolves and re-add it to the queue, or does not change the resolve status.

## Example Usage

```python
from moderation_api.models import UpdateActionQueueBehaviourRequest
value: UpdateActionQueueBehaviourRequest = "REMOVE"
```


## Values

- `"REMOVE"`
- `"ADD"`
- `"NO_CHANGE"`
