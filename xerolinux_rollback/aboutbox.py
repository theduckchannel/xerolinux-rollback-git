import qdarkstyle
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy.QtCore import *
from xerolinux_rollback.version import Version
from xerolinux_rollback.api import FileUtil


class AboutBox(QDialog):

    def __init__(self, parent=None):
        super(AboutBox, self).__init__(parent)
        self.setFixedWidth(480)
        self.centerMe()
        self.setWindowTitle(f'{Version.getAppName()} v. {Version.getVersion()}')
        alignCenter = Qt.AlignHCenter
        self.okButton = QDialogButtonBox(QDialogButtonBox.Ok)
        self.okButton.accepted.connect(self.hideMe)
        self.layout = QVBoxLayout()
        # ------------------------------------------------------------------------------------------
        # Logo
        self.logoLabel = QLabel()
        self.logoLabel.setPixmap(QPixmap(f'{FileUtil.getResourcePath()}/images/xerolinux-logo128x128.png'))
        self.layout.addWidget(self.logoLabel)
        self.logoLabel.setAlignment(alignCenter)
        # ------------------------------------------------------------------------------------------
        # text about box
        xerolinux_rollbackLabel = QLabel(f'<strong>{Version.getAppName()}</strong>')
        xerolinux_rollbackLabel.setTextFormat(Qt.RichText)
        xerolinux_rollbackLabel.setAlignment(alignCenter)
        self.layout.addWidget(xerolinux_rollbackLabel)
        versionLabel = QLabel(f'Version <strong>{Version.getVersion()}</strong>')
        versionLabel.setTextFormat(Qt.RichText)
        versionLabel.setAlignment(alignCenter)
        self.layout.addWidget(versionLabel)
        # contributors text
        contHeader = QLabel('Contributors')
        contHeader.setAlignment(Qt.AlignHCenter)
        cont1 = QLabel('<a href="https://www.youtube.com/c/TheDuckChannel">The Duck Channel</a>')
        cont1.setAlignment(Qt.AlignHCenter)
        cont2 = QLabel('<a href="https://github.com/theduckchannel">Fred Junior</a>')
        cont2.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(contHeader)
        self.layout.addWidget(cont1)
        self.layout.addWidget(cont2)

        # warrantyText
        textAboutLabel = QLabel('This program comes with absolutely no warranty')
        textAboutLabel.setTextFormat(Qt.RichText)
        textAboutLabel.setAlignment(alignCenter)
        self.layout.addWidget(textAboutLabel)
        urlLink = '<a href=\"https://github.com/theduckchannel/xerolinux-rollback/blob/master/LICENSE\">https://github.com/theduckchannel/xerolinux-rollback/blob/master/LICENSE</a>'
        urlLabel = QLabel(urlLink)
        urlLabel.setAlignment(alignCenter)
        urlLabel.setOpenExternalLinks(True)
        self.layout.addWidget(urlLabel)
        self.layout.addSpacing(30)

        self.layout.addWidget(self.okButton, alignment=Qt.AlignHCenter)
        self.setLayout(self.layout)

    def centerMe(self):
        screenGeo = QApplication.desktop().screenGeometry()
        x = (screenGeo.width() - self.width()) / 2
        # y = (screenGeo.height() - self.height()) / 2
        self.move(x, 100)

    def hideMe(self):
        self.hide()
