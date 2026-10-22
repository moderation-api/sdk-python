# Verdict

The ruling your past decisions point to for this content.

## Example Usage

```python
from moderation_api.models import Verdict

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Verdict = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"reject"`
