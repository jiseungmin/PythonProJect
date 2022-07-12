from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 도착지 설정 김포에서 제주
browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()

time.sleep(1)
browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()

browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()

# 출발 날짜 클릭
browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

time.sleep(1)

# 가는 날짜 클릭 format(3,4,4)
# tbody 오른쪽 tr[번호] 그리고 td[번호]가 있는데 여기가 1달치 로우 랑 컬럼으로 각각의 날짜 위치
# table 왼쪽 div[번호] 부분이있는데 2가 이번달 3이 다음달처럼 되어있어
browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button".format(2, 4, 4)).click()
time.sleep(1)
browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button".format(3, 4, 4)).click()

browser.find_element_by_xpath(
    "//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

# try:
#     elem = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located(
#         (By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/button")))
time.sleep(15)
print(browser.find_element_by_class_name(
    "domestic_num__2roTW").text)
# finally:
#     browser.quit()
