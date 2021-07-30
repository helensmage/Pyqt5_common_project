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
from app import App
from house import House


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


class Voyage(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(750, 200, 730, 700)
        self.setWindowTitle('Выбор рейса')
        self.setWindowIcon(QIcon('images/race.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 500)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(127, 199, 255))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        self.readfile()
        self.makeaview()

    def readfile(self):
        fin = open('voyage.txt', 'r')
        self.a = []
        s = fin.readline()
        while s:
            self.a.append(list(map(str, s.replace('\n', '').split(','))))
            s = fin.readline()
        fin.close()

    def makeaview(self):
        layout = QGridLayout()
        scrollArea = QScrollArea()
        scrollArea.setStyleSheet(qss3)
        scrollArea1 = QScrollArea()
        scrollArea1.setStyleSheet(qss3)
        content_widget = QWidget()
        scrollArea.setWidget(content_widget)
        scrollArea.setWidgetResizable(True)
        content_widget1 = QWidget()
        scrollArea1.setWidget(content_widget1)
        scrollArea1.setWidgetResizable(True)
        lay = QVBoxLayout(content_widget)
        lay1 = QVBoxLayout(content_widget1)
        self.checklist1 = []
        self.checklist2 = []
        for i in self.a:
            self.title = QRadioButton(i[0], self)
            self.checklist1.append(self.title)
            self.title1 = QRadioButton(i[0], self)
            self.checklist2.append(self.title1)
            self.image = QImage()
            self.image.loadFromData(requests.get(i[1]).content)
            self.image_label = QLabel()
            self.image_label.setPixmap(QPixmap(self.image).scaled(300, 300, Qt.KeepAspectRatio))
            self.image_label1 = QLabel()
            self.image_label1.setPixmap(QPixmap(self.image).scaled(300, 300, Qt.KeepAspectRatio))
            self.tex = QLabel(i[2], self)
            self.tex1 = QLabel(i[2], self)
            lay.addWidget(self.title)
            lay.addWidget(self.image_label)
            lay.addWidget(self.tex)
            lay1.addWidget(self.title1)
            lay1.addWidget(self.image_label1)
            lay1.addWidget(self.tex1)

        self.toMars = QLabel('<h2>НА МАРС</h2>', self)
        self.chooseship = QLabel('<h3>Выберите космический корабль:</h3>', self)
        self.toEarth = QLabel('<h2>НА ЗЕМЛЮ</h2>', self)
        self.chooseship1 = QLabel('<h3>Выберите космический корабль:</h3>', self)

        self.choosedate = QLabel('<h3>Выберите дату и время:</h3>', self)
        self.date = QDateTimeEdit(self)
        self.date.setCalendarPopup(True)
        self.date.setDateTime(QDateTime.currentDateTime())

        self.choosedate1 = QLabel('<h3>Выберите дату и время:</h3>', self)
        self.date1 = QDateTimeEdit(self)
        self.date1.setCalendarPopup(True)
        self.date1.setDateTime(QDateTime.currentDateTime())

        self.sendbutton = self.addButton('Отправить', qss2, self.send, self.checklist1, self.date, 0)
        self.sendbutton1 = self.addButton('Отправить', qss2, self.send, self.checklist2, self.date1, 1)

        self.gotohome = QLabel('<h2>Перейти к выбору дома ------></h2>', self)
        self.next = QPushButton('Далее', self)
        self.next.setStyleSheet(qss2)
        self.next.clicked.connect(self.OpenHouse)

        layout.addWidget(self.toMars, 1, 0)
        layout.addWidget(self.chooseship, 2, 0)
        layout.addWidget(scrollArea, 3, 0)
        layout.addWidget(self.choosedate, 4, 0)
        layout.addWidget(self.date, 5, 0)
        layout.addWidget(self.sendbutton, 6, 0)
        layout.addWidget(self.gotohome, 7, 0)
        layout.addWidget(self.toEarth, 1, 1)
        layout.addWidget(self.chooseship1, 2, 1)
        layout.addWidget(scrollArea1, 3, 1)
        layout.addWidget(self.choosedate1, 4, 1)
        layout.addWidget(self.date1, 5, 1)
        layout.addWidget(self.sendbutton1, 6, 1)
        layout.addWidget(self.next, 7, 1)
        self.setLayout(layout)

    def addButton(self, txt, style, func, checklist, date, flag):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(lambda checked, i=checklist, j=date, k=flag: func(i, j, k))
        return self.button1

    def send(self, listics, ddate, flag):
        self.Signal_OneParameter.connect(App().deal_emit_slot)
        check = 0
        for i in range(len(listics)):
            if listics[i].isChecked():
                self.num = int(listics[i].text()[0])
                check += 1
        if check == 0:
            QMessageBox.critical(self, "Пустой выбор", "Выберите, пожалуйста, корабль!", QMessageBox.Ok)
        else:
            self.listships = []
            self.checkerror(self.num, self.listships)
            self.checkerror(ddate.dateTime().toString(), self.listships)
            if not flag:
                self.updatesql = """UPDATE Users SET Корабль1 = ?, Отправление = ? 
                                        where id = (SELECT max(id) FROM Users)""", (self.listships[0], self.listships[1])
            else:
                self.updatesql = """UPDATE Users SET Корабль2 = ?, Прибытие = ? 
                                        where id = (SELECT max(id) FROM Users)""", (self.listships[0], self.listships[1])
            App().deal_emit_slot(self.updatesql)

    def checkerror(self, param, listic):
        if param:
            listic.append(param)
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)

    def OpenHouse(self):
        self.close()
        self.another_form = House()
        self.another_form.show()
