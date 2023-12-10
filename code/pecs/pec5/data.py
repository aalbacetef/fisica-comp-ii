from math import pi as PI
from math import cos, sin

import os


def antideriv_C(x: float) -> float:
    angle = PI * 0.5
    return cos(angle * x * x)


def antideriv_S(x: float) -> float:
    angle = PI * 0.5
    return sin(angle * x * x)


def quad_point_data() -> dict:
    fpath = os.path.realpath(__file__)
    base_dir = os.path.dirname(fpath)

    data = {"legendre_roots": [], "weights": []}
    with open(base_dir + "/QG64.dat", mode="r") as f:
        lines = f.readlines()
        legendre_roots = []
        weights = []
        for line in lines:
            cols = line.split("\t")
            legendre_roots.append(float(cols[0]))
            weights.append(float(cols[1]))
        data["legendre_roots"] = legendre_roots
        data["weights"] = weights

    return data
