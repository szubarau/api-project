import json
from requests import Response


class Assertion:
    """Утилиты для проверки API-ответов"""

    @staticmethod
    def check_status_code(response: Response, expected_status: int):
        """Проверка статус-кода ответа."""
        actual_status = response.status_code
        assert actual_status == expected_status, f"Ожидался статус {expected_status}, но получен {actual_status}"
        print(f"[✔] Status code OK: {actual_status}")

    @staticmethod
    def check_json_keys(response: Response, expected_keys: list):
        """Проверка, что JSON содержит все обязательные ключи."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        if not isinstance(json_data, dict):
            raise AssertionError("JSON должен быть объектом (dict).")

        for key in expected_keys:
            assert key in json_data, f"Ключ '{key}' отсутствует в JSON."

        print(f"[✔] JSON содержит обязательные ключи: {expected_keys}")

    @staticmethod
    def check_json_field_value(response: Response, field_name: str, expected_value):
        """Проверка значения поля в JSON."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        actual_value = json_data.get(field_name)
        print(f"[ℹ] Поле '{field_name}': фактическое = {actual_value}, ожидаемое = {expected_value}")
        assert actual_value == expected_value, (
            f"Значение поля '{field_name}' должно быть '{expected_value}', но получено '{actual_value}'"
        )
        print(f"[✔] Значение поля '{field_name}' корректно.")

    @staticmethod
    def check_json_field_type(response: Response, field_name: str, expected_type: type):
        """Проверка типа поля в JSON."""
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        if field_name not in json_data:
            raise AssertionError(f"Поле '{field_name}' отсутствует в JSON.")

        actual_value = json_data[field_name]
        assert isinstance(actual_value, expected_type), (
            f"Тип поля '{field_name}' должен быть {expected_type.__name__}, "
            f"но получен {type(actual_value).__name__}"
        )
        print(f"[✔] Поле '{field_name}' имеет тип {expected_type.__name__}")

    @staticmethod
    def check_json_field_types(response: Response, field_types: dict):
        """
        Проверка нескольких полей на соответствие ожидаемым типам.

        :param response: объект Response
        :param field_types: словарь {имя_поля: тип}
        """
        try:
            json_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        for field_name, expected_type in field_types.items():
            if field_name not in json_data:
                raise AssertionError(f"Поле '{field_name}' отсутствует в JSON.")
            actual_value = json_data[field_name]
            assert isinstance(actual_value, expected_type), (
                f"Тип поля '{field_name}' должен быть {expected_type.__name__}, "
                f"но получен {type(actual_value).__name__}"
            )
            print(f"[✔] Поле '{field_name}' имеет тип {expected_type.__name__}")

    @staticmethod
    def check_response_text(response: Response, expected_body: dict):
        """
        Проверка, что response.text соответствует ожидаемому JSON-объекту.
        """
        try:
            actual_body = json.loads(response.text)
        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON.")

        assert actual_body == expected_body, (
            f"Ожидаемое тело: {expected_body}, но получено: {actual_body}"
        )
        print("[✔] Тело ответа совпадает с ожидаемым.")