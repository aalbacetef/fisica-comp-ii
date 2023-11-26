from matplotlib import pyplot as plt
from math import exp, cos, sin

from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params
from code.pecs.pec4.ex5 import pade

if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]

    params = compute_params(xvals, yvals)

    pade_fn = [
        pade(params[ALPHA], params[BETA], 1.0),
        pade(params[ALPHA], params[BETA], 1.5),
        pade(params[ALPHA], params[BETA], 2.0),
    ]

    least_squares = [f_k(params, x_k) for x_k in xvals]
    pade_errors = [
        [abs(least_squares[k] - fn(xvals[k])) for k in range(len(xvals))]
        for fn in pade_fn
    ]

    plt.figure(1)
    plt.plot(xvals, pade_errors[0], label="error t0 = 1.0")
    plt.plot(xvals, pade_errors[1], label="error t0 = 1.5")
    plt.plot(xvals, pade_errors[2], label="error t0 = 2.0")
    plt.legend()
    plt.savefig("pecs/pec4/figures/error_abs_pade.png")

    t0 = [1.0, 1.5, 2.0]
    for k in range(len(pade_errors)):
        pd = pade_errors[k]
        s = 0.0
        for v in pd:
            s += v
        print("error t0=%f = %f" % (t0[k], s))
