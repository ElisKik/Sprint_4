from typing import List

from selenium.webdriver.remote.webelement import WebElement

class EqualityMismatch:
    @staticmethod
    def strings(expected: str, actual: str):
        return f'Strings are not equal\nexpected: {expected}\n  actual: {actual}'

class WebElementState:
    @staticmethod
    def not_displayed(locator: List[str]):
        return f'WebElement is not displayed at locator\n{locator}'
