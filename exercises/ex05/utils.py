"""EX05 - 'list' Utility Functions."""
__author__ = "730544275"


def only_evens(my_list: list[int]) -> int:
    """A function that returns only the even numbers in a list."""
    i: int = 0
    new_list: list[int] = []
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            new_list.append(my_list[i])
            i += 1
        else:
            i += 1
    return new_list


def concat(my_first_list: list[int], my_second_list: list[int]) -> int:
    """A function that generates a new list that contains all of the elements in both lists."""
    new_list: list[int] = []
    for x in my_first_list: 
        new_list.append(x)
    for x in my_second_list:
        new_list.append(x)
    return new_list


def sub(a_list: list[int], first_num: int, second_num: int) -> int:
    """A function that generates a list that is a subset of the given list between the start index and the end minus one."""
    new_list: list[int] = []
    if first_num < 0:
        starting_place: int = 0
    else:
        starting_place = first_num
    if second_num > len(a_list):
        ending_place: int = len(a_list)
    else:
        ending_place = second_num
    if len(a_list) == 0 or starting_place > len(a_list) or ending_place <= 0:
        return []
    new_list.append(a_list[starting_place])
    new_list.append(a_list[ending_place - 1])
    return new_list