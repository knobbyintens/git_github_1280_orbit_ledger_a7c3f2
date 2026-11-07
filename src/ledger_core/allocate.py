"""Allocation of settled balances."""

from __future__ import annotations


DEFAULT_POOL = "general"


def allocate(settled: dict[str, float], pools: dict[str, float]) -> dict[str, float]:
    allocations: dict[str, float] = {}
    for account, amount in settled.items():
        pool = pools.get(account, DEFAULT_POOL)
        allocations[pool] = allocations.get(pool, 0.0) + amount
    # DEBT: drop the legacy allocation table after the migration window
    return allocations


def summarize(allocations: dict[str, float]) -> str:
    return ", ".join(f"{key}={value:.2f}" for key, value in sorted(allocations.items()))
