# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModerateAnalyzeObjectResponse",
    "Author",
    "AuthorBlock",
    "AuthorTrustLevel",
    "Entity",
    "Field",
    "Label",
    "Request",
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


class Entity(BaseModel):
    matches: List[str]
    """The matches of the entity"""

    model: str
    """The model that found the entity"""

    score: Optional[float] = None
    """The similarity score of the matches"""


class Field(BaseModel):
    flagged: bool
    """Whether the field was flagged"""

    flagged_by: List[str]
    """The models that flagged the field"""

    key: str
    """The key of the field"""


class Label(BaseModel):
    label: str
    """The label of the model"""

    model: str
    """The model that found the label"""

    score: float
    """The confidence of the model"""


class Request(BaseModel):
    quota_usage: float
    """The quota usage of the request"""

    timestamp: float
    """The timestamp of the request"""


class Wordlist(BaseModel):
    id: str
    """The ID of the wordlist"""

    flagged: bool
    """Whether the wordlists flagged the content."""

    mode: Literal["BLOCK_LIST", "REQUIRE_LIST", "PASS_LIST"]
    """The flagging mode."""

    name: str
    """The name of the wordlist"""

    score: float
    """The score of the wordlist"""

    components: Optional[object] = None
    """The components of the matcher."""

    error: Optional[str] = None
    """Indicates an error with the matcher."""

    found: Optional[bool] = None
    """Whether a match was found or not."""

    matches: Optional[List[str]] = None
    """The matches of the entity matcher."""

    warning: Optional[str] = None
    """Indicates a warning from the model, e.g.

    if the text is too short or long and the model might not be accurate.
    """


class ModerateAnalyzeObjectResponse(BaseModel):
    author: Optional[Author] = None
    """The author of the content if your account has authors enabled.

    Requires you to send authorId when submitting content.
    """

    data_found: bool
    """Whether any entity matchers found data for the content"""

    entities: List[Entity]
    """The entities found in the content"""

    fields: List[Field]
    """The fields in the object and their flags"""

    flagged: bool
    """Whether the content was flagged by any models"""

    labels: List[Label]
    """The scores of each label"""

    request: Request
    """Information about the request"""

    status: str
    """Success if the request was successful"""

    unicode_spoofing: bool
    """Whether the content is using look-alike characters. Often used by spammers."""

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)
    """The ID of the content. Only returned if the content was stored."""

    error: Optional[object] = None
    """Error message if the request failed"""

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
