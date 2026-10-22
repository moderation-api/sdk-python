# GetQueueContentType

## Example Usage

```python
from moderation_api.models import GetQueueContentType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetQueueContentType = "profile"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"profile"`
- `"message"`
- `"post"`
- `"comment"`
- `"event"`
- `"product"`
- `"review"`
- `"voice"`
- `"other"`
