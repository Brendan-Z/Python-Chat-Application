from PyQt5.QtWidgets import *


class InvitePopup(QDialog):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("Available Users To Invite")
        vDialog = QVBoxLayout()
        inviteLabel = QLabel('Connected Users')

        sendInviteBtn = QPushButton('Send Invitation', self)
        sendInviteBtn.resize(sendInviteBtn.sizeHint())
        sendInviteBtn.clicked.connect(self.informInviteSent)

        cancelInviteBtn = QPushButton('Cancel', self)
        cancelInviteBtn.resize(cancelInviteBtn.sizeHint())
        cancelInviteBtn.clicked.connect(self.close)

        availableUsers = QListWidget()
        availableUsers.addItem('Test 1')
        availableUsers.addItem('Test 2')

        hInviteControls = QHBoxLayout()
        hInviteControls.addWidget(sendInviteBtn)
        hInviteControls.addWidget(cancelInviteBtn)

        vDialog.addWidget(inviteLabel)
        vDialog.addWidget(availableUsers)
        vDialog.addLayout(hInviteControls)

        self.setLayout(vDialog)
        self.exec_()

    def informInviteSent(self):
        msg = QMessageBox()
        msg.setText("Invites Sent To Specified Users!")
        msg.setInformativeText("\n\n\n\n\n\n\n")
        msg.setWindowTitle("Invitation Notification")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.resize(200, 200)
        returnValue = msg.exec()

        if (returnValue == QMessageBox.Ok):
            msg.close()
            self.close()
