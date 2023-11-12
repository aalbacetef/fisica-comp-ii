from typing import Callable, TypeAlias
from code.methods.types import DataPoints, FloatFunc, PolynomialList


def l_k(k: int, points: list[float]) -> FloatFunc:
    """generate the l_k basis function of the lagrange polynomial."""
    n = len(points)

    x_k = points[k]

    def l_k_fn(x: float) -> float:
        value = 1.0
        for i in range(n):
            if i == k:
                continue

            x_i = points[i]

            if x_i == x_k:
                raise ValueError("x_%d == x_%d (val=%f)" % (i, k, x_i))

            value *= (x - x_i) / (x_k - x_i)

        return value

    return l_k_fn


def lagrangian_interpolation(data_points: DataPoints) -> FloatFunc:
    """generate the L_n(x) function."""
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    n = len(x)
    basis = [l_k(k, x) for k in range(n)]

    def interpolation_fn(x_p: float) -> float:
        value = 0.0

        for k in range(n):
            value += y[k] * basis[k](x_p)
        return value

    return interpolation_fn


def generate_polynomials(order: int, data_points: DataPoints) -> PolynomialList:
    # for an m-order polynomial, we need m+1 points
    req_points = order + 1

    if len(data_points) < req_points:
        raise ValueError(
            "insufficient points, want at least %d, got %d"
            % (req_points, len(data_points)),
        )

    # the number of polynomials we'll generate
    n = len(data_points) - order
    polynomials = [
        lagrangian_interpolation(data_points[k : k + req_points])
        for k in range(n)
    ]

    return polynomials
