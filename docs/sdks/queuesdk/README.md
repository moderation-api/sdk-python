# Queue

## Overview

### Available Operations

* [list](#list) - List queues
* [retrieve](#retrieve) - Get a queue
* [get_stats](#get_stats) - Get queue statistics

## list

List the review queues of the project. The default queue comes first. The list is paginated. To get the item counts of a queue, use `GET /queue/{id}`.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQueues" method="get" path="/queue" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.list(page=1, page_size=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `page_size`                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.ListQueuesResponse](../../models/listqueuesresponse.md)**

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

## retrieve

Get a review queue with its item counts. The counts use the filters and the date window of the queue, the same as the dashboard.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQueue" method="get" path="/queue/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The queue ID.                                                                                                                                                                                                                                |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.GetQueueResponse](../../models/getqueueresponse.md)**

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

## get_stats

Get review statistics of a queue for a period: resolved and pending items, the top reviewers and the resolved items per day.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQueueStats" method="get" path="/queue/{id}/stats" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.get_stats(id="<id>", within_days=30)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The queue ID.                                                                                                                                                                                                                                |
| `within_days`                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.GetQueueStatsResponse](../../models/getqueuestatsresponse.md)**

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