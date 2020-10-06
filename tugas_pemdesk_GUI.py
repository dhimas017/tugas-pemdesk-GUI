from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 400) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
    def UiComponents(self):

        textLabel = QLabel(self)
        textLabel.setText("kotak angka: ")
        textLabel.move(50,10)  
  
        # creating a push button 
        button1 = QPushButton("1", self)
        button2 = QPushButton("2", self)
        button3 = QPushButton("3", self)
        button4 = QPushButton("4", self)
        button5 = QPushButton("5", self)

        button1.setStyleSheet("color: red")
        button2.setStyleSheet("color: red")
        button3.setStyleSheet("color: red")
        button4.setStyleSheet("color: red")
        button5.setStyleSheet("color: red")

        button1.resize(50,50)
        button2.resize(50,50)
        button3.resize(50,50)
        button4.resize(50,50)
        button5.resize(50,50)
  
        # setting geometry of button 
        button1.move(50,50)
        button2.move(115,50)
        button3.move(180,50)
        button4.move(245,50)
        button5.move(310,50)
  
        # changing font and size of text 
        button1.setFont(QFont('Times', 20)) 
        button2.setFont(QFont('Times', 20)) 
        button3.setFont(QFont('Times', 20)) 
        button4.setFont(QFont('Times', 20)) 
        button5.setFont(QFont('Times', 20)) 
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 
