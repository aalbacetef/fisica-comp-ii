from typing import Callable
from code.methods.linalg import vec_copy, vec_scalar, vec_sum

from code.methods.types import FuncVectorX, FuncXVector, Vector


def rk4_vec(
    f: FuncXVector, t_0: float, y_0: Vector, h: float
) -> Callable[[], Vector]:
    t_i = t_0
    y_i = y_0
    coeff = 0.5 * h
    coeff2 = 1.0 / 6.0
    iter_cnt = 1

    def step() -> Vector:
        nonlocal y_i
        nonlocal t_i
        nonlocal iter_cnt
        arg0 = t_i + coeff

        k1 = vec_scalar(f(t_i, y_i), h)
        k2 = vec_scalar(f(arg0, vec_sum(y_i, vec_scalar(k1, 0.5))), h)
        k3 = vec_scalar(f(arg0, vec_sum(y_i, vec_scalar(k2, 0.5))), h)
        k4 = vec_scalar(f(t_i + h, vec_sum(y_i, k3)), h)

        y_incr = vec_sum(
            vec_sum(k1, vec_scalar(k2, 2.0)), vec_sum(vec_scalar(k3, 2.0), k4)
        )

        # update variables
        y_i = vec_sum(y_i, vec_scalar(y_incr, coeff2))
        t_i += h
        print("iter: %d" % iter_cnt)
        print("y_i: %s" % y_i.__str__())
        print("h: %f" % h)
        print("t_i: %f" % t_i)
        iter_cnt += 1
        print("--------------\n")
        return vec_copy(y_i)

    return step


def rk4_scalar(f, t_0: float, y_0: float, h: float):
    t_i = t_0
    y_i = y_0
    coeff = 0.5 * h
    coeff2 = h / 6.0

    def step() -> float:
        nonlocal y_i
        nonlocal t_i

        arg0 = t_i + coeff

        k1 = f(t_i, y_i)
        k2 = f(arg0, y_i + (k1 * coeff))
        k3 = f(arg0, y_i + (k2 * coeff))
        k4 = f(t_i + h, y_i + (k3 * h))

        y_incr = k1 + (k2 * 2.0) + k4 + (k3 * 2.0)

        # update variables
        y_i = y_i + (y_incr * coeff2)
        t_i += h

        return y_i

    return step
