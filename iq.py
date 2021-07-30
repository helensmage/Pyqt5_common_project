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


qss2 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             color: white;
             background: #183bd9;
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


class IQ(QWidget):
    Signal_OneParameter = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 40, 1070, 1000)
        self.setWindowTitle('Тест')
        self.setWindowIcon(QIcon('images/iq.jpg'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 700)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(0, 33, 55))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.score = 0
        self.radiolist = []
        self.linelist = []
        self.answerlist = ['Успокаивать', '2718', 'горн', '1', '3', 'патент', '12', '36', '17/7', 'знание']

        layout1 = QGridLayout()
        scrollArea = QScrollArea()
        scrollArea.setStyleSheet(qss7)
        content_widget = QWidget()
        scrollArea.setWidget(content_widget)
        scrollArea.setWidgetResizable(True)
        content_widget.setStyleSheet('background: #f0f8ff;')

        layout = QVBoxLayout(content_widget)
        layout.setSpacing(50)

        lay = QHBoxLayout()
        self.label0 = QLabel('<h2>Выберите только 1 правильный вариант ответа</h2>', self)
        self.label = QLabel('<h3>1 Что значит слово "умиротворять"?</h3>', self)
        self.radio11 = QCheckBox('Обтёсывать', self)
        self.radiolist.append(self.radio11)
        self.radio12 = QCheckBox('Устанавливать', self)
        self.radiolist.append(self.radio12)
        self.radio13 = QCheckBox('Выстраивать', self)
        self.radiolist.append(self.radio13)
        self.radio14 = QCheckBox('Успокаивать', self)
        self.radiolist.append(self.radio14)

        lay.addWidget(self.radio11)
        lay.addWidget(self.radio12)
        lay.addWidget(self.radio13)
        lay.addWidget(self.radio14)
        layout.addWidget(self.label0)
        layout.addWidget(self.label)
        layout.addLayout(lay)

        lay1 = QHBoxLayout()
        self.label2 = QLabel('<h3>2 Какое число лишнее?</h3>', self)
        self.radio21 = QCheckBox('2718', self)
        self.radiolist.append(self.radio21)
        self.radio22 = QCheckBox('4519', self)
        self.radiolist.append(self.radio22)
        self.radio23 = QCheckBox('4915', self)
        self.radiolist.append(self.radio23)
        self.radio24 = QCheckBox('6328', self)
        self.radiolist.append(self.radio24)
        self.radio25 = QCheckBox('9514', self)
        self.radiolist.append(self.radio25)
        self.radio26 = QCheckBox('5617', self)
        self.radiolist.append(self.radio26)

        lay1.addWidget(self.radio21)
        lay1.addWidget(self.radio22)
        lay1.addWidget(self.radio23)
        lay1.addWidget(self.radio24)
        lay1.addWidget(self.radio25)
        lay1.addWidget(self.radio26)
        layout.addWidget(self.label2)
        layout.addLayout(lay1)

        self.label3 = QLabel('<h3>3 Впишите в скобки слово, '
                             'которое обозначает то же, что определения, расположенные по обеим сторонам скобок:</h3>', self)
        self.label31 = QLabel('<h2>плавильная печь (?) музыкальный инструмент</h2>', self)
        self.plain1 = QLineEdit(self)
        self.plain1.setFixedWidth(150)
        self.linelist.append(self.plain1)

        layout.addWidget(self.label3)
        layout.addWidget(self.label31)
        layout.addWidget(self.plain1)

        self.label4 = QLabel('<h3>4 Из левого числа получается правое число по одной и той же формуле. '
                             'Что за число вместо знака вопроса?</h3>', self)
        self.label41 = QLabel('<h2>12  ...  2</h2>')
        self.label42 = QLabel('<h2> 3  ...  -1</h2>')
        self.label43 = QLabel('<h2>18  ...	4</h2>')
        self.label44 = QLabel('<h2> 9  ...  ?</h2>')
        self.plain2 = QLineEdit(self)
        self.plain2.setFixedWidth(150)
        self.linelist.append(self.plain2)

        layout.addWidget(self.label4)
        layout.addWidget(self.label41)
        layout.addWidget(self.label42)
        layout.addWidget(self.label43)
        layout.addWidget(self.label44)
        layout.addWidget(self.plain2)

        lay2 = QHBoxLayout()
        self.label5 = QLabel('<h3>5 Какой из кубиков можно собрать из данной развёртки?</h3>', self)
        self.img = QImage()
        self.img.loadFromData(requests.get('http://ichebnik.ru/i_cimages/iq/iq10_1.png').content)
        self.image_lab = QLabel()
        self.image_lab.setPixmap(QPixmap(self.img))
        self.radio51 = QCheckBox('1', self)
        self.radiolist.append(self.radio51)
        self.radio52 = QCheckBox('2', self)
        self.radiolist.append(self.radio52)
        self.radio53 = QCheckBox('3', self)
        self.radiolist.append(self.radio53)
        self.radio54 = QCheckBox('4', self)
        self.radiolist.append(self.radio54)
        self.radio55 = QCheckBox('5', self)
        self.radiolist.append(self.radio55)

        layout.addWidget(self.label5)
        layout.addWidget(self.image_lab)
        lay2.addWidget(self.radio51)
        lay2.addWidget(self.radio52)
        lay2.addWidget(self.radio53)
        lay2.addWidget(self.radio54)
        lay2.addWidget(self.radio55)
        layout.addLayout(lay2)

        self.label6 = QLabel('<h3>6 Образуйте слово состоящее из 6 букв, использовав следующие буквы: ТАПНЕ</h3>', self)
        self.plain3 = QLineEdit(self)
        self.plain3.setFixedWidth(150)
        self.linelist.append(self.plain3)

        layout.addWidget(self.label6)
        layout.addWidget(self.plain3)

        lay3 = QHBoxLayout()
        self.label7 = QLabel('<h3>7 Сколько линий изображено на рисунке?</h3>', self)
        self.img1 = QImage()
        self.img1.loadFromData(requests.get('http://ichebnik.ru/i_cimages/iq/lines_1.png').content)
        self.image_lab1 = QLabel()
        self.image_lab1.setPixmap(QPixmap(self.img1))
        self.radio71 = QCheckBox('9', self)
        self.radiolist.append(self.radio71)
        self.radio72 = QCheckBox('12', self)
        self.radiolist.append(self.radio72)
        self.radio73 = QCheckBox('8', self)
        self.radiolist.append(self.radio73)
        self.radio74 = QCheckBox('13', self)
        self.radiolist.append(self.radio74)
        self.radio75 = QCheckBox('11', self)
        self.radiolist.append(self.radio75)
        self.radio76 = QCheckBox('10', self)
        self.radiolist.append(self.radio76)

        layout.addWidget(self.label7)
        layout.addWidget(self.image_lab1)
        lay3.addWidget(self.radio71)
        lay3.addWidget(self.radio72)
        lay3.addWidget(self.radio73)
        lay3.addWidget(self.radio74)
        lay3.addWidget(self.radio75)
        lay3.addWidget(self.radio76)
        layout.addLayout(lay3)

        self.label8 = QLabel('<h3>8 Каким числом следует заменить знак вопроса?</h3>', self)
        self.label81 = QLabel('<h2>1, 2, 4, 6, 9, 12, 15, 19, 23, 27, 31, ?</h2>', self)
        self.plain4 = QLineEdit(self)
        self.plain4.setFixedWidth(150)
        self.linelist.append(self.plain4)

        layout.addWidget(self.label8)
        layout.addWidget(self.label81)
        layout.addWidget(self.plain4)

        lay4 = QHBoxLayout()
        self.label9 = QLabel('<h3>9 Упростите выражение:</h3>', self)
        self.label91 = QLabel('<h2>24/18:56/9:3/34</h2>', self)
        self.radio91 = QCheckBox('3/4', self)
        self.radiolist.append(self.radio91)
        self.radio92 = QCheckBox('17/7', self)
        self.radiolist.append(self.radio92)
        self.radio93 = QCheckBox('7/8', self)
        self.radiolist.append(self.radio93)
        self.radio94 = QCheckBox('17/9', self)
        self.radiolist.append(self.radio94)
        self.radio95 = QCheckBox('3/7', self)
        self.radiolist.append(self.radio95)
        self.radio96 = QCheckBox('4/3', self)
        self.radiolist.append(self.radio96)

        layout.addWidget(self.label9)
        layout.addWidget(self.label91)
        lay4.addWidget(self.radio91)
        lay4.addWidget(self.radio92)
        lay4.addWidget(self.radio93)
        lay4.addWidget(self.radio94)
        lay4.addWidget(self.radio95)
        lay4.addWidget(self.radio96)
        layout.addLayout(lay4)

        self.label10 = QLabel('<h3>10 Угадайте слово, которое стоит в алфавитном порядке'
                              ' между данными словами и удовлетворяет подсказке:</h3>', self)
        self.label101 = QLabel('<h2>знак - (обладание какими-либо сведениями) - знахарь</h2>', self)
        self.plain5 = QLineEdit(self)
        self.plain5.setFixedWidth(150)
        self.linelist.append(self.plain5)

        layout.addWidget(self.label10)
        layout.addWidget(self.label101)
        layout.addWidget(self.plain5)

        self.butsend = self.addButton('Отправить', qss2, 1, 150, 46, self.send)


        layout1.addWidget(scrollArea, 1, 0, 7, 5)
        layout1.addWidget(self.butsend, 8, 4)
        self.setLayout(layout1)

    def send(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)
        for i in self.radiolist:
            if i.isChecked():
                if i.text() in self.answerlist:
                    self.score += 10

        for i in self.linelist:
            if i.text() in self.answerlist:
                self.score += 10
        print(self.score)
        self.insertsql = """UPDATE Users SET IQ = ?
                                                where id = (SELECT max(id) FROM Users)""", (self.score,)

        App().deal_emit_slot(self.insertsql)
        self.close()
        self.toplist = App()
        self.toplist.show()
        msg = QMessageBox(self)
        msg.setWindowTitle('Успешно')
        msg.setText('Поздравляем! Вы успешно зарегистрировались!\n'
                    'Найдите себя в рейтинге на полёт.')
        msg.setFixedWidth(350)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def addButton(self, txt, style, flag, a, b, func):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(func)
        if flag:
            self.button1.resize(a, b)
        return self.button1
