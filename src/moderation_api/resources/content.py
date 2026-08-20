# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import content_submit_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.content_submit_response import ContentSubmitResponse

__all__ = ["ContentResource", "AsyncContentResource"]


class ContentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moderation-api/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moderation-api/sdk-python#with_streaming_response
        """
        return ContentResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        sec_web_socket_protocol: Literal["moderationapi.v1"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Open a WebSocket to moderate live voice/call audio in real time.

        Speech is
        transcribed and each finalized utterance is moderated by your enabled text
        policies; you receive a verdict per utterance as it's spoken.

        **This is a WebSocket upgrade, not a regular HTTP call.** The request body below
        documents the frames you _send_ over the socket; the `101` response documents
        the events you _receive_.

        - **Auth:** `Authorization: Bearer <api_key>` on the upgrade. A missing/invalid
          key closes `4401`; voice not enabled on the plan/channel closes `4403`.
        - **Subprotocol:** request `moderationapi.v1`.
        - **Flow:** send one `start` frame, then `media` frames as audio arrives, then
          `stop` (or disconnect). You receive `session.started`, `utterance.final` per
          utterance, optional `utterance.partial`/`warning`, and `session.ended`.
        - **Close codes:** `1000` normal · `1011` server error · `4400` bad request ·
          `4401` auth failed · `4403` voice not enabled · `4429` concurrency limit.

        See the
        [Real-time voice guide](https://docs.moderationapi.com/content-moderation/real-time-voice)
        for the full walkthrough and code examples.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Sec-WebSocket-Protocol": str(sec_web_socket_protocol)})
        return self._get(
            "/stream" if self._client._base_url_overridden else "wss://voice.moderationapi.com/v1/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def submit(
        self,
        *,
        content: content_submit_params.Content,
        author_id: str | Omit = omit,
        channel: str | Omit = omit,
        client_action: content_submit_params.ClientAction | Omit = omit,
        content_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        meta_type: Literal["profile", "message", "post", "comment", "event", "product", "review", "voice", "other"]
        | Omit = omit,
        policies: Iterable[content_submit_params.Policy] | Omit = omit,
        timestamp: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentSubmitResponse:
        """
        Args:
          content: The content sent for moderation

          author_id: The author of the content.

          channel: Provide a channel ID or key. Will use the project's default channel if not
              provided.

          client_action: A recommendation from your own client-side flagging (e.g. a banned-IP list or a
              third-party tool). Feeds the rules engine and can escalate or override the
              recommended action. Does not change whether our analysis flagged the content.

          content_id: The unique ID of the content in your database.

          conversation_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          meta_type: The meta type of content being moderated

          policies: (Enterprise) override the channel policies for this moderation request only.

          timestamp: Unix timestamp (in milliseconds) of when the content was created. Use if content
              is not submitted in real-time.

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
                    "client_action": client_action,
                    "content_id": content_id,
                    "conversation_id": conversation_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                    "meta_type": meta_type,
                    "policies": policies,
                    "timestamp": timestamp,
                },
                content_submit_params.ContentSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentSubmitResponse,
        )


class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moderation-api/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moderation-api/sdk-python#with_streaming_response
        """
        return AsyncContentResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        sec_web_socket_protocol: Literal["moderationapi.v1"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Open a WebSocket to moderate live voice/call audio in real time.

        Speech is
        transcribed and each finalized utterance is moderated by your enabled text
        policies; you receive a verdict per utterance as it's spoken.

        **This is a WebSocket upgrade, not a regular HTTP call.** The request body below
        documents the frames you _send_ over the socket; the `101` response documents
        the events you _receive_.

        - **Auth:** `Authorization: Bearer <api_key>` on the upgrade. A missing/invalid
          key closes `4401`; voice not enabled on the plan/channel closes `4403`.
        - **Subprotocol:** request `moderationapi.v1`.
        - **Flow:** send one `start` frame, then `media` frames as audio arrives, then
          `stop` (or disconnect). You receive `session.started`, `utterance.final` per
          utterance, optional `utterance.partial`/`warning`, and `session.ended`.
        - **Close codes:** `1000` normal · `1011` server error · `4400` bad request ·
          `4401` auth failed · `4403` voice not enabled · `4429` concurrency limit.

        See the
        [Real-time voice guide](https://docs.moderationapi.com/content-moderation/real-time-voice)
        for the full walkthrough and code examples.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Sec-WebSocket-Protocol": str(sec_web_socket_protocol)})
        return await self._get(
            "/stream" if self._client._base_url_overridden else "wss://voice.moderationapi.com/v1/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def submit(
        self,
        *,
        content: content_submit_params.Content,
        author_id: str | Omit = omit,
        channel: str | Omit = omit,
        client_action: content_submit_params.ClientAction | Omit = omit,
        content_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        meta_type: Literal["profile", "message", "post", "comment", "event", "product", "review", "voice", "other"]
        | Omit = omit,
        policies: Iterable[content_submit_params.Policy] | Omit = omit,
        timestamp: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentSubmitResponse:
        """
        Args:
          content: The content sent for moderation

          author_id: The author of the content.

          channel: Provide a channel ID or key. Will use the project's default channel if not
              provided.

          client_action: A recommendation from your own client-side flagging (e.g. a banned-IP list or a
              third-party tool). Feeds the rules engine and can escalate or override the
              recommended action. Does not change whether our analysis flagged the content.

          content_id: The unique ID of the content in your database.

          conversation_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          meta_type: The meta type of content being moderated

          policies: (Enterprise) override the channel policies for this moderation request only.

          timestamp: Unix timestamp (in milliseconds) of when the content was created. Use if content
              is not submitted in real-time.

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
                    "client_action": client_action,
                    "content_id": content_id,
                    "conversation_id": conversation_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                    "meta_type": meta_type,
                    "policies": policies,
                    "timestamp": timestamp,
                },
                content_submit_params.ContentSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentSubmitResponse,
        )


class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.stream = to_raw_response_wrapper(
            content.stream,
        )
        self.submit = to_raw_response_wrapper(
            content.submit,
        )


class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.stream = async_to_raw_response_wrapper(
            content.stream,
        )
        self.submit = async_to_raw_response_wrapper(
            content.submit,
        )


class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.stream = to_streamed_response_wrapper(
            content.stream,
        )
        self.submit = to_streamed_response_wrapper(
            content.submit,
        )


class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.stream = async_to_streamed_response_wrapper(
            content.stream,
        )
        self.submit = async_to_streamed_response_wrapper(
            content.submit,
        )
