from PyQt5.QtWidgets import *
from chat import ChatWindow


class GroupChatWindow(ChatWindow):

    def __init__(self, stackedWidget):
        super().__init__(stackedWidget)
        self.addGroupChatUI()

    def addGroupChatUI(self):
        vGroupChat = QVBoxLayout()

        membersLabel = QLabel("Members")
        vGroupChat.addWidget(membersLabel)

        memberList = QListWidget()
        memberList.addItem('Test member 1')
        memberList.addItem('Test member 2')
        vGroupChat.addWidget(memberList)

        self.inviteBtn = QPushButton('Invite', self)
        self.inviteBtn.resize(self.inviteBtn.sizeHint())
        vGroupChat.addWidget(self.inviteBtn)

        self.hMaster.addLayout(vGroupChat)
        self.show()
