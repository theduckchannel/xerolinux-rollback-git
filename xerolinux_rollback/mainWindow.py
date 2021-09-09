import os
import sys
import subprocess as sp
import qdarkstyle
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy.QtCore import *
from xerolinux_rollback.api import FileUtil
from xerolinux_rollback.version import Version


# Only for debug .setStyleSheet("background-color: red")


class mainWindow(QMainWindow):
    horHeaders = ['ID', 'Type', 'Date', 'User', 'Cleanup', 'Description']
    commands = {
        'snapper-list': "snapper list | sed '1,3d'",
    }
    app = QApplication(sys.argv)
    snapshotsTableWidget = QTableWidget()

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
        infoLabel = QLabel("Select the snapshot from the list below and click the xerolinux_rollback button.")
        # infoLabel.setStyleSheet("background-color: red")
        infoLabel.setFont(QFont('Fira Code', 14))
        infoLabel.setWordWrap(True)
        ###
        topHorizontalLayout.addWidget(infoLabel)
        verticalLayout.addLayout(topHorizontalLayout)
        ############
        # Snapshots List QTableWidget
        self.snapshotsTableWidget.verticalHeader().hide()
        verticalLayout.addWidget(self.snapshotsTableWidget)
        self.snapshotsTableWidget.setColumnCount(6)
        self.snapshotsTableWidget.setHorizontalHeaderLabels(self.horHeaders)
        ############
        # Set the central widget of the Window.
        centralWidget = QWidget()
        centralWidget.setLayout(verticalLayout)
        self.setCentralWidget(centralWidget)
        ############
        self.show()
        self.refreshSnapshotsList()
        sys.exit(self.app.exec())

    def exitApp(self):
        self.app.quit()

    def refreshSnapshotsList(self):
        lines = self.getSnapshotLines()
        # print(lines)
        self.snapshotsTableWidget.setRowCount(len(lines))
        for idx, line in enumerate(lines):
            col = line.split('|')
            # ID
            idItem = QTableWidgetItem(col[0].rstrip())
            self.snapshotsTableWidget.setItem(idx, 0, idItem)
            # Type
            typeItem = QTableWidgetItem(col[1].rstrip())
            self.snapshotsTableWidget.setItem(idx, 1, typeItem)
            # Date
            dateItem = QTableWidgetItem(col[3].rstrip())
            self.snapshotsTableWidget.setItem(idx, 2, dateItem)
            # User
            userItem = QTableWidgetItem(col[4].rstrip())
            self.snapshotsTableWidget.setItem(idx, 3, userItem)
            # Cleanup
            cleanupItem = QTableWidgetItem(col[5].rstrip())
            self.snapshotsTableWidget.setItem(idx, 4, cleanupItem)
            # Description
            descriptionItem = QTableWidgetItem(col[6].rstrip())
            self.snapshotsTableWidget.setItem(idx, 5, descriptionItem)

        header = self.snapshotsTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.Stretch)
        self.snapshotsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        if len(lines) > 0:
            self.snapshotsTableWidget.selectRow(0)

    def getSnapshotLines(self):
        output = sp.getoutput(self.commands['snapper-list'])
        lines = output.splitlines()
        return lines

    def clearData(self):
        for header in self.data:
            self.data[header].clear()
