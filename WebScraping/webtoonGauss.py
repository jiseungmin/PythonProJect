import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 만화 제목 링크 가져오기
#cartoons = soup.find_all("td", attrs={"class": "title"})
#title = cartoons[0].a.get_text()
#link = cartoons[0].a.get_text()
# print(title)
#print("https://comic.naver.com/webtoon/" + link)
# for cartoon in cartoons:
#   title = cartoon.a.get_text()
#   link = "https://comic.naver.com/webtoon/" + cartoon.a["href"]
#   print(title, link)


# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    result = cartoon.find("strong").get_text()
    print(result)
    total_rates += float(result)

print("현재 평점의 합은 {}".format(result))
print("평정의 평균은 {}".format(total_rates/len(cartoons)))
