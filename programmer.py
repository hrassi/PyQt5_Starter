import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


# initialize application:
app=QApplication(sys.argv)

# create a window widget :
window=QWidget()
window.setWindowTitle("Houssam App")
window.setFixedWidth(1000)
window.move(100,200) # set window position along the monitor with x,y coordinates
window.setStyleSheet("background: #161219;")


# initialize grid layout:
grid=QGridLayout()

# display logo
image=QPixmap("logo.png") # load image file
logo=QLabel() # create a label widget
logo.setPixmap(image) # place image inside it
logo.setAlignment(QtCore.Qt.AlignCenter) # align widget to center
logo.setStyleSheet("margin-top: 100px;") # place widget 100 pixels from top

# button widget (padding is the space inside the button to write 25pixel from up and down and 0 pixel from left and right)
button=QPushButton("PLAY")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # set cursor to hand when hover over button
button.setStyleSheet(
    "*{border:4px solid '#BC006C';"+
    "border-radius: 45px;"+
    "font-size:35px;"+
    "color:'white';"+
    "padding: 25px 0;"+
    "margin: 100px 200px;}"+
    "*:hover{background: '#BC006C';}"
)


# place the widgets inside the grid structure
grid.addWidget(logo,0,0)
grid.addWidget(button,1,0)

# apply grid on window object :
window.setLayout(grid)




window.show()
sys.exit(app.exec())


