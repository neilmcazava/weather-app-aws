import pytest
import requests_mock
from src.utils import retrieve
from tests import data


mock_id = "12345"
mock_url = "http://mock_url.com"
mock_endpoint = mock_url + mock_id


def test_retrieve_happy_path():
    with requests_mock.Mocker() as mock_request:
        mock_request.get(mock_endpoint, text=data.mock_html_temp)
            
        response = retrieve.fetch_data(mock_url, mock_id)

    assert type(response) == str
    assert response == data.mock_html_temp


def test_retrieve_unhappy_path():
    with pytest.raises(Exception):
        with requests_mock.Mocker() as mock_request:
            mock_request.get(mock_endpoint, text=data.mock_html_temp)
                
            retrieve.fetch_data(mock_url + "/", mock_id)
