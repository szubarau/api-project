from utils.request import Request
from config import Base_url, Key, Resource_Post, Resource_Get, Resource_Put, Resource_Delete


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        json_create_new_location = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"
        }

        url = Base_url + Resource_Post + Key
        print(url)
        result_post = Request.post(url, json_create_new_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def check_new_place(place_id):
        url = Base_url + Resource_Get + Key + f'&place_id={place_id}'
        print(url)
        result = Request.get(url)
        print(result.text)
        return result

    @staticmethod
    def update_new_place(place_id):
        url = Base_url + Resource_Put + Key
        print(url)
        json_update_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result = Request.put(url, json_update_place)
        print(result.text)
        return result

    @staticmethod
    def delete_new_place(place_id):
        url = Base_url + Resource_Delete + Key
        print(url)
        json_delete_place = {
            "place_id": place_id
        }
        result = Request.delete(url, json_delete_place)
        print(result.text)
        return result
