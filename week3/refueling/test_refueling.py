import pytest
from refueling import convert, gauge

def test_convert_normal():
    assert convert("1/2") == 50


def test_convert_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("1/0") == "Invalid"

    with pytest.raises(ValueError):
        convert("10/2") == "Invalid"

    with pytest.raises(ValueError):
        convert("-2/10") == "Invalid"

    with pytest.raises(ZeroDivisionError):
        convert("2/-5") == "Invalid"

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"            