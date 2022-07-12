from selenium import webdriver  # headless 크롬 gui 없이 바로 실행

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

id = browser.find_element_by_id("detected_value")
print(id.text)
browser.quit()
