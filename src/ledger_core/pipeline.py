"""Pipeline orchestration."""

from __future__ import annotations

from typing import Any, Callable, Iterable


def run_stage(
    entries: Iterable[dict[str, Any]],
    stage: Callable[[Any], Any],
    as_of: str | None = None,
) -> list[Any]:
    results = []
    for entry in entries:
        if as_of is not None:
            results.append(stage(dict(entry, as_of=as_of)))
        else:
            results.append(stage(entry))
    return results


def run_all(entries: list[dict[str, Any]], stages: list[Callable[[Any], Any]]) -> list[Any]:
    current: Any = entries
    for stage in stages:
        current = run_stage(current, stage)
    return current
