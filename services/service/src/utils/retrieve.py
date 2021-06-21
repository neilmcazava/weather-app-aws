import requests


# returns parsed html web page from location id
def fetch_data(url: str, location_id: str) -> str:
    try:
        # fetch bbc weather page
        endpoint = url + location_id
        response = requests.get(endpoint)

    except Exception:
        raise Exception(f"Failed to fetch page with id : {location_id}")
    
    # return html content
    return  response.text
