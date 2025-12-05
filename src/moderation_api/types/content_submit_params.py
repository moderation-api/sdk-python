# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ContentSubmitParams",
    "Content",
    "ContentText",
    "ContentImage",
    "ContentVideo",
    "ContentAudio",
    "ContentObject",
    "ContentObjectData",
    "ContentObjectDataText",
    "ContentObjectDataImage",
    "ContentObjectDataVideo",
    "ContentObjectDataAudio",
    "Policy",
    "PolicyToxicity",
    "PolicyPersonalInformation",
    "PolicyToxicitySevere",
    "PolicyHate",
    "PolicyIllicit",
    "PolicyIllicitDrugs",
    "PolicyIllicitAlcohol",
    "PolicyIllicitFirearms",
    "PolicyIllicitTobacco",
    "PolicyIllicitGambling",
    "PolicySexual",
    "PolicyFlirtation",
    "PolicyProfanity",
    "PolicyViolence",
    "PolicySelfHarm",
    "PolicySpam",
    "PolicySelfPromotion",
    "PolicyPolitical",
    "PolicyReligion",
    "PolicyCodeAbuse",
    "PolicyPiiMasking",
    "PolicyPiiMaskingEntities",
    "PolicyURLMasking",
    "PolicyURLMaskingEntities",
    "PolicyGuideline",
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
    """(Enterprise) override the channel policies for this moderation request only."""


class ContentText(TypedDict, total=False):
    text: Required[str]
    """The content text"""

    type: Required[Literal["text"]]


class ContentImage(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """A public URL of the image content"""


class ContentVideo(TypedDict, total=False):
    type: Required[Literal["video"]]

    url: Required[str]
    """A public URL of the video content"""


class ContentAudio(TypedDict, total=False):
    type: Required[Literal["audio"]]

    url: Required[str]
    """The URL of the audio content"""


class ContentObjectDataText(TypedDict, total=False):
    text: Required[str]
    """The content text"""

    type: Required[Literal["text"]]


class ContentObjectDataImage(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """A public URL of the image content"""


class ContentObjectDataVideo(TypedDict, total=False):
    type: Required[Literal["video"]]

    url: Required[str]
    """A public URL of the video content"""


class ContentObjectDataAudio(TypedDict, total=False):
    type: Required[Literal["audio"]]

    url: Required[str]
    """The URL of the audio content"""


ContentObjectData: TypeAlias = Union[
    ContentObjectDataText, ContentObjectDataImage, ContentObjectDataVideo, ContentObjectDataAudio
]


class ContentObject(TypedDict, total=False):
    data: Required[Dict[str, ContentObjectData]]
    """Values in the object. Can be mixed content types."""

    type: Required[Literal["object"]]


Content: TypeAlias = Union[ContentText, ContentImage, ContentVideo, ContentAudio, ContentObject]


class PolicyToxicity(TypedDict, total=False):
    id: Required[Literal["toxicity"]]

    flag: Required[bool]


class PolicyPersonalInformation(TypedDict, total=False):
    id: Required[Literal["personal_information"]]

    flag: Required[bool]


class PolicyToxicitySevere(TypedDict, total=False):
    id: Required[Literal["toxicity_severe"]]

    flag: Required[bool]


class PolicyHate(TypedDict, total=False):
    id: Required[Literal["hate"]]

    flag: Required[bool]


class PolicyIllicit(TypedDict, total=False):
    id: Required[Literal["illicit"]]

    flag: Required[bool]


class PolicyIllicitDrugs(TypedDict, total=False):
    id: Required[Literal["illicit_drugs"]]

    flag: Required[bool]


class PolicyIllicitAlcohol(TypedDict, total=False):
    id: Required[Literal["illicit_alcohol"]]

    flag: Required[bool]


class PolicyIllicitFirearms(TypedDict, total=False):
    id: Required[Literal["illicit_firearms"]]

    flag: Required[bool]


class PolicyIllicitTobacco(TypedDict, total=False):
    id: Required[Literal["illicit_tobacco"]]

    flag: Required[bool]


class PolicyIllicitGambling(TypedDict, total=False):
    id: Required[Literal["illicit_gambling"]]

    flag: Required[bool]


class PolicySexual(TypedDict, total=False):
    id: Required[Literal["sexual"]]

    flag: Required[bool]


class PolicyFlirtation(TypedDict, total=False):
    id: Required[Literal["flirtation"]]

    flag: Required[bool]


class PolicyProfanity(TypedDict, total=False):
    id: Required[Literal["profanity"]]

    flag: Required[bool]


class PolicyViolence(TypedDict, total=False):
    id: Required[Literal["violence"]]

    flag: Required[bool]


class PolicySelfHarm(TypedDict, total=False):
    id: Required[Literal["self_harm"]]

    flag: Required[bool]


class PolicySpam(TypedDict, total=False):
    id: Required[Literal["spam"]]

    flag: Required[bool]


class PolicySelfPromotion(TypedDict, total=False):
    id: Required[Literal["self_promotion"]]

    flag: Required[bool]


class PolicyPolitical(TypedDict, total=False):
    id: Required[Literal["political"]]

    flag: Required[bool]


class PolicyReligion(TypedDict, total=False):
    id: Required[Literal["religion"]]

    flag: Required[bool]


class PolicyCodeAbuse(TypedDict, total=False):
    id: Required[Literal["code_abuse"]]

    flag: Required[bool]


class PolicyPiiMaskingEntities(TypedDict, total=False):
    id: Required[
        Literal["email", "phone", "url", "address", "name", "username", "ip_address", "credit_card", "sensitive_other"]
    ]

    enable: Required[bool]

    flag: Required[bool]

    should_mask: Required[Annotated[bool, PropertyInfo(alias="shouldMask")]]

    mask: str


class PolicyPiiMasking(TypedDict, total=False):
    id: Required[Literal["pii"]]

    entities: Required[Dict[str, PolicyPiiMaskingEntities]]


class PolicyURLMaskingEntities(TypedDict, total=False):
    id: Required[
        Literal["email", "phone", "url", "address", "name", "username", "ip_address", "credit_card", "sensitive_other"]
    ]

    enable: Required[bool]

    flag: Required[bool]

    should_mask: Required[Annotated[bool, PropertyInfo(alias="shouldMask")]]

    mask: str


class PolicyURLMasking(TypedDict, total=False):
    id: Required[Literal["url"]]

    entities: Required[Dict[str, PolicyURLMaskingEntities]]


class PolicyGuideline(TypedDict, total=False):
    id: Required[Literal["guideline"]]

    flag: Required[bool]

    guideline_key: Required[Annotated[str, PropertyInfo(alias="guidelineKey")]]

    instructions: Required[str]


Policy: TypeAlias = Union[
    PolicyToxicity,
    PolicyPersonalInformation,
    PolicyToxicitySevere,
    PolicyHate,
    PolicyIllicit,
    PolicyIllicitDrugs,
    PolicyIllicitAlcohol,
    PolicyIllicitFirearms,
    PolicyIllicitTobacco,
    PolicyIllicitGambling,
    PolicySexual,
    PolicyFlirtation,
    PolicyProfanity,
    PolicyViolence,
    PolicySelfHarm,
    PolicySpam,
    PolicySelfPromotion,
    PolicyPolitical,
    PolicyReligion,
    PolicyCodeAbuse,
    PolicyPiiMasking,
    PolicyURLMasking,
    PolicyGuideline,
]
