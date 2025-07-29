import pytest
from stringutils import StringUtils

utils = StringUtils

@pytest.mark.parametrize("input_text, excepted_text", [("hi, man", "Hi, man"), 
("kinopoisk", "Kinopoisk"), 
("dear", " ") ],)
def test_capitalize_positiv_negative (input_text, expected_text):
    assert utils.capitalize(input_text) == expected_text

@pytest.mark.parametrize("input_text, output_text", [("  Hi", "Hi"), 
("trouble", "  trouble"), ("none", "none"), ('violence', ""),],)
def test_trim_positive_negative (input_text, output_text):
    assert utils.trim(input_text) == output_text


@pytest.mark.parametrize("text, letter", [("book", "o"), 
("Street", "S"), 
("room", "t")],)
def test_contains_positive_negative(text, letter):
    assert utils.contains(text) == letter

@pytest.mark.parametrize("input_text, without_symbol", [("trust", "r"),
("symbol", "m"), 
("text", "y"), ],)
def test_exit_positive_negative(input_text, without_symbol):
    assert utils.delete_symbol(input_text) == without_symbol