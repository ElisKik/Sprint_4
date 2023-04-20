import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class TrackPage(BasePage):
    container_order_info = [By.XPATH, './/div[starts-with(@class, "Track_OrderInfo")]']

    @allure.step('Проверка присутствия блока информации о заказе на странице')
    def check_has_order_info(self):
        assert len(self.webdriver.find_elements(*self.container_order_info)) > 0, 'Order info was not found'

