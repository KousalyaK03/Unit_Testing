import pytest
from math_utils import MathUtils

@pytest.fixture
def math_utils_instance():
    return MathUtils()

def test_add():
    assert MathUtils.add(2, 3) == 5
    assert MathUtils.add(-1, 1) == 0
    assert MathUtils.add(0, 0) == 0

def test_subtract():
    assert MathUtils.subtract(5, 2) == 3
    assert MathUtils.subtract(-1, 1) == -2
    assert MathUtils.subtract(0, 0) == 0


def test_multiply():
    assert MathUtils.multiply(2, 3) == 6
    assert MathUtils.multiply(-1, 1) == -1
    assert MathUtils.multiply(0, 5) == 0

def test_divide(math_utils_instance):
    assert math_utils_instance.divide(6, 3) == 2
    assert math_utils_instance.divide(5, 2) == 2.5
    assert math_utils_instance.divide(0, 5) == 0

def test_divide_by_zero(math_utils_instance):
    assert math_utils_instance.divide(10, 0) == -1.0
