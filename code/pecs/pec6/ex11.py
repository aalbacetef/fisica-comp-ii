import csv
from math import sqrt
from typing import Tuple

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


def unzip(
    v: list[Vector]
) -> Tuple[Vector, Vector] | Tuple[Vector, Vector, Vector]:
    """For a list of 2D-3D vectors, returns 2-3 lists for each component."""
    is_2d = len(v[0]) == 2

    x = [v_k[0] for v_k in v]
    y = [v_k[1] for v_k in v]
    if is_2d:
        return (x, y)
    z = [v_k[2] for v_k in v]

    return (x, y, z)


def gen_ticks(v: Vector, n: int) -> list[float]:
    v_start = min(v)
    h = (max(v) - v_start) / float(n)
    return [v_start + (float(k) * h) for k in range(n)]


def mk_plot(t: list[float], w: list[Vector], titles: list[str], path: str):
    v = unzip(w)
    n = len(v)

    n_ticks = 5
    _, axes = plt.subplots(n)

    for k in range(n):
        ax = axes[k]
        v_k = v[k]
        ax.plot(t, v_k)
        ax.set_yticks(ticks=gen_ticks(v_k, n_ticks), minor=True)
        ax.set_ylabel(titles[k])
        ax.tick_params(labelsize="medium", width=3)
        ax.grid(True, which="both")

    plt.tight_layout()
    plt.savefig(path)
    plt.close()


if __name__ == "__main__":
    # leer csv ya generados
    png_paths = [
        "pecs/pec6/figures/rel_rx_ry_rz.png",
        "pecs/pec6/figures/rel_vx_vy_vz.png",
        "pecs/pec6/figures/rel_adim_vx_vy_vz.png",
        "pecs/pec6/figures/rel_v_radial_vz.png",
    ]

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

    v_radial = [sqrt((v_k[0] * v_k[0]) + (v_k[1] * v_k[1])) for v_k in v]
    vz = [v_k[2] for v_k in v]
    mk_plot(
        t,
        [[v_radial[k], vz[k]] for k in range(len(vz))],
        ["v_radial(t)", "v_z(t)"],
        png_paths[3],
    )
