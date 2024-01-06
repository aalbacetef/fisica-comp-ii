from math import cos, pi, sin
from code.methods.linalg import vec_scalar
from code.methods.runge_kutta import rk4_vec
from code.util import write_csv

from code.pecs.pec6.data import (
    f_rel,
    gamma_v,
    m_no_rel,
    q_electron,
    v_light,
)


def f(v_fn):
    def inner(t, w):
        v = w[3:]
        dv = v_fn(t, v)
        return v + dv

    return inner


if __name__ == "__main__":
    # define time steps
    t_0 = 0.0
    t_end = 2.0 * 1e-7
    h = 1e-12
    n = int((t_end - t_0) / h)
    t = [t_0 + (k * h) for k in range(n)]

    # constants provided
    q = q_electron
    m = m_no_rel
    B_0 = 0.05
    z_0 = 1.0

    # initial values
    arg = pi / 9.0
    v_0 = vec_scalar(
        [sin(arg), 0.0, cos(arg)],
        2.0 * v_light * (1.0 / 3.0),
    )

    coeff = gamma_v(v_light, v_0) * m * v_light

    r_0 = vec_scalar(
        [-1.0, 1.0, 0.0],
        coeff,
    )
    w_0 = r_0 + v_0

    # the rk4 step function
    dw = f_rel(q, m, B_0, z_0)
    step = rk4_vec(dw, t_0, w_0, h)

    w = [w_0]
    for k in range(1, n):
        w.append(step())

    r = [w_k[:3] for w_k in w]
    v = [w_k[3:] for w_k in w]

    hdr = ["t", "r_x", "r_y", "r_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, r))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_rel_r.csv")

    hdr = ["t", "v_x", "v_y", "v_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, v))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_rel_v.csv")

    # 50 points (latex struggles with the full size)
    n = 50
    t = t[:n]
    r = r[:n]
    v = v[:n]

    hdr = ["t", "r_x", "r_y", "r_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, r))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_rel_r_capped.csv")

    hdr = ["t", "v_x", "v_y", "v_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, v))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_rel_v_capped.csv")
