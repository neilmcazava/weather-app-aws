from src.utils import validate
from bs4 import BeautifulSoup


# returns string (current temperature) from parsed html
def find_temperature(html: str, forecast_index: int, unit: str) -> int:
    parsed_html = BeautifulSoup(html, features="html.parser")

    # select first hour (ie current time) forecast slot
    first_forecast_slot = validate.check_one_selected(parsed_html.select(f".wr-js-time-slot:nth-child({forecast_index})"))

    # select only temperature element span
    temperature_span = validate.check_one_selected(first_forecast_slot.select(f'span[class^="wr-value--temperature--{unit}"]'))

    # return selected element content
    temperature_content = temperature_span.get_text()

    # remove unparsable '°' character & create response
    temperature = temperature_content[0: -1]

    return validate.check_is_number(temperature)
