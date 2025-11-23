
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium import webdriver
from time import sleep

try:
    # Открыть браузер Google Chrome
    driver.get("http://uitestingplayground.com/classattr")
    
    # Подождём, пока страница полностью загрузится
    sleep(5)
    
    # Кликнуть на синюю кнопку
    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    # Подождём, чтобы увидеть результат
    sleep(5)

finally:
    # Закрыть браузер
    driver.quit()