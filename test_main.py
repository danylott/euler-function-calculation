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
def test_euler_function_calculation(value, result):
    assert euler_function_calculation(value) == result
