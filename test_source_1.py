import pytest
from source_1 import add_func


def test_add_one():
    assert add_func(2, 5) == 7


@pytest.mark.xfail
def test_add_fail():
    assert add_func(5, 5) == 9