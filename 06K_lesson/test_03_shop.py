from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_shopping_cart():
    # Установка драйвера для Firefox
    driver = webdriver.Firefox()  # Убедитесь, что geckodriver установлен и доступен в PATH.

    try:
        # Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизуемся как пользователь standard_user
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce" + Keys.RETURN)

        # Добавляем товары в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item in items_to_add:
            item_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']/descendant::button"))
            )
            item_button.click()

        # Переход в корзину
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        )
        cart_button.click()

        # Нажимаем Checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()

        # Заполняем форму с данными
        first_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")
        
        first_name.send_keys("Руслан")
        last_name.send_keys("Батманов")
        postal_code.send_keys("156016")
        
        # Нажимаем кнопку Continue
        continue_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Continue']")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        total_price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_info']//*[contains(text(),'Total')]/following-sibling::div"))
        )
        
        # Читаем итоговую стоимость
        total_price = total_price_element.text
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
