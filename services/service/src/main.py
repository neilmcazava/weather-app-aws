import json
from src.utils import retrieve, process, helpers

logger = helpers.get_logger()

lerwick_id = "2644605"
url = "https://www.bbc.co.uk/weather/"

def handler(event, context):
    # log event
    logger.info(f'Event: {json.dumps(event, indent=4)}')

    # scrape webpage
    webpage_html = retrieve.fetch_data(url, lerwick_id)

    # forecast slot index number
    forecast_index = 1

    # 'c' celsius | 'f' fahrenheit
    unit = 'c'

    # search for current temperature in html
    temperature = process.find_temperature(webpage_html, forecast_index, unit)

    response = {
        "statusCode": 200,
        "body": {
            "message": f"Current temperature in Lerwick is {temperature} Celsius"
        }
    }

    # log response
    logger.info(f'Successful Request: {json.dumps(response, indent=4)}')

    # return valid response
    return json.dumps(response, indent=4)
