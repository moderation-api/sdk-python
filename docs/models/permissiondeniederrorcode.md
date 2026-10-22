# PermissionDeniedErrorCode

Exactly what went wrong. Stable; safe to branch on. New codes may be added.

- `permission_denied`: The API key cannot perform this request.
- `account_disabled`: The organization account is disabled.
- `quota_exceeded`: The organization has used all API requests on its plan.
- `plan_feature_unavailable`: The current plan does not include this feature.
- `plan_limit_exceeded`: The request goes over a limit of the current plan.
- `project_key_required`: This endpoint needs a project API key, but an organization key was used.
- `organization_key_required`: This endpoint needs an organization API key, but a project key was used.
- `missing_key_permission`: The organization key does not have the permission this endpoint needs.
- `project_not_reachable`: The organization key is limited to other projects.

## Example Usage

```python
from moderation_api.models import PermissionDeniedErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PermissionDeniedErrorCode = "permission_denied"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"permission_denied"`
- `"account_disabled"`
- `"quota_exceeded"`
- `"plan_feature_unavailable"`
- `"plan_limit_exceeded"`
- `"project_key_required"`
- `"organization_key_required"`
- `"missing_key_permission"`
- `"project_not_reachable"`
