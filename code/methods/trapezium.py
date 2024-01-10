from code.methods.types import FloatFunc, IntFloatFunc


def trapezium(f: FloatFunc, interval: tuple[float, float]) -> IntFloatFunc:
    """Implementation of the trapezium rule."""
    [a, b] = interval

    def inner(n: int) -> float:
        delta_x = (b - a) / float(n)

        x_0 = a
        x_n = b

        s = 0.0
        for k in range(1, n):
            x_k = x_0 + (float(k) * delta_x)
            s += f(x_k)

        return (0.5 * delta_x) * (f(x_0) + f(x_n) + (2.0 * s))

    return inner


def approx_antideriv(t: list[float], f: list[float]) -> list[float]:
    """Use the trapezium rule to approximate the antiderivative of f."""
    s = 0.0
    n = len(t)

    v = []
    for k in range(1, n):
        delta_t = t[k] - t[k - 1]
        avg_f = f[k] + f[k - 1]
        s += (0.5 * avg_f) / delta_t
        v.append(s)

    return v
