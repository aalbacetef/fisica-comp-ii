from code.methods.gaussian_quadrature import gaussian_quadrature
from code.pecs.pec5.data import antideriv_C, antideriv_S, quad_point_data
from code.util import write_csv


if __name__ == "__main__":
    w = 5.0
    interval = (0.0, w)
    quad_points = quad_point_data()

    c_w = gaussian_quadrature(antideriv_C, interval)
    s_w = gaussian_quadrature(antideriv_S, interval)

    GQC = c_w(quad_points["legendre_roots"], quad_points["weights"])
    GQS = s_w(quad_points["legendre_roots"], quad_points["weights"])

    hdr = ["fn", "value"]
    rows = [
        ["C(w)", GQC],
        ["S(w)", GQS],
    ]

    write_csv(hdr, rows, "pecs/pec5/data/gauss_quad_c_s.csv")
