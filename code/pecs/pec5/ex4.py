from typing import Callable

from matplotlib import pyplot as plt

from code.methods.types import FloatFunc
from code.pecs.pec5.data import quad_point_data


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
    n = 64

    # generate gaussian quadrature x_i
    gauss_f = shifted_x(interval)
    gauss_x = [gauss_f(xi) for xi in points]
    gauss_x.sort()

    # generate trapezium points (n=64)
    trap_f = trapezium_points(interval)
    trap_x = trap_f(n)

    indices = [k + 1 in range(n)]

    plt.figure(1)
    plt.plot(indices, gauss_x, linestyle="dotted", marker="o", label="gauss")
    plt.plot(indices, trap_x, linestyle="dotted", marker="x", label="trap")
    plt.legend()
    plt.savefig("pecs/pec5/figures/gauss_trap_xi.png")
    plt.close()

    # errors
    r
