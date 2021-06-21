import pytest
from src.utils import validate


def test_validate_is_one_happy_path():
    found_element = [1]

    validation = validate.check_one_selected(found_element)

    assert validation == 1


def test_validate_is_one_unhappy_path():
    no_elements = []
    too_many_elements = [1, 2, 3]

    with pytest.raises(IndexError):
        validate.check_one_selected(too_many_elements)
    
    with pytest.raises(IndexError):
        validate.check_one_selected(no_elements)


def test_validate_is_number_happy_path():
    temperature = "20"

    validation = validate.check_is_number(temperature)

    assert validation == 20


def test_validate_is_number_unhappy_path():
    not_temperature_invalid = "20w"
    not_temperature_empty = ""
    not_temperature_char = "20°"

    with pytest.raises(ValueError):
        validate.check_is_number(not_temperature_invalid)
    
    with pytest.raises(ValueError):
        validate.check_is_number(not_temperature_empty)
    
    with pytest.raises(ValueError):
        validate.check_is_number(not_temperature_char)
