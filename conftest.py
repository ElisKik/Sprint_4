"""
Script for definitions of fixtures.
"""

import pytest

from typing import Iterable

from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait

from data.constants import TIMEOUT
from data.urls import Urls

@pytest.fixture
def webdriver() -> Iterable[WebDriver]:
    """
    Fixture of Selenium WebDriver configured
    with maximized window and headless mode
    by default.
    """
    options = Options()

    options.add_argument('--headless')

    webdriver = WebDriver(options=options)

    webdriver.maximize_window()

    webdriver.get(Urls.BASE)

    yield webdriver

    webdriver.quit()

@pytest.fixture
def wait(webdriver: WebDriver) -> WebDriverWait:
    """
    Fixture that returns instance of :class:`WebDriverWait`
    """

    return WebDriverWait(webdriver, TIMEOUT)