"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_smpty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0

#Pytest is not working on my computer, I will go to office hours!