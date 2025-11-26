# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModerateAnalyzeAudioParams"]


class ModerateAnalyzeAudioParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the audio you want to analyze."""

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
