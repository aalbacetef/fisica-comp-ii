from code.methods.newton import generate_polynomials as gen_newton
from code.methods.lagrangian_interpolation import (
    generate_polynomials as gen_lagrange,
)
from code.pecs.pec3.data import carbon_age_tbl
from code.pecs.pec3.util import write_csv


if __name__ == "__main__":
    data_points = carbon_age_tbl

    # in exercises 3 and 4 we use only the k=2 and k=3 polynomials.
    ex_3 = gen_lagrange(3, data_points)[2:4]
    ex_4 = gen_newton(3, data_points)[2:4]

    polynomials = ex_3 + ex_4
    next_ex_3 = gen_lagrange(4, data_points)[2:4]
    next_ex_4 = gen_newton(4, data_points)[2:4]

    next_ordr = next_ex_3 + next_ex_4

    labels = [
        "cubic. k = 2",
        "cubic. k = 3",
        "newt. k = 2",
        "newt. k = 3",
    ]

    point = 0.8705

    hdr = ["polynomial", "error"]
    rows = []
    for k in range(len(polynomials)):
        p = polynomials[k]
        y = p(point)
        next_ord = next_ordr[k](point)
        err = next_ord - y
        rows.append([labels[k], err])

    write_csv(hdr, rows, "pecs/pec3/data/errors05.csv")
