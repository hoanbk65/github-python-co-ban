
from calculator import add


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_two_negative_numbers():
    assert add(-2, -3) == -5


def test_add_positive_and_negative_numbers():
    assert add(5, -3) == 2


def test_add_zero():
    assert add(0, 0) == 0


def test_add_decimal_numbers():
    assert add(1.5, 2.5) == 4.0
