import os
import random
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QRadioButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor, QPalette, QLinearGradient, QBrush, QIcon
from PyQt5.QtCore import Qt, QDateTime, QRect, QMetaObject, QCoreApplication, pyqtSignal, QDate
import requests
from marstown import MarsTown
from dontfly import DontFly
from marsabout import MarsAbout
from uidialog import Ui_Dialog
from app import App
from window import Window

qss = '''QPushButton{
             border: none;
             font-size: 18px;
             font-style: italic;
         }
         QPushButton:hover{
            color: rgba(0, 82, 136, 1);
         }'''

qss1 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             background: rgba(195, 144, 214);
         }'''

qss2 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             color: white;
             background: #183bd9;
         }'''

qss3 = '''QScrollBar{
            background : #003494;
             }
             QScrollBar::handle
             {
             background : #589ce0;
             }
             QScrollBar::handle::pressed
             {
             background : #003494;
             }
'''

qss4 = '''QScrollBar{
            background : #003494;
             }
             QScrollBar::handle
             {
             background : #d1a9a5;
             }
             QScrollBar::handle::pressed
             {
             background : #79443b;
             }
'''

qss5 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             color: 79443b;
             background: #d1a9a5;
         }'''

qss6 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             background: #59942f;
         }'''

qss7 = '''QScrollBar{
            background : #003494;
             }
             QScrollBar::handle
             {
             background : #00406b;
             }
             QScrollBar::handle::pressed
             {
             background : #002137;
             }
'''

class Test(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 40, 700, 1000)
        self.setWindowTitle('ПОЛЁТ НА МАРС')
        self.setWindowIcon(QIcon('images/Mars.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 750)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(0.5, QColor(86, 29, 255))
        gradient.setColorAt(1.0, QColor(230, 230, 250))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.addText('<p style="color:rgba(0, 82, 136, 1);'
                             'font-size:18px;font-style:italic;">'
                             '<span style="font-size:36px;">3000</span>'
                             ' год<br>космических<br>путешествий</p>', 22, 36)
        self.addButton('Марсгородок', qss, 164, 69, 0, 0, 0, self.MarsCity)
        self.addButton('Противопоказания', qss, 303, 69, 0, 0, 0, self.Dontrecommend)
        self.addButton('О Марсе', qss, 477, 69, 1, 85, 20, self.AboutMars)

        self.addImage('Elon.png', 116, 100, 574, 10)
        self.addImage('spaceX.png', 116, 63, 574, 94)

        self.addButton('Администратор', qss2, 250, 125, 1, 187, 46, self.Admin)

        self.addText('<h1>Приветствуем Вас, Дорогие Земляне!</h1>', 100, 235)

        self.addImage('Earth.png', 150, 150, 120, 302)
        self.addImage('people.png', 175, 80, 260, 280)
        self.addImage('arrow.png', 150, 100, 275, 325)
        self.addImage('arrow1.png', 150, 100, 275, 354)
        self.addImage('Mars.png', 140, 140, 434, 307)

        self.addText('<h1>Мы поможем Вам:</h1>', 100, 525)
        self.addText('<h1>Спланировать инопланетный досуг!</h1>', 138, 574)
        self.addText('<h1>Безопасно добраться до Марса!</h1>', 200, 616)
        self.addText('<h1>Выбрать подходящий дом!</h1>', 266, 658)
        self.addText('<h1>Если вы решили сделать шаг навстречу'
                     '<br>Красной Планете, пожалуйста,'
                     '<br>заполните анкету!</h1>', 100, 770)

        self.addButton('Анкета', qss2, 280, 900, 1, 142, 46, self.Anketa)

    def addImage(self, name, a, b, x, y):
        fullname = os.path.join('images', name)
        self.pixmap = QPixmap(fullname).scaled(a, b, Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.move(x, y)
        self.image.setPixmap(self.pixmap)

    def addText(self, txt, x, y):
        self.label1 = QLabel(txt, self)
        self.label1.move(x, y)

    def addButton(self, txt, style, x, y, flag, a, b, func):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(func)
        self.button1.move(x, y)
        if flag:
            self.button1.resize(a, b)

    def MarsCity(self):
        self.second_form = MarsTown()
        self.second_form.show()

    def Dontrecommend(self):
        self.forth_form = DontFly()
        self.forth_form.show()

    def AboutMars(self):
        self.third_form = MarsAbout()
        self.third_form.show()

    def Anketa(self):
        self.anket = Window()
        self.anket.show()

    def Admin(self):
        self.autorization = Ui_Dialog()
        self.autorization.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
