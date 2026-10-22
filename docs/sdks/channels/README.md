# Channels

## Overview

### Available Operations

* [list](#list) - List channels
* [create](#create) - Create a channel
* [retrieve](#retrieve) - Get a channel
* [update](#update) - Update a channel
* [delete](#delete) - Delete a channel
* [duplicate](#duplicate) - Duplicate a channel

## list

List the channels in a project. The list is paginated. Needs the `channels:read` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="listChannels" method="get" path="/projects/{projectId}/channels" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.list(project_id="<id>", page=1, page_size=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project.                                              |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListChannelsResponse](../../models/listchannelsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## create

Create a channel in a project, with the default rules. The project's first channel becomes its default. Needs the `channels:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="createChannel" method="post" path="/projects/{projectId}/channels" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.create(project_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                                           | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The ID of the project to add the channel to.                                                                                           |
| `name`                                                                                                                                 | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The channel's name.                                                                                                                    |
| `key`                                                                                                                                  | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The key you pass as `channel` when you moderate content. Defaults to the name in lowercase with dashes. Must be unique in the project. |
| `description`                                                                                                                          | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The channel's description.                                                                                                             |
| `content_type`                                                                                                                         | [Optional[models.CreateChannelContentType]](../../models/createchannelcontenttype.md)                                                  | :heavy_minus_sign:                                                                                                                     | The kind of content the channel moderates.                                                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.Channel](../../models/channel.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get a channel by ID. Needs the `channels:read` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="getChannel" method="get" path="/channels/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the channel.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Channel](../../models/channel.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## update

Update a channel. Fields you leave out keep their value. Needs the `channels:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateChannel" method="put" path="/channels/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                            | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The ID of the channel to update.                                                                                |
| `name`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | The channel's name.                                                                                             |
| `key`                                                                                                           | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | The key you pass as `channel` when you moderate content. Changing it breaks integrations that send the old key. |
| `description`                                                                                                   | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | The channel's description.                                                                                      |
| `content_type`                                                                                                  | [Optional[models.UpdateChannelContentType]](../../models/updatechannelcontenttype.md)                           | :heavy_minus_sign:                                                                                              | The kind of content the channel moderates.                                                                      |
| `flagging_mode`                                                                                                 | [Optional[models.UpdateChannelFlaggingMode]](../../models/updatechannelflaggingmode.md)                         | :heavy_minus_sign:                                                                                              | `ACTIVE` flags content. `DRY_RUN` evaluates content without flagging it.                                        |
| `context_enabled`                                                                                               | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether earlier messages in the conversation are read when moderating a message.                                |
| `enable_image_moderation`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether images are moderated.                                                                                   |
| `enable_video_moderation`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether videos are moderated.                                                                                   |
| `enable_audio_moderation`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether audio is moderated.                                                                                     |
| `enable_voice_moderation`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether real-time voice streams are moderated.                                                                  |
| `include_transcript_in_response`                                                                                | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether audio and video transcripts are returned in responses.                                                  |
| `transcription_quality`                                                                                         | [Optional[models.UpdateChannelTranscriptionQuality]](../../models/updatechanneltranscriptionquality.md)         | :heavy_minus_sign:                                                                                              | Trade-off between transcription speed and accuracy.                                                             |
| `unicode_spoof_detection_enabled`                                                                               | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether look-alike Unicode characters are normalized before moderation.                                         |
| `frame_capture_interval`                                                                                        | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | Seconds between frames captured from a video.                                                                   |
| `max_frames_per_video`                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | The most frames moderated per video.                                                                            |
| `spread_frames`                                                                                                 | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Whether frames are spread evenly across the whole video.                                                        |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.Channel](../../models/channel.md)**

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

Delete a channel. Its key is freed for a new channel. When it was the default, the oldest remaining channel becomes the default. A channel that still moderates a Slack workspace must be disconnected first. Needs the `channels:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteChannel" method="delete" path="/channels/{id}" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the channel.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteChannelResponse](../../models/deletechannelresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |

## duplicate

Copy a channel in its project, with every setting, policy, rule and wordlist. Integrations (Discord, Slack, WordPress) are not copied. Needs the `channels:write` permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="duplicateChannel" method="post" path="/channels/{id}/duplicate" -->
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.channels.duplicate(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | The ID of the channel to copy.                                                                 |
| `name`                                                                                         | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Name of the copy. Defaults to the original name with "(copy)".                                 |
| `key`                                                                                          | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Key of the copy. Defaults to the original key with a timestamp. Must be unique in the project. |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.Channel](../../models/channel.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.BadRequestError           | 400                              | application/json                 |
| errors.AuthenticationError       | 401                              | application/json                 |
| errors.PermissionDeniedError     | 403                              | application/json                 |
| errors.NotFoundError             | 404                              | application/json                 |
| errors.RateLimitError            | 429                              | application/json                 |
| errors.ModerationAPIDefaultError | 4XX, 5XX                         | \*/\*                            |