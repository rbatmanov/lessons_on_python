from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains

def test_form_submission():
    # Установка драйвера для Edge
    edge_driver_path = r"E:\Скайпро\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    try:
        # Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        wait = WebDriverWait(driver, 10)

        # Заполняем форму с использованием ожидания
        firstname_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "first-name"))
        )
        firstname_field.send_keys("Иван")

        lastname_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "last-name"))
        )
        lastname_field.send_keys("Петров")

        address_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "address"))
        )
        address_field.send_keys("Ленина, 55-3")

        email_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "e-mail"))
        )
        email_field.send_keys("test@skypro.com")

        phone_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "phone"))
        )
        phone_field.send_keys("+7985899998787")

        zip_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "zip-code"))
        )
        zip_field.send_keys("")   # Оставляем Zip code пустым

        city_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "city"))
        )
        city_field.send_keys("Москва")

        country_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "country"))
        )
        country_field.send_keys("Россия")

        job_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "job-position"))
        )
        job_field.send_keys("QA")

        company_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "company"))
        )
        company_field.send_keys("SkyPro")

        # Нажимаем кнопку Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        try:
            submit_button.click()

        except:

            driver.execute_script("arguments[0].click();", submit_button)


       # Ожидаем, пока форма будет обработана и поле Zip code будет подсвечено красным
        #WebDriverWait(driver, 30).until(
           # EC.presence_of_element_located((By.NAME, "zip-code"))
        #)

        # Проверяем, что поле Zip code подсвечено красным
        zip_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "zip-code"))
        )
        assert "red" in zip_code_field.get_attribute("style"), "Zip code field should be highlighted in red."
        
        # Проверяем остальные поля на наличие зеленой подсветки
        fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        for field_name in fields_to_check:
            field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, field_name))
            )
            assert "green" in field.get_attribute("style"), f"{field_name} should be highlighted in green."


    except AssertionError as ae:
        print("Ошибка утверждения:", str(ae))
    except Exception as e:
        print("Ошибка:", str(e))
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_form_submission()