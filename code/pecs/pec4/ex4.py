from math import exp, sin

from code.methods.types import FuncVectorK, Vector
from code.pecs.pec4.data import ALPHA, datos, r_k
from code.pecs.pec4.ex3 import compute_params


def second_partial_alpha(
    r_fn: FuncVectorK, xvals: Vector, params: Vector
) -> float:
    alpha = params[ALPHA]
    s = 0.0
    n = len(xvals)
    for k in range(n):
        x_k = xvals[k]
        c0 = exp(-1.0 * alpha * x_k)
        c1 = x_k * x_k

        a = r_fn(params, k) * c0 * c1
        b = c1 * c0 * c0

        s += a - b

    return -2.0 * s


def second_partial_beta(xvals: Vector) -> float:
    s = 0.0
    for x_k in xvals:
        v = sin(x_k)
        s += v * v
    return 2.0 * s


if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]

    params = compute_params(xvals, yvals)
    r_fn = r_k(xvals, yvals)
    alpha_test = second_partial_alpha(r_fn, xvals, params)
    print("alpha_test:")
    print(alpha_test)
    beta_test = second_partial_beta(xvals)
    print("beta_test: ")
    print(beta_test)
