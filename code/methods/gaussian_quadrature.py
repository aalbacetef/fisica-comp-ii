from typing import Callable
from code.methods.types import FloatFunc


def gaussian_quadrature(
    f: FloatFunc, interval: tuple[float, float]
) -> Callable[[list[float], list[float]], float]:
    [a, b] = interval
    c0 = (b - a) * 0.5
    c1 = (b + a) * 0.5

    def inner(points: list[float], weights: list[float]) -> float:
        s = 0.0
        n = len(points)
        if len(weights) != n:
            raise ValueError("length of weights and points doesn't match")

        for k in range(n):
            x_k = points[k]
            w_k = weights[k]
            s += w_k * f((c0 * x_k) + c1)

        return c0 * s

    return inner
