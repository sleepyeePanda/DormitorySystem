# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 530, 300))
        self.frame.setStyleSheet("background:url(:/img/resources/bg.jpg)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_5.setGeometry(QtCore.QRect(60, 120, 381, 131))
        self.stackedWidget_5.setStyleSheet("background:transparent")
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.frame_5 = QtWidgets.QFrame(self.page_15)
        self.frame_5.setGeometry(QtCore.QRect(190, 10, 151, 111))
        self.frame_5.setStyleSheet("background:rgba(5,5,15,100);\n"
"border-radius : 5px")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.weatherVal = QtWidgets.QLabel(self.frame_5)
        self.weatherVal.setGeometry(QtCore.QRect(90, 35, 51, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(14)
        self.weatherVal.setFont(font)
        self.weatherVal.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.weatherVal.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherVal.setObjectName("weatherVal")
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(10, 3, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.label_18.setObjectName("label_18")
        self.stackedWeather = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWeather.setGeometry(QtCore.QRect(10, 35, 71, 81))
        self.stackedWeather.setStyleSheet("background:transparent;")
        self.stackedWeather.setObjectName("stackedWeather")
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.graphicsView_14 = QtWidgets.QGraphicsView(self.page_16)
        self.graphicsView_14.setGeometry(QtCore.QRect(0, 0, 63, 67))
        self.graphicsView_14.setStyleSheet("background:url(:/img/resources/weather/day.png);\n"
"border:transparent;\n"
"")
        self.graphicsView_14.setObjectName("graphicsView_14")
        self.stackedWeather.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.graphicsView_15 = QtWidgets.QGraphicsView(self.page_17)
        self.graphicsView_15.setGeometry(QtCore.QRect(5, 5, 63, 56))
        self.graphicsView_15.setStyleSheet("background:url(:/img/resources/weather/night.png);\n"
"border:transparent")
        self.graphicsView_15.setObjectName("graphicsView_15")
        self.stackedWeather.addWidget(self.page_17)
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setObjectName("page_18")
        self.graphicsView_16 = QtWidgets.QGraphicsView(self.page_18)
        self.graphicsView_16.setGeometry(QtCore.QRect(0, 10, 63, 47))
        self.graphicsView_16.setStyleSheet("background:url(:/img/resources/weather/cloudy.png);\n"
"border:transparent")
        self.graphicsView_16.setObjectName("graphicsView_16")
        self.stackedWeather.addWidget(self.page_18)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.graphicsView_17 = QtWidgets.QGraphicsView(self.page_19)
        self.graphicsView_17.setGeometry(QtCore.QRect(0, 10, 63, 39))
        self.graphicsView_17.setStyleSheet("background:url(:/img/resources/weather/more_cloudy.png);\n"
"border:transparent")
        self.graphicsView_17.setObjectName("graphicsView_17")
        self.stackedWeather.addWidget(self.page_19)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.graphicsView_23 = QtWidgets.QGraphicsView(self.page_5)
        self.graphicsView_23.setGeometry(QtCore.QRect(0, 7, 63, 55))
        self.graphicsView_23.setStyleSheet("background:url(:/img/resources/weather/haze.png);\n"
"border:transparent")
        self.graphicsView_23.setObjectName("graphicsView_23")
        self.stackedWeather.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.graphicsView_24 = QtWidgets.QGraphicsView(self.page_6)
        self.graphicsView_24.setGeometry(QtCore.QRect(0, 0, 63, 67))
        self.graphicsView_24.setStyleSheet("background:url(:/img/resources/weather/rainy.png);\n"
"border:transparent")
        self.graphicsView_24.setObjectName("graphicsView_24")
        self.stackedWeather.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.graphicsView_25 = QtWidgets.QGraphicsView(self.page_7)
        self.graphicsView_25.setGeometry(QtCore.QRect(0, 0, 63, 66))
        self.graphicsView_25.setStyleSheet("background:url(:/img/resources/weather/snowy.png);\n"
"border:transparent")
        self.graphicsView_25.setObjectName("graphicsView_25")
        self.stackedWeather.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.graphicsView_26 = QtWidgets.QGraphicsView(self.page_8)
        self.graphicsView_26.setGeometry(QtCore.QRect(0, 5, 63, 61))
        self.graphicsView_26.setStyleSheet("background:url(:/img/resources/weather/thunder.png);\n"
"border:transparent")
        self.graphicsView_26.setObjectName("graphicsView_26")
        self.stackedWeather.addWidget(self.page_8)
        self.dust_2 = QtWidgets.QLabel(self.frame_5)
        self.dust_2.setGeometry(QtCore.QRect(90, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(12)
        self.dust_2.setFont(font)
        self.dust_2.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.dust_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dust_2.setObjectName("dust_2")
        self.frame_6 = QtWidgets.QFrame(self.page_15)
        self.frame_6.setGeometry(QtCore.QRect(30, 10, 151, 111))
        self.frame_6.setStyleSheet("background:rgba(5,5,15,100);\n"
"border-radius : 5px")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.dust = QtWidgets.QLabel(self.frame_6)
        self.dust.setGeometry(QtCore.QRect(95, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(12)
        self.dust.setFont(font)
        self.dust.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.dust.setAlignment(QtCore.Qt.AlignCenter)
        self.dust.setObjectName("dust")
        self.stackedDust = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedDust.setGeometry(QtCore.QRect(15, 35, 71, 71))
        self.stackedDust.setStyleSheet("background:transparent;")
        self.stackedDust.setObjectName("stackedDust")
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.graphicsView_18 = QtWidgets.QGraphicsView(self.page_20)
        self.graphicsView_18.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.graphicsView_18.setStyleSheet("background:url(:/img/resources/good.png);\n"
"border:transparent")
        self.graphicsView_18.setObjectName("graphicsView_18")
        self.stackedDust.addWidget(self.page_20)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.graphicsView_19 = QtWidgets.QGraphicsView(self.page_21)
        self.graphicsView_19.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.graphicsView_19.setStyleSheet("background:url(:/img/resources/normal.png);\n"
"border:transparent")
        self.graphicsView_19.setObjectName("graphicsView_19")
        self.stackedDust.addWidget(self.page_21)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.graphicsView_20 = QtWidgets.QGraphicsView(self.page_22)
        self.graphicsView_20.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.graphicsView_20.setStyleSheet("background:url(:/img/resources/bad.png);\n"
"border:transparent")
        self.graphicsView_20.setObjectName("graphicsView_20")
        self.stackedDust.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.graphicsView_21 = QtWidgets.QGraphicsView(self.page_23)
        self.graphicsView_21.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.graphicsView_21.setStyleSheet("background:url(:/img/resources/worst.png);\n"
"border:transparent")
        self.graphicsView_21.setObjectName("graphicsView_21")
        self.stackedDust.addWidget(self.page_23)
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(10, 3, 81, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.label_21.setObjectName("label_21")
        self.dustVal = QtWidgets.QLabel(self.frame_6)
        self.dustVal.setGeometry(QtCore.QRect(100, 35, 41, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(14)
        self.dustVal.setFont(font)
        self.dustVal.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.dustVal.setAlignment(QtCore.Qt.AlignCenter)
        self.dustVal.setObjectName("dustVal")
        self.stackedWidget_5.addWidget(self.page_15)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.frame_7 = QtWidgets.QFrame(self.page_24)
        self.frame_7.setGeometry(QtCore.QRect(30, 10, 311, 111))
        self.frame_7.setStyleSheet("background:rgba(5,5,15,100);\n"
"border-radius : 5px")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_25 = QtWidgets.QLabel(self.frame_7)
        self.label_25.setGeometry(QtCore.QRect(10, 3, 101, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(10, 69, 251, 31))
        self.lineEdit.setStyleSheet("background:rgba(255,255,255,245)\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 69, 31, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:1px solid rgba(250,250,250,245);\n"
"border-radius:6px;\n"
"background:transparent;\n"
"color:rgba(250,250,250,245);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_7)
        self.timeEdit.setGeometry(QtCore.QRect(10, 31, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(12)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("background:transparent;\n"
"color:white;\n"
"selection-color:white")
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 30, 30, 30))
        self.pushButton_7.setStyleSheet("background:url(:/img/resources/add.png);\n"
"border:transparent\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget_5.addWidget(self.page_24)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setGeometry(QtCore.QRect(30, 10, 311, 111))
        self.frame_8.setStyleSheet("background:rgba(5,5,15,100);\n"
"border-radius : 5px")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_26 = QtWidgets.QLabel(self.frame_8)
        self.label_26.setGeometry(QtCore.QRect(10, 3, 101, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white;\n"
"background:transparent\n"
"\n"
"")
        self.label_26.setObjectName("label_26")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 69, 251, 31))
        self.lineEdit_2.setStyleSheet("background:rgba(255,255,255,245)\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 69, 31, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border:1px solid rgba(250,250,250,245);\n"
"border-radius:6px;\n"
"background:transparent;\n"
"color:rgba(250,250,250,245);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame_8)
        self.timeEdit_2.setGeometry(QtCore.QRect(10, 31, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(12)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setStyleSheet("background:transparent;\n"
"color:white;\n"
"selection-color:white")
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setGeometry(QtCore.QRect(270, 30, 30, 30))
        self.pushButton.setStyleSheet("background:url(:/img/resources/add.png);\n"
"border:transparent\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget_5.addWidget(self.page_3)
        self.time = QtWidgets.QLabel(self.frame)
        self.time.setGeometry(QtCore.QRect(120, 70, 251, 51))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setStyleSheet("background: transparent;\n"
"color:white\n"
"")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(280, 80, 21, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(38)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(5,5,15,130);\n"
"background:transparent")
        self.label_9.setObjectName("label_9")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(150, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet("background: transparent;\n"
"color:white\n"
"")
        self.date.setObjectName("date")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(192, 80, 16, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(38)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(5,5,15,130);\n"
"background:transparent")
        self.label_3.setObjectName("label_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(450, 190, 31, 101))
        self.stackedWidget.setStyleSheet("background:transparent\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 69, 24, 24))
        self.pushButton_3.setStyleSheet("background:url(:/img/resources/home-button.png);\n"
"border:transparent")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 40, 23, 23))
        self.pushButton_4.setStyleSheet("background:url(:/img/resources/music-note-in-a-circle.png);\n"
"border:transparent")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 10, 24, 24))
        self.pushButton_6.setStyleSheet("background:url(:/img/resources/microphone.png);\n"
"border:transparent")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWeather.setCurrentIndex(0)
        self.stackedDust.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weatherVal.setText(_translate("MainWindow", "00.0"))
        self.label_18.setText(_translate("MainWindow", "Weather"))
        self.dust_2.setText(_translate("MainWindow", "맑음"))
        self.dust.setText(_translate("MainWindow", "매우\n"
"나쁨"))
        self.label_21.setText(_translate("MainWindow", "Fine Dust"))
        self.dustVal.setText(_translate("MainWindow", "00"))
        self.label_25.setText(_translate("MainWindow", "Reservation"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.label_26.setText(_translate("MainWindow", "Song"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.time.setText(_translate("MainWindow", "12  00  00"))
        self.label_9.setText(_translate("MainWindow", ":"))
        self.date.setText(_translate("MainWindow", "2019년 12월 31일"))
        self.label_3.setText(_translate("MainWindow", ":"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

