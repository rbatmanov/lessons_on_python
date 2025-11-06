from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

# Установка драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открыть браузер Firefox
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Подождём, пока страница полностью загрузится
    time.sleep(5)

    # Найти поле ввода и ввести текст "Sky"
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")  # Находим поле ввода типа 'number'
    input_field.send_keys("Sky")  # Вводим текст "Sky"
    
    # Подождем, чтобы увидеть введенный текст
    time.sleep(5)
    
    # Очистить поле
    input_field.clear()  # Очищаем поле

    # Ввести текст "Pro"
    input_field.send_keys("Pro")  # Вводим текст "Pro"
    
    # Подождем, чтобы увидеть введенный текст
    time.sleep(5)

finally:
    # Закрыть браузер
    driver.quit()