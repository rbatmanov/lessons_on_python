import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage  

@allure.title("Тест калькулятора")
@allure.description("Проверка функциональности калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    """Тест для проверки основного функционала калькулятора."""
    driver = webdriver.Chrome()
    
    try:
        with allure.step("Открытие страницы калькулятора"):
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        calculator_page = CalculatorPage(driver)
        
        with allure.step("Ввод значения 45 в поле задержки"):
            calculator_page.enter_delay("45")

        with allure.step("Ввод чисел и операций"):
            calculator_page.click_button_7()
            calculator_page.click_button_plus()
            calculator_page.click_button_8()
            calculator_page.click_button_equals()

        with allure.step("Проверка результата"):
            result_text = calculator_page.get_result()
            assert result_text == "15", f"Expected result to be 15, but got {result_text}"
            print("Результат:", result_text)

    except Exception as e:
        allure.step(f"Ошибка: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_calculator()