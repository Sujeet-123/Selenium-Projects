
# from curses import KEY_ENTER
# from lib2to3.pgen2 import driver
# from optparse import Option
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome import ChromeDriverManager





from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.options import Option
# from optparse import Option



options = webdriver_ChromeOptions()





# opt = Option()
# # opt.headless = True
# opt = opt.add
# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
# driver.get("https://www.google.com/")

















s = Service("/home/zec/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")
time.sleep(2)


txt = "LinkedIn"

driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(txt)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'gNO89b').click()

time.sleep(3)

driver.find_element(By.CLASS_NAME,'iUh30.qLRx3b.tjvcx').click()
time.sleep(3)

email = "sujeet.p@zecdata.com"

driver.find_element(By.ID,'username').send_keys(email)
time.sleep(2)

password = "#123456"

driver.find_element(By.ID,'password').send_keys(password)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'btn__primary--large.from__button--floating').click()
time.sleep(8)
  

try:

    driver.find_element(By.CLASS_NAME,'search-global-typeahead__collapsed-search-button').click()
    time.sleep(2)
except:
    pass


srch = "python developer"


# id = driver.find_element(By.ID,'global-nav-typeahead')
id = driver.find_element(By.CLASS_NAME,'search-typeahead-v2.search-global-typeahead__typeahead')

id.find_element(By.TAG_NAME,'input').send_keys(srch)
time.sleep(5)

id.find_element(By.TAG_NAME,'input').send_keys(Keys.ENTER)
time.sleep(5)




show = driver.find_element(By.CLASS_NAME,'search-results__cluster-bottom-banner.artdeco-button.artdeco-button--tertiary.artdeco-button--muted')

show.find_element(By.TAG_NAME,'a').click()





class1 = driver.find_elements(By.CLASS_NAME,'reusable-search__result-container')


# class1 = driver.find_elements(By.CLASS_NAME,'rentity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light')

for i in class1:
    i.find_element(By.CLASS_NAME,'rentity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light').click()

    print("++++++++++++++++++++++++++++++=========+++++++++++++++++++++++++++")

    time.sleep(5)

















# all_filter = driver.find_element(By.CLASS_NAME,'relative.mr2')
# all_filter.find_element(By.TAG_NAME,'button').click()
# time.sleep(3)




# # 
# # driver.execute_script("window.scrollTo(0, 500)") 
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")




# easy = driver.find_elements(By.CLASS_NAME,'search-reusables__secondary-filters-filter')

# # easy = driver.find_element(By.CLASS_NAME,'artdeco-toggle.artdeco-toggle--32dp.artdeco-toggle--default.ember-view').click()

# print("============================================================")

# # n=1
# # for i in easy:
# #     n = n+1
# #     try:
# #         id1 = i.find_element(By.ID,'advanced-filter-applyWithLinkedin-true')
# #         id1.find_element(By.TAG_NAME,'label').click()
# #         print("DONE")
# #         print(n)
# #         break
# #     except:
# #         print("error")
# #         pass

# # id1 = driver.find_element(By.ID,'advanced-filter-applyWithLinkedin-true')
# b1 = driver.find_element(By.TAG_NAME,'label').click()
# print("================ Done ===================",'\n',b1)







# # esay.find_element(By.ID,'advanced-filter-applyWithLinkedin-true').click()

# # esay.find_element(By.CLASS_NAME,'search-reusables__select-input').click()
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# time.sleep(5)



# search-reusables__secondary-filters-filter

# id = advanced-filter-applyWithLinkedin-true