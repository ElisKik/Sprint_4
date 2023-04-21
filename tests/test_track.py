import allure

from selenium.webdriver import Firefox as WebDriver

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
    def test_get_order_status_on_completed(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)
        main_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver)
        order_completed_page.click_button_status()

        track_page = TrackPage(webdriver)
        track_page.check_has_order_info()

    @allure.title('Тест получения статуса заказа с поля поиска в хэдере')
    @allure.description('Создаём заказ, кликаем на кнопку **Статус заказа**, вводим номер заказа \
                        кликаем на кнопку поиска заказа, проверяем, что на странице присутствует блок информации о заказе')
    def test_get_order_status_from_header(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)
        main_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver)

        order_id = order_completed_page.get_order_id()

        assert order_id is not None, 'Order ID was not found on page'

        webdriver.get(Urls.BASE)

        main_page.click_button_status()
        main_page.check_input_appeared_on_button_status()

        main_page.set_order_id(order_id)
        main_page.click_button_search_order()

        track_page = TrackPage(webdriver)
        track_page.check_has_order_info()

