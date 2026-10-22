<!-- Start Custom [intro] -->
# Moderation API Python SDK

[![PyPI](https://img.shields.io/pypi/v/moderation_api.svg)](https://pypi.org/project/moderation_api/)

The official Python library for [Moderation API](https://moderationapi.com). Use it to moderate text, images, video and audio, manage authors, review queues, actions and wordlists, and verify webhooks. It supports both synchronous and `asyncio` code.

- Get an API key in the [dashboard](https://dash.moderationapi.com).
- Read the [documentation](https://docs.moderationapi.com) and the [API reference](https://docs.moderationapi.com/api-reference/introduction).
<!-- End Custom [intro] -->

<!-- Start Summary [summary] -->
## Summary

Moderation API: Moderate text, images, video and audio in real time, manage authors, review queues and actions, and receive webhooks.

More information about the API can be found at https://docs.moderationapi.com
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Moderation API Python SDK](#moderation-api-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Moderating content](#moderating-content)
  * [Verifying webhooks](#verifying-webhooks)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Timeouts](#timeouts)
  * [Requirements](#requirements)
  * [Support](#support)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add moderation_api
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install moderation_api
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add moderation_api
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from moderation_api python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "moderation_api",
# ]
# ///

from moderation_api import ModerationAPI

sdk = ModerationAPI(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.content.submit(content={
        "type": "text",
        "text": "Hey, check out my profile for a deal!",
    }, content_id="message-48213", author_id="user-1092", conversation_id="room-general", metadata={
        "platform": "ios",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from moderation_api import ModerationAPI
import os

async def main():

    async with ModerationAPI(
        secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
    ) as ma_client:

        res = await ma_client.content.submit_async(content={
            "type": "text",
            "text": "Hey, check out my profile for a deal!",
        }, content_id="message-48213", author_id="user-1092", conversation_id="room-general", metadata={
            "platform": "ios",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->
<!-- Start Custom [guide] -->
## Moderating content

Use `content.submit` to moderate text, images, video, audio, or objects with several fields. All parameters except `content` are optional.

The client reads your API key from the `MODAPI_SECRET_KEY` environment variable. To set it in code, pass `secret_key`.

```python
from moderation_api import ModerationAPI

with ModerationAPI() as client:  # reads MODAPI_SECRET_KEY
    # Text
    client.content.submit(
        content={"type": "text", "text": "Your text here"},
        content_id="message-123",  # your ID for the content
        author_id="user-123",  # your ID for the user who wrote it
        conversation_id="room-123",  # groups related content
        metadata={"platform": "ios"},
    )

    # Image, video and audio: send a URL
    client.content.submit(content={"type": "image", "url": "https://example.com/image.jpg"})
    client.content.submit(content={"type": "video", "url": "https://example.com/video.mp4"})
    client.content.submit(content={"type": "audio", "url": "https://example.com/audio.mp3"})

    # An object with several fields, moderated together
    client.content.submit(
        content={
            "type": "object",
            "data": {
                "title": {"type": "text", "text": "Post title"},
                "body": {"type": "text", "text": "Post content"},
                "thumbnail": {"type": "image", "url": "https://example.com/thumb.jpg"},
            },
        },
    )
```

Every method has an `async` version with the suffix `_async`, for example `await client.content.submit_async(...)`.

### Using the result

`evaluation.flagged` tells you if any policy flagged the content. `recommendation.action` is the action the API recommends after it applies your thresholds and rules: `allow`, `review` or `reject`.

```python
from moderation_api import ModerationAPI

with ModerationAPI() as client:
    result = client.content.submit(content={"type": "text", "text": "Some content"})

    if result.evaluation.flagged:
        print("A policy flagged the content")

    if result.recommendation.action == "reject":
        pass  # Block the content
    elif result.recommendation.action == "review":
        pass  # Publish or hold it, and send it to a review queue
    else:
        pass  # Publish the content

    for policy in result.policies:
        print(f"{policy.id}: flagged={policy.flagged}")
```

## Verifying webhooks

Moderation API signs every webhook delivery with your project's webhook signing secret. The signature is in the `modapi-signature` header.

### Webhook signing secret

Find the secret on the [API keys page in the dashboard](https://dash.moderationapi.com/project/latest/configure/api-keys), or get it with `client.webhook_secret.retrieve()`. Store it in the `MODAPI_WEBHOOK_SECRET` environment variable. It is not your API key. Get it once, for example in a setup script, and do not call `retrieve` for each delivery, so verification does not depend on a call to the API. Keep it as secret as your API key: anyone with it can sign webhooks.

### Verify a delivery

`construct_event` checks the signature against the raw body and returns the event as a dictionary. It reads the secret from `MODAPI_WEBHOOK_SECRET`; to set it in code, pass `secret`. It raises `WebhookSignatureError` if the signature does not match.

```python
from flask import Flask, request
from moderation_api.webhook_signature import WebhookSignatureError, construct_event

app = Flask(__name__)

@app.post("/webhooks/moderation")
def moderation_webhook():
    try:
        event = construct_event(
            request.get_data(),  # the raw body, not parsed JSON
            request.headers.get("modapi-signature", ""),
        )
    except WebhookSignatureError:
        return "Invalid signature", 400

    print(event["type"])
    return "", 200
```
<!-- End Custom [guide] -->


<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name         | Type | Scheme      | Environment Variable |
| ------------ | ---- | ----------- | -------------------- |
| `secret_key` | http | HTTP Bearer | `MODAPI_SECRET_KEY`  |

To authenticate with the API the `secret_key` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->
<!-- Start Custom [auth] -->
### Project and organization keys

Moderation API has two kinds of API keys:

- A **project key** works with one project: content, authors, review queues, actions, wordlists, webhooks and the account. Most integrations need only this key.
- An **organization key** works with the [management API](https://docs.moderationapi.com/api-reference/management-api): projects and channels. The management API is available on Enterprise plans.

Each key works only with its own endpoints. With the wrong key the API returns `403` with the code `project_key_required` or `organization_key_required`. If you use both, create one client for each key:

```python
import os
from moderation_api import ModerationAPI

# Project key, from MODAPI_SECRET_KEY
client = ModerationAPI()

# Organization key
management = ModerationAPI(secret_key=os.environ["MODAPI_ORGANIZATION_KEY"])

res = management.projects.list()
while res is not None:
    for project in res.result.data:
        print(project.id, project.name)
    res = res.next()
```

Create the organization client only where you manage projects and channels, for example in a setup script, and keep the organization key out of the code that moderates content.
<!-- End Custom [auth] -->


<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Account](docs/sdks/account/README.md)

* [retrieve](docs/sdks/account/README.md#retrieve) - Get account details

### [Actions](docs/sdks/actions/README.md)

* [list](docs/sdks/actions/README.md#list) - List moderation actions
* [create](docs/sdks/actions/README.md#create) - Create an action
* [retrieve](docs/sdks/actions/README.md#retrieve) - Get an action
* [update](docs/sdks/actions/README.md#update) - Update an action
* [delete](docs/sdks/actions/README.md#delete) - Delete an action
* [execute](docs/sdks/actions/README.md#execute) - Execute moderation action

### [Authors](docs/sdks/authors/README.md)

* [list](docs/sdks/authors/README.md#list) - List authors
* [create](docs/sdks/authors/README.md#create) - Create a new author
* [retrieve](docs/sdks/authors/README.md#retrieve) - Get author details
* [update](docs/sdks/authors/README.md#update) - Update author details
* [delete](docs/sdks/authors/README.md#delete) - Delete an author

### [Channels](docs/sdks/channels/README.md)

* [list](docs/sdks/channels/README.md#list) - List channels
* [create](docs/sdks/channels/README.md#create) - Create a channel
* [retrieve](docs/sdks/channels/README.md#retrieve) - Get a channel
* [update](docs/sdks/channels/README.md#update) - Update a channel
* [delete](docs/sdks/channels/README.md#delete) - Delete a channel
* [duplicate](docs/sdks/channels/README.md#duplicate) - Duplicate a channel

### [Content](docs/sdks/contentsdk/README.md)

* [submit](docs/sdks/contentsdk/README.md#submit) - Submit content

### [Projects](docs/sdks/projects/README.md)

* [list](docs/sdks/projects/README.md#list) - List projects
* [create](docs/sdks/projects/README.md#create) - Create a project
* [retrieve](docs/sdks/projects/README.md#retrieve) - Get a project
* [update](docs/sdks/projects/README.md#update) - Update a project
* [delete](docs/sdks/projects/README.md#delete) - Delete a project
* [duplicate](docs/sdks/projects/README.md#duplicate) - Duplicate a project

### [Queue](docs/sdks/queuesdk/README.md)

* [retrieve](docs/sdks/queuesdk/README.md#retrieve) - Get a queue
* [get_stats](docs/sdks/queuesdk/README.md#get_stats) - Get queue statistics

#### [Queue.Items](docs/sdks/items/README.md)

* [list](docs/sdks/items/README.md#list) - Get queue items
* [resolve](docs/sdks/items/README.md#resolve) - Resolve a queue item
* [unresolve](docs/sdks/items/README.md#unresolve) - Unresolve a queue item

### [Webhooks](docs/sdks/webhooks/README.md)

* [list](docs/sdks/webhooks/README.md#list) - List webhooks
* [create](docs/sdks/webhooks/README.md#create) - Create a webhook
* [retrieve](docs/sdks/webhooks/README.md#retrieve) - Get a webhook
* [update](docs/sdks/webhooks/README.md#update) - Update a webhook
* [delete](docs/sdks/webhooks/README.md#delete) - Delete a webhook

### [WebhookSecret](docs/sdks/webhooksecret/README.md)

* [retrieve](docs/sdks/webhooksecret/README.md#retrieve) - Get the webhook signing secret

### [Wordlist](docs/sdks/wordlist/README.md)

* [list](docs/sdks/wordlist/README.md#list) - List wordlists
* [retrieve](docs/sdks/wordlist/README.md#retrieve) - Get wordlist
* [update](docs/sdks/wordlist/README.md#update) - Update wordlist
* [get_embedding_status](docs/sdks/wordlist/README.md#get_embedding_status) - Get embedding status

#### [Wordlist.Words](docs/sdks/words/README.md)

* [add](docs/sdks/words/README.md#add) - Add words to wordlist
* [remove](docs/sdks/words/README.md#remove) - Remove words from wordlist

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
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
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from moderation_api import ModerationAPI
from moderation_api.utils import BackoffStrategy, RetryConfig
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.list(request={},
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    while res is not None:
        # Handle items

        res = res.next()

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from moderation_api import ModerationAPI
from moderation_api.utils import BackoffStrategy, RetryConfig
import os


with ModerationAPI(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.list(request={})

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ModerationAPIError`](./src/moderation_api/errors/moderationapierror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from moderation_api import ModerationAPI, errors
import os
from typing import Literal


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:
    res = None
    try:

        res = ma_client.authors.list(request={})

        while res is not None:
            # Handle items

            res = res.next()


    except errors.ModerationAPIError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.BadRequestError):
            print(e.data.type)  # Literal["invalid_request_error"]
            print(e.data.code)  # models.BadRequestErrorCode
            print(e.data.message)  # str
            print(e.data.issues)  # Optional[List[models.ErrorIssue]]
            print(e.data.request_id)  # str
```

### Error Classes
**Primary errors:**
* [`ModerationAPIError`](./src/moderation_api/errors/moderationapierror.py): The base class for HTTP error responses.
  * [`AuthenticationError`](./src/moderation_api/errors/authenticationerror.py): The API key is missing, invalid or revoked. Status code `401`.
  * [`RateLimitError`](./src/moderation_api/errors/ratelimiterror.py): Too many requests. Retry after the number of seconds in the `Retry-After` header. Status code `429`.

<details><summary>Less common errors (10)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ModerationAPIError`](./src/moderation_api/errors/moderationapierror.py)**:
* [`BadRequestError`](./src/moderation_api/errors/badrequesterror.py): The request is malformed or a parameter is invalid. Status code `400`. Applicable to 32 of 42 methods.*
* [`NotFoundError`](./src/moderation_api/errors/notfounderror.py): The resource does not exist or the key cannot see it. Status code `404`. Applicable to 31 of 42 methods.*
* [`PermissionDeniedError`](./src/moderation_api/errors/permissiondeniederror.py): The API key cannot do this, or the plan limit for this resource is reached. Status code `403`. Applicable to 27 of 42 methods.*
* [`InternalServerError`](./src/moderation_api/errors/internalservererror.py): Something went wrong on our side. Retry with backoff. Status code `500`. Applicable to 15 of 42 methods.*
* [`ConflictError`](./src/moderation_api/errors/conflicterror.py): The request conflicts with the current state of a resource. Status code `409`. Applicable to 2 of 42 methods.*
* [`ResponseValidationError`](./src/moderation_api/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    server_url="https://api.moderationapi.com/v1",
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.authors.list(request={})

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from moderation_api import ModerationAPI
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = ModerationAPI(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from moderation_api import ModerationAPI
from moderation_api.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = ModerationAPI(async_client=CustomClient(httpx.AsyncClient()))
```
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from moderation_api import ModerationAPI

s = ModerationAPI()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `ModerationAPI` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from moderation_api import ModerationAPI
import os
def main():

    with ModerationAPI(
        secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
    ) as ma_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with ModerationAPI(
        secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
    ) as ma_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from moderation_api import ModerationAPI
import logging

logging.basicConfig(level=logging.DEBUG)
s = ModerationAPI(debug_logger=logging.getLogger("moderation_api"))
```

You can also enable a default debug logger by setting an environment variable `MODAPI_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Custom [more] -->
## Timeouts

Set a timeout in milliseconds for all requests on the client, or for one request:

```python
from moderation_api import ModerationAPI

with ModerationAPI(timeout_ms=10_000) as client:
    client.content.submit(content={"type": "text", "text": "Hello"}, timeout_ms=5_000)
```

## Requirements

Python 3.10 or later.


## Support

- [API reference](https://docs.moderationapi.com/api-reference/introduction)
- [Errors and error codes](https://docs.moderationapi.com/api-reference/errors)
- [Rate limits](https://docs.moderationapi.com/api-reference/rate-limits)
- [Guides](https://docs.moderationapi.com/get-started/introduction)
- Email [support@moderationapi.com](mailto:support@moderationapi.com)

Found a bug? Open an issue in this repository. This package is generated from the [Moderation API OpenAPI spec](https://api.moderationapi.com/v1/openapi.json), so pull requests to the generated code can't be merged as they are, but we use them to fix the generator.
<!-- End Custom [more] -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=moderation-api&utm_campaign=python)
