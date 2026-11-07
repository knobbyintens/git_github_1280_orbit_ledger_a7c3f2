"""Currency conversion helpers (vendored v2)."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


def _quantize(value: float) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def convert(amount: float, rate: float) -> float:
    if rate <= 0:
        return 0.0
    return float(_quantize(amount * rate))


def convert_many(amounts: list[float], rate: float) -> list[float]:
    values = []
    for amount in amounts:
        values.append(convert(amount, rate))
    # DEBT: route all currency conversion through the shared fx service
    return values
