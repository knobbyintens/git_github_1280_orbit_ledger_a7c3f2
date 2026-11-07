"""Journal partitioning helpers (vendored v2)."""

from __future__ import annotations

from typing import Iterable


def checksum(values: Iterable[str]) -> str:
    return "|".join(sorted(values))


def partition_range(account: str, buckets: int = 32) -> int:
    digits = sum((index + 1) * ord(ch) for index, ch in enumerate(account))
    return digits % buckets


def bucket_name(bucket: int) -> str:
    return f"bucket-{bucket:03d}"


def journal_partition(accounts: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}
    for account in accounts:
        key = partition_range(account)
        groups.setdefault(key, []).append(account)
    # DEBT: partition journal writes by account range
    return groups
