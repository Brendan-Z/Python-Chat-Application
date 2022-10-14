import ipaddress
import sys
from PyQt5.QtWidgets import *
from connection import Connection
from connected import ConnectedWindow
from chat import ChatWindow
from invite import InvitePopup
from groupChat import GroupChatWindow
from backend.client import Client


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uiController = QStackedWidget()

        self.Connection = Connection(self)
        self.Connection.connectButton.clicked.connect(
            self.onConnectClick)
        self.Connection.quitButton.clicked.connect(self.quitApp)

        self.connectedWindow = ConnectedWindow(self)
        self.connectedWindow.oneToOneBtn.clicked.connect(
            self.openIndividualChatroom)
        self.connectedWindow.createChatroomBtn.clicked.connect(
            self.openGroupChatroom)
        self.connectedWindow.joinChatroomBtn.clicked.connect(
            self.openGroupChatroom)
        self.connectedWindow.disconnectBtn.clicked.connect(
            self.disconnectFromServer)

        self.chatWindow = ChatWindow(self)
        self.chatWindow.closeChatBtn.clicked.connect(self.exitChatroom)

        self.groupChatWindow = GroupChatWindow(self)
        self.groupChatWindow.closeChatBtn.clicked.connect(self.exitChatroom)
        self.groupChatWindow.inviteBtn.clicked.connect(self.inviteClicked)

        self.uiController.addWidget(self.Connection)
        self.uiController.addWidget(self.connectedWindow)
        self.uiController.addWidget(self.chatWindow)
        self.uiController.addWidget(self.groupChatWindow)
        self.setGeometry(350, 100, 300, 300)
        self.setCentralWidget(self.uiController)

    def onConnectClick(self):
        print(self.Connection.ipEdit.text())
        print(self.Connection.portNumEdit.text())
        print(self.Connection.nicknameEdit.text())
        ipAddress = self.Connection.ipEdit.text()
        portNumber = self.Connection.portNumEdit.text()
        nickname = self.Connection.nicknameEdit.text()
        if (ipAddress == ""):
            client = Client(nickname, portNumber)
        else:
            client = Client(nickname, portNumber, ipAddress)

        self.Connection.ipEdit.clear()
        self.Connection.portNumEdit.clear()
        self.Connection.nicknameEdit.clear()
        self.uiController.setCurrentWidget(self.connectedWindow)

    def openIndividualChatroom(self):
        self.uiController.setCurrentWidget(self.chatWindow)
        self.setWindowTitle('Now Chatting 1:1')

    def openGroupChatroom(self):
        self.uiController.setCurrentWidget(self.groupChatWindow)
        self.setWindowTitle('Now In Group Chat')

    def inviteClicked(self):
        InvitePopup()

    def quitApp(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def disconnectFromServer(self, event):
        reply = QMessageBox.question(self, 'Message', 'Disconnect From Chat Server?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.uiController.setCurrentWidget(self.Connection)
            self.setWindowTitle("Connect to a Chat Server!")

    def exitChatroom(self, event):
        reply = QMessageBox.question(self, 'Message', 'Exit Chatroom?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.uiController.setCurrentWidget(self.connectedWindow)
            self.setWindowTitle("Connected - Start Chatting!")


if __name__ == '__main__':
    clientApp = QApplication(sys.argv)
    clientWindow = ClientWindow()
    clientWindow.show()

    sys.exit(clientApp.exec_())
