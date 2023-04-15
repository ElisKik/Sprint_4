import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.order_customer_page import OrderCustomerPage
from pages.order_rent_page import OrderRentPage
from pages.order_confirm_page import OrderConfirmPage
from utils.random import RandomData

class TestOrder:
    @allure.title('Тест заказа')
    @allure.description('Отправляем заказ')
    def test_order(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)

        base_page.click_button_accept_cookies()
        base_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver, wait)

        first_name, last_name = RandomData.get_name()

        order_customer_page.set_first_name(first_name)
        order_customer_page.check_valid_first_name()

        order_customer_page.set_last_name(last_name)
        order_customer_page.check_valid_last_name()

        address = RandomData.get_address()
        order_customer_page.set_address(address)
        order_customer_page.check_valid_address()

        metro = RandomData.get_metro_station()
        order_customer_page.set_metro(metro)

        phone_number = RandomData.get_phone()
        order_customer_page.set_phone(phone_number)
        order_customer_page.check_valid_phone()

        order_customer_page.click_button_next()
        order_customer_page.check_form_switched()

        order_rent_page = OrderRentPage(webdriver, wait)

        date_string = RandomData.get_date_string()
        order_rent_page.set_date(date_string)

        order_rent_page.set_random_duration()
        order_rent_page.set_random_color()

        comment = RandomData.get_text()
        order_rent_page.set_comment(comment)

        order_rent_page.click_button_order()
        order_rent_page.check_form_submitted()

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()
