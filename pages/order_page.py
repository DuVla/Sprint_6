import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_INPUT = (By.XPATH,"//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    RENT_HEADER = (By.XPATH, "//div[text()='Про аренду']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')
    COLOR_GRAY_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_MODAL = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ')]")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")


    @staticmethod
    def station_option(station_name):
        return By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{station_name}']"

    @staticmethod
    def rent_period_option(period):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"

    @allure.step('Заполнить первый шаг формы')
    def fill_first_step(self, data):
        self.set_text(self.FIRST_NAME_INPUT, data['first_name'])
        self.set_text(self.LAST_NAME_INPUT, data['last_name'])
        self.set_text(self.ADDRESS_INPUT, data['address'])
        self.set_text(self.STATION_INPUT, data['station'])
        self.click_element(self.station_option(data['station']))
        self.set_text(self.PHONE_INPUT, data['phone'])
        self.click_element(self.NEXT_BUTTON)

    @allure.step('Проверить что открылся второй шаг формы')
    def is_second_step_opened(self):
        return self.wait_visible(self.RENT_HEADER).is_displayed()

    @allure.step('Заполнить второй шаг формы')
    def fill_second_step(self, data):
        self.set_text(self.DATE_INPUT, data['date'])
        self.click_element(self.RENT_HEADER)
        self.click_element(self.RENT_PERIOD_DROPDOWN)
        self.click_element(self.rent_period_option(data['rent_period']))
        self.select_color(data['color'])
        if data['comment']:
            self.set_text(self.COMMENT_INPUT, data['comment'])
        self.click_element(self.ORDER_BUTTON)

    @allure.step('Выбрать цвет самоката')
    def select_color(self, color):
        if color == 'black':
            self.click_element(self.COLOR_BLACK_CHECKBOX)
        elif color == 'grey':
            self.click_element(self.COLOR_GRAY_CHECKBOX)
        else:
            raise ValueError(f'Неизвестный цвет: {color}')

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        self.wait_visible(self.CONFIRM_MODAL)
        self.click_element(self.CONFIRM_YES_BUTTON)

    @allure.step('Получить текст модального окна об успешном заказе')
    def get_success_modal_text(self):
        return self.get_text(self.SUCCESS_MODAL)
