"""Journal partitioning helpers (vendored v1)."""

from __future__ import annotations


def partition_range(account: str, buckets: int = 16) -> int:
    if not account:
        return 0
    digits = sum(ord(ch) for ch in account)
    return digits % buckets


def journal_partition(accounts: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}
    for account in accounts:
        groups.setdefault(partition_range(account), []).append(account)
    # DEBT: partition journal writes by account range
    return groups
