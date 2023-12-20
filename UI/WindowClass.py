# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WindowClass
   Description :
   Author :       guxu
   date：          11/29/23
-------------------------------------------------
   Change Activity:
                   11/29/23:
-------------------------------------------------
"""
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQT 6')
        self.setWindowIcon(QIcon('qt.png'))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()

        btn1 = QPushButton('Button1')
        btn2 = QPushButton('Button2')
        btn3 = QPushButton('Button3')
        btn4 = QPushButton('Button4')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())