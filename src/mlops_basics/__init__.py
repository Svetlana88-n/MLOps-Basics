from collections.abc import Sequence
from math import sqrt


def rmse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    """RMSE for pressure values (hPa)."""
    if len(actual) != len(predicted):
        raise ValueError("lengths differ")
    if len(actual) == 0:
        raise ValueError("empty input")

    total = 0.0
    for i in range(len(actual)):
        diff = actual[i] - predicted[i]
        total += diff * diff
    return sqrt(total / len(actual))


def main() -> None:
    measured = [1013.2, 1010.5, 1008.9, 1015.1]
    forecast = [1012.8, 1011.0, 1008.5, 1016.0]
    print("Pressure RMSE:", round(rmse(measured, forecast), 4), "hPa")


def mae(actual: Sequence[float], predicted: Sequence[float]) -> float:
    if len(actual) != len(predicted):
        raise ValueError("lengths differ")
    if len(actual) == 0:
        raise ValueError("empty")

    total = 0.0
    for i in range(len(actual)):
        total += abs(actual[i] - predicted[i])
    return total / len(actual)
