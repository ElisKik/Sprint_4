from typing import List

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import TIMEOUT
class BasePage:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(webdriver, TIMEOUT)

    def check_valid_input(self, locator: List[str]):
        input_element = self.webdriver.find_element(*locator)

        given_value = input_element.get_attribute('value')

        input_element.clear()
        input_element.send_keys(given_value)

        error_locator = [By.XPATH, f'{locator[1]}/../div']

        error_element = self.webdriver.find_element(*error_locator)

        is_valid = len(error_element.text) == 0

        assert is_valid, f'Input \'{given_value}\' is invalid: {error_element.text}'

    def wait_url_to_be_in_any_window(self, expected_url: str) -> None:
        self.wait.until(lambda driver: BasePage.check_url_in_any_window(driver, expected_url))

    @staticmethod
    def check_url_in_any_window(webdriver: WebDriver, expected_url: str) -> bool:
        for window_handle in webdriver.window_handles:
            webdriver.switch_to.window(window_handle)

            if webdriver.current_url == expected_url:
                return True

        return False

