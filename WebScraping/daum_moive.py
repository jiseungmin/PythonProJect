import requests
from bs4 import BeautifulSoup

for i in range(2015, 2021):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    imageed = soup.find(
        "ol", attrs={"class": "type_plural list_exact movie_list"})
    images = imageed.find_all("img", attrs={"class": "thumb_img"})

    for index, image in enumerate(images):
        print(image["src"])
        image_res = requests.get(image["src"])
        image_res.raise_for_status()

        with open("movie{}_{}.jpg".format(i, index+1), "wb") as f:
            f.write(image_res.content)
        if index >= 4:
            break
