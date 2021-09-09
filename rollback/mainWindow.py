import os
import sys
import subprocess as sp
import qdarkstyle
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy.QtCore import *
from rollback.api import FileUtil
from rollback.version import Version


# Only for debug .setStyleSheet("background-color: red")


class mainWindow(QMainWindow):
    data = {
        'ID': [],
        'Date': [],
        'User': [],
        'Description': [],
        'Cleanup': []
    }

    commands = {
        'snapper-list': "snapper list | sed '1,3d'",
    }

    app = QApplication(sys.argv)

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'Xerolinux Rollback Utility version {Version.getVersion()}')
        self.setFixedSize(QSize(800, 600))
        # setup stylesheet
        # the default system in qdarkstyle uses qtpy environment variable
        self.app.setStyleSheet(qdarkstyle.load_stylesheet())
        ###################################################
        # Vertical Layout ###
        verticalLayout = QVBoxLayout()
        verticalLayout.setAlignment(Qt.AlignTop)
        ####
        # Horizontal Layout Logo and QLabel for message
        topHorizontalLayout = QHBoxLayout()
        ####
        # Xerolinux Logotype Label
        xerolinuxLabel = QLabel(self)
        xerolinuxLabel.setPixmap(QPixmap(f'{FileUtil.getResourcePath()}/images/xerolinux-logo96x96.png'))
        # xerolinuxLabel.setStyleSheet("background-color: red")
        xerolinuxLabel.setFixedWidth(96)
        topHorizontalLayout.addWidget(xerolinuxLabel)
        ####
        # Info Label
        infoLabel = QLabel("Select the snapshot from the list below and click the rollback button.")
        # infoLabel.setStyleSheet("background-color: red")
        infoLabel.setFont(QFont('Fira Code', 14))
        infoLabel.setWordWrap(True)

        topHorizontalLayout.addWidget(infoLabel)
        #

        verticalLayout.addLayout(topHorizontalLayout)

        # Set the central widget of the Window.
        centralWidget = QWidget()
        centralWidget.setLayout(verticalLayout)
        self.setCentralWidget(centralWidget)
        self.show()
        sys.exit(self.app.exec())

    def exitApp(self):
        print(f'Locale dir ====> {FileUtil.getResourcePath()}')
        self.getSnapshotList()
        self.app.quit()

    # def refreshSnapshotsList(self):
    #     self.getSnapshotList()
    #     self.tableWidget.setColumnCount(4)
    #     horHeaders = []
    #     self.tableWidget.setRowCount(len(self.data['ID']))
    #     for n, key in enumerate(self.data):
    #         horHeaders.append(key)
    #         for m, item in enumerate(self.data[key]):
    #             newitem = QtWidgets.QTableWidgetItem(item)
    #             self.tableWidget.setItem(m, n, newitem)
    #
    #     self.tableWidget.setHorizontalHeaderLabels(horHeaders)

    def getSnapshotList(self):
        output = sp.getoutput(self.commands['snapper-list'])
        lines = output.splitlines()
        self.clearData()  # Clear data array
        for line in lines:
            # print(f'Line ===> {line}')
            # split line
            cols = line.split('|')
            # print(f'cols ====> {cols}')
            self.data['ID'].append(cols[0].rstrip())
            self.data['Date'].append(cols[3].rstrip())
            self.data['User'].append(cols[4].rstrip())
            self.data['Cleanup'].append(cols[5].rstrip())
            self.data['Description'].append(cols[6].rstrip())

    def clearData(self):
        for header in self.data:
            self.data[header].clear()
