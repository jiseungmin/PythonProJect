from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from WebScraping.beautifulsoup import BeautifulSoup as bs
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mnet.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.listbutton.clicked.connect(self.listbuttonFuntion)

    def listbuttonFuntion(self) :
      driver = wb.Chrome()
      url = ('https://www.youtube.com/watch?v=iEMWSHRSDzY')
      driver.get(url)
      body = driver.find_element_by_tag_name('body')
      body.send_keys(Keys.PAGE_DOWN)
      number = self.spinBox.value()
      for i in range(1,number):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        soup = bs(driver.page_source, 'lxml')
        chat = soup.find_all("div",'style-scope ytd-item-section-renderer')
        print(chat) 



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()