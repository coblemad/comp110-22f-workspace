"""EX07 - Dictionary Functions. This implements skeleton functions and implementations below."""

__author__ = "730544275"


def invert(my_numbers: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and the values."""
    result: dict[str, str] = {}
    for key in my_numbers:
        if key in result:
            raise KeyError("Cannot have duplicate keys in resulting list.")
        else:
            result[my_numbers[key]] = key
    return result


def favorite_color(color_list: dict[str, str]) -> str:
    """Function that returns the color that appears most frequently in a dictionary."""
    new_dict: dict[str, int] = {}
    result: str = ""
    color_counter: int = 0
    for key in color_list:
        if key in new_dict:
            new_dict[color_list[key]] += 1
        else: 
            new_dict[color_list[key]] = 1
    for key in new_dict:
        if new_dict[key] > color_counter:
            color_counter = new_dict[key]
            result = key
    return key
    


def count(my_list: list[str]) -> dict[str, int]:
    """A function that returns a dictionary that counts eash of the items in the input list. """
    result: dict[str, int] = {}
    for key in my_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result