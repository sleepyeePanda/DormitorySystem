from PyQt5 import QtCore, QtGui
from system_gui import *
import datetime
from urllib.request import urlopen, Request
import urllib
import bs4
from data import *

class UpdateTimeThread(QtCore.QThread):

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.start()

    def updateTime(self):
        curTime = QtCore.QTime.currentTime()
        ui.time.setText(curTime.toString('hh  mm  ss'))
        curDate = QtCore.QDate.currentDate()
        ui.date.setText(curDate.toString('yyyy년 MM월 dd일'))
        pass

class UpdateValuesThread(QtCore.QThread):
    updateInfoSignal = QtCore.pyqtSignal(str)

    def __init__(self, uiThread):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.curInfo)
        self.timer.start(10000)
        self.updateInfoSignal.connect(uiThread.updateInfo)
        self.start()

    def curInfo(self):
        enc_location = urllib.parse.quote('대전+유성구+장동+날씨')
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html,'lxml')
        INFO.fineDust = tuple(soup.select('#main_pack > div.sc.cs_weather._weather > div:nth-child(2) > \
            div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > \
            div.sub_info > div > dl > dd.lv2')[0].get_text().split('㎍/㎥'))
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
        #self.weatherState = {'맑음':1, '흐림':2}
        self.start()

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