"""Unit Testing for EX07."""
__author__ = "730544275"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_use1() -> None:
    """Tests the first use case for the invert function to see if it changes the of letters as commanded."""
    xs: dict({'b' : 'c', 'r' : 'x', 'y' : 'z'})
    assert invert(xs) == {'c' : 'b', 'x' : 'r', 'z' : 'y'}


def test_invert_use2() -> None:
    """Tests the second use case for the invert function to see if it flips two words put into the dictionary."""
    xs: dict({'slay': 'purr'})
    assert invert(xs) == {'purr' : 'slay'}


def test_invert_edge() -> None:
    """Tests the edge case for the invert function to see if it returns an empty list when given one."""
    xs: dict({})
    assert invert(xs) == {}


def test_favorite_color_use1() -> None:
    """Tests the first use case for the favorite_color function to see if it returns the correct color."""
    xs: dict({"Madelyn": "pink", "Molly": "yellow", "Leah": "red", "Alaina": "pink"})
    assert favorite_color(xs) == "pink"

def test_favorite_color_use2() -> None:
    """Tests the second use case for the favorite_color function to see if it returns the correct color."""
    xs: dict({"Trixie": "pink", "Katya": "purple", "Todrick": "purple"})
    assert favorite_color(xs) == "purple"


def test_favorite_color_edge() -> None:
    """Tests the edge case for the favorite_color function."""
    xs: dict({})
    assert favorite_color(xs) == ""


def test_count_use1() -> None: 
    """Tests the first use case for the count function to see if it counts correctly."""
    xs: list("Slay", "Slay", "Slay")
    assert count(xs) == [{"Slay": 3}]


def test_count_use2() -> None: 
    """Tests the second use case for the count function to see if it counts one word correctly."""
    xs: list("Material", "girl")
    assert count(xs) == [{"Material": 1, "girl": 1}]


def test_count_edge() -> None: 
    """Tests the edge case for the count function to see if it returns an empty list."""
    xs:  list()
    assert count(xs) == [{}]