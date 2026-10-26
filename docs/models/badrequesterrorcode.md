# BadRequestErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `invalid_request`: A parameter is invalid. `message` says which one.
- `project_id_required`: An organization key called a project endpoint without naming the project in `Project-Id`, and the key reaches more than one project. `message` lists the projects it reaches.
- `project_name_ambiguous`: The name in `Project-Id` fits more than one project the key reaches. `message` lists them; name the project by ID instead.
- `validation_failed`: The request body does not match the schema. `issues` lists each problem with its `path`.

## Example Usage

```python
from moderation_api.models import BadRequestErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BadRequestErrorCode = "invalid_request"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_request"`
- `"project_id_required"`
- `"project_name_ambiguous"`
- `"validation_failed"`
