from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Spider_GUI import Ui_SPIDER
import sys
import main


class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
         
    def run(self):
        main.spider_password()
        

startExe=MainThread()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_SPIDER()
        self.ui.setupUi(self)
        self.startTask()
        # self.ui.pushButton_quit.clicked.connect(self.close) 
        
    def startTask(self):
        self.ui.label1=QtGui.QMovie("Jarvis_Gui (1).gif") 
        self.ui.GUI_label.setMovie(self.ui.label1)
        self.ui.label1.start()
        
        
        
        startExe.start()
        
app=QApplication(sys.argv)
spider=Gui_start()
spider.show()
exit(app.exec_())