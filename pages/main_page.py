import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")

    @staticmethod
    def faq_question(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def faq_answer(index):
        return By.ID, f'accordion__panel-{index}'

    @allure.step('Закрыть баннер с куки')
    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step('Раскрыть вопрос №{index} в разделе FAQ')
    def click_faq_question(self, index):
        self.click_element(self.faq_question(index))

    @allure.step('Получить текст ответа на вопрос №{index}')
    def get_faq_answer_text(self, index):
        return self.get_text(self.faq_answer(index))

    @allure.step('Получить текст вопроса №{index}')
    def get_faq_question_text(self, index):
        return self.get_text(self.faq_question(index))

    @allure.step('Нажать кнопку Заказать в шапке страницы')
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step('Нажать кнопку Заказать внизу страницы')
    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажать кнопку Заказать (точка входа: {position})')
    def click_order_button(self, position):
        if position == 'top':
            self.click_order_button_top()
        elif position == 'bottom':
            self.click_order_button_bottom()
        else:
            raise ValueError(f'Неизвестная точка входа: {position}')

    @allure.step('Кликнуть по логотипу САМОКАТА')
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
