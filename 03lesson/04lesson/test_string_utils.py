import pytest
from stringutils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("input_text, excepted_text", [("hi, man", "Hi, man"), 
("kinopoisk", "Kinopoisk"), 
("dear", "Dear ") ],)
def test_capitalize_positiv_negative (input_text, expected_text):
    assert utils.capitalize(input_text) == expected_text

@pytest.mark.parametrize("input_text, output_text", [("  Hi", "Hi"), 
("  trouble", "trouble"), ("none", "none"), ('violence', ""),],)
def test_trim_positive_negative (input_text, output_text):
    assert utils.trim(input_text) == output_text


@pytest.mark.parametrize("text, letter, expexted", [("book", "o", True), 
("Street", "S", True), 
("room", "t", False)],)
def test_contains_positive_negative(text, letter, expexted):
    assert utils.contains(text,letter) == expexted

@pytest.mark.parametrize("input_text, symbol, without_symbol ", [("trust", "r", "rust"),
("symbol", "m", "symbol"), 
("text", "y"), "text" ],)
def test_delete_symbol_positive_negative(input_text, symbol, without_symbol):
    assert utils.delete_symbol(input_text, symbol) == without_symbol