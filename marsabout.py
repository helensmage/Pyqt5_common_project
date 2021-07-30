import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel


class MarsAbout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 700, 544)
        self.setWindowTitle('О Марсе')
        self.setWindowIcon(QIcon('images/Mars.png'))
        self.addImage('AboutMars', 700, 544, 0, 0)

    def addImage(self, name, a, b, x, y):
        fullname = os.path.join('images', name)
        self.pixmap = QPixmap(fullname).scaled(a, b, Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.move(x, y)
        self.image.setPixmap(self.pixmap)
