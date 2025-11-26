# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import auth, account, authors, moderate
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ModerationAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.queue import queue
from .resources.actions import actions
from .resources.wordlist import wordlist

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ModerationAPI",
    "AsyncModerationAPI",
    "Client",
    "AsyncClient",
]


class ModerationAPI(SyncAPIClient):
    authors: authors.AuthorsResource
    queue: queue.QueueResource
    actions: actions.ActionsResource
    moderate: moderate.ModerateResource
    account: account.AccountResource
    auth: auth.AuthResource
    wordlist: wordlist.WordlistResource
    with_raw_response: ModerationAPIWithRawResponse
    with_streaming_response: ModerationAPIWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ModerationAPI client instance.

        This automatically infers the `bearer_token` argument from the `MODERATION_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("MODERATION_API_BEARER_TOKEN")
        if bearer_token is None:
            raise ModerationAPIError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the MODERATION_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("MODERATION_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.moderationapi.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authors = authors.AuthorsResource(self)
        self.queue = queue.QueueResource(self)
        self.actions = actions.ActionsResource(self)
        self.moderate = moderate.ModerateResource(self)
        self.account = account.AccountResource(self)
        self.auth = auth.AuthResource(self)
        self.wordlist = wordlist.WordlistResource(self)
        self.with_raw_response = ModerationAPIWithRawResponse(self)
        self.with_streaming_response = ModerationAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncModerationAPI(AsyncAPIClient):
    authors: authors.AsyncAuthorsResource
    queue: queue.AsyncQueueResource
    actions: actions.AsyncActionsResource
    moderate: moderate.AsyncModerateResource
    account: account.AsyncAccountResource
    auth: auth.AsyncAuthResource
    wordlist: wordlist.AsyncWordlistResource
    with_raw_response: AsyncModerationAPIWithRawResponse
    with_streaming_response: AsyncModerationAPIWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncModerationAPI client instance.

        This automatically infers the `bearer_token` argument from the `MODERATION_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("MODERATION_API_BEARER_TOKEN")
        if bearer_token is None:
            raise ModerationAPIError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the MODERATION_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("MODERATION_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.moderationapi.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authors = authors.AsyncAuthorsResource(self)
        self.queue = queue.AsyncQueueResource(self)
        self.actions = actions.AsyncActionsResource(self)
        self.moderate = moderate.AsyncModerateResource(self)
        self.account = account.AsyncAccountResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.wordlist = wordlist.AsyncWordlistResource(self)
        self.with_raw_response = AsyncModerationAPIWithRawResponse(self)
        self.with_streaming_response = AsyncModerationAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ModerationAPIWithRawResponse:
    def __init__(self, client: ModerationAPI) -> None:
        self.authors = authors.AuthorsResourceWithRawResponse(client.authors)
        self.queue = queue.QueueResourceWithRawResponse(client.queue)
        self.actions = actions.ActionsResourceWithRawResponse(client.actions)
        self.moderate = moderate.ModerateResourceWithRawResponse(client.moderate)
        self.account = account.AccountResourceWithRawResponse(client.account)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.wordlist = wordlist.WordlistResourceWithRawResponse(client.wordlist)


class AsyncModerationAPIWithRawResponse:
    def __init__(self, client: AsyncModerationAPI) -> None:
        self.authors = authors.AsyncAuthorsResourceWithRawResponse(client.authors)
        self.queue = queue.AsyncQueueResourceWithRawResponse(client.queue)
        self.actions = actions.AsyncActionsResourceWithRawResponse(client.actions)
        self.moderate = moderate.AsyncModerateResourceWithRawResponse(client.moderate)
        self.account = account.AsyncAccountResourceWithRawResponse(client.account)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.wordlist = wordlist.AsyncWordlistResourceWithRawResponse(client.wordlist)


class ModerationAPIWithStreamedResponse:
    def __init__(self, client: ModerationAPI) -> None:
        self.authors = authors.AuthorsResourceWithStreamingResponse(client.authors)
        self.queue = queue.QueueResourceWithStreamingResponse(client.queue)
        self.actions = actions.ActionsResourceWithStreamingResponse(client.actions)
        self.moderate = moderate.ModerateResourceWithStreamingResponse(client.moderate)
        self.account = account.AccountResourceWithStreamingResponse(client.account)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.wordlist = wordlist.WordlistResourceWithStreamingResponse(client.wordlist)


class AsyncModerationAPIWithStreamedResponse:
    def __init__(self, client: AsyncModerationAPI) -> None:
        self.authors = authors.AsyncAuthorsResourceWithStreamingResponse(client.authors)
        self.queue = queue.AsyncQueueResourceWithStreamingResponse(client.queue)
        self.actions = actions.AsyncActionsResourceWithStreamingResponse(client.actions)
        self.moderate = moderate.AsyncModerateResourceWithStreamingResponse(client.moderate)
        self.account = account.AsyncAccountResourceWithStreamingResponse(client.account)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.wordlist = wordlist.AsyncWordlistResourceWithStreamingResponse(client.wordlist)


Client = ModerationAPI

AsyncClient = AsyncModerationAPI
