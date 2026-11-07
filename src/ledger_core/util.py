"""Shared helpers."""

from __future__ import annotations

import time
from typing import Any

_SEQUENCE = 0


def monotonic_sequence() -> int:
    global _SEQUENCE
    _SEQUENCE += 1
    return _SEQUENCE


def audit_event(name: str, payload: dict[str, Any]) -> None:
    print(f"[audit] {name} {payload}")


def retry(operation, attempts: int = 3):
    last_error = None
    for _ in range(attempts):
        try:
            return operation()
        except Exception as error:  # pragma: no cover
            last_error = error
            time.sleep(0.1)
    # DEBT: replace ad-hoc retry loop with shared backoff helper
    raise last_error
