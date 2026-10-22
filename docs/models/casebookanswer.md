# CasebookAnswer

## Example Usage

```python
from moderation_api.models import CasebookAnswer

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CasebookAnswer = "ALL"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ALL"`
- `"ALLOWED"`
- `"REJECTED"`
- `"NO_ANSWER"`
