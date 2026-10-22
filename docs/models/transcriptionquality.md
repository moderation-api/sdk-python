# TranscriptionQuality

Trade-off between transcription speed and accuracy.

## Example Usage

```python
from moderation_api.models import TranscriptionQuality

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TranscriptionQuality = "SPEED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"SPEED"`
- `"BALANCED"`
- `"ACCURACY"`
