def odd_and_even(my_nums: list[int]) -> list[int]:
    """Practice."""
    new_list: list[int] = []
    for number in my_nums:
        if number / 2 != 0 and my_nums[number] / 2:
            new_list.append(number)
    return new_list