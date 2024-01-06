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


def mk_plot(t: list[float], v: list[Vector], titles: list[str], path: str):
    (v1, v2, v3) = unzip(v)

    ax1 = plt.subplot(3, 1, 1)
    ax1.plot(t, v1)
    ax1.set_title(titles[0])

    ax2 = plt.subplot(3, 1, 2)
    ax2.plot(t, v2)
    ax2.set_title(titles[1])

    ax3 = plt.subplot(3, 1, 3)
    ax3.plot(t, v3)
    ax3.set_title(titles[2])

    plt.savefig(path)
    plt.tight_layout()

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

    for p in png_paths:
        print(p)

    ax = plt.figure(1).add_subplot(projection="3d")
    (rx, ry, _) = unzip(r)
    (vx, vy, _) = unzip(v)

    ax.plot(rx, t, ry)
    plt.savefig("3d.png")
    plt.close()

    v_drift = []
    avg = [0.0, 0.0, 0.0]
    n = len(v)
    for k in range(n):
        avg[0] += abs(v[k][0])
        avg[1] += abs(v[k][1])

    avg[0] = avg[0] / float(n)
    avg[1] = avg[1] / float(n)

    avg_x = max(rx) / (2e-10)
    avg_y = max(ry) / (2e-10)

    print("avg: ")
    print(avg)
    print("avg_x: %f" % avg_x)
    print("avg_y: %f" % avg_y)
    print("avg: %f" % (sqrt(avg_x + avg_y)))
    plt.figure(1)
    plt.plot(ry, rx)
    plt.grid(True)
    plt.savefig("x_y.png")
    plt.close()
    plt.figure(1)
    plt.plot(t, rx)
    plt.grid(True)
    plt.savefig("rx.png")
    plt.close()
    plt.figure(1)
    plt.plot(t, ry)
    plt.grid(True)
    plt.savefig("ry.png")

    plt.close()
