# ActionResponse

The action to take based on the recommendation

## Example Usage

```python
from moderation_api.models import ActionResponse

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ActionResponse = "review"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"review"`
- `"allow"`
- `"reject"`
