# Wordlist.Words

## Overview

### Available Operations

* [add](#add) - Add words to wordlist
* [remove](#remove) - Remove words from wordlist

## add

Add words to an existing wordlist

### Example Usage

<!-- UsageSnippet language="python" operationID="addWordlistWords" method="post" path="/wordlist/{id}/words" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.words.add(id="<id>", words=[
        "free money",
        "click here",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | ID of the wordlist to add words to                                                                                                                                                    |
| `words`                                                                                                                                                                               | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | Array of words to add to the wordlist. Duplicate words will be ignored.                                                                                                               |
| `project_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The project to act on, when you call with an organization key. Optional when the organization has one project. A project key acts on its own project: naming another one is an error. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.AddWordlistWordsResponse](../../models/addwordlistwordsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## remove

Remove words from an existing wordlist

### Example Usage

<!-- UsageSnippet language="python" operationID="removeWordlistWords" method="delete" path="/wordlist/{id}/words" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.wordlist.words.remove(id="<id>", words=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                  | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | ID of the wordlist to remove words from                                                                                                                                               |
| `words`                                                                                                                                                                               | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | Array of words to remove from the wordlist                                                                                                                                            |
| `project_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | The project to act on, when you call with an organization key. Optional when the organization has one project. A project key acts on its own project: naming another one is an error. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.RemoveWordlistWordsResponse](../../models/removewordlistwordsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |