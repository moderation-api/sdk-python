# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ModerateAnalyzeObjectParams", "Value", "ValueData"]


class ModerateAnalyzeObjectParams(TypedDict, total=False):
    value: Required[Value]
    """The object you want to analyze."""

    author_id: Annotated[str, PropertyInfo(alias="authorId")]
    """The author of the content."""

    channel_key: Annotated[str, PropertyInfo(alias="channelKey")]
    """The key of the channel."""

    content_id: Annotated[str, PropertyInfo(alias="contentId")]
    """The unique ID of the content in your database."""

    context_id: Annotated[str, PropertyInfo(alias="contextId")]
    """For example the ID of a chat room or a post"""

    do_not_store: Annotated[bool, PropertyInfo(alias="doNotStore")]
    """Do not store the content. The content won't enter the review queue"""

    metadata: Dict[str, object]
    """Any metadata you want to store with the content"""


class ValueData(TypedDict, total=False):
    type: Required[Literal["text", "image", "video", "audio"]]
    """The type of content (e.g., "text", "image", "video")"""

    value: Required[str]
    """The content to analyze"""

    model_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="modelIds")]
    """Optional array of specific model IDs to use"""


class Value(TypedDict, total=False):
    data: Required[Dict[str, ValueData]]

    type: Required[Literal["profile", "event", "product", "object"]]
    """The type of the object you want to analyze."""
