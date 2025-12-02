# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import moderate_analyze_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.moderate_analyze_response import ModerateAnalyzeResponse

__all__ = ["ModerateResource", "AsyncModerateResource"]


class ModerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/moderation-api-python#accessing-raw-response-data-eg-headers
        """
        return ModerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/moderation-api-python#with_streaming_response
        """
        return ModerateResourceWithStreamingResponse(self)

    def analyze(
        self,
        *,
        content: moderate_analyze_params.Content,
        author_id: str | Omit = omit,
        channel: str | Omit = omit,
        content_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        meta_type: Literal["profile", "message", "post", "comment", "event", "product", "review", "other"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeResponse:
        """
        Args:
          content: The content sent for moderation

          author_id: The author of the content.

          channel: Provide a channel ID or key. Will use the project's default channel if not
              provided.

          content_id: The unique ID of the content in your database.

          conversation_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          meta_type: The meta type of content being moderated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate",
            body=maybe_transform(
                {
                    "content": content,
                    "author_id": author_id,
                    "channel": channel,
                    "content_id": content_id,
                    "conversation_id": conversation_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                    "meta_type": meta_type,
                },
                moderate_analyze_params.ModerateAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeResponse,
        )


class AsyncModerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/moderation-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/moderation-api-python#with_streaming_response
        """
        return AsyncModerateResourceWithStreamingResponse(self)

    async def analyze(
        self,
        *,
        content: moderate_analyze_params.Content,
        author_id: str | Omit = omit,
        channel: str | Omit = omit,
        content_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        meta_type: Literal["profile", "message", "post", "comment", "event", "product", "review", "other"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeResponse:
        """
        Args:
          content: The content sent for moderation

          author_id: The author of the content.

          channel: Provide a channel ID or key. Will use the project's default channel if not
              provided.

          content_id: The unique ID of the content in your database.

          conversation_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          meta_type: The meta type of content being moderated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "author_id": author_id,
                    "channel": channel,
                    "content_id": content_id,
                    "conversation_id": conversation_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                    "meta_type": meta_type,
                },
                moderate_analyze_params.ModerateAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeResponse,
        )


class ModerateResourceWithRawResponse:
    def __init__(self, moderate: ModerateResource) -> None:
        self._moderate = moderate

        self.analyze = to_raw_response_wrapper(
            moderate.analyze,
        )


class AsyncModerateResourceWithRawResponse:
    def __init__(self, moderate: AsyncModerateResource) -> None:
        self._moderate = moderate

        self.analyze = async_to_raw_response_wrapper(
            moderate.analyze,
        )


class ModerateResourceWithStreamingResponse:
    def __init__(self, moderate: ModerateResource) -> None:
        self._moderate = moderate

        self.analyze = to_streamed_response_wrapper(
            moderate.analyze,
        )


class AsyncModerateResourceWithStreamingResponse:
    def __init__(self, moderate: AsyncModerateResource) -> None:
        self._moderate = moderate

        self.analyze = async_to_streamed_response_wrapper(
            moderate.analyze,
        )
