import csv
from math import sqrt
from matplotlib import pyplot as plt

from code.methods.types import PolynomialList, FloatFunc, DataPoints


def find_errors(
    data_points: DataPoints, polynomials: PolynomialList, start: int, end: int
) -> list[list[int | float]]:
    """calculate RMSE and MAE for the polynomials around a range."""
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    N = end - start
    rows = []

    for indx in range(len(polynomials)):
        p = polynomials[indx]
        rmse = 0.0
        mae = 0.0

        for k in range(start, end + 1):
            v = p(x[k])
            err = y[k] - v
            mae += abs(err)
            rmse += err * err

        rmse = sqrt(rmse / N)
        mae = mae / N

        rows.append([indx, rmse, mae])

    return rows


def write_csv(hdr: list[str], rows: list, name: str):
    data = [hdr] + rows
    with open(name, mode="w", newline="") as f:
        w = csv.writer(f)
        for row in data:
            w.writerow(row)


def csv_error(
    data_points: DataPoints,
    polynomials: PolynomialList,
    start: int,
    end: int,
    name: str,
):
    """
    generate CSV of RMSE (root mean square error) and MAE (mean average error).
    """
    hdr = ["polynomial", "RMSE", "MAE"]
    rows = find_errors(data_points, polynomials, start, end)

    write_csv(hdr, rows, name)


def csv_interpolate_age(
    polynomials: PolynomialList,
    point: float,
    name: str,
    offset: int = 0,
):
    rows = []

    for k in range(len(polynomials)):
        p_k = polynomials[k]
        approx = p_k(point)
        rows.append([offset + k, approx])

    write_csv(["polynomial", "age"], rows, name)


def plot_polynomials(
    data_points: DataPoints,
    polynomials: PolynomialList,
    name: str,
    labels: list[str] = [],
):
    """plot polynomials."""
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    plt.figure(1)

    for k in range(len(polynomials)):
        label = "k = %d" % k
        if len(labels) != 0:
            label = labels[k]
        px = [polynomials[k](x_p) for x_p in x]
        plt.plot(x, px, label=label, marker="o")

    plt.plot(x, y, label="samples", marker="x")

    plt.legend()
    plt.savefig(name)
    plt.close()


def plot_diff(
    start: float,
    end: float,
    steps: int,
    p0: FloatFunc,
    p1: FloatFunc,
    name: str,
):
    """plot the difference over an interval for two polynomials."""

    plt.figure(1)
    yvals = []
    xvals = []
    step_size = (end - start) / float(steps)
    for k in range(steps):
        x = start + (float(k) * step_size)
        y = abs(p1(x) - p0(x))
        yvals.append(y)
        xvals.append(x)

    plt.plot(xvals, yvals, label="|p_b - p_a|")
    plt.legend()
    plt.savefig(name)
