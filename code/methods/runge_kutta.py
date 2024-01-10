from typing import Callable
from code.methods.linalg import vec_copy, vec_scalar, vec_sum

from code.methods.types import FuncXVector, Vector


def rk4_vec(
    f: FuncXVector, t_0: float, y_0: Vector, h: float
) -> Callable[[], Vector]:
    t_i = t_0
    y_i = y_0
    coeff = 0.5
    coeff2 = 1.0 / 6.0
    coeff3 = 2.0

    def step() -> Vector:
        nonlocal y_i
        nonlocal t_i

        arg0 = t_i + coeff

        k1 = vec_scalar(f(t_i, y_i), h)
        k2 = vec_scalar(f(arg0, vec_sum(y_i, vec_scalar(k1, coeff))), h)
        k3 = vec_scalar(f(arg0, vec_sum(y_i, vec_scalar(k2, coeff))), h)
        k4 = vec_scalar(f(t_i + h, vec_sum(y_i, k3)), h)

        y_incr = vec_sum(
            vec_sum(k1, vec_scalar(k2, coeff3)),
            vec_sum(vec_scalar(k3, coeff3), k4),
        )

        # update variables
        y_i = vec_sum(y_i, vec_scalar(y_incr, coeff2))
        t_i += h

        return vec_copy(y_i)

    return step
