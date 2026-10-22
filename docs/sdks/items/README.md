# Queue.Items

## Overview

### Available Operations

* [list](#list) - Get queue items
* [resolve](#resolve) - Resolve a queue item
* [unresolve](#unresolve) - Unresolve a queue item

## list

Get paginated list of items in a moderation queue with filtering options

### Example Usage

<!-- UsageSnippet language="python" operationID="listQueueItems" method="get" path="/queue/{id}/items" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.list(id="<id>", page=1, page_size=20, sort_direction="desc")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The queue ID                                                                                                                                                                          |
| `page`                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `sort_field`                                                                                                                                                                          | [Optional[models.SortField]](../../models/sortfield.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `sort_direction`                                                                                                                                                                      | [Optional[models.ListQueueItemsSortDirection]](../../models/listqueueitemssortdirection.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Sort direction                                                                                                                                                                        |
| `conversation_ids`                                                                                                                                                                    | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `labels`                                                                                                                                                                              | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `after_date`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `before_date`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `include_resolved`                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `author_id`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `filtered_action_ids`                                                                                                                                                                 | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `project_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The project to act on, when you call with an organization key. Optional when the organization has one project. A project key acts on its own project: naming another one is an error. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

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

Mark a queue item as resolved with a specific moderation action

### Example Usage

<!-- UsageSnippet language="python" operationID="resolveQueueItem" method="post" path="/queue/{id}/items/{itemId}/resolve" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.resolve(id="<id>", item_id="<id>", comment="Reviewed: no violation.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The queue ID                                                                                                                                                                          |
| `item_id`                                                                                                                                                                             | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The item ID to resolve                                                                                                                                                                |
| `project_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The project to act on, when you call with an organization key. Optional when the organization has one project. A project key acts on its own project: naming another one is an error. |
| `comment`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Optional comment                                                                                                                                                                      |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

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

## unresolve

Mark a previously resolved queue item as unresolved/pending

### Example Usage

<!-- UsageSnippet language="python" operationID="unresolveQueueItem" method="post" path="/queue/{id}/items/{itemId}/unresolve" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.queue.items.unresolve(id="<id>", item_id="<id>", comment="Reopened after an appeal.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The queue ID                                                                                                                                                                          |
| `item_id`                                                                                                                                                                             | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The item ID to unresolve                                                                                                                                                              |
| `project_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The project to act on, when you call with an organization key. Optional when the organization has one project. A project key acts on its own project: naming another one is an error. |
| `comment`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Optional reason for unresolving the item                                                                                                                                              |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

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