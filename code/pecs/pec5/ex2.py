from code.methods.linalg import dim
from code.methods.romberg import romberg
from code.methods.types import Table
from code.util import write_csv

from code.pecs.pec5.data import antideriv_C, antideriv_S


def count(table: Table) -> int:
    c = 0
    for row in table:
        for _ in row:
            c += 1

    return c


if __name__ == "__main__":
    w = 5.0
    interval = (0.0, w)

    # generate subdivisions
    max_pow = 9
    subdivisions = [6] + [1 << k for k in range(max_pow)]
    subdivisions.sort()

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
