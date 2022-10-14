from PyQt5.QtWidgets import *


class ChatWindow(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.clientWindow = mainWindow
        self.initUI()

    def initUI(self):
        self.hMaster = QHBoxLayout()
        vChat = QVBoxLayout()
        chatLabel = QLabel("Chat with NAME HERE")
        vChat.addWidget(chatLabel)

        self.chatArea = QTextBrowser()
        vChat.addWidget(self.chatArea)

        self.textInput = QLineEdit()
        vChat.addWidget(self.textInput)

        hBoxLayout = QHBoxLayout()
        sendChatBtn = QPushButton('Send Message', self)
        sendImageBtn = QPushButton('Send Image', self)
        hBoxLayout.addWidget(sendChatBtn)
        hBoxLayout.addWidget(sendImageBtn)
        vChat.addLayout(hBoxLayout)

        self.closeChatBtn = QPushButton('Close Chat', self)
        self.closeChatBtn.resize(self.closeChatBtn.sizeHint())

        vChat.addWidget(self.closeChatBtn)
        self.hMaster.addLayout(vChat)

        self.setLayout(self.hMaster)
        self.show()
