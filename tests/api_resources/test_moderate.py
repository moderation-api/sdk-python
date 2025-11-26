# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from moderation_api import ModerationAPI, AsyncModerationAPI
from moderation_api.types import (
    ModerateAnalyzeResponse,
    ModerateAnalyzeTextResponse,
    ModerateAnalyzeAudioResponse,
    ModerateAnalyzeImageResponse,
    ModerateAnalyzeVideoResponse,
    ModerateAnalyzeObjectResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze(self, client: ModerationAPI) -> None:
        moderate = client.moderate.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        )
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_with_all_params(self, client: ModerationAPI) -> None:
        moderate = client.moderate.analyze(
            content={
                "text": "x",
                "type": "text",
            },
            author_id="authorId",
            channel="channel",
            content_id="contentId",
            conversation_id="conversationId",
            do_not_store=True,
            metadata={"foo": "bar"},
            meta_type="profile",
        )
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze(self, client: ModerationAPI) -> None:
        response = client.moderate.with_raw_response.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze(self, client: ModerationAPI) -> None:
        with client.moderate.with_streaming_response.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderate = response.parse()
            assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_audio(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_audio(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_audio_with_all_params(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_audio(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze_audio(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.moderate.with_raw_response.analyze_audio(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze_audio(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.moderate.with_streaming_response.analyze_audio(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = response.parse()
                assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_image(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_image(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_image_with_all_params(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_image(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze_image(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.moderate.with_raw_response.analyze_image(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze_image(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.moderate.with_streaming_response.analyze_image(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = response.parse()
                assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_object(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            )

        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_object_with_all_params(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                            "model_ids": ["string"],
                        }
                    },
                    "type": "profile",
                },
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze_object(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.moderate.with_raw_response.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze_object(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.moderate.with_streaming_response.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = response.parse()
                assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_text(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_text(
                value="x",
            )

        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_text_with_all_params(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_text(
                value="x",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze_text(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.moderate.with_raw_response.analyze_text(
                value="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze_text(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.moderate.with_streaming_response.analyze_text(
                value="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = response.parse()
                assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_video(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_video(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_video_with_all_params(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = client.moderate.analyze_video(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze_video(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.moderate.with_raw_response.analyze_video(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = response.parse()
        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze_video(self, client: ModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.moderate.with_streaming_response.analyze_video(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = response.parse()
                assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze(self, async_client: AsyncModerationAPI) -> None:
        moderate = await async_client.moderate.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        )
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        moderate = await async_client.moderate.analyze(
            content={
                "text": "x",
                "type": "text",
            },
            author_id="authorId",
            channel="channel",
            content_id="contentId",
            conversation_id="conversationId",
            do_not_store=True,
            metadata={"foo": "bar"},
            meta_type="profile",
        )
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncModerationAPI) -> None:
        response = await async_client.moderate.with_raw_response.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncModerationAPI) -> None:
        async with async_client.moderate.with_streaming_response.analyze(
            content={
                "text": "x",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderate = await response.parse()
            assert_matches_type(ModerateAnalyzeResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_audio(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_audio(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_audio_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_audio(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze_audio(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.moderate.with_raw_response.analyze_audio(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_audio(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.moderate.with_streaming_response.analyze_audio(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = await response.parse()
                assert_matches_type(ModerateAnalyzeAudioResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_image(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_image(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_image_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_image(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze_image(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.moderate.with_raw_response.analyze_image(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_image(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.moderate.with_streaming_response.analyze_image(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = await response.parse()
                assert_matches_type(ModerateAnalyzeImageResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_object(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            )

        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_object_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                            "model_ids": ["string"],
                        }
                    },
                    "type": "profile",
                },
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze_object(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.moderate.with_raw_response.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_object(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.moderate.with_streaming_response.analyze_object(
                value={
                    "data": {
                        "foo": {
                            "type": "text",
                            "value": "value",
                        }
                    },
                    "type": "profile",
                },
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = await response.parse()
                assert_matches_type(ModerateAnalyzeObjectResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_text(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_text(
                value="x",
            )

        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_text_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_text(
                value="x",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze_text(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.moderate.with_raw_response.analyze_text(
                value="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_text(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.moderate.with_streaming_response.analyze_text(
                value="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = await response.parse()
                assert_matches_type(ModerateAnalyzeTextResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_video(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_video(
                url="https://example.com",
            )

        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_video_with_all_params(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            moderate = await async_client.moderate.analyze_video(
                url="https://example.com",
                author_id="authorId",
                channel_key="channelKey",
                content_id="x",
                context_id="contextId",
                do_not_store=True,
                metadata={"foo": "bar"},
            )

        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze_video(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.moderate.with_raw_response.analyze_video(
                url="https://example.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderate = await response.parse()
        assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_video(self, async_client: AsyncModerationAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.moderate.with_streaming_response.analyze_video(
                url="https://example.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                moderate = await response.parse()
                assert_matches_type(ModerateAnalyzeVideoResponse, moderate, path=["response"])

        assert cast(Any, response.is_closed) is True
