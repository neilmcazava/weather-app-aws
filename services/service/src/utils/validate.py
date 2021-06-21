
# returns single html element from inside list of 1 item
def check_one_selected(selected_element: list) -> str:
    # check only one html element is selected from selectors
    if len(selected_element) != 1:
        raise IndexError(f'Invalid number of elements selected: {len(selected_element)}')
    else:
        return selected_element[0]

# return number from scraped html, checks is number
def check_is_number(temperature: str) -> int:
    try:
        return int(temperature)
    except ValueError:
        raise ValueError(f"Temperature {temperature} is not number")
