from math import exp, sin
from typing import Callable, TypeAlias

from code.methods.linalg import matrix_multiplication, solve, transpose, zeros
from code.methods.types import Matrix, Vector
from code.pecs.pec4.data import ALPHA, BETA, datos, f_k

# fn( param_list, x_k )
Func: TypeAlias = Callable[[list[float], float], float]


def partial_alpha_k(params: list[float], x_k: float) -> float:
    alpha = params[ALPHA]
    return x_k * exp(-1.0 * alpha * x_k)


def partial_beta_k(params: list[float], x_k: float) -> float:
    return -1.0 * sin(x_k)


def jacobian(xvals: list[float]):
    partials = [partial_alpha_k, partial_beta_k]

    def inner(params: list[float]):
        nrows = len(xvals)
        ncols = len(params)
        J = zeros(nrows, ncols)

        for i in range(nrows):
            for j in range(ncols):
                J[i][j] = partials[j](params, xvals[i])

        return J

    return inner


def r_k(xvals: list[float], yvals: list[float]):
    def inner(params: list[float], k: int):
        y_k = yvals[k]
        return y_k - f_k(params, xvals[k])

    return inner


def step(J: Matrix, params: list[float], xvals, yvals) -> Vector:
    J_T = transpose(J)
    r_fn = r_k(xvals, yvals)
    r = [[r_fn(params, k)] for k in range(len(xvals))]
    A = matrix_multiplication(J_T, J)

    b_mat = matrix_multiplication(J_T, r)
    b_vec = [row[0] for row in b_mat]

    return solve(A, b_vec)


def compute_params(xvals, yvals):
    params_k = [0.0, 0.0]

    J_fn = jacobian(xvals)

    limit = 1e-8
    iters = 0
    max_iters = 1000

    should_compute = True

    while should_compute:
        iters += 1
        J = J_fn(params_k)
        diff = step(J, params_k, xvals, yvals)
        params_k = [params_k[k] - diff[k] for k in range(len(diff))]

        if iters >= max_iters:
            raise Exception("max iterations exceeded")
        should_compute = not (
            (abs(diff[0]) <= limit) and (abs(diff[1]) <= limit)
        )

    return params_k


if __name__ == "__main__":
    xvals = datos[0]
    yvals = datos[1]
    params = compute_params(xvals, yvals)
    print(params)
