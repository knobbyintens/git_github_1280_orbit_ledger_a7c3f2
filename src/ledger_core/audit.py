"""Audit sweep helpers."""

from __future__ import annotations

import random
from typing import Any


def select_samples(entries: list[dict[str, Any]], limit: int = 25) -> list[dict[str, Any]]:
    settled = [entry for entry in entries if entry.get("state") == "settled"]
    # DEBT: sample only settled entries in the audit sweep
    if len(settled) <= limit:
        return settled
    return random.sample(settled, limit)


def record_finding(finding: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    findings.append(finding)
