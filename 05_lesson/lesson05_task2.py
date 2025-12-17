from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Установка драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открыть браузер Google Chrome
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Подождём, пока страница полностью загрузится
    time.sleep(5)

    # Кликнуть на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")  # Используем CSS-селектор для кнопки
    button.click()

    # Подождём, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрыть браузер
    driver.quit()