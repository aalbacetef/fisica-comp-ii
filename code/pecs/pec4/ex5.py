from matplotlib import pyplot as plt
from math import exp, cos, sin
from typing import Callable

from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params


def pade(alpha, beta, t0) -> Callable[[float], float]:
    a0 = exp(-1.0 * alpha * t0) + (beta * sin(t0))
    a1 = (-alpha * exp(-alpha * t0)) + (beta * cos(t0))
    a2 = 0.5 * ((alpha * alpha * exp(-alpha * t0)) - (beta * sin(t0)))
    a3 = (-1.0 / 6.0) * (
        (alpha * alpha * alpha * exp(-alpha * t0)) + (beta * cos(t0))
    )

    q0 = 1
    q1 = (-1.0 * a3) / a2
    p0 = a0
    p1 = a1 + (a0 * q1)
    p2 = a2 + (a1 * q1)

    def inner(t):
        x = t - t0
        p = p0 + (p1 * x) + (p2 * x * x)
        q = q0 + (q1 * x)
        return p / q

    return inner


if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]
    params = compute_params(xvals, yvals)

    pade_fn = pade(params[ALPHA], params[BETA], 1.5)
    pade_approx = [pade_fn(x) for x in xvals]

    least_squares_approx = [f_k(params, x_k) for x_k in xvals]

    plt.figure(1)
    plt.plot(xvals, yvals, marker="x", label="data", linestyle=":")
    plt.plot(xvals, pade_approx, marker="x", label="pade", linestyle=":")
    plt.plot(
        xvals,
        least_squares_approx,
        marker="x",
        label="least squares",
        linestyle=":",
    )
    plt.legend()
    plt.savefig("pecs/pec4/figures/compare_approx.png")
    plt.close()

    n = len(xvals)

    err_pade = []
    err_least_squares = []
    sum_err_pade = 0.0
    sum_err_least_squares = 0.0

    for k in range(n):
        r_pade = yvals[k] - pade_approx[k]
        r_least_squares = yvals[k] - least_squares_approx[k]
        err_pade.append(r_pade * r_pade)
        err_least_squares.append(r_least_squares * r_least_squares)
        sum_err_pade += err_pade[k]
        sum_err_least_squares += err_least_squares[k]

    plt.figure(1)
    plt.plot(xvals, err_pade, label="residue pade")
    plt.plot(xvals, err_least_squares, label="residueleast squares")
    plt.legend()
    plt.savefig("pecs/pec4/figures/errores_quad_approx.png")
    plt.close()

    print("err pade: %f" % sum_err_pade)
    print("err least squares: %f" % sum_err_least_squares)
