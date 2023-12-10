from math import pow

from code.methods.trapezium import trapezium
from code.methods.types import FloatFunc, IntTableFunc, Table


def romberg(f: FloatFunc, interval: tuple[float, float]) -> IntTableFunc:
    T = trapezium(f, interval)

    def inner(m: int) -> Table:
        # initialize table
        R: Table = [[0] * (k + 1) for k in range(m + 1)]

        for k in range(m + 1):
            R[k][0] = T(1 << k)

        for j in range(1, m + 1):
            for i in range(j, m + 1):
                tmp_1 = 4.0**j
                tmp_2 = R[i][j - 1]
                tmp_3 = R[i - 1][j - 1]
                tmp_4 = tmp_1 - 1.0

                R[i][j] = ((tmp_1 * tmp_2) - tmp_3) / tmp_4

        return R

    return inner
