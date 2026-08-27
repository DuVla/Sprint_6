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

    @staticmethod
    def station_option(station_name):
        return By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{station_name}']"

    def fill_first_step(self, data):
        self.set_text(self.FIRST_NAME_INPUT, data['first_name'])
        self.set_text(self.LAST_NAME_INPUT, data['last_name'])
        self.set_text(self.ADDRESS_INPUT, data['address'])
        self.set_text(self.STATION_INPUT, data['station'])
        self.click_element(self.station_option(data['station']))
        self.set_text(self.PHONE_INPUT, data['phone'])
        self.click_element(self.NEXT_BUTTON)

    def is_second_step_opened(self):
        return self.wait_visible(self.RENT_HEADER).is_displayed()