from typing import List

from selenium.webdriver import Firefox as WebDriver

class EqualityMismatch: # TODO: rename
    @staticmethod
    def to_current_url(webdriver: WebDriver, expected: str) -> str:
        actual = webdriver.current_url
        assert expected == actual, f'Strings are not equal\nexpected: {expected}\n  actual: {actual}'

    @staticmethod
    def contains(entry: str, text: str) -> str:
        return f'Text does not contain given string\n text: {text}\nentry: {entry}'

class WebElementState:
    @staticmethod
    def not_displayed(locator: List[str]) -> str:
        return f'WebElement is not displayed at locator\n{locator}'

