from JarvisGUI import Ui_MainWindow
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

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui.la1=QtGui.QMovie("C://Users//shubhu rajput//python26//GUI//B.G//Black_Template.jpg")
        self.gui.label_2.setMovie(self.gui.la1)
        self.gui.la1.start()

        self.gui.la3=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/B.G/Iron_Template_1.gif")
        self.gui.label_3.setMovie(self.gui.la3)
        self.gui.la3.start()

        self.gui.la4=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/voisrec/Siri_1.gif")
        self.gui.label_4.setMovie(self.gui.la4)
        self.gui.la4.start()

        self.gui.la5=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/initial.gif")
        self.gui.label_5.setMovie(self.gui.la5)
        self.gui.la5.start()

        self.gui.la6=QtGui.QMovie("C:/Users/shubhu rajput/python26/GUI/extGUI/B.G_Template_1.gif")
        self.gui.label_6.setMovie(self.gui.la6)
        self.gui.la6.start()

        


        startExe.start()

GuiApp=QApplication(sys.argv)
jar_gui=Gui_Start()
jar_gui.show()
exit(GuiApp.exec_())