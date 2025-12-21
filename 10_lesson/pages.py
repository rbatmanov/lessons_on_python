from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы авторизации.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@type='submit']")

    def login(self, username: str, password: str) -> None:
        """
        Логин пользователя на странице.

        :param username: Имя пользователя для входа (строка).
        :param password: Пароль пользователя (строка).
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class ProductsPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация главной страницы магазина.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавление товара в корзину.

        :param product_name: Название товара для добавления (строка).
        """
        item_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']/descendant::button"))
        )
        item_button.click()

    def go_to_cart(self) -> None:
        """Переход в корзину."""
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        )
        cart_button.click()

class CartPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    def proceed_to_checkout(self) -> None:
        """Переход к оформлению заказа."""
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()

class CheckoutPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение формы оформления заказа.

        :param first_name: Имя покупателя (строка).
        :param last_name: Фамилия покупателя (строка).
        :param postal_code: Почтовый индекс (строка).
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        continue_button = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Continue']")
        continue_button.click()

    def get_total_price(self) -> str:
        """
        Получение итоговой стоимости заказа.

        :return: Итоговая сумма (строка).
        """
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_info']//*[contains(text(),'Total')]/following-sibling::div"))
        )
        return total_price_element.text