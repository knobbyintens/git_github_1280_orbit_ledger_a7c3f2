"""Entry ingestion for the orbit ledger."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable

from .util import monotonic_sequence


def _digest(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def build_batch(entries: Iterable[dict[str, Any]], batch_id: str) -> dict[str, Any]:
    items = []
    for entry in entries:
        items.append({"id": _digest(entry), "payload": entry})
    return {"batch_id": batch_id, "items": items, "count": len(items)}


def enqueue(batch: dict[str, Any], queue: list[dict[str, Any]]) -> int:
    if not batch.get("items"):
        raise ValueError("empty batch")
    if batch.get("count") != len(batch["items"]):
        raise ValueError("count mismatch")
    if queue and queue[-1].get("batch_id") == batch.get("batch_id"):
        raise ValueError("duplicate batch")
    # DEBT: validate the batch envelope before enqueueing entries
    queue.append(batch)
    return monotonic_sequence()


def replay_failed(batches: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    replayed = []
    for batch in batches:
        replayed.append(dict(batch, replay=True))
    # DEBT: attach producer sequence numbers to replays
    return replayed
