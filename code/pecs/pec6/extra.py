from math import cos, pi, sin
from code.methods.linalg import vec_scalar
from code.methods.runge_kutta import rk4_vec

from code.pecs.pec6.data import (
    f_rel,
    gamma_v,
    m_no_rel,
    q_electron,
    v_light,
)
from code.util import mk_3d_plot, unzip


if __name__ == "__main__":
    # define time steps
    t_0 = 0.0
    t_end = 50.0
    h = 1e-3
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

    # divide velocities by c
    adim_coeff = 1.0 / v_light
    v_adim = [vec_scalar(v_k, adim_coeff) for v_k in v]

    (rx, ry, rz) = unzip(r)
    (vx, vy, vz) = unzip(v_adim)

    pfx = "pecs/pec6/figures/extra_rel_"

    mk_3d_plot(t, rx, ry, ["t", "rx", "ry"], pfx + "3d_rx_ry.png")
    mk_3d_plot(t, rx, rz, ["t", "rx", "rz"], pfx + "3d_rx_rz.png")
    mk_3d_plot(t, ry, rz, ["t", "ry", "rz"], pfx + "3d_ry_rz.png")

    mk_3d_plot(t, vx, vy, ["t", "vx", "vy"], pfx + "3d_vx_vy.png")
    mk_3d_plot(t, vx, vz, ["t", "vx", "vz"], pfx + "3d_vx_vz.png")
    mk_3d_plot(t, vy, vz, ["t", "vy", "vz"], pfx + "3d_vy_vz.png")

    mk_3d_plot(rx, ry, rz, ["rx", "ry", "rz"], pfx + "3d_r.png")
    mk_3d_plot(vx, vy, vz, ["vx", "vy", "vz"], pfx + "3d_v.png")
