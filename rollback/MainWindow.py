import sys
import subprocess as sp
from qtpy import QtWidgets
from rollback.api import FileUtil
from rollback.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    headers = {
        'ID': [],
        'Date': [],
        'User': [],
        'Description': [],
        'Cleanup': []
    }
    app = QtWidgets.QApplication(sys.argv)

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.exitPushButton.clicked.connect(self.exitApp)

    def exitApp(self):
        print(f'Locale dir ====> {FileUtil.getResourcePath()}')
        self.getSnapshotList()
        self.app.quit()

    @staticmethod
    def getSnapshotList():
        cmd = "snapper -c root list| sed '1,2d'"
        output = sp.getoutput(cmd)
        lines = output.splitlines()
        for line in lines:
            # print(f'Line ===> {line}')
            # split line
            cols = line.split('|')
            # print(f'cols ====> {cols}')
            for index, col in enumerate(cols):
                if index == 0:  # Id
                    print(f'id ===> {col}')
                elif index == 3:  # Date
                    print(f'Date ===> {col}')
                elif index == 4:  # User
                    print(f'User ===> {col}')
                elif index == 5:  # Cleanup
                    print(f'Cleanup ===> {col}')
                elif index == 6:  # Description
                    print(f'Description ===> {col}')

