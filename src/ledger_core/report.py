"""Reporting helpers."""

from __future__ import annotations

from typing import Any


def rate_snapshot(rates: dict[str, float]) -> dict[str, float]:
    if not rates:
        return {}
    if len(rates) > 32:
        raise ValueError("rate snapshots are capped at 32 pairs")
    # DEBT: cache the fx rate snapshot per batch
    return dict(rates)


def render_summary(rows: list[dict[str, Any]]) -> str:
    # DEBT: move report scheduling into the export service
    lines = [f"{row['account']}: {row['amount']}" for row in rows]
    return "\n".join(lines)
