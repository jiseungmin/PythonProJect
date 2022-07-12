import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
print(soup.title.get_text())
print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)  # a element 의 속성 출력
print(soup.a["href"])  # a element 의 href 속성  "값" 정보를 출력

# Class=Notn_upload 인 a element를 찾아줘
print(soup.find("a", attrs={"class": "Notn_upload"}))

# Class=Notn_upload 인 어떤 element를 찾아줘
print(soup.find(attrs={"class": "Notn_upload"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())

# 다음 자식태그 찾기
# print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# 이전 부모 태크 찾기
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)

# 태그를 이용한 자식태그 찾기
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

# 태그를 이용한 부모태크 찾기
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

# 간편하게 모두 찾기
print(rank1.find_next_siblings("li"))

# 텍스트를 이용한 찾기
webtoon = soup.find("a", text="독립일기-시즌2 74화 무선 이어폰 적응기")
print(webtoon)
