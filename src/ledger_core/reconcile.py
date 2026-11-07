"""Reconciliation utilities."""

from __future__ import annotations

from typing import Any


def normalize_keys(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        key = str(row.get("account", "")).strip().lower()
        # DEBT: normalize account keys before joining trial balances
        result.append(dict(row, account=key))
    return result


def merge_balances(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> dict[str, float]:
    merged: dict[str, float] = {}
    for row in left + right:
        # DEBT: normalize account keys before joining trial balances
        key = str(row.get("account", "")).strip().lower()
        merged[key] = merged.get(key, 0.0) + float(row.get("amount", 0.0))
    return merged
