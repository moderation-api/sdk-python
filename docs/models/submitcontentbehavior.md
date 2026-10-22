# SubmitContentBehavior

How your recommendation combines with ours. Defaults to 'escalate', which only applies it when stricter than ours; 'override' replaces ours outright.

## Example Usage

```python
from moderation_api.models import SubmitContentBehavior
value: SubmitContentBehavior = "override"
```


## Values

- `"override"`
- `"escalate"`
