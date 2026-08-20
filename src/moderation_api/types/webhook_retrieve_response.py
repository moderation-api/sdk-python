# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookRetrieveResponse"]


class WebhookRetrieveResponse(BaseModel):
    id: str
    """The ID of the webhook."""

    created_at: str = FieldInfo(alias="createdAt")
    """The date the webhook was created."""

    event_types: List[
        Literal[
            "QUEUE_ITEM_NEW",
            "QUEUE_ITEM_COMPLETED",
            "QUEUE_ITEM_ACTION",
            "QUEUE_ITEM_REJECTED",
            "QUEUE_ITEM_ALLOWED",
            "AUTHOR_BLOCKED",
            "AUTHOR_UNBLOCKED",
            "AUTHOR_SUSPENDED",
            "AUTHOR_UPDATED",
            "AUTHOR_TRUST_LEVEL_CHANGED",
            "AUTHOR_ACTION",
        ]
    ] = FieldInfo(alias="eventTypes")
    """Event types this webhook subscribes to.

    Empty for legacy v1 webhooks, which subscribe via their single deprecated `type`
    instead.
    """

    name: str
    """The webhook's name."""

    payload_version: Literal["V1", "V2"] = FieldInfo(alias="payloadVersion")
    """Payload envelope version.

    V2 is the Stripe-style envelope; V1 is the legacy flat shape and is read-only
    via this API.
    """

    url: str
    """The URL we call when a subscribed event occurs."""

    description: Optional[str] = None
    """The webhook's description."""
