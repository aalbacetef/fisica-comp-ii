from math import floor

from code.methods.runge_kutta import rk4_vec
from code.methods.trapezium import approx_antideriv
from code.util import write_csv

from code.pecs.pec6.data import f_no_rel, m_no_rel, q_electron


if __name__ == "__main__":
    h = 1e-12
    n = 200  # esto es t_fin / h => 2e-10 / 1e-12

    t_0 = 0.0
    v_0 = [0.0, 1.0, 0.0]

    q = q_electron
    m = m_no_rel

    step = rk4_vec(f_no_rel(q, m), t_0, v_0, h)

    t = [t_0]
    v = [v_0]

    for k in range(1, n):
        t_i = float(k) * h
        v.append(step())
        t.append(t_i)

    hdr = ["t", "v_x", "v_y", "v_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, v))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_no_rel_v.csv")

    r_0 = [0.0, 0.0, 0.0]

    rx = approx_antideriv(t, [v_k[0] for v_k in v])
    ry = approx_antideriv(t, [v_k[1] for v_k in v])

    r = [r_0]
    for k in range(1, len(t)):
        r.append([rx[k - 1], ry[k - 1], 0.0])

    hdr = ["t", "r_x", "r_y", "r_z"]
    rows = [[row[0]] + row[1] for row in list(zip(t, r))]
    write_csv(hdr, rows, "pecs/pec6/data/simul_no_rel_r.csv")
