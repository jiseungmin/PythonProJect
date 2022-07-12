import requests
from bs4 import BeautifulSoup
import re


def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    print("-"*100)
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&oquery=%EC%95%84%ED%8C%8C%ED%8A%B8+%EC%8B%9C%EC%84%B8&tqi=hrbNVsp0J1ZssboXqpKssssssQ8-377857"
    soup = create_soup(url)
    # 어제 와 비교
    totemp = soup.find("p", attrs={"class": "summary"}).get_text()

    # 현재기온 최저기온 최고기온
    temp = soup.find("div", attrs={"class": "temperature_text"}).get_text()
    l_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
    h_temp = soup.find("span", attrs={"class": "highest"}).get_text()

    # 오전 강수확률 / 오후 강수확률
    rain = soup.find_all("span", attrs={"class": "rainfall"})
    m_rain = rain[0].get_text()
    a_rain = rain[1].get_text()

    # 체감 습도 바람
    summary = soup.find("dl", attrs={"class": "summary_list"})
    cha = summary.find_all("dd")[0].get_text()
    suem = summary.find_all("dd")[1].get_text()
    winter = summary.find_all("dd")[2].get_text()

    print(totemp)
    print("현재:{}, 최저:{}, 최고:{}".format(temp, l_temp, h_temp))
    print("오전 {}, 오후{}".format(m_rain, a_rain))
    print("체감:{} 습기:{} 바람:{}".format(cha, suem, winter))
    print("-"*100)


def headline_news():
    print("[스포츠 헤드라인 뉴스]")
    url = "https://sports.news.naver.com/index"
    soup = create_soup(url)
    news_list = soup.find(
        "ul", attrs={"class": "today_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find(
            "strong", attrs={"class": "title"}).get_text().strip()
        link = "https://sports.news.naver.com" + news.find("a")["href"]
        print("{}: {}".format(index+1, title))
        print("링크 : {}".format(link))
    print("-"*100)


def it_news():
    print("[IT뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    news_list = soup.find(
        "div", attrs={"class": "_persist"}).find_all("div", attrs={"class": "cluster_group _cluster_content"}, limit=3)  # 3개 까지만
    for index, news in enumerate(news_list):
        title = news.find(
            "a", attrs={"class": "cluster_text_headline nclicks(cls_sci.clsart)"}).get_text()
        link = "https://news.naver.com"+news.find("a")["href"]
        print("{}: {}".format(index+1, title))
        print("링크 : {}".format(link))
    print("-"*100)


def english():
    print("[영어회화 3문장]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    english_list = soup.find_all(
        "div", attrs={"id": re.compile("^conv_kor_t")})
    print("[영어지문]")
    # index 기준 맨 마지막까지 (len(english_list)//2:)
    for sentence in english_list[len(english_list)//2:]:
        print(sentence.get_text().strip())
    print("-"*100)
    print("[한글 해석]")
    for sentence in english_list[:len(english_list)//2]:
        print(sentence.get_text().strip())
    print("-"*100)


if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 가져오기
    headline_news()  # 헤드라인 뉴스 정보 가져오기
    it_news()
    english()
