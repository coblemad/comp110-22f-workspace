"""EX05 - 'list' Utility Functions."""
__author__ = "730544275"

def only_evens(my_list: list[int]) -> int:
    """A function that returns only the even numbers in a list."""
    i: int = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            my_list.pop[i]
            i += 1
        else:
            i += 1
        return my_list
