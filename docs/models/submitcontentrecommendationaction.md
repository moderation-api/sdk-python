# SubmitContentRecommendationAction

The action to take based on the recommendation

## Example Usage

```python
from moderation_api.models import SubmitContentRecommendationAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SubmitContentRecommendationAction = "review"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"review"`
- `"allow"`
- `"reject"`
