"""Verify webhook deliveries from Moderation API.

Every delivery is signed with HMAC-SHA256 over the raw request body, using
your project's webhook signing secret. The hex-encoded signature is in the
`modapi-signature` header.

Maintained by hand in moderation-api/sdk-generator (custom/python), not
generated.
"""

import hashlib
import hmac
import json
import os
from typing import Any, Optional, Union

SIGNATURE_HEADER = "modapi-signature"
SECRET_ENV_VAR = "MODAPI_WEBHOOK_SECRET"


class WebhookSignatureError(Exception):
    """The webhook signature is missing or does not match the payload."""


def _to_bytes(value: Union[str, bytes]) -> bytes:
    return value.encode("utf-8") if isinstance(value, str) else value


def compute_signature(payload: Union[str, bytes], secret: str) -> str:
    """Return the hex HMAC-SHA256 signature for a raw payload."""
    return hmac.new(_to_bytes(secret), _to_bytes(payload), hashlib.sha256).hexdigest()


def _secret(secret: Optional[str]) -> str:
    if secret:
        return secret
    return os.environ.get(SECRET_ENV_VAR) or ""


def verify_signature(
    payload: Union[str, bytes], signature: str, secret: Optional[str] = None
) -> bool:
    """Return True if `signature` matches the raw `payload`.

    `secret` defaults to the MODAPI_WEBHOOK_SECRET environment variable.
    """
    secret = _secret(secret)
    if not signature or not secret:
        return False
    expected = compute_signature(payload, secret)
    return hmac.compare_digest(expected, signature.strip().lower())


def construct_event(
    payload: Union[str, bytes], signature: str, secret: Optional[str] = None
) -> Any:
    """Verify a delivery and return the parsed event.

    Pass the raw request body exactly as received and the value of the
    `modapi-signature` header. `secret` defaults to the MODAPI_WEBHOOK_SECRET
    environment variable.

    Raises WebhookSignatureError when the signature does not match.
    """
    if not verify_signature(payload, signature, secret):
        raise WebhookSignatureError("Webhook signature does not match the payload")
    return json.loads(payload)
