# GetQueueType

## Example Usage

```python
from moderation_api.models import GetQueueType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetQueueType = "FLAGGED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"FLAGGED"`
- `"NOT_FLAGGED"`
- `"THRESHOLDS"`
- `"MATCHED"`
