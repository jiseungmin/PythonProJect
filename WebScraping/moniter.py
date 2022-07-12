import requests
from bs4 import BeautifulSoup

for i in range(1, 6):
    print("페이지 {}".format(i))
    url = "http://browse.gmarket.co.kr/search?keyword=%eb%aa%a8%eb%8b%88%ed%84%b0&k=32&p={}".format(
        i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("div", attrs={"class": "box__information"})
    for item in items:
        name = item.find("span", attrs={"class": "text__item"}).get_text()
        price = item.find(
            "strong", attrs={"class": "text text__value"}).get_text()
        deliver = item.find("span", attrs={"class": "text__tag"})
        if deliver:
            deliver = deliver.get_text()
        else:
            deliver = "무료 배송이 아님"
        print("--"*50)
        print(name, price, deliver)
        print("--"*50)
