import allure

from selenium.webdriver import Firefox as WebDriver

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.landing_page import LandingPage
from pages.order_customer_page import OrderCustomerPage
from pages.order_rent_page import OrderRentPage
from pages.order_confirm_page import OrderConfirmPage
from pages.order_completed_page import OrderCompletedPage

class TestOrder:
    @allure.title('Тест подтверждения отправки нового заказа с хэдера')
    @allure.description('Переходим к созданию нового заказа через кнопку в хэдере, \
                        заполняем необходимые поля и подтверждаем отправку заказа, \
                        проверяем, что заказ получил свой ID')
    def test_order_from_header_confirm(self, webdriver: WebDriver):
        base_page = BasePage(webdriver)

        main_page = MainPage(webdriver, base_page)
        main_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver, base_page)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver)
        order_completed_page.check_has_order_id()

    @allure.title('Тест подтверждения отправки нового заказа с лендинга')
    @allure.description('Переходим к созданию нового заказа через кнопку в лендинге, \
                        заполняем необходимые поля и подтверждаем отправку заказа, \
                        проверяем, что заказ получил свой ID')
    def test_order_from_landing_confirm(self, webdriver: WebDriver):
        base_page = BasePage(webdriver)

        landing_page = LandingPage(webdriver, base_page)
        landing_page.scroll_to_button_order()
        landing_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver, base_page)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_yes()
        order_confirm_page.check_order_confirmed()

        order_completed_page = OrderCompletedPage(webdriver)
        order_completed_page.check_has_order_id()

    @allure.title('Тест неподтверждения отправки нового заказа с хэдера')
    @allure.description('Переходим к созданию нового заказа через кнопку в хэдере, \
                        заполняем необходимые поля и **не** подтверждаем отправку заказа, \
                        проверяем, что вернулись на форму заполнения информации об аренде')
    def test_order_from_header_not_confirm(self, webdriver: WebDriver):
        base_page = BasePage(webdriver)

        main_page = MainPage(webdriver, base_page)
        main_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver, base_page)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_no()
        order_confirm_page.check_order_not_confirmed()

    @allure.title('Тест неподтверждения отправки нового заказа с лендинга')
    @allure.description('Переходим к созданию нового заказа через кнопку в лендинге, \
                        заполняем необходимые поля и **не** подтверждаем отправку заказа, \
                        проверяем, что вернулись на форму заполнения информации об аренде')
    def test_order_from_landing_not_confirm(self, webdriver: WebDriver):
        base_page = BasePage(webdriver)

        landing_page = LandingPage(webdriver, base_page)
        landing_page.scroll_to_button_order()
        landing_page.click_button_order()

        order_customer_page = OrderCustomerPage(webdriver, base_page)
        order_customer_page.fill_form()

        order_rent_page = OrderRentPage(webdriver)
        order_rent_page.fill_form()

        order_confirm_page = OrderConfirmPage(webdriver)
        order_confirm_page.click_button_no()
        order_confirm_page.check_order_not_confirmed()

