# Value

## Example Usage

```python
from moderation_api.models import Value

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Value = "positive"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"positive"`
- `"neutral"`
- `"negative"`
