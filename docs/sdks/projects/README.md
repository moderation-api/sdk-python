# Projects

## Overview

### Available Operations

* [list](#list) - List projects
* [create](#create) - Create a project
* [retrieve](#retrieve) - Get a project
* [update](#update) - Update a project
* [delete](#delete) - Delete a project
* [duplicate](#duplicate) - Duplicate a project

## list

List the projects in the organization. The list is paginated. Needs the `projects:read` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="listProjects" method="get" path="/projects" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.list(page=1, page_size=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListProjectsResponse](../../models/listprojectsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## create

Create a project with one channel, a review queue inbox and a secret API key. Give a domain or context and the project suggests policies for the platform. Needs the `projects:write` permission and a key that reaches all projects.

### Example Usage

<!-- UsageSnippet language="python" operationID="createProject" method="post" path="/projects" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.create(name="<value>", used_by_minors=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `name`                                                                                              | *str*                                                                                               | :heavy_check_mark:                                                                                  | The project's name.                                                                                 |
| `domain`                                                                                            | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | The website or app the project moderates content for. Used to write the context when none is given. |
| `context`                                                                                           | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | What the platform is and who uses it.                                                               |
| `brief`                                                                                             | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | What you moderate, the problems you see and your guidelines.                                        |
| `used_by_minors`                                                                                    | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether children use the platform.                                                                  |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ProjectWithKey](../../models/projectwithkey.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get a project by ID. Needs the `projects:read` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProject" method="get" path="/projects/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Project](../../models/project.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## update

Update a project. Fields you leave out keep their value. Needs the `projects:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateProject" method="put" path="/projects/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                      | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the project to update.                                                                          |
| `name`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | The project's name.                                                                                       |
| `description`                                                                                             | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | The project's description.                                                                                |
| `domain`                                                                                                  | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | The website or app the project moderates content for. Setting it on a project without context writes one. |
| `context`                                                                                                 | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | What the platform is and who uses it.                                                                     |
| `global_flagging_mode`                                                                                    | [Optional[models.UpdateProjectGlobalFlaggingMode]](../../models/updateprojectglobalflaggingmode.md)       | :heavy_minus_sign:                                                                                        | `ACTIVE` flags content. `DRY_RUN` evaluates without flagging.                                             |
| `enable_request_logging`                                                                                  | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Whether moderated content is stored and shown in the dashboard.                                           |
| `casebook_enabled`                                                                                        | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Whether review queue decisions are recorded in the casebook.                                              |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.Project](../../models/project.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## delete

Delete a project with everything in it: channels, queues, API keys and stored content. This can't be undone. The project's API keys stop working at once. Needs the `projects:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteProject" method="delete" path="/projects/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteProjectResponse](../../models/deleteprojectresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## duplicate

Copy a project's configuration into a new project: its settings, every channel with its policies, rules and wordlists, its moderation actions and its review queues. The copy gets its own secret API key. Webhooks, integrations, API keys and content are not copied. Needs the `projects:write` permission and a key that reaches all projects.

### Example Usage

<!-- UsageSnippet language="python" operationID="duplicateProject" method="post" path="/projects/{id}/duplicate" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.projects.duplicate(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to copy.                                      |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Name of the copy. Defaults to the original name with "(copy)".      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProjectWithKey](../../models/projectwithkey.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |