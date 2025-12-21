from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome

from selenium import webdriver

# Пример для Google Chrome
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()