from matplotlib import pyplot as plt

from code.pecs.pec4.data import ALPHA, BETA, datos, f_k
from code.pecs.pec4.ex3 import compute_params
from code.pecs.pec4.ex5 import pade

if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]
    t0 = [1.0, 1.5, 2.0]

    params = compute_params(xvals, yvals)
    pade_fn = [pade(params[ALPHA], params[BETA], t0_k) for t0_k in t0]

    least_squares = [f_k(params, x_k) for x_k in xvals]
    pade_errors = [
        [abs(least_squares[k] - fn(xvals[k])) for k in range(len(xvals))]
        for fn in pade_fn
    ]

    plt.figure(1)
    for k in range(len(t0)):
        plt.plot(xvals, pade_errors[k], label="error t0 = {}".format(t0[k]))
    plt.legend()
    plt.savefig("pecs/pec4/figures/error_abs_pade.png")

    for k in range(len(pade_errors)):
        pd = pade_errors[k]
        s = 0.0
        for v in pd:
            s += v
        print("error t0=%f = %f" % (t0[k], s))
