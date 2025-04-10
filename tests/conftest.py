import pytest
from controllers.api import GoogleMapsApi


@pytest.fixture(scope='session')
def create_new_place():
    response = GoogleMapsApi.create_new_place()
    data = response.json()
    return data
