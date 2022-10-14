from PyQt5.QtWidgets import *


class ConnectedWindow(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.clientWindow = mainWindow
        self.initUI()

    def initUI(self):
        vMaster = QVBoxLayout()
        vBoxOne = QVBoxLayout()
        vBoxTwo = QVBoxLayout()
        clientList = QListWidget()
        clientList.addItem('Test 1')
        clientList.addItem('Test 2')
        clientList.addItem('Test 3')
        vBoxOne.addWidget(clientList)
        hBoxChatroom = QHBoxLayout()

        self.oneToOneBtn = QPushButton('Connect 1:1', self)
        self.oneToOneBtn.resize(self.oneToOneBtn.sizeHint())

        vBoxOne.addWidget(self.oneToOneBtn)

        chatroomList = QListWidget()
        chatroomList.addItem('Groupchat test 1')
        chatroomList.addItem('Groupchat test 2')

        self.createChatroomBtn = QPushButton('Create Chatroom', self)
        self.createChatroomBtn.resize(self.createChatroomBtn.sizeHint())
        self.joinChatroomBtn = QPushButton('Join Chatroom', self)
        self.joinChatroomBtn.resize(self.joinChatroomBtn.sizeHint())

        vBoxTwo.addWidget(chatroomList)
        hBoxChatroom.addWidget(self.createChatroomBtn)
        hBoxChatroom.addWidget(self.joinChatroomBtn)
        vBoxTwo.addLayout(hBoxChatroom)

        self.disconnectBtn = QPushButton('Disconnect', self)
        self.disconnectBtn.resize(self.disconnectBtn.sizeHint())

        vMaster.addLayout(vBoxOne)
        vMaster.addLayout(vBoxTwo)
        vMaster.addWidget(self.disconnectBtn)

        self.setLayout(vMaster)
        self.show()
