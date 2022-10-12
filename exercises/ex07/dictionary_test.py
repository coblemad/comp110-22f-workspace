"""Unit Testing for EX07."""
__author__ = "730544275"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_use1() -> None:
    """Tests the first use case for the invert function to see if it changes the of letters as commanded."""
    my_numbers = ({'b': 'c', 'r': 'x', 'y': 'z'})
    assert invert(my_numbers) == {'c': 'b', 'x':'r', 'z': 'y'}


def test_invert_use2() -> None:
    """Tests the second use case for the invert function to see if it flips two words put into the dictionary."""
    my_numbers = ({'slay': 'purr'})
    assert invert(my_numbers) == {'purr': 'slay'}


def test_invert_edge() -> None:
    """Tests the edge case for the invert function to see if it returns an empty list when given one."""
    my_numbers = ({})
    assert invert(my_numbers) == {}


def test_favorite_color_use1() -> None:
    """Tests the first use case for the favorite_color function to see if it returns the correct color."""
    color_list = ({"Madelyn": "pink", "Molly": "yellow", "Leah": "red", "Alaina": "pink"})
    assert favorite_color(color_list) == "pink"


def test_favorite_color_use2() -> None:
    """Tests the second use case for the favorite_color function to see if it returns the correct color."""
    color_list = ({"Trixie": "pink", "Katya": "purple", "Todrick": "purple"})
    assert favorite_color(color_list) == "purple"


def test_favorite_color_edge() -> None:
    """Tests the edge case for the favorite_color function."""
    color_list = ({})
    assert favorite_color(color_list) == ""


def test_count_use1() -> None: 
    """Tests the first use case for the count function to see if it counts correctly."""
    my_list = ["Slay", "Slay", "Slay"]
    assert count(my_list) == [{"Slay": 3}]


def test_count_use2() -> None: 
    """Tests the second use case for the count function to see if it counts one word correctly."""
    my_list = ["Material", "girl"]
    assert count(my_list) == [{"Material": 1, "girl": 1}]


def test_count_edge() -> None: 
    """Tests the edge case for the count function to see if it returns an empty list."""
    my_list = []
    assert count(my_list) == [{}]