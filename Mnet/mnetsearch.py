from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

driver = wb.Chrome()

url = ('https://www.youtube.com/results?search_query=mnet')
driver.get(url)

body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.PAGE_DOWN)

for i in range(1,51):
  body.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.5)

  soup = bs(driver.page_source, 'lxml') 
  title = soup.select('a#video-title')
for i in title:
    print(i.text.strip())
    view = soup.select('span.style-scope.ytd-video-meta-block') 

title_list = []
view_list = []
  
for i in range(len(title)):
      title_list.append(title[i].text.strip())   
      view_list.append(view[i].text.strip())

print(title_list)
print(view_list)

      








