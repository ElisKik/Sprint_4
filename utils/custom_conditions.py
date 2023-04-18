from selenium.webdriver import Firefox as WebDriver

class CustomConditions:
    @staticmethod
    def url_to_be_in_any_window(webdriver: WebDriver, expected_url: str) -> bool:
        for window_handle in webdriver.window_handles:
            webdriver.switch_to.window(window_handle)

            if webdriver.current_url == expected_url:
                return True

        return False

