import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from data.urls import Urls
from pages.main_page import MainPage
from pages.order_customer_page import OrderCustomerPage
from pages.order_rent_page import OrderRentPage
from pages.order_confirm_page import OrderConfirmPage
from pages.order_completed_page import OrderCompletedPage
from pages.track_page import TrackPage
from utils.random import RandomData

class TestTrack:
    @allure.title('Тест получения статуса заказа со страницы успешного завершения оформления заказа')
    @allure.description('Создаём заказ, кликаем на кнопку **Посмотреть статус** сразу после создания заказа, \
                        проверяем, что на странице присутствует блок информации о заказе')
    def test_get_order_status_on_completed(self, webdriver: WebDriver, wait: WebDriverWait):
        main_page = MainPage(webdriver, wait)

        main_page.click_button_order()

        self.__make_order_common(webdriver, wait)

        order_completed_page = OrderCompletedPage(webdriver, wait)
        order_completed_page.click_button_status()

        track_page = TrackPage(webdriver, wait)
        track_page.check_has_order_info()

    @allure.title('Тест получения статуса заказа с поля поиска в хэдере')
    @allure.description('Создаём заказ, кликаем на кнопку **Статус заказа**, вводим номер заказа \
                        кликаем на кнопку поиска заказа, проверяем, что на странице присутствует блок информации о заказе')
    def test_get_order_status_from_header(self, webdriver: WebDriver, wait: WebDriverWait):
        main_page = MainPage(webdriver, wait)
        main_page.click_button_order()

        self.__make_order_common(webdriver, wait)

        order_completed_page = OrderCompletedPage(webdriver, wait)

        order_id = order_completed_page.get_order_id()

        assert order_id is not None, 'Order ID was not found on page'

        webdriver.get(Urls.BASE)

        main_page.click_button_status()
        main_page.check_input_appeared_on_button_status()

        main_page.set_order_id(order_id)
        main_page.click_button_search_order()

        track_page = TrackPage(webdriver, wait)
        track_page.check_has_order_info()

    def __make_order_common(self, webdriver: WebDriver, wait: WebDriverWait):
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

        order_confirm_page = OrderConfirmPage(webdriver, wait)

        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

