from math import exp, cos, sin

from matplotlib import pyplot as plt

from code.methods.types import Vector
from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params
from code.pecs.pec4.ex5 import pade


def taylor_coeffs(alpha: float, beta: float, t0: float) -> Vector:
    a0 = exp(-1.0 * alpha * t0) + (beta * sin(t0))
    a1 = (-alpha * exp(-alpha * t0)) + (beta * cos(t0))
    a2 = 0.5 * ((alpha * alpha * exp(-alpha * t0)) - (beta * sin(t0)))
    a3 = (-1.0 / 6.0) * (
        (alpha * alpha * alpha * exp(-alpha * t0)) + (beta * cos(t0))
    )

    return [a0, a1, a2, a3]


def taylor(coeffs: Vector, t: float) -> float:
    [a0, a1, a2, a3] = coeffs

    x = t - t0
    x_2 = x * x
    x_3 = x * x * x
    return a0 + (a1 * x) + (a2 * x_2) + (a3 * x_3)


if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]
    params = compute_params(xvals, yvals)
    t0 = 1.5

    # compute values for taylor approximation
    coeffs = taylor_coeffs(params[ALPHA], params[BETA], t0)
    for k in range(len(coeffs)):
        print("a{} = {}".format(k, coeffs[k]))

    tvals = [taylor(coeffs, x) for x in xvals]

    # compute values for pade approximation
    p = pade(params[ALPHA], params[BETA], t0)
    pvals = [p(x) for x in xvals]

    # plot taylor approximation
    plt.figure(1)
    plt.plot(xvals, yvals, label="data", marker="x")
    plt.plot(xvals, tvals, label="taylor", marker="o", linestyle="")
    plt.legend()
    plt.savefig("pecs/pec4/figures/taylor_expansion.png")
    plt.close()

    # calculate quadratic error for taylor
    n = len(xvals)
    sum_err_taylor = 0.0
    err_taylor_qd = []
    for k in range(n):
        r_k_t = yvals[k] - tvals[k]
        err_taylor_qd.append(r_k_t * r_k_t)
        sum_err_taylor += err_taylor_qd[k]

    # plot taylor quadratic error
    plt.figure(1)
    plt.plot(xvals, err_taylor_qd, label="T(x) SRR")
    plt.legend()
    plt.savefig("pecs/pec4/figures/taylor_quad_err.png")
    plt.close()

    print("quadratic err taylor: ")
    print(sum_err_taylor)

    # least squares approx
    l_sq = [f_k(params, x_k) for x_k in xvals]
    n = len(xvals)
    approximations = [pvals, tvals]

    # plot errors (abs, quad) for pade and taylor with respect to least squares approx.
    abs_errors = [
        [abs(l_sq[k] - approx[k]) for k in range(n)]
        for approx in approximations
    ]
    quad_errors = [
        [((l_sq[k] - approx[k]) ** 2) for k in range(n)]
        for approx in approximations
    ]

    # plot absolute error w.r.t least squares approx
    plt.subplot(1, 2, 1)
    plt.plot(xvals, abs_errors[0], label="S - Pade", marker="x", linestyle="-.")
    plt.plot(
        xvals, abs_errors[1], label="S - Taylor", marker="x", linestyle="-."
    )
    plt.legend()

    # plot quadratic error w.r.t least squares approx
    plt.subplot(1, 2, 2)
    plt.plot(
        xvals, quad_errors[0], label="SRR - Pade", marker="x", linestyle="-."
    )
    plt.plot(
        xvals, quad_errors[1], label="SRR - Taylor", marker="x", linestyle="-."
    )
    plt.legend()

    plt.tight_layout()

    plt.savefig("pecs/pec4/figures/approximation_errors.png")
    plt.close()

    # print computed errors
    print("S - Pade: %f" % sum(abs_errors[0]))
    print("S - Taylor: %f" % sum(abs_errors[1]))
    print("SRR - Pade: %f" % sum(quad_errors[0]))
    print("SRR - Taylor: %f" % sum(quad_errors[1]))
