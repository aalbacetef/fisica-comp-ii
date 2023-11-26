from matplotlib import pyplot as plt
from math import exp, cos, sin
from typing import Callable

from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params
from code.pecs.pec4.ex5 import pade


def taylor(alpha, beta, t0) -> Callable[[float], float]:
    a0 = exp(-1.0 * alpha * t0) + (beta * sin(t0))
    a1 = (-alpha * exp(-alpha * t0)) + (beta * cos(t0))
    a2 = 0.5 * ((alpha * alpha * exp(-alpha * t0)) - (beta * sin(t0)))
    a3 = (-1.0 / 6.0) * (
        (alpha * alpha * alpha * exp(-alpha * t0)) + (beta * cos(t0))
    )

    def inner(t):
        x = t - t0
        x_2 = x * x
        x_3 = x * x * x
        return a0 + (a1 * x) + (a2 * x_2) + (a3 * x_3)

    return inner


if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]
    params = compute_params(xvals, yvals)
    t0 = 1.5

    T = taylor(params[ALPHA], params[BETA], t0)
    tvals = [T(x) for x in xvals]

    p = pade(params[ALPHA], params[BETA], t0)
    pvals = [p(x) for x in xvals]

    plt.figure(1)
    plt.plot(xvals, yvals, label="data", marker="x")
    plt.plot(xvals, tvals, label="taylor", marker="o", linestyle="")
    plt.plot(xvals, pvals, label="pade", marker="o", linestyle="")
    plt.legend()
    plt.savefig("t.png")
    plt.close()

    n = len(xvals)
    sum_err_taylor = 0.0
    sum_err_pade = 0.0
    for k in range(n):
        r_k_t = yvals[k] - tvals[k]
        r_k_p = yvals[k] - pvals[k]
        sum_err_taylor += r_k_t * r_k_t
        sum_err_pade += r_k_p * r_k_p

    print("err taylor: ")
    print(sum_err_taylor)
    print("err pade")
    print(sum_err_pade)
