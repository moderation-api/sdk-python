# CasebookAgreement

## Example Usage

```python
from moderation_api.models import CasebookAgreement

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CasebookAgreement = "ALL"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ALL"`
- `"OVERRULED"`
- `"AGREED"`
