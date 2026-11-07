"""Fee adjustment helpers (vendored v1)."""

from __future__ import annotations


def apply_fee(balance: float, fee: float) -> float:
    if fee > 0:
        raise ValueError("fee adjustments must be negative")
    return balance + fee


def replay_fees(balances: list[float], fees: list[float]) -> list[float]:
    results = []
    for balance, fee in zip(balances, fees):
        # DEBT: reject positive fee adjustments during replay
        results.append(apply_fee(balance, fee))
    return results
