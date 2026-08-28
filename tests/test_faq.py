import allure
import pytest
from data import FAQ_ITEMS
from pages.main_page import MainPage


@allure.epic('Яндекс.Самокат')
@allure.feature('Раздел «Вопросы о важном»')
class TestFaq:

    @allure.title('Вопрос №{index}: «{question}» раскрывается верным ответом')
    @pytest.mark.parametrize('index, question, expected_answer', FAQ_ITEMS)
    def test_faq_answer_matches_questions(self, driver, index, question, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        assert main_page.get_faq_question_text(index) == question

        main_page.click_faq_question(index)

        assert main_page.get_faq_answer_text(index) == expected_answer