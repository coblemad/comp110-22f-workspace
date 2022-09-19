"""EX04 - 'list' Utiity Functions."""
__author__ = "730544275"


def all(my_list: list[int], guess_number: int) -> bool:
    """A function that returns a bool indicating whether or not the ints in the list are the same as the given int."""
    i: int = 0
    if len(my_list) == 0:
        return False
    while i < len(my_list):
        if my_list[i] != guess_number:
            return False
        i += 1
    return True

def max(input: list[int]) -> int:
    """A function that returns a maximum in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_check: int = input[0]
    while i < len(input):
        if input[i] > max_check:
            max_check == input[i]
            i += 1
        else:
            i += 1
    return max_check

def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Given two list of int values, returns True if every element of at every index is equal in both lists."""
    i: int = 0
    if len(first_list) != len(second_list):
        return False
    while i < len(first_list) and i < len(second_list):
        if first_list[i] != second_list[i]:
            return False
        i += 1
    return True 