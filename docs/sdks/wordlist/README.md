# Wordlist

## Overview

### Available Operations

* [list](#list) - List wordlists
* [create](#create) - Create wordlist
* [retrieve](#retrieve) - Get wordlist
* [update](#update) - Update wordlist
* [get_embedding_status](#get_embedding_status) - Get embedding status

## list

List the wordlists of the organization. The list is paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="listWordlists" method="get" path="/wordlist" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.list(page=1, page_size=20)

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

**[models.ListWordlistsResponse](../../models/listwordlistsresponse.md)**

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

Create a wordlist in the organization. You can add words now or later. Each word is embedded in the background for similarity matching. Use the embedding status endpoint to follow the progress. To use the wordlist in moderation, add it to a policy.

### Example Usage

<!-- UsageSnippet language="python" operationID="createWordlist" method="post" path="/wordlist" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.create(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | Name of the wordlist                                                                                                                                                                                                                         |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `key`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Key of the wordlist. Default: made from the name. If the key is already in use, a suffix is added.                                                                                                                                           |
| `description`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Description of the wordlist                                                                                                                                                                                                                  |
| `words`                                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                           | Words to add to the wordlist. Words are converted to lowercase. Duplicate and empty words are ignored. Maximum 5000 words.                                                                                                                   |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.CreateWordlistResponse](../../models/createwordlistresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get a specific wordlist by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getWordlist" method="get" path="/wordlist/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | ID of the wordlist to get                                                                                                                                                                                                                    |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.GetWordlistResponse](../../models/getwordlistresponse.md)**

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

Update a wordlist. Fields that you do not send stay the same. If you send words, they replace all existing words, and the embeddings are updated in the background.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWordlist" method="put" path="/wordlist/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | ID of the wordlist to update                                                                                                                                                                                                                 |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `name`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | New name for the wordlist                                                                                                                                                                                                                    |
| `key`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | New key for the wordlist                                                                                                                                                                                                                     |
| `description`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | New description for the wordlist                                                                                                                                                                                                             |
| `words`                                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                           | New words for the wordlist. Replace the existing words with these new ones. Words are converted to lowercase. Duplicate and empty words are ignored. Maximum 5000 words.                                                                     |
| `strict`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Deprecated. Now using threshold in project settings.                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.UpdateWordlistResponse](../../models/updatewordlistresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## get_embedding_status

Get the current embedding progress status for a wordlist

### Example Usage

<!-- UsageSnippet language="python" operationID="getWordlistEmbeddingStatus" method="get" path="/wordlist/{id}/embedding-status" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.get_embedding_status(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | ID of the wordlist to check embedding status for                                                                                                                                                                                             |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.GetWordlistEmbeddingStatusResponse](../../models/getwordlistembeddingstatusresponse.md)**

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