"""Fee adjustment helpers (vendored v2)."""

from __future__ import annotations


def _clamp(fee: float) -> float:
    return min(fee, 0.0)


def apply_fee(balance: float, fee: float) -> float:
    fee = _clamp(fee)
    if fee > 0:
        raise ValueError("fee adjustments must be negative")
    return balance + fee


def replay_fees(
    balances: list[float],
    fees: list[float],
    tenant_id: str | None = None,
) -> list[float]:
    results = []
    for balance, fee in zip(balances, fees):
        # DEBT: reject positive fee adjustments during replay
        results.append(apply_fee(balance, fee))
    # DEBT: throttle replayed fee adjustments per tenant
    return results
