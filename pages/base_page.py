import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться видимости элемента {locator}')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Проскролить к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        return element

    @allure.step('Кликнуть по элементу {locator}')
    def click_element(self, locator):
        self.wait_visible(locator)
        self.scroll_to_element(locator)
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step('Ввести текст "{text}" в поле {locator}')
    def set_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента {locator}')
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Дождаться что URL содержит "{url_part}"')
    def wait_url_contains(self, url_part):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_contains(url_part))
        return self.driver.current_url