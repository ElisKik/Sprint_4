"""
Script for definitions of fixtures.
"""

import allure
import pytest

from typing import Iterable

from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By

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

    button_accept_cookies = [By.ID, 'rcc-confirm-button']
    webdriver.find_element(*button_accept_cookies).click()

    yield webdriver

    webdriver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield

    result: pytest.CollectReport = outcome.get_result()

    if result.when == 'call' and result.failed:
        if 'webdriver' in item.fixturenames:
            webdriver: WebDriver = item.funcargs['webdriver']
            allure.attach(
                body=webdriver.get_screenshot_as_png(),
                name=f'{item.originalname}.png',
                attachment_type=allure.attachment_type.PNG)

