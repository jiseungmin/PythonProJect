import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")

# 네이버 이동
browser.get("https://www.naver.com/")

# 로그인 이동
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id pw 입력
browser.find_element_by_id("id").send_keys("naver id")
browser.find_element_by_id("pw").send_keys("naver pw")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close() # 현재 탭만 종료
time.sleep(10)
browser.quit()
