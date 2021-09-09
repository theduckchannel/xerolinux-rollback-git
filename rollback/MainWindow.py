import sys
import subprocess as sp
from qtpy import QtWidgets
from rollback.api import FileUtil
from rollback.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
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
        print(output)