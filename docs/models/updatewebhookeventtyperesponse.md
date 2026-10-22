# UpdateWebhookEventTypeResponse

## Example Usage

```python
from moderation_api.models import UpdateWebhookEventTypeResponse

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UpdateWebhookEventTypeResponse = "QUEUE_ITEM_NEW"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"QUEUE_ITEM_NEW"`
- `"QUEUE_ITEM_COMPLETED"`
- `"QUEUE_ITEM_ACTION"`
- `"QUEUE_ITEM_REJECTED"`
- `"QUEUE_ITEM_ALLOWED"`
- `"AUTHOR_BLOCKED"`
- `"AUTHOR_UNBLOCKED"`
- `"AUTHOR_SUSPENDED"`
- `"AUTHOR_UPDATED"`
- `"AUTHOR_TRUST_LEVEL_CHANGED"`
- `"AUTHOR_ACTION"`
