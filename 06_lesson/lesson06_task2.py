from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(25)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

button_text = button.text
print(button_text)

driver.quit()