# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModerateAnalyzeVideoResponse", "Author", "AuthorBlock", "AuthorTrustLevel", "Request"]


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


class ModerateAnalyzeVideoResponse(BaseModel):
    author: Optional[Author] = None
    """The author of the content if your account has authors enabled.

    Requires you to send authorId when submitting content.
    """

    flagged: bool
    """Whether the content was flagged by any models"""

    request: Request
    """Information about the request"""

    status: str
    """Success if the request was successful"""

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)
    """The ID of the content. Only returned if the content was stored."""

    error: Optional[object] = None
    """Error message if the request failed"""

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
