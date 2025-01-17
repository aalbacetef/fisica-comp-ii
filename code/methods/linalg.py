from typing import Tuple
from code.methods.types import Matrix, Vector


def dim(A: Matrix) -> Tuple[int, int]:
    """Find the dimensions of a matrix."""
    m = len(A)
    if m == 0:
        return (0, 0)

    n = len(A[0])

    ## check: every row has the same length
    for row in A:
        if len(row) != n:
            raise ValueError("not all rows are the same size")

    return (m, n)


def mult_row(scalar: float, V: list[float]) -> list[float]:
    return [v * scalar for v in V]


def add_rows(v: list[float], w: list[float]) -> list[float]:
    u = []
    for k in range(len(v)):
        u.append(v[k] + w[k])
    return u


def copy_matrix(A: Matrix) -> Matrix:
    """Copies a matrix."""
    C = []
    for row in A:
        r = [elem for elem in row]
        C.append(r)

    return C


def zeros(m: int, n: int) -> Matrix:
    """Creates a zero matrix of size (m, n)."""
    C = []

    for _ in range(m):
        row = [0 for _ in range(n)]
        C.append(row)

    return C


def identity(m: int, n: int) -> Matrix:
    """Creates an identity matrix of size (m, n)."""
    C = []
    for i in range(m):
        row = [0 for _ in range(n)]
        if i < n:
            row[i] = 1
        C.append(row)

    return C


def matrix_multiplication(A: Matrix, B: Matrix) -> Matrix:
    """
    Multiply two matrices. Raise an error if the dimensions
    don't match.
    """

    [m, n_a] = dim(A)
    [n_b, p] = dim(B)

    if n_a != n_b:
        raise ValueError(
            "dimension mismath: A=(%d, %d); B=(%d, %d)" % (m, n_a, n_b, p)
        )

    C = identity(m, p)
    n = n_a

    for i in range(m):
        for j in range(p):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def transpose(A: Matrix) -> Matrix:
    """Returns the transpose of A."""
    [m, n] = dim(A)
    T = zeros(n, m)

    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]

    return T


def lu_decomposition(A: Matrix, crout: bool = False) -> Tuple[Matrix, Matrix]:
    """Returns the LU decomposition of A."""
    # TODO: dim check

    [nrows, ncols] = dim(A)
    L = identity(nrows, ncols)
    U = copy_matrix(A)

    if crout:
        U = transpose(A)

    for i in range(1, nrows):
        for j in range(i):
            m_ij = U[i][j] / U[j][j]
            L[i][j] = m_ij

            src_row = U[j]
            dst_row = [x for x in U[i]]
            U[i] = add_rows(dst_row, mult_row(-1.0 * m_ij, src_row))

    if crout:
        L0 = transpose(U)
        U0 = transpose(L)
        L = L0
        U = U0

    return (L, U)


def sub_forward(L: Matrix, b: Vector) -> Vector:
    """Solves L x = b"""
    [nrows, ncols] = dim(L)
    x = [0.0 for _ in range(ncols)]

    for i in range(ncols):
        s = b[i]
        for j in range(i):
            s -= L[i][j] * x[j]
        x[i] = s / L[i][i]
    return x


def sub_backward(U: Matrix, b: Vector) -> Vector:
    """Solves U x = b"""
    [nrows, ncols] = dim(U)
    x = [0.0 for _ in range(ncols)]

    for i in range(ncols - 1, -1, -1):
        s = b[i]
        for j in range(i + 1, ncols):
            s -= U[i][j] * x[j]
        x[i] = s / U[i][i]
    return x


def solve(A: Matrix, b: Vector) -> Vector:
    """Solves a given matrix A x = b"""
    [L, U] = lu_decomposition(A)

    y = sub_forward(L, b)
    x = sub_backward(U, y)
    return x


def vec_sum(a: Vector, b: Vector) -> Vector:
    """Sums two vectors. Raises an exception if lengths don't match."""
    m = len(a)
    n = len(b)
    if n != m:
        raise Exception("lengths of vectors differ: m=%d, n=%d" % (m, n))

    c = [a_k for a_k in a]
    for k in range(n):
        c[k] += b[k]

    return c


def vec_scalar(a: Vector, k: float) -> Vector:
    """Multiplies a vector by a scalar."""
    return [k * a_k for a_k in a]


def vec_copy(a: Vector) -> Vector:
    return [a_k for a_k in a]


def curl(v: Vector, w: Vector) -> Vector:
    """Compute the curl of a vector with a matrix."""
    # sanity check
    n = 3
    if len(v) != n or len(w) != n:
        raise ValueError("expected a vector of length: %d" % n)

    ux = (v[1] * w[2]) - (v[2] * w[1])
    uy = (v[2] * w[0]) - (v[0] * w[2])
    uz = (v[0] * w[1]) - (v[1] * w[0])

    return [ux, uy, uz]
