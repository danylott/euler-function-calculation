import pytest

from main import euler_function_calculation


@pytest.mark.parametrize(
    "value,result",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 4),
        (6, 2),
        (7, 6),
        (8, 4),
        (9, 6),
        (10, 4)
    ]
)
def test_euler_function_calculation_simple(value, result):
    assert euler_function_calculation(value) == result


@pytest.mark.parametrize(
    "value,result",
    [
        (13, 12),
        (17, 16),
        (131, 130),
    ]
)
def test_euler_function_calculation_prime(value, result):
    assert euler_function_calculation(value) == result


@pytest.mark.parametrize(
    "first,second,third",
    [
        (165, 11, 15),
        (12, 3, 4),
        (221, 13, 17),
        (494, 19, 26),
    ]
)
def test_euler_function_calculation_multiplication(first, second, third):
    assert euler_function_calculation(first) == euler_function_calculation(second) * euler_function_calculation(third)
