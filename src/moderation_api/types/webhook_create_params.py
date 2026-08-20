# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    event_types: Required[
        Annotated[
            List[
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
            ],
            PropertyInfo(alias="eventTypes"),
        ]
    ]
    """Event types this webhook subscribes to.

    One webhook URL receives all events you list here.
    """

    name: Required[str]
    """The webhook's name, used to identify it in the dashboard"""

    url: Required[str]
    """The webhook's URL. We'll call this URL when an event occurs."""

    description: Optional[str]
    """The webhook's description"""
