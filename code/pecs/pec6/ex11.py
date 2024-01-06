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


def unzip(v: list[Vector]) -> Tuple[list[float], list[float], list[float]]:
    """For a list of 3D vectors, returns 3 lists for each component."""
    x = [v_k[0] for v_k in v]
    y = [v_k[1] for v_k in v]
    z = [v_k[2] for v_k in v]

    return (x, y, z)


def gen_ticks(v: Vector, n: int) -> list[float]:
    v_start = min(v)
    h = (max(v) - v_start) / float(n)
    return [v_start + (float(k) * h) for k in range(n)]


def mk_plot(t: list[float], v: list[Vector], titles: list[str], path: str):
    (v1, v2, v3) = unzip(v)

    _, (ax1, ax2, ax3) = plt.subplots(3)

    ax1.plot(t, v1)
    ax2.plot(t, v2)
    ax3.plot(t, v3)

    n_ticks = 5

    ax1.set_yticks(ticks=gen_ticks(v1, n_ticks), minor=True)
    ax1.set_ylabel(titles[0])
    ax1.tick_params(labelsize="medium", width=3)
    ax1.grid(True, which="both")

    ax2.set_yticks(ticks=gen_ticks(v2, n_ticks), minor=True)
    ax2.set_ylabel(titles[1])
    ax2.tick_params(labelsize="medium", width=3)
    ax2.grid(True, which="both")

    ax3.set_yticks(ticks=gen_ticks(v3, n_ticks), minor=True)
    ax3.set_ylabel(titles[2])
    ax3.tick_params(labelsize="medium", width=3)
    ax3.grid(True, which="both")

    plt.tight_layout()
    plt.savefig(path)

    plt.close()


if __name__ == "__main__":
    # leer csv ya generados
    png_paths = [
        "pecs/pec6/figures/rel_rx_ry_rz.png",
        "pecs/pec6/figures/rel_vx_vy_vz.png",
        "pecs/pec6/figures/rel_adim_vx_vy_vz.png",
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
    _, (ax1, ax2) = plt.subplots(2)
    ax1.plot(t, v_radial)
    ax2.plot(t, vz)
