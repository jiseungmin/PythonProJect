import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS|ONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=CjwKCAjwtcCVBhA0EiwAT1fY75I7jMAFploGo1faWMWySJ1s4oUfFphmFr4wTzucjD-II_ZHSyNyhRoC3nkQAvD_BwE"
browser.get(url)

# 지정된 위치로 스크롤 내리기
# 모니터 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36", "Accept-Language": "ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "VfPpkd-EScbFb-JIbuQc UVEnyf"})

for movie in movies:
    title = movie.find("div", attrs={"class": "Epkrse"}).get_text()
    print(title)

    # 할인전 가격
    origin_price = movie.find("span", attrs={"class": "SUZt4c P8AFK"})
    if origin_price:
        origin_price = origin_price.get_text()
    else:
        print(title + " 할인 되지 않는 영화입니다.")

    # 할인 된 가격
    sale_price = movie.find(
        "span", attrs={"class": "VfPpfd VixbEe"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "Si6A0c ZD8Cqc"})["href"]

    print("제목: {}".format(title))
    print("할인전 가격 : {}".format(origin_price))
    print("할인 후 가격 : {}".format(sale_price))
    print("링크:", "https://play.google.com"+link)
    print("---------"*30)


# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html 문서로 이쁘게
