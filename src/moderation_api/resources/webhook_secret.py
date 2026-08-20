# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_secret_retrieve_response import WebhookSecretRetrieveResponse

__all__ = ["WebhookSecretResource", "AsyncWebhookSecretResource"]


class WebhookSecretResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moderation-api/sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhookSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moderation-api/sdk-python#with_streaming_response
        """
        return WebhookSecretResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretRetrieveResponse:
        """
        Get the signing secret used to sign webhook deliveries for this project,
        creating one if none exists yet. Verify deliveries by comparing the
        `modapi-signature` header to HMAC-SHA256(raw request body, secret) hex-encoded.
        """
        return self._get(
            "/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretRetrieveResponse,
        )


class AsyncWebhookSecretResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moderation-api/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moderation-api/sdk-python#with_streaming_response
        """
        return AsyncWebhookSecretResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretRetrieveResponse:
        """
        Get the signing secret used to sign webhook deliveries for this project,
        creating one if none exists yet. Verify deliveries by comparing the
        `modapi-signature` header to HMAC-SHA256(raw request body, secret) hex-encoded.
        """
        return await self._get(
            "/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretRetrieveResponse,
        )


class WebhookSecretResourceWithRawResponse:
    def __init__(self, webhook_secret: WebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.retrieve = to_raw_response_wrapper(
            webhook_secret.retrieve,
        )


class AsyncWebhookSecretResourceWithRawResponse:
    def __init__(self, webhook_secret: AsyncWebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.retrieve = async_to_raw_response_wrapper(
            webhook_secret.retrieve,
        )


class WebhookSecretResourceWithStreamingResponse:
    def __init__(self, webhook_secret: WebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.retrieve = to_streamed_response_wrapper(
            webhook_secret.retrieve,
        )


class AsyncWebhookSecretResourceWithStreamingResponse:
    def __init__(self, webhook_secret: AsyncWebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.retrieve = async_to_streamed_response_wrapper(
            webhook_secret.retrieve,
        )
