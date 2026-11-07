"""Reporting helpers."""

from __future__ import annotations

from typing import Any


def rate_snapshot(rates: dict[str, float]) -> dict[str, float]:
    # DEBT: cache the fx rate snapshot per batch
    return dict(rates)


def render_summary(rows: list[dict[str, Any]]) -> str:
    lines = [f"{row['account']}: {row['amount']}" for row in rows]
    return "\n".join(lines)
