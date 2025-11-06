from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

# Установка драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открыть браузер Firefox
    driver.get("http://the-internet.herokuapp.com/login")
    
    # Подождём, пока страница полностью загрузится
    time.sleep(5)

    # Найти поле ввода для username и ввести значение 'tomsmith'
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Найти поле ввода для password и ввести значение 'SuperSecretPassword!'
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    
    # Найти кнопку 'Login' и нажать на нее
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Подождём, пока страница обновится
    time.sleep(5)

    # Выведем текст с зеленой плашки в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text)

finally:
    # Закрыть браузер
    driver.quit()