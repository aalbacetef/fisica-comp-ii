from typing import Callable, TypeAlias

DataPoints: TypeAlias = list[list[float]]
FloatFunc: TypeAlias = Callable[[float], float]
PolynomialList: TypeAlias = list[FloatFunc]

Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
FuncVectorK: TypeAlias = Callable[[Vector, int], float]
FuncVectorX: TypeAlias = Callable[[Vector, float], float]
