"""EX05 - Test File."""
__author__ = "730544275"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_use1() -> None:
    """Tests function to see if it pulls out even numbers when commanded."""
    xs: list[int] = [1, 2, 3, 4, 4]
    assert only_evens(xs) == [2, 4, 4]


def test_only_evens_use2() -> None:
    """Tests function to see if it returns a blank list when given all odd numbers."""
    xs: list[int] = [1, 3, 7, 11]
    assert only_evens(xs) == []


def test_only_evens_edge() -> None:
    """Edge case to test if correct when no numbers are in the list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_concat_use1() -> None:
    """Tests if concat function puts two lists together of the same size."""
    xs:list[int] = [1, 2, 3]
    xs:list[int] = [1, 2, 3]
    assert concat(xs) == [1, 2, 3, 1, 2, 3]


def test_concat_use2() -> None:
    """Tests if concat function puts two lists together of different sizes."""
    xs: list[int] = [1, 3, 4, 5, 9]
    xs: list[int] = [4, 5]
    assert concat(xs) == [1, 3, 4, 5, 9, 4, 5]


def test_concat_edge() -> None:
    """Edge cast to test if concat function leaves an empty list empty."""
    xs: list[int] = []
    xs: list[int] = []
    assert concat(xs) == []