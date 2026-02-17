import pytest
from vanity_plate import is_valid

def test_length_long(benchmark):
    result = benchmark.pedantic(is_valid, args=("sadafafasfac",), rounds=3, iterations=5)
    assert result == "Invalid"

def test_length_short(benchmark):
    result = benchmark.pedantic(is_valid, args=("a",), rounds=3, iterations=5)
    assert result == "Invalid"

def test_start(benchmark):
    result = benchmark.pedantic(is_valid, args=("a01234",), rounds=3, iterations=5)
    assert result == "Invalid"

def test_first_digit(benchmark):
    result = benchmark.pedantic(is_valid, args=("aa0234",), rounds=3, iterations=5)
    assert result == "Invalid"

def test_normal(benchmark):
     result = benchmark.pedantic(is_valid, args=("aa1234",), rounds=3, iterations=5)
     assert result == "Valid"

def test_end(benchmark):
    result = benchmark.pedantic(is_valid, args=("aa123w",), rounds=3, iterations=5)
    assert result == "Invalid"