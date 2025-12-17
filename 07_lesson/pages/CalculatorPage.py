from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.CSS_SELECTOR, 'div.screen')

    def enter_delay(self, delay):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        input_field.clear()
        input_field.send_keys(delay)

    def click_button_7(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        ).click()

    def click_button_plus(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()

    def click_button_8(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        ).click()

    def click_button_equals(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()

    def get_result(self):
        waiter = WebDriverWait(self.driver, 60)
        result = waiter.until(
            EC.text_to_be_present_in_element(self.result_display, '15')
        )
        return self.driver.find_element(*self.result_display).text

