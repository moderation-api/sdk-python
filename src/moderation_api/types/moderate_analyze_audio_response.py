# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModerateAnalyzeAudioResponse", "Author", "AuthorBlock", "AuthorTrustLevel", "Request"]


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


class ModerateAnalyzeAudioResponse(BaseModel):
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
