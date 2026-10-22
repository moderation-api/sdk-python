# ListWebhooksPayloadVersion

Payload envelope version. V2 is the Stripe-style envelope; V1 is the legacy flat shape and is read-only via this API.

## Example Usage

```python
from moderation_api.models import ListWebhooksPayloadVersion

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ListWebhooksPayloadVersion = "V1"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"V1"`
- `"V2"`
