# WithinUnit

## Example Usage

```python
from moderation_api.models import WithinUnit

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WithinUnit = "MINUTES"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"MINUTES"`
- `"HOURS"`
- `"DAYS"`
- `"WEEKS"`
- `"MONTHS"`
- `"YEARS"`
