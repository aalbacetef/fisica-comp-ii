import csv

from code.methods.types import DataPoints, PolynomialList
from code.methods.lagrangian_interpolation import generate_polynomials
from code.pecs.pec3.data import carbon_age_tbl
from code.pecs.pec3.util import csv_error, csv_interpolate_age, plot_polynomials


if __name__ == "__main__":
    data_points: DataPoints = carbon_age_tbl
    order = 2
    polynomials = generate_polynomials(order, data_points)

    ## figure 1: polynomials plotted vs samples
    plot_polynomials(data_points, polynomials, "pecs/pec3/figures/figure1.png")

    ## csv 1: RMSE and MAE
    start = 0
    end = 7
    csv_error(
        data_points, polynomials, start, end, "pecs/pec3/data/errors01.csv"
    )

    ## csv 2: interpolated age
    point = 0.8705
    csv_interpolate_age(polynomials, point, "pecs/pec3/data/age01.csv")
