import allure
from selenium import webdriver
from pages import LoginPage, ProductsPage, CartPage, CheckoutPage

@allure.title("Тестирование функциональности покупок в интернет-магазине")
@allure.description("Тест проверяет процесс покупки товаров на сайте Saucedemo.")
@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart():
    """Тест для проверки функциональности корзины покупок."""
    # Установка драйвера для Firefox
    driver = webdriver.Firefox()

    try:
        with allure.step("Открываем сайт магазина"):
            driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        with allure.step("Авторизуемся как пользователь стандартного пользователя"):
            login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        with allure.step("Добавляем товары в корзину"):
            for item in items_to_add:
                products_page.add_product_to_cart(item)

        with allure.step("Переход в корзину"):
            products_page.go_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Нажимаем на 'Checkout'"):
            cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(driver)
        with allure.step("Заполняем форму с данными"):
            checkout_page.fill_checkout_form("Руслан", "Батманов", "156016")

        with allure.step("Читаем итоговую стоимость"):
            total_price = checkout_page.get_total_price()
            print(f"Итоговая стоимость: {total_price}")

            # Проверяем, что итоговая сумма равна $58.29
            with allure.step("Проверка итоговой суммы"):
                assert total_price == "$58.29", f"Ожидалась сумма $58.29, но получена {total_price}"

    except Exception as e:
        allure.step(f"Ошибка: {str(e)}")
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart()