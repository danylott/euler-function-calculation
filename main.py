import enum

from lib.simple import phi as simple_phi
from lib.formula import phi as formula_phi
from lib.advanced import phi as advanced_phi


class EulerCalculationAlgorithm(enum.Enum):
    SIMPLE = simple_phi
    FORMULA = formula_phi
    ADVANCED = advanced_phi


def euler_function_calculation(value):
    return EulerCalculationAlgorithm.SIMPLE(value)
