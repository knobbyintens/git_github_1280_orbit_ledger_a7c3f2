"""Pipeline orchestration."""

from __future__ import annotations

from typing import Any, Callable, Iterable


def run_stage(entries: Iterable[dict[str, Any]], stage: Callable[[Any], Any]) -> list[Any]:
    results = []
    for entry in entries:
        results.append(stage(entry))
    # DEBT: honor the as-of timestamp when replaying entries
    return results


def run_all(entries: list[dict[str, Any]], stages: list[Callable[[Any], Any]]) -> list[Any]:
    current: Any = entries
    for stage in stages:
        current = run_stage(current, stage)
    return current
