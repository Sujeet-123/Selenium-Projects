
# Camera Amazone

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time


s = Service("/home/zec/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

txt = "Amazone"

driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(txt)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'gNO89b').click()

time.sleep(3)

driver.find_element(By.CLASS_NAME,'iUh30.tjvcx').click()
time.sleep(3)

camera = "Canon camera"

driver.find_element(By.ID,'twotabsearchtextbox').send_keys(camera)
time.sleep(2)

driver.find_element(By.ID,'nav-search-submit-button').click()
time.sleep(4)



image_li = []
name_li = []
price_li=[]
rating_li = []





divs = driver.find_elements(By.CLASS_NAME,'sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.s-list-col-right')




for i in divs:

    try:

        nm = i.find_element(By.CLASS_NAME,'a-size-medium.a-color-base.a-text-normal').text
        name_li.append(nm)

        # print(nm)
    except:
        name_li.append('NaN')
        # print("NaN")

 
    price = i.find_element(By.CLASS_NAME,'a-price-whole').text
    # print(price)
    price_li.append(price)
    try:

        rating = i.find_element(By.CLASS_NAME,'a-size-base.s-underline-text').text
        rating_li.append(rating)
    except:
        rating_li.append('NaN')

imgs = driver.find_elements(By.CLASS_NAME,'a-section.aok-relative.s-image-fixed-height')
   
for i in imgs:
    
    ch = i.find_element(By.TAG_NAME,'img')

    mg =ch.get_attribute("src")

    image_li.append(mg)

    

# print(name_li)
# print(price_li)
# print(rating_li)
# print(image_li)


dict = {
    'Camera name' : name_li,
    'Price' : price_li,
    'Number of People by Rating' : rating_li,
    'Images' : image_li  
}

df = pd.DataFrame.from_dict(dict, orient='index')
df = df.transpose()

df.to_csv("project_06_camera.csv")