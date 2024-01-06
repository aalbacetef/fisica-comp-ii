from math import cos, sin, sqrt
from code.methods.linalg import curl, vec_scalar
from code.methods.types import FuncVectorVector, FuncXVector, Vector


q_electron = -1.602e-19
m_no_rel = 9.109e-31
v_light = 299792458.0


def f_no_rel(q: float, m: float) -> FuncXVector:
    coeff = q / m

    def inner(_, v: Vector) -> Vector:
        ax = coeff * v[1]
        ay = coeff * (1.0 - v[0])
        return [ax, ay, 0.0]

    return inner


def theoretical_v_no_rel(q: float, m: float, v_0: Vector):
    w: float = q / m
    vx_0 = v_0[0]
    vy_0 = v_0[1]
    vy_prime_0 = w * (1 - vx_0)
    A = vy_0
    B = w / (vy_prime_0)

    def inner(t: float) -> Vector:
        arg = w * t
        _cos = cos(arg)
        _sin = sin(arg)
        vy_t = (A * _cos) + (B * _sin)
        vx_t = 1 - (w * (B * _cos) - (A * _sin))
        return [vx_t, vy_t, 0.0]

    return inner


def B_rel(B_0: float, z_0: float) -> FuncVectorVector:
    z_0_2 = z_0 * z_0
    coeff = 1.0 / z_0_2

    def inner(r: Vector) -> Vector:
        [x, y, z] = r
        bx = -B_0 * x * z * coeff
        by = -B_0 * y * z * coeff
        bz = B_0 * (1 + (coeff * z * z))
        return [bx, by, bz]

    return inner


def gamma(m: float, c: float, p_rel: Vector) -> float:
    a = m * m * c * c
    b = 1.0 / a
    sum_p = sum([p_k * p_k for p_k in p_rel])
    return sqrt(1 + (b * sum_p))


def gamma_v(c: float, v: Vector) -> float:
    v_2 = sum([v_k * v_k for v_k in v])
    den = sqrt(1.0 - ((v_2) / (c * c)))
    return 1.0 / den


def f_rel(q: float, m: float, B_0: float, z_0: float) -> FuncXVector:
    B = B_rel(B_0, z_0)

    def inner(t: float, w: Vector) -> Vector:
        r = w[:3]
        p_rel = w[3:]

        gamma_m = m * gamma(m, v_light, p_rel)
        coeff = q / gamma_m

        dp_rel = vec_scalar(curl(p_rel, B(r)), coeff)
        return p_rel + dp_rel

    return inner
