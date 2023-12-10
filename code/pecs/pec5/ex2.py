from matplotlib import pyplot as plt

from code.methods.romberg import romberg
from code.methods.types import Table
from code.util import write_csv

from code.pecs.pec5.data import antideriv_C, antideriv_S


def count(table: Table) -> int:
    rows = len(table)
    s = 0
    for k in range(rows):
        # the trapezoid function is called with n = 2^k once
        # for each row
        s += 1 << k

    return s


if __name__ == "__main__":
    w = 5.0
    interval = (0.0, w)

    # C(w) and S(w)
    r_c = romberg(antideriv_C, interval)
    r_s = romberg(antideriv_S, interval)

    m = 8
    RC = r_c(m)
    RS = r_s(m)

    hdr = ["fn", "Value", "num of eval"]
    rows = [
        ["C(w)", RC[-1][-1], count(RC)],
        ["S(w)", RS[-1][-1], count(RS)],
    ]
    write_csv(hdr, rows, "pecs/pec5/data/romberg_c_s.csv")

    # generate figure for value of approximation with increasing m
    indices = [k + 1 for k in range(10)]
    approx_R_C = [r_c(m)[-1][-1] for m in indices]
    approx_R_S = [r_s(m)[-1][-1] for m in indices]

    plt.figure(1)
    plt.plot(indices, approx_R_C, label="R_C")
    plt.plot(indices, approx_R_S, label="R_S")
    plt.legend()
    plt.savefig("pecs/pec5/figures/romb_for_m.png")
