import csv
from math import sqrt
from typing import Tuple
from code.util import mk_3d_plot, mk_plot, unzip

from matplotlib import pyplot as plt

from code.methods.linalg import vec_scalar
from code.methods.types import Vector
from code.pecs.pec6.data import v_light


def load_data(path: str) -> Tuple[Vector, list[Vector]]:
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)  # skip the headers
        t = []
        w = []

        for row in reader:
            t.append(float(row[0]))
            w.append([float(x) for x in row[1:]])

        return (t, w)


if __name__ == "__main__":
    pec_fig_path = "pecs/pec6/figures/"
    pngs = [
        "rel_rx_ry_rz.png",
        "rel_vx_vy_vz.png",
        "rel_adim_vx_vy_vz.png",
        "rel_v_mod_rad_z.png",
        "rel_3d_r.png",
        "rel_3d_v.png",
    ]
    png_paths = [pec_fig_path + p for p in pngs]

    t, r = load_data("pecs/pec6/data/simul_rel_r.csv")
    mk_plot(
        t,
        r,
        ["r_x(t)", "r_y(t)", "r_z(t)"],
        png_paths[0],
    )

    t, v = load_data("pecs/pec6/data/simul_rel_v.csv")
    mk_plot(
        t,
        v,
        ["v_x(t)", "v_y(t)", "v_z(t)"],
        png_paths[1],
    )

    v_adim = [vec_scalar(v_k, v_light) for v_k in v]
    mk_plot(
        t,
        v_adim,
        ["'v_x(t)", "'v_y(t)", "'v_z(t)"],
        png_paths[2],
    )

    coeff = 1.0 / v_light
    v_mod = [
        sqrt((v_k[0] * v_k[0]) + (v_k[1] * v_k[1]) + (v_k[2] * v_k[2]))
        for v_k in v_adim
    ]
    v_radial = [sqrt((v_k[0] * v_k[0]) + (v_k[1] * v_k[1])) for v_k in v_adim]
    vz = [v_k[2] for v_k in v_adim]

    mk_plot(
        t,
        list(zip(v_mod, v_radial, vz)),
        ["||v||(t)", "v_radial(t)", "v_z(t)"],
        png_paths[3],
    )

    # 3d plots
    (rx, ry, rz) = unzip(r)
    (vx, vy, vz) = unzip(v_adim)

    mk_3d_plot(rx, ry, rz, ["rx", "ry", "rz"], png_paths[4])
    mk_3d_plot(vx, vy, vz, ["vx", "vy", "vz"], png_paths[5])
