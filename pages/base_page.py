from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from data.constants import TIMEOUT
class BasePage:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(webdriver, TIMEOUT)

    def wait_url_to_be_in_any_window(self, expected_url: str) -> None:
        self.wait.until(lambda driver: BasePage.__check_url_in_any_window(driver, expected_url))

    @staticmethod
    def __check_url_in_any_window(webdriver: WebDriver, expected_url: str) -> bool:
        for window_handle in webdriver.window_handles:
            webdriver.switch_to.window(window_handle)

            if webdriver.current_url == expected_url:
                return True

        return False

