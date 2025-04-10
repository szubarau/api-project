import json
from assertpy import assert_that
from requests import Response



class Assertion:
    """Утилиты для проверки API-ответов."""

    @staticmethod
    def check_status_code(response: Response, expected_status: int):
        """Проверка статус-кода ответа."""
        actual_status = response.status_code
        assert_that(actual_status).is_equal_to(expected_status)
        print(f"[✔] Status code OK: {actual_status}")

    @staticmethod
    def check_json_keys(response: Response, expected_keys: list):
        """Проверка, что JSON содержит все обязательные ключи."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Response is not valid JSON.")

        assert_that(json_data).is_type_of(dict)
        assert_that(json_data).contains(*expected_keys)
        print(f"[✔] JSON contains required keys: {expected_keys}")

    @staticmethod
    def check_json_field_value(response: Response, field_name: str, expected_value):
        """Проверка значения поля в JSON."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Response is not valid JSON.")

        actual_value = json_data.get(field_name)
        print(f"[ℹ] Field '{field_name}': actual = {actual_value}, expected = {expected_value}")
        assert_that(actual_value).is_equal_to(expected_value)
        print(f"[✔] Field '{field_name}' has correct value.")

    @staticmethod
    def check_json_field_type(response: Response, field_name: str, expected_type: type):
        """Проверка типа данных полей в JSON."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Response is not valid JSON.")

        actual_value = json_data.get(field_name)
        assert_that(actual_value).is_not_none()
        assert_that(actual_value).is_instance_of(expected_type)
        print(f"[✔] Field '{field_name}' is of type {expected_type.__name__}")

    def check_json_field_types(response: Response, field_types: dict):
        """
        Проверка нескольких полей на соответствие ожидаемым типам.

        :param response: объект Response
        :param field_types: словарь {имя_поля: тип}, например {'place_id': str, 'location': dict}
        """
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        for field_name, expected_type in field_types.items():
            actual_value = json_data.get(field_name)
            assert_that(actual_value).is_not_none(), f"Поле '{field_name}' отсутствует в ответе."
            assert_that(actual_value).is_instance_of(expected_type), (
                f"Поле '{field_name}' должно быть типа {expected_type.__name__}, "
                f"но получено {type(actual_value).__name__}"
            )
            print(f"[✔] Поле '{field_name}' имеет тип {expected_type.__name__}")

    def check_response_text(response, expected_body: dict):
        """
        Проверяет, что response.text соответствует ожидаемому значению с использованием assertpy

        :param response: Объект ответа (response).
        :param expected_body: Ожидаемое тело ответа в виде строки.
        """
        actual_body = json.loads(response.text)
        assert_that(actual_body).is_equal_to(expected_body)
        print("Успех! Тело ответа совпадает с ожидаемым.")