# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(120, 70, 521, 61))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.serch = QtWidgets.QLabel(self.centralwidget)
        self.serch.setGeometry(QtCore.QRect(100, 200, 81, 61))
        self.serch.setObjectName("serch")
        self.serchpage = QtWidgets.QLabel(self.centralwidget)
        self.serchpage.setGeometry(QtCore.QRect(20, 280, 151, 61))
        self.serchpage.setObjectName("serchpage")
        self.secrchprint = QtWidgets.QLineEdit(self.centralwidget)
        self.secrchprint.setGeometry(QtCore.QRect(180, 210, 421, 41))
        self.secrchprint.setObjectName("secrchprint")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(190, 293, 61, 31))
        self.spinBox.setObjectName("spinBox")
        self.serchButton = QtWidgets.QPushButton(self.centralwidget)
        self.serchButton.setGeometry(QtCore.QRect(610, 210, 113, 51))
        self.serchButton.setObjectName("serchButton")
        self.textbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(100, 360, 431, 321))
        self.textbox.setObjectName("textbox")
        self.csvpilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.csvpilebutton.setGeometry(QtCore.QRect(580, 370, 121, 41))
        self.csvpilebutton.setObjectName("csvpilebutton")
        self.textbox.raise_()
        self.title.raise_()
        self.serch.raise_()
        self.serchpage.raise_()
        self.secrchprint.raise_()
        self.spinBox.raise_()
        self.serchButton.raise_()
        self.csvpilebutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.csvpilebutton.clicked.connect(MainWindow.store)
        self.serchButton.clicked.connect(MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">검색 프로그램</span></p></body></html>"))
        self.serch.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">검색어</span></p></body></html>"))
        self.serchpage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">검색 페이지수</span></p></body></html>"))
        self.serchButton.setText(_translate("MainWindow", "검색"))
        self.csvpilebutton.setText(_translate("MainWindow", "CSV파일로저장"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

