import pytest
from util import math


def test_square():
    assert(math.cube(3)) == 29


def test_raise_exception_on_not_integer_argument():
    with pytest.raises(TypeError):
        math.cube([78, 90])
