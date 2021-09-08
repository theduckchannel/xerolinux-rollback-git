from PyQt5 import QtWidgets, QtCore, QtGui
import subprocess
from rollback.api import StringUtil
from rollback.api import FileUtil
import sys
import time
import gettext
import os


class MainWindow(QtWidgets.QMainWindow):
    app = QtWigets.QApplication(sys.argv)
    # --------------------------------------------------------------
    # itens hide by default
    nvidiaGroupBox = QtWidgets.QGroupBox()

    def __init__(self):
        super(MainWindow, self).__init__()
        print(_('Start MainWindow'))
        self.setWindowTitle("Xerolinux Rollback Utility")
        # -------------------------------------------------------------
        # Window Flags
        # self.windowFlags = QtCore.Qt.FramelessWindowHint
        # self.windowFlags |= QtCore.Qt.WindowStaysOnBottomHint
        # self.windowFlags |= QtCore.Qt.Tool
        # self.setWindowFlags(self.windowFlags)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # -------------------------------------------------------------
        # Central Widget and Global vertical Layout
        centralWidget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(centralWidget)
        # -----------------------------------------------------------------------------
        # aboutBox
        # self.aboutBox = AboutBox(self)

    # def showAboutBox(self):
    # self.aboutBox.exec_()
    #    self.aboutBox.show()

    @staticmethod
    def getScreenGeometry():
        return QtWidgets.QApplication.desktop().screenGeometry()
