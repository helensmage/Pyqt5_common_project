import os
import random
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QRadioButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor
from PyQt5.QtCore import Qt, QDateTime, QRect, QMetaObject, QCoreApplication, pyqtSignal, QDate
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

    def Anketa(self):
        self.anket = Window()
        self.anket.show()

    def Admin(self):
        self.autorization = Ui_Dialog()
        self.autorization.show()


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


class Ui_Dialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Dialog")
        self.setGeometry(500, 30, 812, 632)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(90, 80, 631, 461))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel("Добро пожаловать!", self.frame)
        self.label.setGeometry(QRect(200, 80, 250, 51))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QLabel("Логин", self.frame)
        self.label_2.setGeometry(QRect(90, 190, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel("Пароль", self.frame)
        self.label_3.setGeometry(QRect(90, 260, 121, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QLineEdit(self.frame)#
        self.lineEdit.setGeometry(QRect(260, 190, 231, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(209, 207, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame)#
        self.lineEdit_2.setGeometry(QRect(260, 260, 231, 31))
        self.lineEdit_2.setStyleSheet("background-color:#d1cfff;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QPushButton("Вход", self.frame)
        self.pushButton.setGeometry(QRect(230, 360, 161, 41))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")

        QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        login = 'DreamTeam'
        password = 'admin'
        textboxValue = self.lineEdit.text()
        textboxValue1 = self.lineEdit_2.text()
        if not textboxValue or not textboxValue1:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)
        elif textboxValue == login and textboxValue1 == password:
            self.close
            self.adminform = App()
            self.adminform.show()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Предупреждение!")
            msg.setText("У Вас нет доступа к панели администратора")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Коллекция фильмов')
        self.setGeometry(100, 300, 500, 500)

        self.sql1 = """SELECT * FROM Users"""

        self.fromDataBase(self.sql1)
        self.createTable()

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.setLayout(self.layout)

        self.show()

    def fromDataBase(self, FavGenre):
        try:
            self.con = sqlite3.connect("space.db")
            self.cur = self.con.cursor()
            try:
                self.result = self.cur.execute(FavGenre).fetchmany(50)
            except:
                self.result = self.cur.execute(*FavGenre).fetchmany(50)
            self.con.commit()
            try:
                self.names = [description[0] for description in self.cur.description]
            except:
                pass
            #self.allgenres = self.cur.execute("""SELECT title FROM genres""").fetchall()
            self.con.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def createTable(self):
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.names)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.fillMyTable()

    def fillMyTable(self):
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                self.item = QTableWidgetItem(str(self.result[i][j]))
                self.item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                if j == 0:
                    self.tableWidget.setItem(i, j, self.createItem(self.item,
                                                                   Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                else:
                    self.tableWidget.setItem(i, j,
                                             self.createItem(self.item,
                                                             Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.colorRow(i)

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def colorRow(self, row):
        for i in range(self.tableWidget.columnCount()):
            if row % 2 == 0:
                self.tableWidget.item(row, i).setBackground(QColor(209, 207, 255))

    def deal_emit_slot(self, dateStr):

        self.fromDataBase(dateStr)


class Window(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Анкета")
        self.setGeometry(300, 50, 700, 950)

        self.main_text = QLabel(self)
        self.main_text.setText("Анкета жителей Марса")
        self.main_text.setFont(QFont("Times", 13, QFont.Bold))
        self.main_text.move(225, 20)
        self.main_text.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("*Загрузите фото")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(230, 70)
        self.text2.adjustSize()

        self.text1 = QLabel(self)
        self.text1.setText("Персональные данные")
        self.text1.setFont(QFont("Times", 13, QFont.Bold))
        self.text1.move(50, 250)
        self.text1.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Фамилия:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 290)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Имя:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 330)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Отчество:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 370)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Пол:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 410)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Вес:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 450)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Дата рождения:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 490)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Гражданство:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 530)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Место жительства")
        self.text2.setFont(QFont("Times", 13, QFont.Bold))
        self.text2.move(50, 570)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Страна:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 610)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Город:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 650)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Адрес:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 690)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Профессия")
        self.text2.setFont(QFont("Times", 13, QFont.Bold))
        self.text2.move(50, 730)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Место работы:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 770)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Должность:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 810)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Зарплата:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 850)
        self.text2.adjustSize()

        self.btn = QPushButton(self)
        self.btn.move(480, 880)
        self.btn.setText("Отправить")
        self.btn.setFont(QFont("Times", 12, QFont.Bold))
        self.btn.setFixedWidth(170)
        self.btn.setFixedHeight(40)

        self.line = QLabel(self)
        self.line.move(320, 245)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(330)

        self.line = QLabel(self)
        self.line.move(270, 565)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(380)

        self.line = QLabel(self)
        self.line.move(190, 725)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(460)

        self.pushButton = QPushButton('Выбрать', self)
        self.pushButton.move(230, 100)
        self.pushButton_2 = QPushButton('Загрузить', self)
        self.pushButton_2.move(400, 100)
        self.pushButton.clicked.connect(self.openImage)
        self.pushButton_2.clicked.connect(self.saveImage)
        self.image = QLabel(self)
        self.image.move(55, 30)
        self.image.resize(150, 187)

        self.initUI()

    def openImage(self):
        # выбрать фото
        self.imagePath = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        self.pixmap = QPixmap(self.imagePath[0])
        self.image.setPixmap(self.pixmap.scaled(150, 187))

    def saveImage(self):
        current_dir = os.getcwd()
        self.file_name = str(random.random()) + '.png'
        if self.file_name:
            path = os.path.join(current_dir + '/UsersImages', self.file_name)
            self.image.pixmap().save(path)

    def initUI(self):

        self.lbl = QLabel(self)
        self.surname = QLineEdit(self)
        self.surname.move(230, 285)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.weight = QLineEdit(self)
        self.weight.move(230, 445)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.fathername = QLineEdit(self)
        self.fathername.move(230, 370)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.name = QLineEdit(self)
        self.name.move(230, 325)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.citizenship = QLineEdit(self)
        self.citizenship.move(230, 530)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.country = QLineEdit(self)
        self.country.move(230, 610)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.city = QLineEdit(self)
        self.city.move(230, 650)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.adress = QLineEdit(self)
        self.adress.move(230, 690)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)


        self.lbl = QLabel(self)
        self.workplace = QLineEdit(self)
        self.workplace.move(230, 765)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.profession = QLineEdit(self)
        self.profession.move(230, 810)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.salary = QLineEdit(self)
        self.salary.move(230, 850)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.gender = QComboBox(self)
        self.gender.addItems(["М", "Ж"])
        self.gender.move(230, 410)

        self.dateofbirth = QDateEdit(self)
        self.dateofbirth.setCalendarPopup(True)
        self.dateofbirth.setDate(QDate.currentDate())
        self.dateofbirth.move(230, 490)
        self.dateofbirth.setFixedWidth(137)

        self.setGeometry(300, 50, 700, 950)
        self.setWindowTitle('Анкета')

        self.btn.clicked.connect(self.send_a_signal)

    def send_a_signal(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)

        self.additionlist = []
        self.livinglist = []
        self.prolist = []

        self.checkerror(self.surname.text(), self.additionlist)
        self.checkerror(self.name.text(), self.additionlist)
        self.checkerror(self.fathername.text(), self.additionlist)
        self.checkerror(self.gender.currentText(), self.additionlist)
        self.checkerror(self.weight.text(), self.additionlist)
        self.val = str(self.dateofbirth.date())
        for r in (('PyQt5.QtCore.QDate(', ''), (')', ''), (', ', '.')):
            self.val = self.val.replace(*r)
        self.checkerror(self.val, self.additionlist)
        self.checkerror(self.citizenship.text(), self.additionlist)
        #print(self.additionlist)

        self.insertsql = """INSERT INTO Users (Фото, Фамилия, Имя, Отчество, Пол, Вес_кг, Дата_рождения, Гражданство)
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", \
                         (self.file_name, self.additionlist[0], self.additionlist[1], self.additionlist[2], self.additionlist[3], \
                          self.additionlist[4], self.additionlist[5], self.additionlist[6])

        if len(self.additionlist) == 7:
            App().deal_emit_slot(self.insertsql)

        self.checkerror(self.country.text(), self.livinglist)
        self.checkerror(self.city.text(), self.livinglist)
        self.checkerror(self.adress.text(), self.livinglist)

        self.insertsql = """INSERT INTO Living_place (Страна, Город, Адрес) VALUES (?, ?, ?)""", \
                         (self.livinglist[0], self.livinglist[1], self.livinglist[2])

        if len(self.livinglist) == 3:
            App().deal_emit_slot(self.insertsql)

        self.insertsql = """UPDATE Users SET Место_жительства = (SELECT max(id) FROM Living_place) 
                                where id = (SELECT max(id) FROM Users)"""

        App().deal_emit_slot(self.insertsql)

        #
        self.checkerror(self.workplace.text(), self.prolist)
        self.checkerror(self.profession.text(), self.prolist)
        self.checkerror(self.salary.text(), self.prolist)

        self.insertsql = """INSERT INTO profession (Место_работы, Должность, Зарплата) VALUES (?, ?, ?)""", \
                         (self.prolist[0], self.prolist[1], self.prolist[2])

        if len(self.prolist) == 3:
            App().deal_emit_slot(self.insertsql)

        self.insertsql = """UPDATE Users SET Профессия = (SELECT max(id) FROM profession) 
                                        where id = (SELECT max(id) FROM Users)"""

        App().deal_emit_slot(self.insertsql)

        self.close()
        self.another_form = Voyage()
        self.another_form.show()

    def checkerror(self, param, listic):
        if param:
            listic.append(param)
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)


class Voyage(QWidget):
    Signal_OneParameter = pyqtSignal(str)

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

        self.sendbutton = self.addButton('Отправить', qss1, self.send, self.checklist1, self.date, 0)
        self.sendbutton1 = self.addButton('Отправить', qss1, self.send, self.checklist2, self.date1, 1)

        self.gotohome = QLabel('<h2>Перейти к выбору дома ------></h2>', self)
        self.next = QPushButton('Далее', self)
        self.next.setStyleSheet(qss1)
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
        for i in range(len(listics)):
            if listics[i].isChecked():
                self.num = int(listics[i].text()[0])
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


class House(QWidget):
    Signal_OneParameter = pyqtSignal(str)

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

        self.price = QPlainTextEdit('$50000', self)
        self.price.setReadOnly(True)
        self.price.setFixedHeight(30)

        self.butforsend = QPushButton('Отправить', self)
        self.butforsend.clicked.connect(self.sendata)

        layout.addWidget(scrollArea, 1, 0, 1, 2)
        layout.addWidget(self.labelroom, 2, 0)
        layout.addWidget(self.numberoom, 2, 1)
        layout.addWidget(self.labelprice, 3, 0)
        layout.addWidget(self.price, 3, 1)
        layout.addWidget(self.butforsend, 4, 0)
        self.setLayout(layout)

    def showprice(self):
        for i in range(5):
            if self.numberoom.currentText() == str(i + 1):
                self.price.setPlainText('')
                self.price.insertPlainText(self.pricelist[i])

    def sendata(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)
        for i in range(len(self.checklist1)):
            if self.checklist1[i].isChecked():
                self.num = int(self.checklist1[i].text()[0])
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

    def checkerror(self, param, listic):
        if param:
            listic.append(param)
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
