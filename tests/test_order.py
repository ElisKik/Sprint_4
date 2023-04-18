import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.landing_page import LandingPage
from pages.order_customer_page import OrderCustomerPage
from pages.order_rent_page import OrderRentPage
from pages.order_confirm_page import OrderConfirmPage
from pages.order_completed_page import OrderCompletedPage
from utils.random import RandomData

class TestOrder:
    @allure.title('Тест подтверждения отправки нового заказа с хэдера')
    @allure.description('Переходим к созданию нового заказа через кнопку в хэдере, \
                        заполняем необходимые поля и подтверждаем отправку заказа, \
                        проверяем, что заказ получил свой ID')
    def test_order_from_header_confirm(self, webdriver: WebDriver, wait: WebDriverWait):
        self.__enter_order_from_header(webdriver, wait)
        self.__fill_order_common(webdriver, wait)

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver, wait)

        order_completed_page.check_has_order_id()

    @allure.title('Тест подтверждения отправки нового заказа с лендинга')
    @allure.description('Переходим к созданию нового заказа через кнопку в лендинге, \
                        заполняем необходимые поля и подтверждаем отправку заказа, \
                        проверяем, что заказ получил свой ID')
    def test_order_from_landing_confirm(self, webdriver: WebDriver, wait: WebDriverWait):
        self.__enter_order_from_landing(webdriver, wait)
        self.__fill_order_common(webdriver, wait)

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver, wait)

        order_completed_page.check_has_order_id()

    @allure.title('Тест неподтверждения отправки нового заказа с хэдера')
    @allure.description('Переходим к созданию нового заказа через кнопку в хэдере, \
                        заполняем необходимые поля и **не** подтверждаем отправку заказа, \
                        проверяем, что вернулись на форму заполнения информации об аренде')
    def test_order_from_header_not_confirm(self, webdriver: WebDriver, wait: WebDriverWait):
        self.__enter_order_from_header(webdriver, wait)
        self.__fill_order_common(webdriver, wait)

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_no()
        order_confirm_page.check_order_not_confirmed()

    @allure.title('Тест неподтверждения отправки нового заказа с лендинга')
    @allure.description('Переходим к созданию нового заказа через кнопку в лендинге, \
                        заполняем необходимые поля и **не** подтверждаем отправку заказа, \
                        проверяем, что вернулись на форму заполнения информации об аренде')
    def test_order_from_landing_not_confirm(self, webdriver: WebDriver, wait: WebDriverWait):
        self.__enter_order_from_landing(webdriver, wait)
        self.__fill_order_common(webdriver, wait)

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_no()
        order_confirm_page.check_order_not_confirmed()

    def __enter_order_from_header(self, webdriver: WebDriver, wait: WebDriverWait):
        main_page = MainPage(webdriver, wait)

        main_page.click_button_accept_cookies()
        main_page.click_button_order()

    def __enter_order_from_landing(self, webdriver: WebDriver, wait: WebDriverWait):
        main_page = MainPage(webdriver, wait)

        main_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_button_order()
        landing_page.click_button_order()

    def __fill_order_common(self, webdriver: WebDriver, wait: WebDriverWait):
        order_customer_page = OrderCustomerPage(webdriver, wait)

        first_name, last_name = RandomData.get_name()

        order_customer_page.set_first_name(first_name)
        order_customer_page.check_valid_first_name()

        order_customer_page.set_last_name(last_name)
        order_customer_page.check_valid_last_name()

        address = RandomData.get_address()
        order_customer_page.set_address(address)
        order_customer_page.check_valid_address()

        order_customer_page.set_random_metro_station()

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

