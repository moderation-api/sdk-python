# Authors

## Overview

### Available Operations

* [list](#list) - List authors
* [create](#create) - Create a new author
* [retrieve](#retrieve) - Get author details
* [update](#update) - Update author details
* [delete](#delete) - Delete an author
* [block](#block) - Block author
* [suspend](#suspend) - Suspend author
* [unblock](#unblock) - Unblock author

## list

List the authors of the project, with their status, trust level and content metrics. The list is paginated. By default, the authors that were active most recently come first.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAuthors" method="get" path="/authors" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.list(request={})

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListAuthorsRequest](../../models/listauthorsrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAuthorsResponse](../../models/listauthorsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## create

Create a new author. Typically not needed as authors are created automatically when content is moderated.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAuthor" method="post" path="/authors" -->
```python
from moderation_api import ModerationAPI, models
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.create(external_id="user-1092", name="Jamie Rivera", email="jamie@example.com", metadata=models.CreateAuthorMetadata(
        email_verified=True,
        is_paying_customer=False,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `external_id`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | External ID of the user, typically the ID of the author in your database.                                                                                                                                                                    |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `profile_picture`                                                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | URL of the author's profile picture                                                                                                                                                                                                          |
| `external_link`                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | URL of the author's external profile                                                                                                                                                                                                         |
| `name`                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | Author name or identifier                                                                                                                                                                                                                    |
| `email`                                                                                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | Author email address                                                                                                                                                                                                                         |
| `company`                                                                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | The author's company or organization                                                                                                                                                                                                         |
| `metadata`                                                                                                                                                                                                                                   | [Optional[models.CreateAuthorMetadata]](../../models/createauthormetadata.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                           | Additional metadata provided by your system. We recommend including any relevant information that may assist in the moderation process.                                                                                                      |
| `first_seen`                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | Timestamp when author first appeared                                                                                                                                                                                                         |
| `last_seen`                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | Timestamp of last activity                                                                                                                                                                                                                   |
| `manual_trust_level`                                                                                                                                                                                                                         | *OptionalNullable[float]*                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.PublicAuthor](../../models/publicauthor.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get detailed information about a specific author including historical data and analysis

### Example Usage

<!-- UsageSnippet language="python" operationID="getAuthor" method="get" path="/authors/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.PublicAuthor](../../models/publicauthor.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## update

Update the details of a specific author

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAuthor" method="put" path="/authors/{id}" -->
```python
from moderation_api import ModerationAPI, models
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.update(id="<id>", metadata=models.UpdateAuthorMetadata(
        identity_verified=True,
    ), manual_trust_level=2.0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `profile_picture`                                                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | URL of the author's profile picture                                                                                                                                                                                                          |
| `external_link`                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | URL of the author's external profile                                                                                                                                                                                                         |
| `name`                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | Author name or identifier                                                                                                                                                                                                                    |
| `email`                                                                                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | Author email address                                                                                                                                                                                                                         |
| `company`                                                                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                           | The author's company or organization                                                                                                                                                                                                         |
| `metadata`                                                                                                                                                                                                                                   | [Optional[models.UpdateAuthorMetadata]](../../models/updateauthormetadata.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                           | Additional metadata provided by your system. We recommend including any relevant information that may assist in the moderation process.                                                                                                      |
| `first_seen`                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | Timestamp when author first appeared                                                                                                                                                                                                         |
| `last_seen`                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | Timestamp of last activity                                                                                                                                                                                                                   |
| `manual_trust_level`                                                                                                                                                                                                                         | *OptionalNullable[float]*                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.PublicAuthor](../../models/publicauthor.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## delete

Delete a specific author. This resets the author: status, blocks, trust level, metrics and action history are removed. The author is created again with a clean record the next time content is moderated for the same ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAuthor" method="delete" path="/authors/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.DeleteAuthorResponse](../../models/deleteauthorresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## block

Block an author with the built-in block action. A blocked author cannot post new content until unblocked.

### Example Usage

<!-- UsageSnippet language="python" operationID="blockAuthor" method="post" path="/authors/{id}/block" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.block(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `reason`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Why the action was taken. Saved with the action and sent in the webhook event.                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.BlockAuthorResponse](../../models/blockauthorresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## suspend

Block an author for a limited time with the built-in suspend action.

### Example Usage

<!-- UsageSnippet language="python" operationID="suspendAuthor" method="post" path="/authors/{id}/suspend" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.suspend(id="<id>", reason="Violation of community guidelines", duration=604800000.0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `reason`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Why the action was taken. Saved with the action and sent in the webhook event.                                                                                                                                                               |
| `duration`                                                                                                                                                                                                                                   | *Optional[float]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | How long the suspension lasts, in milliseconds. Defaults to 24 hours.                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.SuspendAuthorResponse](../../models/suspendauthorresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## unblock

Unblock a blocked or suspended author with the built-in unblock action, so they can post new content again.

### Example Usage

<!-- UsageSnippet language="python" operationID="unblockAuthor" method="post" path="/authors/{id}/unblock" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.unblock(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Either external ID or the ID assigned by moderation API.                                                                                                                                                                                     |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `reason`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Why the action was taken. Saved with the action and sent in the webhook event.                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.UnblockAuthorResponse](../../models/unblockauthorresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |