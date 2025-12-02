# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ContentSubmitParams",
    "Content",
    "ContentUnionMember0",
    "ContentUnionMember1",
    "ContentUnionMember2",
    "ContentUnionMember3",
    "ContentUnionMember4",
    "ContentUnionMember4Data",
    "ContentUnionMember4DataUnionMember0",
    "ContentUnionMember4DataUnionMember1",
    "ContentUnionMember4DataUnionMember2",
    "ContentUnionMember4DataUnionMember3",
]


class ContentSubmitParams(TypedDict, total=False):
    content: Required[Content]
    """The content sent for moderation"""

    author_id: Annotated[str, PropertyInfo(alias="authorId")]
    """The author of the content."""

    channel: str
    """Provide a channel ID or key.

    Will use the project's default channel if not provided.
    """

    content_id: Annotated[str, PropertyInfo(alias="contentId")]
    """The unique ID of the content in your database."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """For example the ID of a chat room or a post"""

    do_not_store: Annotated[bool, PropertyInfo(alias="doNotStore")]
    """Do not store the content. The content won't enter the review queue"""

    metadata: Dict[str, object]
    """Any metadata you want to store with the content"""

    meta_type: Annotated[
        Literal["profile", "message", "post", "comment", "event", "product", "review", "other"],
        PropertyInfo(alias="metaType"),
    ]
    """The meta type of content being moderated"""


class ContentUnionMember0(TypedDict, total=False):
    text: Required[str]
    """The content text"""

    type: Required[Literal["text"]]


class ContentUnionMember1(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """A public URL of the image content"""


class ContentUnionMember2(TypedDict, total=False):
    type: Required[Literal["video"]]

    url: Required[str]
    """A public URL of the video content"""


class ContentUnionMember3(TypedDict, total=False):
    type: Required[Literal["audio"]]

    url: Required[str]
    """The URL of the audio content"""


class ContentUnionMember4DataUnionMember0(TypedDict, total=False):
    text: Required[str]
    """The content text"""

    type: Required[Literal["text"]]


class ContentUnionMember4DataUnionMember1(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """A public URL of the image content"""


class ContentUnionMember4DataUnionMember2(TypedDict, total=False):
    type: Required[Literal["video"]]

    url: Required[str]
    """A public URL of the video content"""


class ContentUnionMember4DataUnionMember3(TypedDict, total=False):
    type: Required[Literal["audio"]]

    url: Required[str]
    """The URL of the audio content"""


ContentUnionMember4Data: TypeAlias = Union[
    ContentUnionMember4DataUnionMember0,
    ContentUnionMember4DataUnionMember1,
    ContentUnionMember4DataUnionMember2,
    ContentUnionMember4DataUnionMember3,
]


class ContentUnionMember4(TypedDict, total=False):
    data: Required[Dict[str, ContentUnionMember4Data]]
    """Values in the object. Can be mixed content types."""

    type: Required[Literal["object"]]


Content: TypeAlias = Union[
    ContentUnionMember0, ContentUnionMember1, ContentUnionMember2, ContentUnionMember3, ContentUnionMember4
]
