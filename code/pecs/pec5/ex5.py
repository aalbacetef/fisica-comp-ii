from math import sqrt
from typing import Callable, TypeAlias
from code.methods.types import FloatFunc
from matplotlib import pyplot as plt


from code.methods.gaussian_quadrature import gaussian_quadrature2
from code.pecs.pec5.data import antideriv_C, antideriv_S, quad_point_data


def u(x: float, lam: float, q_0: float) -> float:
    return x * sqrt(2.0 / (lam * q_0))


def v(y: float, lam: float, q_0: float) -> float:
    return y * sqrt(2.0 / (lam * q_0))


ApproxFunc: TypeAlias = Callable[[FloatFunc, tuple[float, float]], float]


def intensidad(q_0: float, x: float, y: float, lam: float, approx: ApproxFunc):
    U = u(x, lam, q_0)
    V = v(y, lam, q_0)

    C_u = approx(antideriv_C, (0, U))
    C_v = approx(antideriv_C, (0, V))
    S_u = approx(antideriv_S, (0, U))
    S_v = approx(antideriv_S, (0, V))

    a = pow((C_u), 2) + pow((S_u), 2)
    b = pow((C_v), 2) + pow((S_v), 2)

    return 4.0 * a * b


if __name__ == "__main__":
    L_x = 4.0 * sqrt(79.0) / 25.0
    L_y = 6.0 * sqrt(79.0) / 25.0
    lam = 0.632  # nm -> mm
    q_0 = 400.0

    gauss_quad_data = quad_point_data()
    points = gauss_quad_data["legendre_roots"]
    weights = gauss_quad_data["weights"]

    x = 0.5 * L_x
    y = 0.5 * L_y

    approximated_value = intensidad(
        q_0, x, y, lam, gaussian_quadrature2(points, weights)
    )

    with open("pecs/pec5/data/intensity.txt", mode="w") as file:
        file.write("%f" % approximated_value)
