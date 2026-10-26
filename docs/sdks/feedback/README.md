# Feedback

## Overview

### Available Operations

* [create](#create) - Send feedback

## create

Sends a feature request, bug report or other feedback to the Moderation API team. The team reads every request and can reply by email. Limited to 5 requests per minute per organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="createFeedback" method="post" path="/feedback" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.feedback.create(title="Filter queue items by author trust level", description="We review queue items by hand. We want to see items from new authors first, so we need a filter for trust level on the queue items list.", type_="feature_request", source="mcp")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | A short summary of the request.                                                                                                                                                                                                              |
| `description`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | What you tried to do, why, and what is missing or does not work. Plain text. Blank lines start new paragraphs.                                                                                                                               |
| `project_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The project to act on, by ID or name. Required with an organization key unless the key reaches only one project; list projects with GET /projects. A project key acts on its own project and needs no value: naming another one is an error. |
| `type`                                                                                                                                                                                                                                       | [Optional[models.CreateFeedbackType]](../../models/createfeedbacktype.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | The kind of feedback.                                                                                                                                                                                                                        |
| `source`                                                                                                                                                                                                                                     | [Optional[models.Source]](../../models/source.md)                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                           | Where the feedback was written: MCP server, agent skill, CLI or API.                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.CreateFeedbackResponse](../../models/createfeedbackresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |