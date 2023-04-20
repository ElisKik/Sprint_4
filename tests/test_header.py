import allure

from selenium.webdriver import Firefox as WebDriver

from data.urls import Urls
from pages.main_page import MainPage

class TestHeader:
    @allure.title('Тест перенаправления с клика на логотип Яндекса')
    @allure.description('Кликаем на логотип Яндекса, и проверяем \
                        что произошло перенаправление в любой из вкладок браузера')
    @allure.link(Urls.YANDEX_BASE, name='Ожидаемый URL, на который должно произойти перенаправление')
    def test_click_logo_yandex(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)

        main_page.click_logo_yandex()
        main_page.check_redirected_from_logo_yandex()

    @allure.title('Тест перехода с клика на логотип Яндекс.Самокат')
    @allure.description('Кликаем на логотип Яндекс.Самокат, и проверяем \
                        что произошёл переход на главную страницу \
                        тестируемого сайта, в текущей вкладке браузера')
    @allure.link(Urls.BASE, name='Ожидаемый URL, на который должен произойти переход')
    def test_click_logo_scooter(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)

        main_page.click_logo_scooter()
        main_page.check_redirected_from_logo_scooter()

    @allure.title('Тест перехода с клика в хэдере на кнопку Заказать')
    @allure.description('Кликаем на кнопку **Заказать**, и проверяем \
                        что произошёл переход на страницу начала заказа')
    @allure.link(Urls.ORDER, name='Ожидаемый URL, на который должно произойти перенаправление')
    def test_click_button_order(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)

        main_page.click_button_order()
        main_page.check_page_changed_on_button_order()

    @allure.title('Тест появления поля поиска заказа с клика на кнопку Статус заказа')
    @allure.description('Кликаем на кнопку **Статус заказа**, и проверяем \
                        что появилось поле для поиска заказа по ID')
    def test_click_button_status(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)

        main_page.click_button_status()
        main_page.check_input_appeared_on_button_status()

