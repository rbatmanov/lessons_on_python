from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс для страницы авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@type='submit']")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

# Класс для главной страницы магазина
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        item_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']/descendant::button"))
        )
        item_button.click()

    def go_to_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        )
        cart_button.click()

# Класс для страницы корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()

# Класс для страницы оформления заказа
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        continue_button = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Continue']")
        continue_button.click()

    def get_total_price(self):
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_info']//*[contains(text(),'Total')]/following-sibling::div"))
        )
        return total_price_element.text

# Тестовый сценарий
def test_shopping_cart():
    # Установка драйвера для Firefox
    driver = webdriver.Firefox()  # Убедитесь, что geckodriver установлен и доступен в PATH.

    try:
        # Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизуемся как пользователь standard_user
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Добавляем товары в корзину
        products_page = ProductsPage(driver)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        
        for item in items_to_add:
            products_page.add_product_to_cart(item)

        # Переход в корзину
        products_page.go_to_cart()

        # Нажимаем Checkout
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # Заполняем форму с данными
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Руслан", "Батманов", "156016")

        # Читаем итоговую стоимость
        total_price = checkout_page.get_total_price()
        print(f"Итоговая стоимость: {total_price}")

        # Проверяем, что итоговая сумма равна $58.29
        assert total_price == "$58.29", f"Ожидалась сумма $58.29, но получена {total_price}"

    except Exception as e:
        print("Ошибка:", str(e))
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart()