# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AuthorCreateParams", "Metadata"]


class AuthorCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user, typically the ID of the author in your database."""

    email: Optional[str]
    """Author email address"""

    external_link: Optional[str]
    """URL of the author's external profile"""

    first_seen: float
    """Timestamp when author first appeared"""

    last_seen: float
    """Timestamp of last activity"""

    manual_trust_level: Optional[float]

    metadata: Metadata
    """Additional metadata provided by your system.

    We recommend including any relevant information that may assist in the
    moderation process.
    """

    name: Optional[str]
    """Author name or identifier"""

    profile_picture: Optional[str]
    """URL of the author's profile picture"""


class Metadata(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Additional metadata provided by your system.

    We recommend including any relevant information that may assist in the moderation process.
    """

    email_verified: Optional[bool]
    """Whether the author's email is verified"""

    identity_verified: Optional[bool]
    """Whether the author's identity is verified"""

    is_paying_customer: Optional[bool]
    """Whether the author is a paying customer"""

    phone_verified: Optional[bool]
    """Whether the author's phone number is verified"""
