from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        return element

    def click_element(self, locator):
        self.wait_visible(locator)
        self.scroll_to_element(locator)
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def set_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.invisibility_of_element_located(locator))