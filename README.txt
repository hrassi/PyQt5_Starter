# PyQt5_Starter

this is a starter kit to begin with Pyqt5
u can use also qt designer app that help a lot to reduce writing code
qt designer is an app for gui designing interface
it will give u a file.ui usable witch will be translated to python

********************************************************************

python PyQt5 :

frame button image label

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout,QLineEdit

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor



full tutorial:

https://youtu.be/9iZLDnW_vwU?si=jGDlj90v0veZnMj0

QGrid Layout :
https://www.pythontutorial.net/pyqt/pyqt-qgridlayout/



# example 1  label:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

app=QApplication([])
window=Qwidget()
window.setGeometry(100,100,200,300) window coordinate and dimmentions
window.setWindowTitle(“Houssam App”)

label=QLabel(window)
label.setText(“hello world”)
label.setFont(QFont(“Arial”,16))
label.move(50,100)      #coordinate of label

window.show()
app.exec_()

if __name__ == ‘ __main__’:
    main()



# example 2 layout QVBoxLayout and push button
# and label and text box:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

app=QApplication([])
window=Qwidget()
window.setGeometry(100,100,200,300) 
window.setWindowTitle(“Houssam App”)

label = QLabel(“Press the button “)
textbox=QTextEdit()
button = QPushButton(“Press Me !”)
button.clicked.connect(on_click)
button2 = QPushButton(“send msg”)
button2.clicked.connect(lambda: on_click2(textbox.toPlainText()))

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(textbox)
window.setLayout(layout)



window.show()
app.exec_()

def on_click():
    print(“Hello world”)
    message = QMessageBox()
    message.setText(“Hello world”)
    message.exec_()

def on_click2(msg):
    message.setText(msg)
    message.exec_()
    

if __name__ == ‘ __main__’:
    main()

QT Designer :

https://youtu.be/MOItX2aKTGc?si=HxK15KkHKEDYCnI6

from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi(“mygui.ui” , self) # mygui.ui is the file from QT Designer
        self.show()
        
        self.pushButton.clicked.connect(self.login) # if pushButton is pushed
        self.pushButton_2.clicked.connect(lambda: self.sayit(self.textEdit.toPlainText()
        self.actionClose.triggered.connect(exit)

def login(self):
    if self.lineEdit.text() == “hrassi” and self.lineEdit_2.text() == “password”:
        self.textEdit.setEnabled(True)
        self.pushButton_2.setEnabled(True)
    else:
        message = QMessageBox()
        message.setText(“invalid login”)
        message.exec_()

def sayit(self, msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == ‘ __main__’:
    main()


QT DESIGNER TUTORIAL : youtube NeuralNine chanel

https://youtu.be/MOItX2aKTGc?si=HxK15KkHKEDYCnI6

https://youtu.be/vde95l737PI?si=9fTxVxOJOVkuvl1A

using color and properties and layout:
https://youtu.be/i_Z-1F_U_yw?si=MPfgtebC0dW6Q2WO
