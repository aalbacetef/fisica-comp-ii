from math import exp, sin

from code.methods.types import Vector, FuncVectorK

datos = [
    [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
    [1.095, -0.1569, -1.0157, -1.4740, -1.3616, -0.8342, -0.0135],
]


## indices in param list
ALPHA = 0
BETA = 1


def f_k(params: Vector, x_k: float) -> float:
    """provided function D(t) = exp(-alpha*t) + beta*sin(t)"""
    alpha = params[ALPHA]
    beta = params[BETA]

    c0 = exp(-1.0 * alpha * x_k)
    c1 = beta * sin(x_k)

    return c0 + c1


def r_k(xvals: Vector, yvals: Vector) -> FuncVectorK:
    """k-th residue"""

    def inner(params: Vector, k: int) -> float:
        y_k = yvals[k]
        return y_k - f_k(params, xvals[k])

    return inner
