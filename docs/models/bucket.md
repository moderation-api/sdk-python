# Bucket

The size of each entry in `volumes`.

## Example Usage

```python
from moderation_api.models import Bucket

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Bucket = "hour"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"hour"`
- `"day"`
