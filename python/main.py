import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import tkinter
import tkinter.messagebox
import iris
class DesktopPet(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        self.init()
        #self.initPall()
        self.initPetImage()
        self.petNormalAction()

    def init(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()

    def initPall(self):
        icons = os.path.join('C:\\InterSystems\\IRISHealth\\mgr\\python\\DesktopPettigerIcon.jpg')
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(QIcon(icons))
        showing = QAction(u'显示', self, triggered=self.showwin)
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon_menu.addAction(showing)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icons))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

    def initPetImage(self):
        self.talkLabel = QLabel(self)
        self.talkLabel.setStyleSheet("font:15pt '楷体';border-width: 1px;color:blue;")
        self.image = QLabel(self)
        self.movie = QMovie("C:\\InterSystems\\IRISHealth\\mgr\\python\\normal\\normal1.gif")
        self.movie.setScaledSize(QSize(200, 200))
        self.image.setMovie(self.movie)
        self.movie.start()
        self.resize(1024, 1024)
        self.randomPosition()
        # 展示
        self.show()
        self.pet1 = []
        for i in os.listdir("C:\\InterSystems\\IRISHealth\\mgr\\python\\normal\\"):
            self.pet1.append("C:\\InterSystems\\IRISHealth\\mgr\\python\\normal\\" + i)
        self.dialog = []
        with open("C:\\InterSystems\\IRISHealth\\mgr\\python\\dialog.txt", "r") as f:
            text = f.read()
            self.dialog = text.split("\n")

    def petNormalAction(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.randomAct)
        self.timer.start(3000)
        self.condition = 0
        self.talk_condition = 0

    # 随机动作切换
    def randomAct(self):
        if not self.condition:
            self.movie = QMovie(random.choice(self.pet1))
            self.movie.setScaledSize(QSize(200, 200))
            self.image.setMovie(self.movie)
            self.movie.start()
        else:
            self.movie = QMovie("C:\\InterSystems\\IRISHealth\\mgr\\python\\click\\click.gif")
            self.movie.setScaledSize(QSize(200, 200))
            self.image.setMovie(self.movie)
            self.movie.start()
            self.condition = 0
            self.talk_condition = 0

    def talk(self):
        if not self.talk_condition:
            self.talkLabel.setText(random.choice(self.dialog))
            self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:white;"
                "background-color: white"
                "url(:/)"
            )
            self.talkLabel.adjustSize()
        else:
            self.talkLabel.setText("~~")
            self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:white;"
                "background-color: white"
                "url(:/)"
            )
            self.talkLabel.adjustSize()
            self.talk_condition = 0
    def getText(self):
       text, okPressed = QInputDialog.getText(self, "Get text","有什么问题吗", QLineEdit.Normal, "")
       if okPressed and text != '':
         print(text)
         return text


    def talkInput(self,input):
        if not self.talk_condition:
            self.talkLabel.setText(input)
            self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:white;"
                "background-color: white"
                "url(:/)"
            )
            self.talkLabel.adjustSize()
    def irisconnect(self,NS):
        args={
          'hostname':'127.0.0.1',
          'port':'51773',
          'username':'_system',
          'password':'jiahemk',
          'namespace':NS
        }
        conn = iris.connect(args)
        irispy = iris.createIRIs(conn)
        return irispy
        


    def quit(self):
        self.close()
        sys.exit()


    def showwin(self):

        self.setWindowOpacity(1)


    def randomPosition(self):

        screen_geo = QDesktopWidget().screenGeometry()

        pet_geo = self.geometry()
        width = (screen_geo.width() - pet_geo.width()) * random.random()
        height = (screen_geo.height() - pet_geo.height()) * random.random()
        print(width)
        print(height)
        self.move(74, 22)

    def mousePressEvent(self, event):

        self.condition = 1

        self.talk_condition = 1

        self.talk()

        self.randomAct()
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True

        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()

        self.setCursor(QCursor(Qt.OpenHandCursor))


    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def enterEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        quitAction = menu.addAction("EXIT")
        ask = menu.addAction("TALK")
        sysinfo = menu.addAction("View iris runtime")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            qApp.quit()
       
        if action == ask:
           input=self.getText()
           TEMP=self.irisconnect("TEST")
           stringVal = TEMP.classMethodstring("EmbeddedPython.Bard", 'Call',input)
           self.talkInput(stringVal)
        if action == sysinfo:
           TEMP=self.irisconnect("TEST")
           stringVal = TEMP.classMethodstring("EmbeddedPython.Bard", 'SystemInfo')
           #print(stringVal)
           self.talkInput("has been running for "+stringVal+" hours")
           


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    sys.exit(app.exec_())
