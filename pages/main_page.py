from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    @staticmethod
    def faq_question(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def faq_answer(index):
        return By.ID, f'accordion__panel-{index}'

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_faq_question(self, index):
        self.click_element(self.faq_question(index))

    def get_faq_answer_text(self, index):
        return self.get_text(self.faq_answer(index))

    def get_faq_question_text(self, index):
        return self.get_text(self.faq_question(index))

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)