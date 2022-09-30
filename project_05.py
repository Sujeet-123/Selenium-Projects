
#shoes data from flipkart

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("/home/zec/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

txt = "flipkart"

# driver.find_element(By.ID,'input').send_keys(txt)
driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(txt)
time.sleep(2)
driver.find_element(By.CLASS_NAME,'gNO89b').click()
time.sleep(4)
driver.find_element(By.CLASS_NAME,'TbwUpd.NJjxre').click()
time.sleep(4)
driver.find_element(By.CLASS_NAME,'_2KpZ6l._2doB4z').click()
time.sleep(4)

sh = "Shoes men"
driver.find_element(By.CLASS_NAME,'_3704LK').send_keys(sh)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'L0Z3Pu').click()
time.sleep(4)


names = []
prices = []
ratings = []


divs = driver.find_elements(By.CLASS_NAME,'_1xHGtK._373qXS')

for i in divs:
    i.click()
    time.sleep(3)

  
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    



    name = driver.find_element(By.CLASS_NAME,'B_NuCI').text
    # time.sleep(2)
    names.append(name)
    print(name)



    price = driver.find_element(By.CLASS_NAME,'_30jeq3._16Jk6d').text
    print(price)
    prices.append(price)
    time.sleep(2)

    try:

        rating = driver.find_element(By.CLASS_NAME,'_3LWZlK._3uSWvT').text
        ratings.append(rating)
        print(rating)
        
    except:
        ratings.append("NaN")
        print("NaN")

 


    
    driver.close()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)



data = {
    'Shoes Name' : names,
    'Price' : prices,
    'Rating' : ratings
}

df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

df.to_csv("project_05_shoes.csv")

driver.close()