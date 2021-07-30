import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QBrush, QPalette, QLinearGradient, QIcon, QColor
from PyQt5.QtWidgets import QLabel, QWidget


class MarsTown(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Марсгородок')
        self.setWindowIcon(QIcon('images/Mars.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 2000)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(201, 22, 40))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

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
