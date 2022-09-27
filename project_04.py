
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
lp = []
la = []

# end = driver.find_element

try:
    while True:

        divs = driver.find_elements(By.CLASS_NAME,'VkpGBb')

        for i in divs:

            x = i.find_element(By.CLASS_NAME,'dbg0pd.eDIkBe').click()
            time.sleep(5)

            
            name = driver.find_element(By.CLASS_NAME,'qrShPb.kno-ecr-pt.PZPZlf.q8U8x.PPT5v').text

            ln.append(name)


            try:
                add = driver.find_element(By.CLASS_NAME,'LrzXr').text
                
                la.append(add)
            except:
                la.append('NaN')


            try:
                phone = driver.find_element(By.CLASS_NAME,'LrzXr.zdqRlf.kno-fv')

                spn= phone.find_element(By.TAG_NAME,'a').text
                lp.append(spn)

            except:
                lp.append('NaN')

        elm = driver.find_element(By.LINK_TEXT,'Next')
        try:
            if elm:

                elm.click()
                time.sleep(6)
        except:
            break
        # print('==============================================================')
             
      
except:
    print('Job is done')



data ={
    "Coaching Name": ln,
    "Coaching Phone_Number":lp,
    "Coching Address": la
}


df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

df.to_csv("pro4.csv")

driver.close()




