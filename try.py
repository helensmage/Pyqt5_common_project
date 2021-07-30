import os
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QLineEdit, \
    QMessageBox
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal
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
    Signal_OneParameter = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Анкета')
        self.setGeometry(300, 50, 700, 950)

        '''self.sql1 = """SELECT * FROM Films 
                            WHERE genre=(
                                SELECT id FROM genres 
                                WHERE title = 'детектив')"""

        self.fromDataBase(self.sql1)'''

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

        self.lbl = QLabel(self)
        self.surname = QPlainTextEdit(self)
        self.surname.move(230, 285)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.name = QPlainTextEdit(self)
        self.name.move(230, 325)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.fathername = QPlainTextEdit(self)
        self.fathername.move(230, 370)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.buttonadd = QPushButton('Добавить', self)
        self.buttonadd.clicked.connect(self.OpenFly)

    def fromDataBase(self, FavGenre):
        try:
            self.con = sqlite3.connect("space.db")
            self.cur = self.con.cursor()
            try:
                self.cur.execute(FavGenre).fetchmany(50)
            except:
                self.cur.execute(*FavGenre).fetchmany(50)
            self.con.commit()
            try:
                self.names = [description[0] for description in self.cur.description]
            except:
                pass
            #self.allgenres = self.cur.execute("""SELECT title FROM genres""").fetchall()
            self.con.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def deal_emit_slot(self, dateStr):
        self.insertsql = """INSERT INTO Users (Фамилия, Имя, Отчество)
                                        VALUES (?, ?, ?)""", (dateStr[0], dateStr[1], dateStr[2])
        self.fromDataBase(self.insertsql)
        print(dateStr)

    def OpenFly(self):
        self.Signal_OneParameter.connect(self.deal_emit_slot)

        self.additionlist = []

        self.checkerror(self.surname)
        self.checkerror(self.name)
        self.checkerror(self.fathername)

        if len(self.additionlist) == 3:
            self.deal_emit_slot(self.additionlist)
            self.close()

    def checkerror(self, param):
        if param.toPlainText():
            self.additionlist.append(param.toPlainText())
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
