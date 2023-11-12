from matplotlib import pyplot as plt

from code.methods.newton import generate_polynomials
from code.pecs.pec3.data import carbon_age_tbl
from code.pecs.pec3.util import (
    csv_error,
    csv_interpolate_age,
    plot_diff,
    plot_polynomials,
)


if __name__ == "__main__":
    order = 3
    data_points = carbon_age_tbl
    polynomials = generate_polynomials(order, data_points)[2:4]

    point = 0.8705

    # csv 2:
    csv_interpolate_age(
        polynomials, point, "pecs/pec3/data/age03.csv", offset=2
    )

    ## figure: polynomials plotted vs samples
    plot_polynomials(
        data_points,
        polynomials,
        "pecs/pec3/figures/figure4.png",
        labels=["k = 2", "k = 3"],
    )

    ## figure: polynomial difference
    plot_diff(
        data_points[0][0],
        data_points[-1][0],
        30,
        polynomials[0],
        polynomials[1],
        "pecs/pec3/figures/figure5.png",
    )

    ## csv 3: RMSE and MAE
    csv_error(data_points, polynomials, 0, 7, "pecs/pec3/data/errors03.csv")
