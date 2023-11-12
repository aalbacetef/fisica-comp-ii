from math import log

from code.methods.newton import generate_polynomials as gen_newton
from code.methods.lagrangian_interpolation import (
    generate_polynomials as gen_lagrange,
)
from code.pecs.pec3.data import carbon_age_tbl
from code.pecs.pec3.util import write_csv


def age_sample(n14: float) -> float:
    """calculate the age of a sample given a proportion of N14C"""
    coeff = 5730 / log(2)
    return -1 * coeff * log(n14)


if __name__ == "__main__":
    data_points = carbon_age_tbl

    # in the first exercise we found the best fit was k = 1
    index_best_ex_1 = 1
    quadratic_polynomials = [gen_lagrange(2, data_points)[index_best_ex_1]]

    # in exercises 3 and 4 we use only the k=2 and k=3 polynomials.
    cubic_polynomials = gen_lagrange(3, data_points)[2:4]
    newton_polynomials = gen_newton(3, data_points)[2:4]

    polynomials = quadratic_polynomials + cubic_polynomials + newton_polynomials
    labels = [
        "quadr. k = 1",
        "cubic. k = 2",
        "cubic. k = 3",
        "newt. k = 2",
        "newt. k = 3",
    ]

    point = 0.8705
    fp = age_sample(point)

    hdr = ["polynomial", "age", "error"]
    rows = []
    for k in range(len(polynomials)):
        p = polynomials[k]
        y = p(point)
        err = abs(y - fp)
        rows.append([labels[k], y, err])

    write_csv(hdr, rows, "pecs/pec3/data/errors04.csv")
