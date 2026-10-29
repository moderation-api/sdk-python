# Queue.Items

## Overview

### Available Operations

* [list](#list) - List queue items
* [resolve](#resolve) - Resolve a queue item
* [resolve_many](#resolve_many) - Resolve queue items
* [unresolve](#unresolve) - Unresolve a queue item

## list

List the items of a review queue, with the filters and the date window of the queue applied. By default only pending items. The list is paginated. Use the item `id` or `contentId` to resolve or unresolve an item.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQueueItems" method="get" path="/queue/{id}/items" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.list(id="<id>", page=1, page_size=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The queue ID.                                                                                                                                                                                                                                |
| `page`                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `page_size`                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `sort`                                                                                                                                                                                                                                       | [Optional[models.Sort]](../../models/sort.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `include_resolved`                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `conversation_ids`                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `labels`                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `author_id`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `filtered_action_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `after_date`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `before_date`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                          |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.ListQueueItemsResponse](../../models/listqueueitemsresponse.md)**

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

## resolve

Mark an item of a queue as resolved. It is the same as a check-off in the dashboard: the item leaves the pending list and a QUEUE_ITEM_COMPLETED webhook is sent. `itemId` is the item `id` or your `contentId`. To also take a moderation action, use `POST /actions/execute`.

### Example Usage

<!-- UsageSnippet language="python" operationID="resolveQueueItem" method="post" path="/queue/{id}/items/{itemId}/resolve" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.resolve(id="<id>", item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | The queue ID.                                                                                                                                                                                                                                  |
| `item_id`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | The item to resolve: the item `id` from `GET /queue/{id}/items`, or the `contentId` you sent to `POST /moderate` (webhooks send it as `item.id`). For a content ID, the newest submission with that content ID is used, as the queue shows it. |
| `project_id`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error.   |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |

### Response

**[models.ResolveQueueItemResponse](../../models/resolvequeueitemresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## resolve_many

Mark up to 100 items of a queue as resolved in one request. Each item is resolved the same as with `POST /queue/{id}/items/{itemId}/resolve`, and each ID is an item `id` or your `contentId`. IDs that match no item in the project are skipped and returned in `notFoundIds`.

### Example Usage

<!-- UsageSnippet language="python" operationID="resolveQueueItems" method="post" path="/queue/{id}/items/resolve" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.resolve_many(id="<id>", item_ids=[
        "clx8k2v0e000108l4a9bz3f7q",
        "clx8k2v0e000208l4h2mc6d1r",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                 | The queue ID.                                                                                                                                                                                                                                                      |
| `item_ids`                                                                                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                 | The items to resolve, up to 100. Each is the item `id` from `GET /queue/{id}/items`, or the `contentId` you sent to `POST /moderate` (webhooks send it as `item.id`). For a content ID, the newest submission with that content ID is used, as the queue shows it. |
| `project_id`                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                 | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error.                       |
| `retries`                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                |

### Response

**[models.ResolveQueueItemsResponse](../../models/resolvequeueitemsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## unresolve

Mark a resolved item of a queue as pending again. It is the same as removing a check-off in the dashboard: the item comes back in the pending list. `itemId` is the item `id` or your `contentId`.

### Example Usage

<!-- UsageSnippet language="python" operationID="unresolveQueueItem" method="post" path="/queue/{id}/items/{itemId}/unresolve" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.unresolve(id="<id>", item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | The queue ID.                                                                                                                                                                                                                                    |
| `item_id`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | The item to unresolve: the item `id` from `GET /queue/{id}/items`, or the `contentId` you sent to `POST /moderate` (webhooks send it as `item.id`). For a content ID, the newest submission with that content ID is used, as the queue shows it. |
| `project_id`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error.     |
| `retries`                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                              |

### Response

**[models.UnresolveQueueItemResponse](../../models/unresolvequeueitemresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.InternalServerError       | 500                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |