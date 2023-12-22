

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1379, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.JarvisGUI = QtWidgets.QLabel(self.centralwidget)
        self.JarvisGUI.setGeometry(QtCore.QRect(-290, -150, 1751, 1001))
        self.JarvisGUI.setText("")
        self.JarvisGUI.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/B.G/Black_Template.jpg"))
        self.JarvisGUI.setScaledContents(True)
        self.JarvisGUI.setObjectName("JarvisGUI")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 30, 681, 441))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/B.G/Iron_Template_1.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 540, 631, 241))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/voisrec/Siri_1.gif"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 290, 571, 341))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/extGUI/initial.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 40, 491, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/extGUI/Jarvis_Gui (1).gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 560, 381, 271))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/shubhu rajput/python26/GUI/extGUI/B.G_Template_1.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 660, 141, 71))
        self.pushButton.setStyleSheet("background-color: rgb(40, 69, 106);\n"
"font: 8pt \"Palatino Linotype\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 660, 141, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(40, 69, 106);\n"
"font: 8pt \"Mongolian Baiti\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "QUIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
