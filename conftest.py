# conftest.py (корень проекта)
import pytest
from typing import List


def pytest_collection_modifyitems(items: List[pytest.Item]):
    """
    Автоматически добавляет маркеры тестам на основе их расположения.
    - Тесты в tests/api/ получают маркер @pytest.mark.api
    - Тесты в tests/ui/ получают маркер @pytest.mark.ui
    """
    for item in items:
        # API тесты
        if "tests/api" in str(item.nodeid):
            item.add_marker(pytest.mark.api)

        # UI тесты
        if "tests/ui" in str(item.nodeid):
            item.add_marker(pytest.mark.ui)


def pytest_addoption(parser):
    """Добавляет кастомные опции командной строки"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome/firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def browser_type(request):
    """Фикстура для получения браузера из командной строки"""
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless_mode(request):
    """Фикстура для получения режима headless"""
    return request.config.getoption("--headless")