# Projects.ApiKeys

## Overview

### Available Operations

* [create](#create) - Create a project API key

## create

Create a new secret API key for a project and return it. Give each app or computer its own key, so you can revoke one without breaking the others. The project's existing keys keep working. Needs the `projects:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="createProjectApiKey" method="post" path="/projects/{id}/api-keys" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.api_keys.create(id="<id>", name="API key")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                       | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | The ID of the project.                                                                                                                     |
| `name`                                                                                                                                     | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | A name for the key, shown on the API keys page of the dashboard. Name it after where the key is used, for example the app or the computer. |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[models.ProjectAPIKey](../../models/projectapikey.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |