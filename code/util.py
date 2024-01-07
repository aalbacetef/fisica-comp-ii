import csv
from typing import Tuple

from matplotlib import pyplot as plt

from code.methods.types import Vector


def write_csv(hdr: list[str], rows: list, name: str):
    data = [hdr] + rows
    with open(name, mode="w", newline="") as f:
        w = csv.writer(f)
        for row in data:
            w.writerow(row)


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


def mk_3d_plot(x1: Vector, x2: Vector, x3: Vector, names: list[str], path: str):
    ax = plt.figure().add_subplot(projection="3d")
    ax.plot(x1, x2, x3)
    ax.set_xlabel(names[0])
    ax.set_ylabel(names[1])
    ax.set_zlabel(names[2])
    plt.savefig(path)
    plt.close()


def mk_plot(
    t: list[float],
    w: list[Vector],
    titles: list[str],
    path: str,
):
    """Plot N vectors vertically as a function of time t."""
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
