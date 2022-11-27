import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

class Window2(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1080, 640)
        self.setWindowTitle("Pyqt5 App_1")

        self.verticalAndHorizontal()
        #self.vertical()
        #self.horizontal()
        self.show()

    def horizontal(self):
        hbox = QHBoxLayout()

        #Widgets
        button1 = QPushButton("yes" , self)
        text1 = QLabel("HELLO")
        button2 = QPushButton("NO", self)
        text2 = QLabel("WORLD")
        button3 = QPushButton("1", self)
        text3 = QLabel("2")


        #add widgets into hbox

        hbox.addStretch() # sağa veya sola yaslamak için kullanılır.
        hbox.addWidget(button1)
        hbox.addWidget(text1)
        hbox.addWidget(button2)
        hbox.addWidget(text2)
        hbox.addWidget(button3)
        hbox.addWidget(text3)
        hbox.addStretch() # sağa veya sola yaslamak için kullanılır.

        self.setLayout(hbox)

    def vertical(self):
        vbox = QVBoxLayout()

        #Widgets
        button1 = QPushButton("yes" , self)
        text1 = QLabel("HELLO")
        button2 = QPushButton("NO", self)
        text2 = QLabel("WORLD")
        button3 = QPushButton("1", self)
        text3 = QLabel("2")


        #add widgets into hbox

        vbox.addStretch() # sağa veya sola yaslamak için kullanılır.
        vbox.addWidget(button1)
        vbox.addWidget(text1)
        vbox.addWidget(button2)
        vbox.addWidget(text2)
        vbox.addWidget(button3)
        vbox.addWidget(text3)
        vbox.addStretch() # sağa veya sola yaslamak için kullanılır.

        self.setLayout(vbox)

    def verticalAndHorizontal(self):

        mainlayout = QHBoxLayout() # main layout olarak horizontal bir layout oluşturuldu.

        leftlayout = QVBoxLayout() # left layout olarak vertical bir layout oluşturuldu.
        midlayout = QVBoxLayout() # mid layout olarak vertical bir layout oluşturuldu.
        rightlayout = QVBoxLayout() # right layout olarak vertical bir layout oluşturuldu.

        # main layout a left, mid ve right layoutları ekleyerek birleştirildi.
        mainlayout.addLayout(leftlayout)
        mainlayout.addLayout(midlayout)
        mainlayout.addLayout(rightlayout)

        #widgets
        button1 = QPushButton("left")
        button2 = QPushButton("mid")
        button3 = QPushButton("r1")
        button4 = QPushButton("r2")


        leftlayout.addWidget(button1)

        midlayout.addWidget(button2)

        rightlayout.addStretch()  # sağa veya sola yaslamak için kullanılır.
        rightlayout.addWidget(button3)
        rightlayout.addWidget(button4)
        rightlayout.addStretch()  # sağa veya sola yaslamak için kullanılır.

        self.setLayout(mainlayout)


app = QApplication(sys.argv)
window2 = Window2()
sys.exit(app.exec_())