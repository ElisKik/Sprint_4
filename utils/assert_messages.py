from typing import List

class EqualityMismatch:
    @staticmethod
    def strings(expected: str, actual: str) -> str:
        return f'Strings are not equal\nexpected: {expected}\n  actual: {actual}'

    @staticmethod
    def contains(entry: str, text: str) -> str:
        return f'Text does not contain given string\n text: {text}\nentry: {entry}'

class WebElementState:
    @staticmethod
    def not_displayed(locator: List[str]) -> str:
        return f'WebElement is not displayed at locator\n{locator}'
