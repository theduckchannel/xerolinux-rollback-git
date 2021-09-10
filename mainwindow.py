import sys
import subprocess as sp
import qdarkstyle
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy.QtCore import *
from api import *
from version import Version
from aboutbox import AboutBox


# Only for debug .setStyleSheet("background-color: red")

class mainWindow(QMainWindow):
    horHeaders = ['ID', 'Type', 'Date', 'User', 'Cleanup', 'Description']
    sudoPassword = ''
    commands = {
        'snapper-list': "snapper list | sed '1,3d'"
    }
    app = QApplication(sys.argv)
    snapshotsTableWidget = QTableWidget()
    aboutBox = AboutBox()

    def __init__(self):
        super().__init__(parent=None)
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
        topHorizontalLayout.addWidget(infoLabel)
        ####
        # aboutPushButton
        aboutPushButton = QPushButton()
        aboutPushButton.setIcon(QIcon(f'{FileUtil.getResourcePath()}/images/about.png'))
        aboutPushButton.setIconSize(QSize(32, 32))
        aboutPushButton.setFixedSize(QSize(32, 32))
        aboutPushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        aboutPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        aboutPushButton.clicked.connect(self.showAboutBox)
        topHorizontalLayout.addWidget(aboutPushButton)
        ###
        verticalLayout.addLayout(topHorizontalLayout)
        ############
        # Snapshots List QTableWidget
        self.snapshotsTableWidget.verticalHeader().hide()
        verticalLayout.addWidget(self.snapshotsTableWidget)
        self.snapshotsTableWidget.setColumnCount(6)
        self.snapshotsTableWidget.setHorizontalHeaderLabels(self.horHeaders)
        self.snapshotsTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.snapshotsTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        ############
        # Two PushButtons (Rollback and Exit)
        rollbackPushButton = QPushButton("&Rollback")
        rollbackPushButton.setFixedHeight(32)
        rollbackPushButton.setIcon(QIcon(f'{FileUtil.getResourcePath()}/images/rollback.png'))
        rollbackPushButton.setIconSize(QSize(24, 24))
        rollbackPushButton.clicked.connect(self.rollback)
        rollbackPushButton.setFont(QFont('Fira Code', 12))
        exitPushButton = QPushButton("&Exit")
        exitPushButton.setFixedHeight(32)
        exitPushButton.setIcon(QIcon(f'{FileUtil.getResourcePath()}/images/exit.png'))
        exitPushButton.setFont(QFont('Fira Code', 12))
        exitPushButton.clicked.connect(self.exitApp)
        bottonHorizontalLayout = QHBoxLayout()
        bottonHorizontalLayout.addWidget(rollbackPushButton)
        bottonHorizontalLayout.addWidget(exitPushButton)
        verticalLayout.addLayout(bottonHorizontalLayout)
        #######
        # Set the central widget of the Window.
        centralWidget = QWidget()
        centralWidget.setLayout(verticalLayout)
        self.setCentralWidget(centralWidget)
        ############
        if self.checkSudoPassword():
            self.show()
            self.refreshSnapshotsList()
            sys.exit(self.app.exec())
        else:
            sys.exit(1)

    def checkSudoPassword(self):
        retValue = False
        text, ok = QInputDialog.getText(None, "Attention", "Sudo Password:", QLineEdit.Password)
        if ok and text:
            self.sudoPassword = str(text)
            statusOuput = sp.getstatusoutput(f'echo \'{self.sudoPassword}\' | sudo -S whoami')
            if statusOuput[0] == 0:
                retValue = True
            else:
                Alert('Error', 'Wrong password!').exec()

        return retValue

    def exitApp(self):
        self.app.quit()
        sys.exit(0)

    def rollback(self):
        index = self.snapshotsTableWidget.selectionModel().currentIndex()
        snapshotID = index.sibling(index.row(), 0).data()
        print(f'Snapshot ID: {snapshotID}')

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

    def showAboutBox(self):
        self.aboutBox.show()

