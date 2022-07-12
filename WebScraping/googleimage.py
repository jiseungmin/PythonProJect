import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
Url = "https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES-gEJZP1VpXEjcNQa7gELELCMpwgaOgo4CAQSFI8VjjOsMa8ixQT4HtkvpDyzKdsGGhoP_1JRKiZtuzo4iUJmcTUhmCcY4SLyZgfHzhSAFMAQMCxCOrv4IGgoKCAgBEgQz_1MmQDAsQne3BCRqOAQoYCgVzb2xpZNqliPYDCwoJL2EvM21nMWNtCiMKEHN5bnRoZXRpYyBydWJiZXLapYj2AwsKCS9tLzA1czc3MQoYCgZjbHV0Y2japYj2AwoKCC9tLzAxeGY1ChgKA3JpbdqliPYDDQoLL2cvMTIxZzdmNzYKGQoHbWFjaGluZdqliPYDCgoIL20vMGRrdzUM&sxsrf=ALiCzsYOLh8YvhxT4EZPCmQA59ldh7CCug:1656586348185&q=michelin+x+tweel+tires&tbm=isch&ved=2ahUKEwjnxsqGgdX4AhVQl1YBHS9VBxwQjJkEegQIHRAC&biw=1440&bih=821&dpr=2"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
res = requests.get(Url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,  "lxml")

list_ = []
imaged = soup.select(
    "img", attrs={"class": "rg_i Q4LuWd"})
for i in imaged:
    try:
        list_.append(i.attrs["src"])
    except KeyError:
        list_.append(i.attrs["data-src"])
print(list_)

i = 1
for thumbnail in list_:
    urlretrieve(
        thumbnail, f'/Users/jiseungmin/Desktop/PythonProJect/img_homwork/{i}.png')
    i += 1

    with open("tire wheel{}.PNG".format(index+1), "wb") as f:
        f.write(image_res.content)
