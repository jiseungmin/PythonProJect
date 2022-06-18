from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

driver = wb.Chrome()
url = ('https://www.youtube.com/watch?v=iEMWSHRSDzY')
driver.get(url)
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.PAGE_DOWN)
number = input()
for i in range(1,str(number)):
  body.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.5)

  soup = bs(driver.page_source, 'lxml') 
  chat = soup.find_all("div",'style-scope ytd-item-section-renderer')
print(chat)

# title_list = []
# view_list = []
  
# for i in range(len(id)):
#       title_list.append(title[i].text)
# for i in range(len(view)):     
#       view_list.append(view[i].text)

# print(title_list)
# print(view_list)