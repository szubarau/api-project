from base.request import Request
from models.payloads import CreatePlacePayload, UpdatePlacePayload, DeletePlacePayload
from config import Base_url, Key, Resource_Post, Resource_Get, Resource_Put, Resource_Delete


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        payload = CreatePlacePayload(
            location={"lat": -38.383494, "lng": 33.427362},
            accuracy=50,
            name="Frontline house",
            phone_number="(+91) 983 893 3937",
            address="29, side layout, cohen 09",
            types=["shoe park", "shop"],
            website="http://google.com",
            language="French-IN"
        )

        url = Base_url + Resource_Post + Key
        print(url)
        result_post = Request.post(url, payload.model_dump(mode='json'))
        print(result_post.text)
        return result_post

    @staticmethod
    def check_new_place(place_id: str):
        url = Base_url + Resource_Get + Key + f'&place_id={place_id}'
        print(url)
        result = Request.get(url)
        print(result.text)
        return result

    @staticmethod
    def update_new_place(place_id: str):
        url = Base_url + Resource_Put + Key
        print(url)
        payload = UpdatePlacePayload(
            place_id=place_id,
            address="100 Lenina street, RU",
            key="qaclick123"
        )
        result = Request.put(url, payload.model_dump(mode='json'))
        print(result.text)
        return result

    @staticmethod
    def delete_new_place(place_id: str):
        url = Base_url + Resource_Delete + Key
        print(url)
        payload = DeletePlacePayload(place_id=place_id)
        result = Request.delete(url, payload.model_dump(mode='json'))
        print(result.text)
        return result
