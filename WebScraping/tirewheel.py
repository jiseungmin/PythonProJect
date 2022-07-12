import requests
from bs4 import BeautifulSoup
Url = "https://www.istockphoto.com/kr/search/search-by-asset?assetid=469941138&assettype=image"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
res = requests.get(Url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,  "lxml")

imaged = soup.find_all(
    "img", attrs={"class": "MosaicAsset-module__thumb___klD9E"})
for index, image in enumerate(imaged):
    image_res = requests.get(image["src"])
    image_res.raise_for_status()

    with open("tire wheel{}.PNG".format(index+1), "wb") as f:
        f.write(image_res.content)