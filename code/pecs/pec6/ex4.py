from code.methods.runge_kutta import rk4_vec
from code.util import write_csv

from code.pecs.pec6.data import (
    f_no_rel,
    m_no_rel,
    q_electron,
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
    t_end = 2e-10
    h = 1e-12
    n = int((t_end - t_0) / h)
    t = [t_0 + (k * h) for k in range(n)]

    # initial values
    t_0 = 0.0
    r_0 = [0.0, 0.0, 0.0]
    v_0 = [0.0, 1.0, 0.0]
    w_0 = r_0 + v_0

    # constants provided
    q = q_electron
    m = m_no_rel

    # the rk4 step function
    dw = f(f_no_rel(q, m))
    step = rk4_vec(dw, t_0, w_0, h)

    w = [w_0]
    for k in range(1, n):
        w.append(step())

    r = [w_k[:3] for w_k in w]
    v = [w_k[3:] for w_k in w]

    hdr = ["t", "r_x", "r_y", "r_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, r))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_no_rel_r.csv")

    hdr = ["t", "v_x", "v_y", "v_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, v))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_no_rel_v.csv")
