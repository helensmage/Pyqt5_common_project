import os
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt, QDateTime
import requests

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
             background: rgba(115, 194, 246, 1);
         }'''


class Test(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 30, 700, 1000)
        self.setWindowTitle('ПОЛЁТ НА МАРС')

        self.addText('<p style="color:rgba(0, 82, 136, 1);'
                             'font-size:18px;font-style:italic;">'
                             '<span style="font-size:36px;">3000</span>'
                             ' год<br>космических<br>путешествий</p>', 22, 36)
        self.addButton('Марсгородок', qss, 164, 69, 0, 0, 0, self.MarsCity)
        self.addButton('Противопоказания', qss, 303, 69, 0, 0, 0, self.Dontrecommend)
        self.addButton('О Марсе', qss, 477, 69, 1, 85, 20, self.AboutMars)

        self.addImage('Elon.png', 116, 100, 574, 10)
        self.addImage('spaceX.png', 116, 63, 574, 94)

        self.addButton('Администратор', qss1, 250, 125, 1, 187, 46, self.Admin)

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

        self.addButton('Анкета', qss1, 280, 900, 1, 142, 46, self.Anketa)

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

    def Admin(self):
        pass

    def Anketa(self):
        self.fifth_form = Questionnaire()
        self.fifth_form.show()


class MarsTown(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Марсгородок')

        self.addImage('Marsogorod.png', 500, 300, 10, 10)
        self.addText('<p>Перед Вами "Марсгородок" - полностью автономный город со стабильной<br>экологической '
                     'средой обитания для 250 000 человек в каждом городе-сателлите.<br>Жители города смогут '
                     'проживать в наземных системах, соединённых между<br>собой лифтами и другими '
                     'подземными коммуникациями. На первых порах город<br>и первопроходцы будут полностью '
                     'зависеть от постоянных поставок провианта<br>с Земли, но со временем, по мере роста подземных '
                     'и наземных инфраструктур,<br>города-колонии смогут полностью перейти на самообеспечение.</p>', 10, 330)

    def addImage(self, name, a, b, x, y):
        fullname = os.path.join('images', name)
        self.pixmap = QPixmap(fullname).scaled(a, b, Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.move(x, y)
        self.image.setPixmap(self.pixmap)

    def addText(self, txt, x, y):
        self.label1 = QLabel(txt, self)
        self.label1.move(x, y)


class DontFly(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Противопоказания')

        self.label = QLabel('<h4>К полёту не допускаются:</h4>', self)

        self.listWidget = QListWidget(self)
        QListWidgetItem('Лица младше 18 лет и старше 45 лет', self.listWidget)
        QListWidgetItem('Лица с весом меньше 50 кг и больше 90 кг', self.listWidget)
        QListWidgetItem('Наличие тяжёлых хронических заболеваний', self.listWidget)
        QListWidgetItem('Наличие патологий, выявленных томографией', self.listWidget)

        window_layout = QVBoxLayout()
        window_layout.addWidget(self.label)
        window_layout.addWidget(self.listWidget)
        self.setLayout(window_layout)


class MarsAbout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 700, 544)
        self.setWindowTitle('О Марсе')

        self.addImage('AboutMars', 700, 544, 0, 0)

    def addImage(self, name, a, b, x, y):
        fullname = os.path.join('images', name)
        self.pixmap = QPixmap(fullname).scaled(a, b, Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.move(x, y)
        self.image.setPixmap(self.pixmap)


class Questionnaire(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 700, 544)
        self.setWindowTitle('Анкета')

        self.addButton('Отправить', qss1, 177, 30, 0, 0, 0, self.OpenFly)

    def addButton(self, txt, style, x, y, flag, a, b, func):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(func)
        self.button1.move(x, y)
        if flag:
            self.button1.resize(a, b)

    def OpenFly(self):
        self.close()
        self.another_form = Voyage()
        self.another_form.show()


class Voyage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 700, 700)
        self.setWindowTitle('Рейс')
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
        scrollArea1 = QScrollArea()
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
            self.title = QCheckBox(i[0], self)
            self.checklist1.append(self.title)
            self.title1 = QCheckBox(i[0], self)
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

        self.sendbutton = self.addButton('Отправить', qss1, 0, 0, 0, self.send)
        self.sendbutton1 = self.addButton('Отправить', qss1, 0, 0, 0, self.send)

        self.gotohome = QLabel('<h2>Перейти к выбору дома ------></h2>', self)
        self.next = self.addButton('Далее', qss1, 0, 0, 0, self.OpenHouse)

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

    def addButton(self, txt, style, flag, a, b, func):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(func)
        if flag:
            self.button1.resize(a, b)
        return self.button1

    def send(self):
        pass

    def OpenHouse(self):
        self.close()
        self.another_form = House()
        self.another_form.show()


class House(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 700, 544)
        self.setWindowTitle('Выбор дома')

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
        content_widget = QWidget()
        scrollArea.setWidget(content_widget)
        scrollArea.setWidgetResizable(True)
        lay = QGridLayout(content_widget)
        self.checklist1 = []
        for i in range(len(self.a)):
            self.title = QCheckBox(self.a[i][0], self)
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

        layout.addWidget(scrollArea, 1, 0, 1, 1)
        layout.addWidget(self.labelroom, 2, 0)
        layout.addWidget(self.labelprice, 3, 0)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
