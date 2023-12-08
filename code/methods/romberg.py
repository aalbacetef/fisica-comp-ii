from math import pow

from code.methods.trapezium import trapezium
from code.methods.types import FloatFunc, IntTableFunc, Table


def romberg(f: FloatFunc, interval: tuple[float, float]) -> IntTableFunc:
    T = trapezium(f, interval)

    def inner(m: int) -> Table:
        matrix = []
        for j in range(1, m + 1):
            matrix.append([])
            matrix[j - 1].append([])

            matrix[j - 1][0] = T(int(pow(2, j - 1)))
            if j == 1:
                continue
            for k in range(2, j + 1):
                elem = matrix[j - 1][k - 2]
                top = elem - matrix[j - 2][k - 2]
                bot = pow(4, k - 1) - 1
                value = elem + (top / bot)
                matrix[j - 1].append(value)

        return matrix

    return inner
