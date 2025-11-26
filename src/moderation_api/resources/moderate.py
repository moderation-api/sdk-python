# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import (
    moderate_analyze_params,
    moderate_analyze_text_params,
    moderate_analyze_audio_params,
    moderate_analyze_image_params,
    moderate_analyze_video_params,
    moderate_analyze_object_params,
)
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
from ..types.moderate_analyze_text_response import ModerateAnalyzeTextResponse
from ..types.moderate_analyze_audio_response import ModerateAnalyzeAudioResponse
from ..types.moderate_analyze_image_response import ModerateAnalyzeImageResponse
from ..types.moderate_analyze_video_response import ModerateAnalyzeVideoResponse
from ..types.moderate_analyze_object_response import ModerateAnalyzeObjectResponse

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

    @typing_extensions.deprecated("deprecated")
    def analyze_audio(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeAudioResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze audio content
        with your configured moderation models and filters.

        Args:
          url: The URL of the audio you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate/audio",
            body=maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_audio_params.ModerateAnalyzeAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeAudioResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def analyze_image(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeImageResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze image with
        your Moderation API project

        Args:
          url: The URL of the image you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate/image",
            body=maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_image_params.ModerateAnalyzeImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeImageResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def analyze_object(
        self,
        *,
        value: moderate_analyze_object_params.Value,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeObjectResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze an object
        with multiple fields including text, images, video, audio. Use to moderate a
        post, a profile, a form submission or anything that have multiple fields.

        Args:
          value: The object you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate/object",
            body=maybe_transform(
                {
                    "value": value,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_object_params.ModerateAnalyzeObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeObjectResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def analyze_text(
        self,
        *,
        value: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeTextResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze text content
        with your configured moderation models and filters.

        Args:
          value: The text you'd like to analyze. We recommend to submit plain text or HTML

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate/text",
            body=maybe_transform(
                {
                    "value": value,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_text_params.ModerateAnalyzeTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeTextResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def analyze_video(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeVideoResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze video content
        with your configured moderation models and filters.

        Args:
          url: The URL of the video you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderate/video",
            body=maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_video_params.ModerateAnalyzeVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeVideoResponse,
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

    @typing_extensions.deprecated("deprecated")
    async def analyze_audio(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeAudioResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze audio content
        with your configured moderation models and filters.

        Args:
          url: The URL of the audio you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate/audio",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_audio_params.ModerateAnalyzeAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeAudioResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def analyze_image(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeImageResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze image with
        your Moderation API project

        Args:
          url: The URL of the image you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate/image",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_image_params.ModerateAnalyzeImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeImageResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def analyze_object(
        self,
        *,
        value: moderate_analyze_object_params.Value,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeObjectResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze an object
        with multiple fields including text, images, video, audio. Use to moderate a
        post, a profile, a form submission or anything that have multiple fields.

        Args:
          value: The object you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate/object",
            body=await async_maybe_transform(
                {
                    "value": value,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_object_params.ModerateAnalyzeObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeObjectResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def analyze_text(
        self,
        *,
        value: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeTextResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze text content
        with your configured moderation models and filters.

        Args:
          value: The text you'd like to analyze. We recommend to submit plain text or HTML

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate/text",
            body=await async_maybe_transform(
                {
                    "value": value,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_text_params.ModerateAnalyzeTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeTextResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def analyze_video(
        self,
        *,
        url: str,
        author_id: str | Omit = omit,
        channel_key: str | Omit = omit,
        content_id: str | Omit = omit,
        context_id: str | Omit = omit,
        do_not_store: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerateAnalyzeVideoResponse:
        """
        (Deprecated use https://api.moderationapi.com/v1/moderate) Analyze video content
        with your configured moderation models and filters.

        Args:
          url: The URL of the video you want to analyze.

          author_id: The author of the content.

          channel_key: The key of the channel.

          content_id: The unique ID of the content in your database.

          context_id: For example the ID of a chat room or a post

          do_not_store: Do not store the content. The content won't enter the review queue

          metadata: Any metadata you want to store with the content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderate/video",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "author_id": author_id,
                    "channel_key": channel_key,
                    "content_id": content_id,
                    "context_id": context_id,
                    "do_not_store": do_not_store,
                    "metadata": metadata,
                },
                moderate_analyze_video_params.ModerateAnalyzeVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerateAnalyzeVideoResponse,
        )


class ModerateResourceWithRawResponse:
    def __init__(self, moderate: ModerateResource) -> None:
        self._moderate = moderate

        self.analyze = to_raw_response_wrapper(
            moderate.analyze,
        )
        self.analyze_audio = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                moderate.analyze_audio,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_image = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                moderate.analyze_image,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_object = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                moderate.analyze_object,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_text = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                moderate.analyze_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_video = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                moderate.analyze_video,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncModerateResourceWithRawResponse:
    def __init__(self, moderate: AsyncModerateResource) -> None:
        self._moderate = moderate

        self.analyze = async_to_raw_response_wrapper(
            moderate.analyze,
        )
        self.analyze_audio = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                moderate.analyze_audio,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_image = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                moderate.analyze_image,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_object = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                moderate.analyze_object,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_text = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                moderate.analyze_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_video = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                moderate.analyze_video,  # pyright: ignore[reportDeprecated],
            )
        )


class ModerateResourceWithStreamingResponse:
    def __init__(self, moderate: ModerateResource) -> None:
        self._moderate = moderate

        self.analyze = to_streamed_response_wrapper(
            moderate.analyze,
        )
        self.analyze_audio = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                moderate.analyze_audio,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_image = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                moderate.analyze_image,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_object = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                moderate.analyze_object,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_text = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                moderate.analyze_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_video = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                moderate.analyze_video,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncModerateResourceWithStreamingResponse:
    def __init__(self, moderate: AsyncModerateResource) -> None:
        self._moderate = moderate

        self.analyze = async_to_streamed_response_wrapper(
            moderate.analyze,
        )
        self.analyze_audio = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                moderate.analyze_audio,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_image = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                moderate.analyze_image,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_object = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                moderate.analyze_object,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_text = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                moderate.analyze_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.analyze_video = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                moderate.analyze_video,  # pyright: ignore[reportDeprecated],
            )
        )
