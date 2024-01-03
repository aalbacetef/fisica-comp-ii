from matplotlib import pyplot as plt
from math import exp

from code.methods.runge_kutta import rk4_vec, rk4_scalar
from code.methods.types import Vector


def f(q: float, m: float):
    coeff = q / m

    def inner(_, v: Vector) -> Vector:
        ax = coeff * v[1]
        ay = coeff * (1 + v[0])
        return [ax, ay, 0.0]

    return inner


def u(q, m, t):
    coeff = (q * t) / m
    return exp(coeff) + exp(-coeff) - 1.0


def f2(t: float, v: Vector) -> Vector:
    return [v[0] - (t * t) + 1]


if __name__ == "__main__":
    v_0: Vector = [0.0, 1.0, 0.0]
    t_0 = 0.0
    h = 1e-12

    r_0 = [0.0, 0.0, 0.0]

    q = -1.602e-19
    m = 9.109e-31

    print(q / m)
    step = rk4_vec(f(q, m), t_0, v_0, h)

    print(v_0)

    vx = []
    vy = []
    t = []
    for k in range(30):
        [x, y, z] = step()
        vx.append(x)
        vy.append(y)
        t.append(float(k) * h)
