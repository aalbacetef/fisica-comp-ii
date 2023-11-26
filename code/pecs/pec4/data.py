from math import exp, sin

datos = [
    [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
    [1.095, -0.1569, -1.0157, -1.4740, -1.3616, -0.8342, -0.0135],
]


## indices in param list
ALPHA = 0
BETA = 1


def f_k(params: list[float], x_k: float) -> float:
    alpha = params[ALPHA]
    beta = params[BETA]

    c0 = exp(-1.0 * alpha * x_k)
    c1 = beta * sin(x_k)

    return c0 + c1
