import pytest
from bank import value

def test_hello(benchmark):

    result = benchmark.pedantic(
        value,
        args=("Hello",),
        rounds=3,
        iterations=5
    )

    assert result == 0


def test_startwith_hello(benchmark):

    result = benchmark.pedantic(
        value,
        args=("Hello, Sunny",),
        rounds=3,
        iterations=5
    )

    assert result == 0


def test_startwith_h(benchmark):

    result = benchmark.pedantic(
        value,
        args=("How are you",),
        rounds=3,
        iterations=5
    )

    assert result == 20


def test_startwith_other(benchmark):

    result = benchmark.pedantic(
        value,
        args=("Where are you",),
        rounds=3,
        iterations=5
    )

    assert result == 100  