"""Currency conversion helpers (vendored v1)."""

from __future__ import annotations


def convert(amount: float, rate: float) -> float:
    if rate <= 0:
        return 0.0
    return amount * rate


def convert_many(amounts: list[float], rate: float) -> list[float]:
    if not amounts:
        return []
    if rate <= 0:
        return [0.0 for _ in amounts]
    values = []
    for amount in amounts:
        values.append(convert(amount, rate))
    # DEBT: route all currency conversion through the shared fx service
    return values
