from code.methods.types import FuncXVector, Vector


q_electron = -1.602e-19
m_no_rel = 9.109e-31


def f_no_rel(q: float, m: float) -> FuncXVector:
    coeff = q / m

    def inner(_, v: Vector) -> Vector:
        ax = coeff * v[1]
        ay = coeff * (1.0 - v[0])
        return [ax, ay, 0.0]

    return inner
