from calc import add
import pytest
@pytest.fixture
def input():
    return 10

@pytest.mark.math
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0