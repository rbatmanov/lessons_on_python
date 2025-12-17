from selenium import webdriver
from pages.CalculatorPage import CalculatorPage  

def test_calculator():
    # Создаем экземпляр браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открываем страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Создаем объект страницы
        calculator_page = CalculatorPage(driver)

        # Вводим значение в поле задержки
        calculator_page.enter_delay("45")

        # Нажимаем на кнопки 7, +, 8 и =
        calculator_page.click_button_7()
        calculator_page.click_button_plus()
        calculator_page.click_button_8()
        calculator_page.click_button_equals()

        # Получаем и проверяем результат
        result_text = calculator_page.get_result()
        print("Результат:", result_text)  # Результат проверки текста

        # Ассерт проверка
        assert result_text == "15", f"Expected result to be 15, but got {result_text}"

    except Exception as e:
        print("Ошибка:", str(e))
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_calculator()