from typing import Callable, TypeAlias

DataPoints: TypeAlias = list[list[float]]
FloatFunc: TypeAlias = Callable[[float], float]
PolynomialList: TypeAlias = list[FloatFunc]
