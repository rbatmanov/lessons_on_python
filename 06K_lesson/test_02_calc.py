from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    # Создаем экземпляр браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открываем страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Вводим значение в поле ввода
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        input_field.clear()
        input_field.send_keys("45")

        # Нажимаем на кнопки 7, +, 8 и =
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        ).click()

        # Проверяем результат
        waiter = WebDriverWait(driver, 60)
        # Используем правильный локатор для ожидания
        result = waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
        )

        print("Результат:", result)  # Результат проверки текста

        # Получаем текст результата
        result_text = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        
        # Ассерт проверка
        assert result_text == "15", f"Expected result to be 15, but got {result_text}"

    except Exception as e:
        print("Ошибка:", str(e))
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_calculator()