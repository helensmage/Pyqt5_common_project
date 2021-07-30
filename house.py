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
from ent import Ent


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


class House(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(750, 200, 700, 630)
        self.setWindowTitle('Выбор дома')
        self.setWindowIcon(QIcon('images/house.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 700)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(0.5, QColor(252, 203, 187))
        gradient.setColorAt(1.0, QColor(121, 68, 59))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.readfile()
        self.makeaview()

    def readfile(self):
        fin = open('house.txt', 'r')
        self.a = []
        s = fin.readline()
        while s:
            self.a.append(list(map(str, s.replace('\n', '').split(','))))
            s = fin.readline()
        fin.close()

    def makeaview(self):
        layout = QGridLayout()
        scrollArea = QScrollArea()
        scrollArea.setStyleSheet(qss4)
        content_widget = QWidget()
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 700)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(0.5, QColor(252, 203, 187))
        gradient.setColorAt(1.0, QColor(121, 68, 59))
        p.setBrush(QPalette.Window, QBrush(gradient))
        content_widget.setPalette(p)
        scrollArea.setWidget(content_widget)
        scrollArea.setWidgetResizable(True)
        lay = QGridLayout(content_widget)
        self.checklist1 = []
        for i in range(len(self.a)):
            self.title = QRadioButton(self.a[i][0], self)
            self.checklist1.append(self.title)
            self.image = QImage()
            self.image.loadFromData(requests.get(self.a[i][1]).content)
            self.image_label = QLabel()
            self.image_label.setPixmap(QPixmap(self.image).scaled(300, 300, Qt.KeepAspectRatio))
            if i % 2 == 0:
                lay.addWidget(self.title, i + 1, 0)
                lay.addWidget(self.image_label, i + 2, 0)
            else:
                lay.addWidget(self.title, i, 1)
                lay.addWidget(self.image_label, i + 1, 1)

        self.labelroom = QLabel('<h3>Выберите количество комнат:</h3>', self)
        self.labelprice = QLabel('<h3>Стоимость:</h3>')

        self.pricelist = ['$50000', '$100000', '$150000', '$200000', '$250000']

        self.numberoom = QComboBox(self)
        self.numberoom.addItems(['1', '2', '3', '4', '5'])
        self.numberoom.currentTextChanged.connect(self.showprice)
        self.numberoom.setFixedWidth(150)
        self.numberoom.setStyleSheet("background: #e6bbc1;selection-background-color: white")

        self.price = QPlainTextEdit('$50000', self)
        self.price.setReadOnly(True)
        self.price.setFixedHeight(30)
        self.price.setFixedWidth(150)

        self.butforsend = QPushButton('Отправить', self)
        self.butforsend.clicked.connect(self.sendata)
        self.butforsend.setFixedWidth(150)
        self.butforsend.setStyleSheet(qss5)

        layout.addWidget(scrollArea, 1, 0, 1, 2)
        layout.addWidget(self.labelroom, 2, 0)
        layout.addWidget(self.numberoom, 2, 1)
        layout.addWidget(self.labelprice, 3, 0)
        layout.addWidget(self.price, 3, 1)
        layout.addWidget(self.butforsend, 4, 1)
        self.setLayout(layout)

    def showprice(self):
        for i in range(5):
            if self.numberoom.currentText() == str(i + 1):
                self.price.setPlainText('')
                self.price.insertPlainText(self.pricelist[i])

    def sendata(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)
        check = 0
        for i in range(len(self.checklist1)):
            if self.checklist1[i].isChecked():
                self.num = int(self.checklist1[i].text()[0])
                check = 1
        if check:
            self.listships = []
            self.checkerror(self.num, self.listships)
            self.checkerror(int(self.numberoom.currentText()), self.listships)
            self.checkerror(self.price.toPlainText(), self.listships)
            print(self.listships)

            self.updatesql1 = """INSERT INTO House(Название, Количество_комнат, Стоимость)
                                    VALUES(?, ?, ?)""", (self.listships[0], self.listships[1], self.listships[2])

            App().deal_emit_slot(self.updatesql1)

            self.updatesql = """UPDATE Users SET Дом = (SELECT max(id) FROM House)
                                            WHERE id = (SELECT max(id) FROM Users)"""

            App().deal_emit_slot(self.updatesql)
            self.close()
            self.another_form = Ent()
            self.another_form.show()
        else:
            QMessageBox.critical(self, "Пустой выбор", "Выберите, пожалуйста, домик!", QMessageBox.Ok)

    def checkerror(self, param, listic):
        if param:
            listic.append(param)
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)
