# ReasonCodeEnum

## Example Usage

```python
from moderation_api.models import ReasonCodeEnum

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ReasonCodeEnum = "severity_reject"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"severity_reject"`
- `"severity_review"`
- `"author_block"`
- `"dry_run"`
- `"trusted_allow"`
- `"untrusted_severity"`
- `"rule_match"`
- `"rule_default"`
- `"rule_fallback"`
- `"client_override"`
- `"casebook_match"`
