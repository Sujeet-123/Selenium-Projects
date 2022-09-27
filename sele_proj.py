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



# for d in driver.find_elements(By.CLASS_NAME,'VkpGBb'):
names = driver.find_elements(By.CLASS_NAME,'dbg0pd.eDIkBe')

for nm in names:
    ln.append(nm.text)

print(ln)

# divs = driver.find_elements(By.CLASS_NAME,'VkpGBb')

# for ah in divs:

#     links = driver.find_elements(By.TAG_NAME,"a")


# for herfs in links:
#     hrf = driver.find_elements(By.TAG_NAME,'herf')

#     ln.append(hrf)

# print(ln)


    # links = driver.find_elements(By.TAG_NAME,'a


# for hrefs in links:
#     hrefs.get_

    # aa = driver.find_element(By.TAG_NAME,'a')

# print(ln)
#     d = driver.find_elements(By.LINK_TEXT,'data-url')
#     la.append(d)

# print(la)
# for hd in aa
# hrf = driver.find_elements(By.TAG_NAME,'href')

# for hh in hrf:
#     ln.append(hh.text)

# print(ln)
  
   

















# web = driver.find_elements(By.CLASS_NAME,'yYlJEf.Q7PwXb.L48Cpd')

# for nm in web:
#     # ht = nm.get_attribute("href")
#     ca = nm.get_attribute("")
#     print(ca)


# add = driver.find_element_by_css_selector(By.CLASS_NAME,'yYlJEf.Q7PwXb.L48Cpd')

# for ca in add:
#     ht = ca.get_attribute("href")
    
#     la.append(ht.text)




# print(ln)



    # web = driver.find_elements(By.CLASS_NAME,'wLAgVc')

    # add = driver.find_elements(By.CLASS_NAME,'UbRuwe')
        

    # ln.append(name.text)
    # lw.append(web.text)
    # la.append(add.text)

# for i in name:
#     ln.append(i.text)


# for i in web:
#     lw.append(i.text)


# for i in add:
#     la.append(i.text)



# data ={
#     "Coaching Name": ln,
#     "Coaching Website":lw,
#     "Coaching Address":la,
# }


# df = pd.DataFrame.from_dict(data, orient='index')
# df = df.transpose()

# df.to_csv("project1.csv")


# search_coaching = driver.find_element(By.CLASS_NAME,'OSrXXb')
# print(search_coaching.text)

# list_name = []
# for coaching in search_coaching:
#     list_name.append(coaching.text)
# print(list_name)

# //*[@id="tsuid_9"]/div/div[2]/div/a/div/div/div[1]