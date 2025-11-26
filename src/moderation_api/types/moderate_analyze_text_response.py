# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModerateAnalyzeTextResponse",
    "Author",
    "AuthorBlock",
    "AuthorTrustLevel",
    "Request",
    "Address",
    "Email",
    "Name",
    "Nsfw",
    "NsfwLabelScores",
    "Phone",
    "Profanity",
    "Propriety",
    "ProprietyLabelScores",
    "Quality",
    "QualityLabelScores",
    "Sensitive",
    "Sentiment",
    "SentimentLabelScores",
    "Toxicity",
    "ToxicityLabelScores",
    "URL",
    "Username",
    "Wordlist",
]


class AuthorBlock(BaseModel):
    reason: Optional[str] = None
    """The moderators reason why the author was blocked or suspended."""

    until: Optional[float] = None
    """The timestamp until which they are blocked if the author is suspended."""


class AuthorTrustLevel(BaseModel):
    level: float
    """Author trust level (-1, 0, 1, 2, 3, or 4)"""

    manual: bool
    """True if the trust level was set manually by a moderator"""


class Author(BaseModel):
    id: str
    """Author ID in Moderation API"""

    block: Optional[AuthorBlock] = None
    """Block or suspension details, if applicable. Null if the author is enabled."""

    status: Literal["enabled", "suspended", "blocked"]
    """Current author status"""

    trust_level: AuthorTrustLevel

    external_id: Optional[str] = None
    """The author's ID from your system"""


class Request(BaseModel):
    quota_usage: float
    """The quota usage of the request"""

    timestamp: float
    """The timestamp of the request"""


class Address(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class Email(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class Name(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class NsfwLabelScores(BaseModel):
    neutral: Optional[float] = FieldInfo(alias="NEUTRAL", default=None)

    sensitive: Optional[float] = FieldInfo(alias="SENSITIVE", default=None)
    """Mentions religion, politics, race, etc., but is neutral or positive."""

    unsafe: Optional[float] = FieldInfo(alias="UNSAFE", default=None)
    """Sexual, hateful, profane, and inappropriate content."""


class Nsfw(BaseModel):
    error: Optional[str] = None
    """Indicates an error with the model"""

    label: Optional[str] = None
    """The label of the model"""

    label_scores: Optional[NsfwLabelScores] = None
    """The confidence of all labels"""

    score: Optional[float] = None
    """The confidence of the model"""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate
    """


class Phone(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class Profanity(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class ProprietyLabelScores(BaseModel):
    flirtation: Optional[float] = FieldInfo(alias="FLIRTATION", default=None)
    """Pickup lines, compliments on appearance, etc."""

    neutral: Optional[float] = FieldInfo(alias="NEUTRAL", default=None)

    sexually_explicit: Optional[float] = FieldInfo(alias="SEXUALLY_EXPLICIT", default=None)
    """References to sexual acts, body parts, etc."""


class Propriety(BaseModel):
    error: Optional[str] = None
    """Indicates an error with the model"""

    label: Optional[str] = None
    """The label of the model"""

    label_scores: Optional[ProprietyLabelScores] = None
    """The confidence of all labels"""

    score: Optional[float] = None
    """The confidence of the model"""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate
    """


class QualityLabelScores(BaseModel):
    incoherent: Optional[float] = FieldInfo(alias="INCOHERENT", default=None)
    """Difficult to understand, nonsensical."""

    neutral: Optional[float] = FieldInfo(alias="NEUTRAL", default=None)

    spam: Optional[float] = FieldInfo(alias="SPAM", default=None)
    """Irrelevant and unsolicited commercial content."""

    unsubstantial: Optional[float] = FieldInfo(alias="UNSUBSTANTIAL", default=None)
    """Trivial or short content."""


class Quality(BaseModel):
    error: Optional[str] = None
    """Indicates an error with the model"""

    label: Optional[str] = None
    """The label of the model"""

    label_scores: Optional[QualityLabelScores] = None
    """The confidence of all labels"""

    score: Optional[float] = None
    """The confidence of the model"""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate
    """


class Sensitive(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class SentimentLabelScores(BaseModel):
    negative: Optional[float] = FieldInfo(alias="NEGATIVE", default=None)
    """Negative sentiment."""

    neutral: Optional[float] = FieldInfo(alias="NEUTRAL", default=None)

    positive: Optional[float] = FieldInfo(alias="POSITIVE", default=None)
    """Positive sentiment."""


class Sentiment(BaseModel):
    error: Optional[str] = None
    """Indicates an error with the model"""

    label: Optional[str] = None
    """The label of the model"""

    label_scores: Optional[SentimentLabelScores] = None
    """The confidence of all labels"""

    score: Optional[float] = None
    """The confidence of the model"""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate
    """


class ToxicityLabelScores(BaseModel):
    discrimination: Optional[float] = FieldInfo(alias="DISCRIMINATION", default=None)
    """Discrimination of race, religion, gender, etc."""

    insult: Optional[float] = FieldInfo(alias="INSULT", default=None)
    """Negative comments about looks or personality etc."""

    neutral: Optional[float] = FieldInfo(alias="NEUTRAL", default=None)

    profanity: Optional[float] = FieldInfo(alias="PROFANITY", default=None)
    """Swearing, curse words, and other obscene language."""

    severe_toxicity: Optional[float] = FieldInfo(alias="SEVERE_TOXICITY", default=None)
    """Very hateful and aggressive content."""

    threat: Optional[float] = FieldInfo(alias="THREAT", default=None)
    """Content containing intention to harm or violence."""

    toxicity: Optional[float] = FieldInfo(alias="TOXICITY", default=None)
    """Rude or disrespectful content."""


class Toxicity(BaseModel):
    error: Optional[str] = None
    """Indicates an error with the model"""

    label: Optional[str] = None
    """The label of the model"""

    label_scores: Optional[ToxicityLabelScores] = None
    """The confidence of all labels"""

    score: Optional[float] = None
    """The confidence of the model"""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate
    """


class URL(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class Username(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class Wordlist(BaseModel):
    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    mode: Optional[Literal["NORMAL", "SUSPICIOUS", "PARANOID"]] = None
    """The detection mode."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class ModerateAnalyzeTextResponse(BaseModel):
    author: Optional[Author] = None
    """The author of the content if your account has authors enabled.

    Requires you to send authorId when submitting content.
    """

    content: str
    """The content after moderation.

    With all mask replacements applied and look-alike characters replaced with the
    original characters.
    """

    content_moderated: bool
    """Whether the content was moderated or not. Same as `content` !== `original`"""

    data_found: bool
    """Whether any entity matchers found data for the content"""

    flagged: bool
    """Whether the content was flagged by any models"""

    original: str
    """The original content"""

    request: Request
    """Information about the request"""

    status: str
    """Success if the request was successful"""

    unicode_spoofing: bool
    """Whether the content is using look-alike characters. Often used by spammers."""

    address: Optional[Address] = None
    """The address entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/address
    """

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)
    """The ID of the content. Only returned if the content was stored."""

    email: Optional[Email] = None
    """The email entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/email
    """

    error: Optional[object] = None
    """Error message if the request failed"""

    name: Optional[Name] = None
    """The name entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/name
    """

    nsfw: Optional[Nsfw] = None
    """The NSFW model output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/nsfw
    """

    phone: Optional[Phone] = None
    """The phone entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/phone
    """

    profanity: Optional[Profanity] = None
    """The profanity entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/profanity
    """

    propriety: Optional[Propriety] = None
    """The propriety model output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/propriety
    """

    quality: Optional[Quality] = None
    """The spam model output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/spam
    """

    sensitive: Optional[Sensitive] = None
    """The sensitive numbers entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/sensitive
    """

    sentiment: Optional[Sentiment] = None
    """The sentiment model output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/sentiment
    """

    toxicity: Optional[Toxicity] = None
    """The toxicity model output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/toxicity
    """

    url: Optional[URL] = None
    """The url entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/url
    """

    username: Optional[Username] = None
    """The username entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/username
    """

    wordlist: Optional[Wordlist] = None
    """The wordlist entity matcher output if enabled in your project.

    Read more at https://docs.moderationapi.com/models/word
    """

    wordlists: Optional[List[Wordlist]] = None
    """The wordlist entity matcher outputs if enabled in your project.

    Read more at https://docs.moderationapi.com/models/word
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
