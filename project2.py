
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


s = Service("/home/zec/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)


driver.get("https://www.google.com/")


x = 'programming coaching in indore'
driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(x)
time.sleep(3)

driver.find_element(By.CLASS_NAME,'gNO89b').click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,'wUrVib.OSrXXb').click()
time.sleep(3)


ln = []
lw = []
la = []


divs = driver.find_elements(By.CLASS_NAME,'VkpGBb')

url = "https://www.google.com"

for i in divs:

    title=i.find_element(By.CLASS_NAME,'dbg0pd.eDIkBe').text

    ankr = i.find_elements(By.TAG_NAME,'a')
    
    hrf=ankr[1].get_attribute("href")

    ln.append(title)
    lw.append(hrf)

    try:


        add=ankr[2].get_attribute('data-url')
    
        la.append( url + add)

    except:
        la.append(0)



data ={
    "Company Name": ln,
    "Company Website":lw,
    "Company Add": la,
}




df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

df.to_csv("project2.csv")




driver.close()


