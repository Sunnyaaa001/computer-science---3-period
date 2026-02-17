import pytest
from reverse_string import reverse_string

def test_normal_string(benchmark):
    # assert reverse_string("hello") == "olleh"
    result = benchmark(reverse_string,"hello")
    assert result == "olleh"


def test_with_space(benchmark):
    result = benchmark(reverse_string,"hello everyone!")
    assert result == "!enoyreve olleh"


def test_same(benchmark):
    result = benchmark(reverse_string,"ded")
    assert result == "ded"

def test_one_symbol(benchmark):
    test = "A" * 100
    result = benchmark(reverse_string,test)
    assert result == "A" * 100