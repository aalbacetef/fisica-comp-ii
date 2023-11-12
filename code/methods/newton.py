from code.methods.types import DataPoints, FloatFunc, PolynomialList


def n_k(k: int, points: list[float]) -> FloatFunc:
    """generate the n_k basis function of the newton polynomial."""
    n = len(points)
    if k > n:
        raise ValueError("index %d is out of bounds (n=%d)" % (k, n))

    def n_k_fn(x: float) -> float:
        value = 1.0

        for i in range(k):
            value *= x - points[i]

        return value

    return n_k_fn


def coefficients(x_values: list[float], y_values: list[float]):
    """calculate the divided differences."""
    n = len(x_values)
    f = [[0] * n for _ in range(n)]

    for i in range(n):
        f[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (
                x_values[i + j] - x_values[i]
            )

    return f


def newtonian_interpolation(data_points: DataPoints) -> FloatFunc:
    """generate the newton interpolation polynomial."""
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    n = len(x)
    basis = [n_k(k, x) for k in range(n)]
    coeffs_tbl = coefficients(x, y)

    def interpolation_fn(x_p: float) -> float:
        value = 0.0

        for k in range(n):
            value += coeffs_tbl[0][k] * basis[k](x_p)
        return value

    return interpolation_fn


def generate_polynomials(order: int, data_points: DataPoints) -> PolynomialList:
    # for an m-order polynomial, we need m+1 points
    req_points = order + 1

    if len(data_points) < req_points:
        raise ValueError(
            "insufficient points, want at least %d, got %d"
            % (req_points, len(data_points)),
        )

    # the number of polynomials we'll generate
    n = len(data_points) - order
    polynomials = [
        newtonian_interpolation(data_points[k : k + req_points])
        for k in range(n)
    ]

    return polynomials
