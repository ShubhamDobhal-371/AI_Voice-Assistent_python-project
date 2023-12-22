from  ADVGUI import Ui_jarvis
from PyQt5 import QtCore ,QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from  PyQt5.uic import loadUiType
import sys
import Main
class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        Main.taskExicution()

startExe=MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui1 = Ui_jarvis()
        self.gui1.setupUi(self)

        self.gui1.pushButton.clicked.connect(self.startTask)
        self.gui1.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui1.la1=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/B.G/Black_Template.jpg")
        self.gui1.label.setMovie(self.gui1.la1)
        self.gui1.la1.start()

        self.gui1.la3=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/B.G/Iron_Template_1.gif")
        self.gui1.label_2.setMovie(self.gui1.la3)
        self.gui1.la3.start()

        self.gui1.la4=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/initial.gif")
        self.gui1.label_3.setMovie(self.gui1.la4)
        self.gui1.la4.start()

        self.gui1.la5=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/Jarvis_Gui (1).gif")
        self.gui1.label_4.setMovie(self.gui1.la5)
        self.gui1.la5.start()

        self.gui1.la6=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/B.G_Template_1.gif")
        self.gui1.label_5.setMovie(self.gui1.la6)
        self.gui1.la6.start()

        self.gui1.la7=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/Earth_Template.gif")
        self.gui1.label_6.setMovie(self.gui1.la7)
        self.gui1.la7.start()

        self.gui1.la8=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/voisrec/Siri_1.gif")
        self.gui1.label_7.setMovie(self.gui1.la8)
        self.gui1.la8.start()

        self.gui1.la9=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/load-loading.gif")
        self.gui1.label_8.setMovie(self.gui1.la9)
        self.gui1.la9.start()





        


        startExe.start()

GuiApp=QApplication(sys.argv)
jar_gui=Gui_Start()
jar_gui.show()
exit(GuiApp.exec_())

