import csv
from math import sqrt
from typing import Tuple

from matplotlib import pyplot as plt

from code.methods.types import Vector


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
    t, r = load_data("pecs/pec6/data/simul_no_rel_r.csv")
    t, v = load_data("pecs/pec6/data/simul_no_rel_v.csv")

    png_paths = [
        "pecs/pec6/figures/no_rel_rx_ry_rz.png",
        "pecs/pec6/figures/no_rel_vx_vy_vz.png",
    ]

    mk_plot(
        t,
        r,
        ["r_x(t)", "r_y(t)", "r_z(t)"],
        png_paths[0],
    )

    mk_plot(
        t,
        v,
        ["v_x(t)", "v_y(t)", "v_z(t)"],
        png_paths[1],
    )

    plt.figure(1)
    x = [r_k[0] for r_k in r]
    y = [r_k[1] for r_k in r]
    plt.ylabel("r_x(t)")
    plt.xlabel("r_y(t)")
    plt.plot(y, x)
    plt.savefig("pecs/pec6/figures/no_rel_y_x.png")
    plt.close()
