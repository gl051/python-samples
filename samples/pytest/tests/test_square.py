import pytest
from util import math


def test_square():
    assert(math.square(2)) == 4


def test_raise_exception_on_not_integer_argument():
    with pytest.raises(TypeError):
        math.square('g')


@pytest.mark.parametrize("ival, result", [
    (2, 4),
    (5, 25),
    (100, 10000)
])
def test_int_values(ival, result):
    assert(math.square(ival)) == result
