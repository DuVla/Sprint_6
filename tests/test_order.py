from data import OrderData
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestOrder:

    def test_first_step_filled_opens_second_step(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_order_button_top()
        order_page.fill_first_step(OrderData.FIRST)

        assert order_page.is_second_step_opened()

    def test_order_created_successfully(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_order_button_top()
        order_page.fill_first_step(OrderData.FIRST)
        order_page.fill_second_step(OrderData.FIRST)
        order_page.confirm_order()

        assert 'Заказ оформлен' in order_page.get_success_modal_text()
