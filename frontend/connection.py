import sys
from PyQt5.QtWidgets import *


class Connection(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.clientWindow = mainWindow
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()
        hBoxIP = QHBoxLayout()
        self.ipEdit = QLineEdit()
        hBoxIP.addWidget(QLabel('Enter IP Address: '))
        hBoxIP.addWidget(self.ipEdit)

        hBoxPort = QHBoxLayout()
        self.portNumEdit = QLineEdit()
        hBoxPort.addWidget(QLabel('Enter Port Number: '))
        hBoxPort.addWidget(self.portNumEdit)

        hBoxNickname = QHBoxLayout()
        self.nicknameEdit = QLineEdit()
        hBoxNickname.addWidget(QLabel('Nickname: '))
        hBoxNickname.addWidget(self.nicknameEdit)

        vLayout.addLayout(hBoxIP)
        vLayout.addLayout(hBoxPort)
        vLayout.addLayout(hBoxNickname)

        buttonBox = QHBoxLayout()
        self.quitButton = QPushButton('Quit Application', self)
        self.quitButton.resize(self.quitButton.sizeHint())

        self.connectButton = QPushButton('Connect', self)
        self.connectButton.resize(self.connectButton.sizeHint())

        buttonBox.addWidget(self.quitButton)
        buttonBox.addWidget(self.connectButton)
        vLayout.addLayout(buttonBox)

        self.setLayout(vLayout)
        self.clientWindow.setWindowTitle('Connect to a chat server!')
        self.show()
