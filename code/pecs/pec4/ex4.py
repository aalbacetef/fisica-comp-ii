from math import exp, sin

from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params


def r_k(xvals: list[float], yvals: list[float]):
    def inner(params: list[float], k: int):
        y_k = yvals[k]
        return y_k - f_k(params, xvals[k])

    return inner


def second_partial_alpha(r_fn, xvals, params):
    alpha = params[ALPHA]
    s = 0.0
    for k in range(len(xvals)):
        x_k = xvals[k]
        c0 = exp(-1.0 * alpha * x_k)
        c1 = x_k * x_k

        a = r_fn(params, k) * c0 * c1
        b = c1 * c0 * c0

        s += a - b

    return -2.0 * s


def second_partial_beta(xvals):
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
