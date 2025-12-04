# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
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
    "Policy",
    "PolicyUnionMember0",
    "PolicyUnionMember1",
    "PolicyUnionMember2",
    "PolicyUnionMember3",
    "PolicyUnionMember4",
    "PolicyUnionMember5",
    "PolicyUnionMember6",
    "PolicyUnionMember7",
    "PolicyUnionMember8",
    "PolicyUnionMember9",
    "PolicyUnionMember10",
    "PolicyUnionMember11",
    "PolicyUnionMember12",
    "PolicyUnionMember13",
    "PolicyUnionMember14",
    "PolicyUnionMember15",
    "PolicyUnionMember16",
    "PolicyUnionMember17",
    "PolicyUnionMember18",
    "PolicyUnionMember19",
    "PolicyUnionMember20",
    "PolicyUnionMember20Entities",
    "PolicyUnionMember21",
    "PolicyUnionMember21Entities",
    "PolicyUnionMember22",
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

    policies: Iterable[Policy]
    """
    Optionally override the channel policies for this moderation request only
    (enterprise).
    """


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


class PolicyUnionMember0(TypedDict, total=False):
    id: Required[Literal["toxicity"]]

    flag: Required[bool]


class PolicyUnionMember1(TypedDict, total=False):
    id: Required[Literal["personal_information"]]

    flag: Required[bool]


class PolicyUnionMember2(TypedDict, total=False):
    id: Required[Literal["toxicity_severe"]]

    flag: Required[bool]


class PolicyUnionMember3(TypedDict, total=False):
    id: Required[Literal["hate"]]

    flag: Required[bool]


class PolicyUnionMember4(TypedDict, total=False):
    id: Required[Literal["illicit"]]

    flag: Required[bool]


class PolicyUnionMember5(TypedDict, total=False):
    id: Required[Literal["illicit_drugs"]]

    flag: Required[bool]


class PolicyUnionMember6(TypedDict, total=False):
    id: Required[Literal["illicit_alcohol"]]

    flag: Required[bool]


class PolicyUnionMember7(TypedDict, total=False):
    id: Required[Literal["illicit_firearms"]]

    flag: Required[bool]


class PolicyUnionMember8(TypedDict, total=False):
    id: Required[Literal["illicit_tobacco"]]

    flag: Required[bool]


class PolicyUnionMember9(TypedDict, total=False):
    id: Required[Literal["illicit_gambling"]]

    flag: Required[bool]


class PolicyUnionMember10(TypedDict, total=False):
    id: Required[Literal["sexual"]]

    flag: Required[bool]


class PolicyUnionMember11(TypedDict, total=False):
    id: Required[Literal["flirtation"]]

    flag: Required[bool]


class PolicyUnionMember12(TypedDict, total=False):
    id: Required[Literal["profanity"]]

    flag: Required[bool]


class PolicyUnionMember13(TypedDict, total=False):
    id: Required[Literal["violence"]]

    flag: Required[bool]


class PolicyUnionMember14(TypedDict, total=False):
    id: Required[Literal["self_harm"]]

    flag: Required[bool]


class PolicyUnionMember15(TypedDict, total=False):
    id: Required[Literal["spam"]]

    flag: Required[bool]


class PolicyUnionMember16(TypedDict, total=False):
    id: Required[Literal["self_promotion"]]

    flag: Required[bool]


class PolicyUnionMember17(TypedDict, total=False):
    id: Required[Literal["political"]]

    flag: Required[bool]


class PolicyUnionMember18(TypedDict, total=False):
    id: Required[Literal["religion"]]

    flag: Required[bool]


class PolicyUnionMember19(TypedDict, total=False):
    id: Required[Literal["code_abuse"]]

    flag: Required[bool]


class PolicyUnionMember20Entities(TypedDict, total=False):
    id: Required[
        Literal["email", "phone", "url", "address", "name", "username", "ip_address", "credit_card", "sensitive_other"]
    ]

    enable: Required[bool]

    flag: Required[bool]

    should_mask: Required[Annotated[bool, PropertyInfo(alias="shouldMask")]]

    mask: str


class PolicyUnionMember20(TypedDict, total=False):
    id: Required[Literal["pii"]]

    entities: Required[Dict[str, PolicyUnionMember20Entities]]


class PolicyUnionMember21Entities(TypedDict, total=False):
    id: Required[
        Literal["email", "phone", "url", "address", "name", "username", "ip_address", "credit_card", "sensitive_other"]
    ]

    enable: Required[bool]

    flag: Required[bool]

    should_mask: Required[Annotated[bool, PropertyInfo(alias="shouldMask")]]

    mask: str


class PolicyUnionMember21(TypedDict, total=False):
    id: Required[Literal["url"]]

    entities: Required[Dict[str, PolicyUnionMember21Entities]]


class PolicyUnionMember22(TypedDict, total=False):
    id: Required[Literal["guideline"]]

    flag: Required[bool]

    guideline_key: Required[Annotated[str, PropertyInfo(alias="guidelineKey")]]

    instructions: Required[str]


Policy: TypeAlias = Union[
    PolicyUnionMember0,
    PolicyUnionMember1,
    PolicyUnionMember2,
    PolicyUnionMember3,
    PolicyUnionMember4,
    PolicyUnionMember5,
    PolicyUnionMember6,
    PolicyUnionMember7,
    PolicyUnionMember8,
    PolicyUnionMember9,
    PolicyUnionMember10,
    PolicyUnionMember11,
    PolicyUnionMember12,
    PolicyUnionMember13,
    PolicyUnionMember14,
    PolicyUnionMember15,
    PolicyUnionMember16,
    PolicyUnionMember17,
    PolicyUnionMember18,
    PolicyUnionMember19,
    PolicyUnionMember20,
    PolicyUnionMember21,
    PolicyUnionMember22,
]
