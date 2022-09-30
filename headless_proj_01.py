

from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()

options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get('https://www.google.com')
time.sleep(5)

driver.find_element(By.NAME,"q").send_keys("LinkedIn")

driver.save_screenshot("/screenshort/image2.png")
time.sleep(5)
print("Screensrt clicked")
image = Image.open("image2.png")
time.sleep(5)


image.show()

print("+++++++++++++++++++++++")

driver.close()
