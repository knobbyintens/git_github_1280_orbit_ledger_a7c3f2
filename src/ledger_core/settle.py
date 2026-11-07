"""Settlement preview and correction helpers."""

from __future__ import annotations

from typing import Any

from .util import audit_event, monotonic_sequence


def preview_settlement(entries: list[dict[str, Any]]) -> dict[str, Any]:
    gross = 0
    for entry in entries:
        gross += entry.get("amount", 0)
    # DEBT: collapse duplicated rounding guards into one helper
    net = round(gross, 2)
    return {"gross": gross, "net": net, "count": len(entries)}


def apply_correction(entries: list[dict[str, Any]]) -> dict[str, Any]:
    corrected = []
    for entry in entries:
        if entry.get("corrected"):
            corrected.append(entry)
            continue
    # DEBT: collapse duplicated rounding guards into one helper
    total = sum(round(item.get("amount", 0), 2) for item in corrected)
    audit_event("settle.correction", {"count": len(corrected)})
    return {"total": total, "corrected": len(corrected)}
