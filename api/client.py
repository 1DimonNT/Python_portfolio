import allure
import json
import requests
from typing import Dict, Any, Optional, Union
from requests import Response
from config.settings import settings


class APIClient:
    """Базовый API клиент"""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    @allure.step("GET {endpoint}")
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Response:
        """GET запрос"""
        response = self.session.get(f"{self.base_url}{endpoint}", params=params)
        self._attach_response(response)
        return response

    @allure.step("POST {endpoint}")
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Response:
        """POST запрос"""
        response = self.session.post(f"{self.base_url}{endpoint}", json=data)
        self._attach_response(response)
        if data:
            allure.attach(json.dumps(data, indent=2, ensure_ascii=False), 'Request Body', allure.attachment_type.JSON)
        return response

    @allure.step("PUT {endpoint}")
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Response:
        """PUT запрос"""
        response = self.session.put(f"{self.base_url}{endpoint}", json=data)
        self._attach_response(response)
        if data:
            allure.attach(json.dumps(data, indent=2, ensure_ascii=False), 'Request Body', allure.attachment_type.JSON)
        return response

    @allure.step("DELETE {endpoint}")
    def delete(self, endpoint: str) -> Response:
        """DELETE запрос"""
        response = self.session.delete(f"{self.base_url}{endpoint}")
        self._attach_response(response)
        return response

    @allure.step("PATCH {endpoint}")
    def patch(self, endpoint: str, data: Optional[Dict] = None) -> Response:
        """PATCH запрос"""
        response = self.session.patch(f"{self.base_url}{endpoint}", json=data)
        self._attach_response(response)
        if data:
            allure.attach(json.dumps(data, indent=2, ensure_ascii=False), 'Request Body', allure.attachment_type.JSON)
        return response

    def _attach_response(self, response: Response):
        """Прикрепить информацию о ответе к Allure отчету"""
        allure.attach(
            str(response.status_code),
            f'Response Status: {response.status_code}',
            allure.attachment_type.TEXT
        )

        if not response.text:
            return

        max_size = getattr(settings, 'ALLURE_MAX_ATTACHMENT_SIZE', 5000)
        preview = response.text[:max_size]

        try:
            # Пытаемся распарсить как JSON
            data = response.json()
            formatted = json.dumps(data, indent=2, ensure_ascii=False)

            # Если ответ был обрезан, добавляем предупреждение
            if len(response.text) > max_size:
                formatted += f"\n\n... [ответ обрезан, превышает {max_size} символов]"

            allure.attach(formatted, 'Response Body', allure.attachment_type.JSON)

        except (ValueError, json.JSONDecodeError):
            # Если не JSON - прикрепляем как текст
            attachment_type = allure.attachment_type.TEXT
            if len(response.text) > max_size:
                preview += f"\n\n... [ответ обрезан, превышает {max_size} символов]"
            allure.attach(preview, 'Response Body (text)', attachment_type)

    def set_header(self, key: str, value: str):
        """Установить заголовок для всех запросов"""
        self.session.headers.update({key: value})

    def clear_headers(self):
        """Очистить все заголовки"""
        self.session.headers.clear()