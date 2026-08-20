# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookSecretRetrieveResponse"]


class WebhookSecretRetrieveResponse(BaseModel):
    secret: str
    """The signing secret for this project.

    Every webhook delivery is signed with HMAC-SHA256 over the raw JSON body,
    hex-encoded in the `modapi-signature` header.
    """
