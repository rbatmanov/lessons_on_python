from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(30)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

images = driver.find_elements(By.TAG_NAME, "img")
while len(images) < 4:
    images = driver.find_elements(By.TAG_NAME, "img")

third_image_src = images[3].get_attribute("src")
print(third_image_src)

driver.quit()