from typing import Callable
from code.methods.gaussian_quadrature import gaussian_quadrature
from code.methods.romberg import romberg
from code.methods.trapezium import trapezium
from code.util import write_csv

from matplotlib import pyplot as plt

from code.methods.types import FloatFunc
from code.pecs.pec5.data import quad_point_data, antideriv_C, antideriv_S


def shifted_x(interval: tuple[float, float]) -> FloatFunc:
    [a, b] = interval
    c0 = (b - a) * 0.5
    c1 = (b + a) * 0.5

    def inner(x: float) -> float:
        return (c0 * x) + c1

    return inner


def trapezium_points(
    interval: tuple[float, float],
) -> Callable[[int], list[float]]:
    [a, b] = interval

    def inner(n: int) -> list[float]:
        delta_x = (b - a) / float(n)

        x_0 = a
        x_n = b

        x_k = [x_0 + (float(k) * delta_x) for k in range(1, n)]

        return x_k + [x_n]

    return inner


if __name__ == "__main__":
    gauss_quad_data = quad_point_data()
    points = gauss_quad_data["legendre_roots"]
    w = 5.0
    interval = (0.0, w)
    m = 8
    n = 64

    # generate gaussian quadrature x_i
    gauss_f = shifted_x(interval)
    gauss_x = [gauss_f(xi) for xi in points]
    gauss_x.sort()

    # generate trapezium points (n=64)
    trap_f = trapezium_points(interval)
    trap_x = trap_f(n)

    indices = [k + 1 for k in range(n)]
    diffs_trap = [trap_x[k] - trap_x[k - 1] for k in range(1, n)]
    diffs_gauss = [gauss_x[k] - gauss_x[k - 1] for k in range(1, n)]

    plt.figure(1)
    plt.plot(indices, gauss_x, linestyle="dotted", marker="o", label="gauss")
    plt.plot(indices, trap_x, linestyle="dotted", marker="x", label="trap")
    plt.legend()
    plt.savefig("pecs/pec5/figures/gauss_trap_xi.png")
    plt.close()
    plt.figure(1)
    plt.plot(indices[1:], diffs_trap, label="trap")
    plt.plot(indices[1:], diffs_gauss, label="gauss")
    plt.legend()
    plt.savefig("pecs/pec5/figures/gauss_trap_diff_xi.png")

    # write csv comparing points
    hdr = ["index", "gaussian quadrature", "trapezium points"]
    rows = [[indices[k], gauss_x[k], trap_x[k]] for k in range(n)]
    write_csv(hdr, rows, "pecs/pec5/data/xi_comp.csv")

    # approximations
    trap_c = trapezium(antideriv_C, interval)(n)
    trap_s = trapezium(antideriv_S, interval)(n)
    gauss_c = gaussian_quadrature(antideriv_C, interval)(
        gauss_quad_data["legendre_roots"], gauss_quad_data["weights"]
    )
    gauss_s = gaussian_quadrature(antideriv_S, interval)(
        gauss_quad_data["legendre_roots"], gauss_quad_data["weights"]
    )
    r_c = romberg(antideriv_C, interval)(m)[-1][-1]
    r_s = romberg(antideriv_S, interval)(m)[-1][-1]

    # calculate errors
    error_trap = [
        trap_c - r_c,
        trap_s - r_s,
    ]

    error_gauss = [
        gauss_c - r_c,
        gauss_s - r_s,
    ]

    # save
    hdr = ["approx.", "C(w)", "S(w)"]
    rows = [
        ["trap", error_trap[0], error_trap[1]],
        ["gauss", error_gauss[0], error_gauss[1]],
    ]

    write_csv(hdr, rows, "pecs/pec5/data/abs_error_approx.csv")

    rows = [
        [
            "trap",
            100.0 * abs(error_trap[0]) / r_c,
            100.0 * abs(error_trap[1]) / r_s,
        ],
        [
            "gauss",
            100.0 * abs(error_gauss[0]) / r_c,
            100.0 * abs(error_gauss[1]) / r_s,
        ],
    ]
    write_csv(hdr, rows, "pecs/pec5/data/rel_error_approx.csv")
