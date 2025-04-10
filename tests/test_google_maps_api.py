import pytest

from controllers.api import GoogleMapsApi
from support.assertion import Assertion


class TestCreatePlace:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_create_new_place(self):
        result_post = GoogleMapsApi.create_new_place()
        Assertion.check_status_code(result_post, 200)
        Assertion.check_json_keys(result_post, ['place_id', 'status', 'scope'])
        Assertion.check_json_field_types(result_post, {'place_id': str, 'status': str, 'scope': str})
        Assertion.check_json_field_value(result_post, 'status', 'OK')

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_check_create_new_place(self, create_new_place):
        place_id = create_new_place['place_id']
        result_get = GoogleMapsApi.check_new_place(place_id)
        Assertion.check_status_code(result_get, 200)
        Assertion.check_json_keys(result_get, [
            'location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'
        ])

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_update_place(self, create_new_place):
        place_id = create_new_place['place_id']
        result_put = GoogleMapsApi.update_new_place(place_id)
        Assertion.check_status_code(result_put, 200)
        Assertion.check_json_keys(result_put, ['msg'])
        Assertion.check_json_field_value(result_put, 'msg', 'Address successfully updated')
        Assertion.check_response_text(result_put, {'msg': 'Address successfully updated'})

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_check_update_place(self, create_new_place):
        place_id = create_new_place['place_id']
        result_get = GoogleMapsApi.check_new_place(place_id)
        Assertion.check_status_code(result_get, 200)
        Assertion.check_json_field_value(result_get, 'address', '100 Lenina street, RU')
        Assertion.check_response_text(result_get, {"location": {"latitude": "-38.383494", "longitude": "33.427362"},
                                                   "accuracy": "50", "name": "Frontline house",
                                                   "phone_number": "(+91) 983 893 3937",
                                                   "address": "100 Lenina street, RU", "types": "shoe park,shop",
                                                   "website": "http://google.com", "language": "French-IN"})

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_delete_place(self, create_new_place):
        place_id = create_new_place['place_id']
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Assertion.check_status_code(result_delete, 200)
        Assertion.check_json_keys(result_delete, ['status'])
        Assertion.check_response_text(result_delete, {'status': 'OK'})

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_check_delete_place(self, create_new_place):
        place_id = create_new_place['place_id']
        result_get = GoogleMapsApi.check_new_place(place_id)
        Assertion.check_status_code(result_get, 404)
        Assertion.check_response_text(result_get, {'msg': 'Get operation failed, looks like place_id  doesn\'t exists'})
