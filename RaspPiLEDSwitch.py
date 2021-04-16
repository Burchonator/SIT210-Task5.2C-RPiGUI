# 

import sys
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import *#QApplication,QWidget,QRadioButton
from PyQt5.QtGui import *#QIcon

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(8,GPIO.OUT) # red
GPIO.setup(10,GPIO.OUT) # green
GPIO.setup(12,GPIO.OUT) # blue

# when output set to high the voltage is 3.3V, 0 for Low
# Never connect a device with an input voltage higher than 3.3V to GPIO pin
# because it will fry the RaspPi

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'LED Light Switch'
        self.left = 200 
        self.top = 200
        self.width = 400
        self.height = 300
        rbtnwidth = 70
        rbtnheight = 40
        layout=QGridLayout()
        #self.init_UI()
        
        #self.setLayout(layout)
    #def init_UI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(200,200,400,300)
        
        self.rbtnRed = QRadioButton("red",self)
        self.rbtnRed.setGeometry(0,0,rbtnwidth,rbtnheight) #x,y,width,height
        self.rbtnRed.clicked.connect(self.redLedOn)
        
        self.rbtnGreen = QRadioButton("green",self)
        self.rbtnGreen.setGeometry(rbtnwidth,0,rbtnwidth,rbtnheight) #x,y,width,height
        self.rbtnGreen.clicked.connect(self.greenLedOn)
        
        self.rbtnBlue = QRadioButton("blue",self)
        self.rbtnBlue.setGeometry(rbtnwidth*2,0,rbtnwidth,rbtnheight) #x,y,width,height
        self.rbtnBlue.clicked.connect(self.blueLedOn)
        
        self.btnExit = QPushButton("Exit",self)
        self.btnExit.setGeometry(0,70,rbtnwidth,rbtnheight)
        self.btnExit.clicked.connect(self.close_application)
        
    def redLedOn(self):
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
    def greenLedOn(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(12,GPIO.LOW)
    def blueLedOn(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
    
    def close_application(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.cleanup()
        self.close()
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_()) # this is needed otherwise you'll see something ugly
