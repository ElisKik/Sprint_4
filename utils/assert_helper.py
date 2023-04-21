from typing import List

from selenium.webdriver import Firefox as WebDriver

class AssertHelper:
    @staticmethod
    def current_url_is(webdriver: WebDriver, expected: str) -> None:
        actual = webdriver.current_url
        assert expected == actual, f'URLs are not equal\nexpected: {expected}\n  actual: {actual}'

    @staticmethod
    def string_contains(entry: str, text: str) -> None:
        assert entry in text, f'Text does not contain given string\n text: {text}\nentry: {entry}'

    @staticmethod
    def is_displayed(webdriver: WebDriver, locator: List[str]) -> None:
        element = webdriver.find_element(*locator)
        assert element.is_displayed(), f'Element is not displayed at locator\n{locator}'

