# Actions

## Overview

### Available Operations

* [list](#list) - List moderation actions
* [create](#create) - Create an action
* [retrieve](#retrieve) - Get an action
* [update](#update) - Update an action
* [delete](#delete) - Delete an action
* [execute](#execute) - Execute moderation action

## list

List the moderation actions of the project. The list is paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="listActions" method="get" path="/actions" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.list(page=1, page_size=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `queue_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActionsResponse](../../models/listactionsresponse.md)**

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

Create an action.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAction" method="post" path="/actions" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.create(name="Suspend for 24 hours", key="suspend-24h", type_="AUTHOR_BLOCK_TEMP", built_in=False, queue_behaviour="REMOVE", position="ALL_QUEUES", value_required=False, free_text=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                          | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The name of the action.                                                                                                         |
| `key`                                                                                                                           | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | User defined key of the action.                                                                                                 |
| `description`                                                                                                                   | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The description of the action.                                                                                                  |
| `type`                                                                                                                          | [OptionalNullable[models.CreateActionTypeRequest]](../../models/createactiontyperequest.md)                                     | :heavy_minus_sign:                                                                                                              | The type of the action.                                                                                                         |
| `built_in`                                                                                                                      | *OptionalNullable[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                              | Whether the action is a built-in action or a custom one.                                                                        |
| `queue_behaviour`                                                                                                               | [Optional[models.CreateActionQueueBehaviourRequest]](../../models/createactionqueuebehaviourrequest.md)                         | :heavy_minus_sign:                                                                                                              | Whether the action resolves and removes the item, unresolves and re-add it to the queue, or does not change the resolve status. |
| `filter_in_queue_ids`                                                                                                           | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | The IDs of the queues the action is available in.                                                                               |
| `position`                                                                                                                      | [Optional[models.CreateActionPositionRequest]](../../models/createactionpositionrequest.md)                                     | :heavy_minus_sign:                                                                                                              | Show the action in all queues, selected queues or no queues (to use via API only).                                              |
| `possible_values`                                                                                                               | List[[models.CreateActionPossibleValueRequest](../../models/createactionpossiblevaluerequest.md)]                               | :heavy_minus_sign:                                                                                                              | The possible values of the action. The user will be prompted to select one of these values when executing the action.           |
| `value_required`                                                                                                                | *Optional[bool]*                                                                                                                | :heavy_minus_sign:                                                                                                              | Whether the action requires a value to be executed.                                                                             |
| `free_text`                                                                                                                     | *Optional[bool]*                                                                                                                | :heavy_minus_sign:                                                                                                              | Whether the action allows any text to be entered as a value or if it must be one of the possible values.                        |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.CreateActionResponse](../../models/createactionresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.ConflictError             | 409                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get an action by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAction" method="get" path="/actions/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the action to get.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetActionResponse](../../models/getactionresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## update

Update an action.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAction" method="put" path="/actions/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.update(id="<id>", built_in=False, queue_behaviour="NO_CHANGE", position="ALL_QUEUES", value_required=False, free_text=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                            | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The ID of the action to update.                                                                                                 |
| `key`                                                                                                                           | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | User defined key of the action.                                                                                                 |
| `name`                                                                                                                          | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The name of the action.                                                                                                         |
| `description`                                                                                                                   | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The description of the action.                                                                                                  |
| `type`                                                                                                                          | [OptionalNullable[models.UpdateActionTypeRequest]](../../models/updateactiontyperequest.md)                                     | :heavy_minus_sign:                                                                                                              | The type of the action.                                                                                                         |
| `built_in`                                                                                                                      | *OptionalNullable[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                              | Whether the action is a built-in action or a custom one.                                                                        |
| `queue_behaviour`                                                                                                               | [Optional[models.UpdateActionQueueBehaviourRequest]](../../models/updateactionqueuebehaviourrequest.md)                         | :heavy_minus_sign:                                                                                                              | Whether the action resolves and removes the item, unresolves and re-add it to the queue, or does not change the resolve status. |
| `filter_in_queue_ids`                                                                                                           | List[*str*]                                                                                                                     | :heavy_minus_sign:                                                                                                              | The IDs of the queues the action is available in.                                                                               |
| `position`                                                                                                                      | [Optional[models.UpdateActionPositionRequest]](../../models/updateactionpositionrequest.md)                                     | :heavy_minus_sign:                                                                                                              | Show the action in all queues, selected queues or no queues (to use via API only).                                              |
| `possible_values`                                                                                                               | List[[models.UpdateActionPossibleValueRequest](../../models/updateactionpossiblevaluerequest.md)]                               | :heavy_minus_sign:                                                                                                              | The possible values of the action. The user will be prompted to select one of these values when executing the action.           |
| `value_required`                                                                                                                | *Optional[bool]*                                                                                                                | :heavy_minus_sign:                                                                                                              | Whether the action requires a value to be executed.                                                                             |
| `free_text`                                                                                                                     | *Optional[bool]*                                                                                                                | :heavy_minus_sign:                                                                                                              | Whether the action allows any text to be entered as a value or if it must be one of the possible values.                        |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.UpdateActionResponse](../../models/updateactionresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.ConflictError             | 409                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## delete

Delete an action and all of its webhooks.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAction" method="delete" path="/actions/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the action to delete.                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteActionResponse](../../models/deleteactionresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## execute

Execute a moderation action on one or more content items.

### Example Usage

<!-- UsageSnippet language="python" operationID="executeAction" method="post" path="/actions/execute" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.actions.execute(action_key="suspend-24h", author_ids=[
        "user-1092",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `action_key`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | ID or key of the action to execute                                          |
| `content_ids`                                                               | List[*str*]                                                                 | :heavy_minus_sign:                                                          | IDs of the content items to apply the action to. Provide this or authorIds. |
| `author_ids`                                                                | List[*str*]                                                                 | :heavy_minus_sign:                                                          | IDs of the authors to apply the action to. Provide this or contentIds.      |
| `value`                                                                     | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Optional value to provide with the action                                   |
| `queue_id`                                                                  | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Optional queue ID if the action is queue-specific                           |
| `duration`                                                                  | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | Optional duration in milliseconds for actions with timeouts                 |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ExecuteActionResponse](../../models/executeactionresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |