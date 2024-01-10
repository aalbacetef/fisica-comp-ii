from typing import Callable, TypeAlias

DataPoints: TypeAlias = list[list[float]]
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
Table: TypeAlias = list[list[float]]

FuncVectorK: TypeAlias = Callable[[Vector, int], float]
FuncVectorX: TypeAlias = Callable[[Vector, float], float]
FuncXVector: TypeAlias = Callable[[float, Vector], Vector]
FuncVectorVector: TypeAlias = Callable[[Vector], Vector]

IntFloatFunc: TypeAlias = Callable[[int], float]
FloatFunc: TypeAlias = Callable[[float], float]
IntMatrixFunc: TypeAlias = Callable[[int], Matrix]
IntTableFunc: TypeAlias = Callable[[int], Table]
ListFloatFunc: TypeAlias = Callable[[list[float]], float]

PolynomialList: TypeAlias = list[FloatFunc]
