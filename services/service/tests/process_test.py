import pytest
from src.utils import process
from tests import data


def test_process_happy_path():
    forecast_slot = 1
    celsius = "c"
    fahrenheit = "f"

    celsius_response = process.find_temperature(data.mock_html_temp, forecast_slot, celsius)

    assert celsius_response == 10

    fahrenheit_response = process.find_temperature(data.mock_html_temp, forecast_slot, fahrenheit)

    assert fahrenheit_response == 50


def test_process_unhappy_path():
    forecast_slot = 1
    celsius = "c"
    fahrenheit = "f"

    with pytest.raises(ValueError):
        process.find_temperature(data.mock_html_no_temp, forecast_slot, celsius)

    with pytest.raises(ValueError):
        process.find_temperature(data.mock_html_no_temp, forecast_slot, fahrenheit)
