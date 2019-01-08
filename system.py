from PyQt5 import QtCore, QtGui
from system_gui import *
import datetime
from urllib.request import urlopen, Request
import urllib
import bs4
from data import *
import threading
import time
import asyncio
import aiohttp

class UpdateValuesThread(QtCore.QThread):
    updateInfoSignal = QtCore.pyqtSignal(str)
    updateReseveSignal = QtCore.pyqtSignal(str,str)

    def __init__(self, uiThread):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getInfoAsync)
        #self.timer.start(1000*60)
        self.updateInfoSignal.connect(uiThread.updateInfo)
        self.updateReseveSignal.connect(uiThread.updateReserve)
        ui.enter.clicked.connect(lambda: self.reserve('add'))
        ui.sub.clicked.connect(lambda: self.reserve('sub'))
        self.start()

    def getInfoAsync(self):
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.getCurInfo())

    def reserve(self,order):
        if order=='add':
            reserveTime = ui.brdcstTime.time().toString('hh:mm')
            INFO.brdcsts[reserveTime]=(ui.every.isChecked(), ui.day.currentText(), ui.brdcstEdit.text())
            self.updateReseveSignal.emit('add',reserveTime)
        elif order=='sub':
            reserveTime = ui.table
            del INFO.brdcsts[reserveTime]
            self.updateReserveSignal.emit('sub',reserveTime)

    async def fetch(self,session, url):
        async with session.get(url) as response:
            return await response.read()

    async def getCurInfo(self):
        enc_location = urllib.parse.quote('대전+유성구+장동+날씨')
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, url)
            print(type(html))
            soup = bs4.BeautifulSoup(html,'lxml')
            INFO.fineDust = tuple(soup.select('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > \
                div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > \
                div.sub_info > div > dl > dd:nth-child(2)')[0].get_text().split('㎍/㎥'))
            #self.updateInfoSignal.emit('d')
            INFO.ultraFineDust = tuple(soup.select('#main_pack > div.sc.cs_weather._weather > div:nth-child(2)> \
                div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > \
                div.sub_info > div > dl > dd:nth-child(4)')[0].get_text().split('㎍/㎥'))
            self.updateInfoSignal.emit('d')
            INFO.weather = (soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text,
                soup.find('p', class_='cast_txt').text.split(',')[0])
            self.updateInfoSignal.emit('w')

class UpdateUIThread(QtCore.QThread):

    def __init__(self):
        super().__init__()
        self.dustState = {'좋음':0, '보통':1, '나쁨':2, '매우나쁨':3}
        self.weatherState = {'맑음':0 , '맑음':1, '흐림':2, '구름조금':3, '구름많음':3,'흐림':4,
            '안개':5, '비':6,'눈':7,'천둥번개':8}
        ui.homeButton.clicked.connect(lambda:ui.stackedPage.setCurrentIndex(0))
        ui.homeButton.clicked.connect(lambda:ui.buttons.setCurrentIndex(0))
        ui.brdcstButton.clicked.connect(lambda:ui.stackedPage.setCurrentIndex(1))
        ui.brdcstButton.clicked.connect(lambda:ui.buttons.setCurrentIndex(1))
        ui.add.clicked.connect(lambda:ui.reservePage.setCurrentIndex(0))
        ui.enter.clicked.connect(lambda:ui.reservePage.setCurrentIndex(1))
        self.start()

    @QtCore.pyqtSlot(str)
    def updateInfo(self,order):
        if order == 'd':
            ui.stackedDust.setCurrentIndex(self.dustState[INFO.ultraFineDust[1]])
            ui.dustVal.setText(INFO.ultraFineDust[0])
            ui.dust.setText(INFO.ultraFineDust[1])
        if order == 'w':
           ui.stackedDust.setCurrentIndex(self.weatherState[INFO.weather[1]])
           ui.weatherVal.setText(INFO.weather[0])
           ui.weather.setText(INFO.weather[1])

    @QtCore.pyqtSlot(str,str)
    def updateReserve(self,order,reserveTime):
        if order == 'add':
            checkBox = QtWidgets.QTableWidgetItem()
            checkBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            checkBox.setCheckState(QtCore.Qt.Checked)       
            rowPosition = ui.table.rowCount()
            ui.table.insertRow(rowPosition)
            ui.table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(checkBox))
            ui.table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(INFO.brdcsts[reserveTime][1]+','+reserveTime))
            ui.table.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(INFO.brdcsts[reserveTime][2]))
        elif order == 'sub':
            for item in ui.table.selectedItems():
                print("selectedItems", item.text())


def updateTime():
    while True:
        curTime = QtCore.QTime.currentTime()
        ui.time.setText(curTime.toString('hh  mm  ss'))
        curDate = QtCore.QDate.currentDate()
        ui.date.setText(curDate.toString('yyyy년 MM월 dd일'))
        time.sleep(1)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)                                                                        
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    t = threading.Thread(target=updateTime)
    t.daemon = True
    t.start()
    updateUIThread = UpdateUIThread()
    UpdateValuesThread = UpdateValuesThread(updateUIThread)
    MainWindow.show()
    sys.exit(app.exec_())

    @QtCore.pyqtSlot(str)
    def updateInfo(self,order):
        if order == 'd':
            ui.stackedDust.setCurrentIndex(self.dustState[INFO.ultraFineDust[1]])
            ui.dustVal.setText(INFO.ultraFineDust[0])
            ui.dust.setText(INFO.ultraFineDust[1])
        #if order == 'w':
        #    ui.stackedDust.setCurrentIndex(INFO.weather[1])
        #    ui.weatherVal.setText(INFO.weather[0])
        #    ui.weather.setText(INFO.waether[1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)                                                                        
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    updateTimeThread = UpdateTimeThread()
    updateUIThread = UpdateUIThread()
    UpdateValuesThread = UpdateValuesThread(updateUIThread)
    MainWindow.show()
    sys.exit(app.exec_())
