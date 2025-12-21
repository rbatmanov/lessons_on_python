from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр WebDriver, используемый для управления браузером.
        """
        self.driver = driver

    def enter_delay(self, delay: str) -> None:
        """
        Ввод значения в поле задержки.

        :param delay: Значение задержки, которое нужно ввести (строка).
        """
        delay_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button_7(self) -> None:
        """Нажимает кнопку '7'."""
        self.driver.find_element(By.CSS_SELECTOR, "button[value='7']").click()

    def click_button_8(self) -> None:
        """Нажимает кнопку '8'."""
        self.driver.find_element(By.CSS_SELECTOR, "button[value='8']").click()

    def click_button_plus(self) -> None:
        """Нажимает кнопку '+'."""
        self.driver.find_element(By.CSS_SELECTOR, "button[value='+']").click()

    def click_button_equals(self) -> None:
        """Нажимает кнопку '='."""
        self.driver.find_element(By.CSS_SELECTOR, "button[value='=']").click()

    def get_result(self) -> str:
        """
        Получает текст результата.

        :return: Результат вычисления (строка).
        """
        return self.driver.find_element(By.CSS_SELECTOR, "#result").text