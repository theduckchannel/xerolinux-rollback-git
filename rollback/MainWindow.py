import sys
import subprocess as sp
from qtpy import QtWidgets
from rollback.api import FileUtil
from rollback.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
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

    app = QtWidgets.QApplication(sys.argv)

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.exitPushButton.clicked.connect(self.exitApp)
        self.refreshSnapshotsList()

    def exitApp(self):
        print(f'Locale dir ====> {FileUtil.getResourcePath()}')
        self.getSnapshotList()
        self.app.quit()

    def refreshSnapshotsList(self):
        self.getSnapshotList()
        self.tableWidget.setColumnCount(4)
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for idx, col in enumerate(self.data[key]):
                print(f'index ===> {idx} data ===> {col}')

        self.tableWidget.setHorizontalHeaderLabels(horHeaders)

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
