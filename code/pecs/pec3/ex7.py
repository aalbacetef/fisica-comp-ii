from math import factorial, log, sqrt

from matplotlib import pyplot as plt

from code.methods.types import FloatFunc
from code.pecs.pec3.data import carbon_age_tbl
from code.pecs.pec3.util import write_csv


def f_err_quad(xi: float) -> float:
    t_12 = 5370
    C = t_12 / log(2)

    return -2 * (xi**-3) * C


def f_err_cub(xi: float) -> float:
    t_12 = 5370
    C = t_12 / log(2)

    return 6 * (xi**-4) * C


def product(data_points: list[float]) -> FloatFunc:
    def a(x):
        p = 1
        for x_i in data_points:
            p = p * (x - x_i)
        return p

    return a


def error(n: int, f_err: float, prod: FloatFunc) -> FloatFunc:
    fac = 1.0 / factorial(n + 1)

    def res(x: float) -> float:
        return fac * f_err * prod(x)

    return res


if __name__ == "__main__":
    data_points = carbon_age_tbl
    xpoints = [point[0] for point in data_points]

    # [min, max]
    xi_quad = [0.92, 0.78]
    xi_cub = [0.92, 0.78]

    step = 0.01
    X = [k * step + 0.78 for k in range(20)]
    plt.figure(1)

    ## error polinomio cuadratico (min)
    n = 2
    err_quad_min = error(n, f_err_quad(xi_quad[0]), product(xpoints))

    Y_a = [sqrt(err_quad_min(x) ** 2) for x in X]

    (a,) = plt.plot(X, Y_a)

    ## error polinomio cuadratico (max)
    n = 2
    err_quad_max = error(n, f_err_quad(xi_quad[1]), product(xpoints))

    Y_b = [sqrt(err_quad_max(x) ** 2) for x in X]

    (b,) = plt.plot(X, Y_b)

    plt.legend([a, b], ["Err_quad | xi = xi_min", "Err_quad | xi = xi_max"])
    plt.savefig("pecs/pec3/figures/figure6.png")
    plt.close()

    plt.figure(1)

    ## error polinomio cubico (min)
    n = 3
    err_cub_min = error(n, f_err_cub(xi_cub[0]), product(xpoints))

    Y_c = [sqrt(err_cub_min(x) ** 2) for x in X]

    (c,) = plt.plot(X, Y_c)

    ## error polinomio cubico (max)
    n = 3
    err_cub_max = error(n, f_err_cub(xi_cub[1]), product(xpoints))

    Y_d = [sqrt(err_cub_max(x) ** 2) for x in X]

    (d,) = plt.plot(X, Y_d)

    plt.legend([c, d], ["Err_cub | xi = xi_min", "Err_cub | xi = xi_max"])

    plt.savefig("pecs/pec3/figures/figure7.png")

    # csv: min, max errors
    point = 0.8705
    hdr = ["error", "value"]
    rows = [
        ["quad. min", err_quad_min(point)],
        ["quad. max", err_quad_max(point)],
        ["cub. min", err_cub_min(point)],
        ["cub. max", err_cub_max(point)],
    ]

    write_csv(hdr, rows, "pecs/pec3/data/errors06.csv")
