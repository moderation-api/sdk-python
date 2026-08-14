# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QueueRetrieveResponse", "Queue", "QueueFilter", "QueueFilterFilterLabel"]


class QueueFilterFilterLabel(BaseModel):
    label: str

    type: Literal["FLAGGED", "NOT_FLAGGED", "THRESHOLDS", "MATCHED"]

    max_threshold: Optional[float] = FieldInfo(alias="maxThreshold", default=None)

    min_threshold: Optional[float] = FieldInfo(alias="minThreshold", default=None)


class QueueFilter(BaseModel):
    after_date: Optional[str] = FieldInfo(alias="afterDate", default=None)

    author_id: Optional[str] = FieldInfo(alias="authorID", default=None)

    author_trust_levels: Optional[List[int]] = FieldInfo(alias="authorTrustLevels", default=None)

    before_date: Optional[str] = FieldInfo(alias="beforeDate", default=None)

    check_status: Optional[Literal["all", "checked", "unchecked"]] = FieldInfo(alias="checkStatus", default=None)

    clear_date_window: Optional[bool] = FieldInfo(alias="clearDateWindow", default=None)

    content_id: Optional[str] = FieldInfo(alias="contentID", default=None)

    content_types: Optional[
        List[Literal["profile", "message", "post", "comment", "event", "product", "review", "voice", "other"]]
    ] = FieldInfo(alias="contentTypes", default=None)

    conversation_ids: Optional[List[Optional[str]]] = FieldInfo(alias="conversationIds", default=None)

    filtered_action_ids: Optional[List[str]] = FieldInfo(alias="filteredActionIds", default=None)

    filtered_channel_ids: Optional[List[str]] = FieldInfo(alias="filteredChannelIds", default=None)

    filter_labels: Optional[List[QueueFilterFilterLabel]] = FieldInfo(alias="filterLabels", default=None)

    is_flagged: Optional[Literal["ALL", "FLAGGED", "NOT_FLAGGED", "SHADOW_FLAGGED"]] = FieldInfo(
        alias="isFlagged", default=None
    )

    labels: Optional[List[str]] = None

    languages: Optional[List[str]] = None

    max_severity: Optional[int] = FieldInfo(alias="maxSeverity", default=None)

    media_types: Optional[List[Literal["text", "image", "video", "object", "audio"]]] = FieldInfo(
        alias="mediaTypes", default=None
    )

    min_severity: Optional[int] = FieldInfo(alias="minSeverity", default=None)

    recommendation_actions: Optional[List[Literal["review", "allow", "reject"]]] = FieldInfo(
        alias="recommendationActions", default=None
    )

    search: Optional[List[str]] = None

    within: Optional[float] = None

    within_unit: Optional[Literal["MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"]] = FieldInfo(
        alias="withinUnit", default=None
    )


class Queue(BaseModel):
    id: str

    description: str

    filter: QueueFilter

    name: str

    resolved_items_count: float = FieldInfo(alias="resolvedItemsCount")

    total_items_count: float = FieldInfo(alias="totalItemsCount")

    unresolved_items_count: float = FieldInfo(alias="unresolvedItemsCount")


class QueueRetrieveResponse(BaseModel):
    queue: Queue
