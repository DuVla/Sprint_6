import allure
from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.epic('Яндекс.Самокат')
@allure.feature('Навигация по логотипам')
class TestLogoNavigation:

    @allure.title('Клик по логотипу «Самоката» ведёт на главную страницу')
    def test_scooter_logo_leads_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_order_button_top()
        order_page.wait_visible(order_page.FIRST_NAME_INPUT)

        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title('Клик по логотипу Яндекса открывает Дзен в новом окне')
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)

        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert 'dzen.ru' in main_page.wait_url_contains('dzen.ru')