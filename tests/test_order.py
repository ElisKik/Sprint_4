import time
import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.order_customer_page import OrderCustomerPage
from utils.random import RandomData

class TestOrder:
    @allure.title('Тест заказа')
    @allure.description('Заполняем все поля, и нажимаем кнопку **Далее**')
    def test_order(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)

        base_page.click_button_accept_cookies()
        base_page.click_button_order()

        first_name, last_name = RandomData.get_name()
        address = RandomData.get_address()
        phone_number = RandomData.get_phone()
        metro = RandomData.get_metro_station()

        order_customer_page = OrderCustomerPage(webdriver, wait)

        order_customer_page.set_first_name(first_name)
        order_customer_page.check_valid_first_name()

        order_customer_page.set_last_name(last_name)
        order_customer_page.check_valid_last_name()

        order_customer_page.set_address(address)
        order_customer_page.check_valid_address()

        order_customer_page.set_metro(metro)

        order_customer_page.set_phone(phone_number)
        order_customer_page.check_valid_phone()

        order_customer_page.click_button_next()
        order_customer_page.check_form_switched()
