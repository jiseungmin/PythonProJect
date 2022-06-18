from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

driver = wb.Chrome()

url = ('https://www.youtube.com/watch?v=iEMWSHRSDzY')
driver.get(url)

body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.PAGE_DOWN)

for i in range(1,10):
  body.send_keys(Keys.PAGE_DOWN)
  time.sleep(3.0)
  soup = bs(driver.page_source, 'lxml') 
  youtube_id = soup.select('h3.style-scope.ytd-comment-renderer')
  for i in youtube_id:
    print(i.text.strip())

# youtube_id_list = []
  
# for i in range(len(youtube_id)):
#       youtube_id_list.append(youtube_id[i].text)   

# print(youtube_id_list)
