import socket
import sys
import ssl
from PyQt5.QtWidgets import *

SERVER_HOST = 'localhost'


class Client():
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        self.addr = ""
        self.portAddr = 0

        self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock = self.context.wrap_socket(
                self.sock, server_hostname=host)

            self.sock.connect((host, self.port))
            print(f'Now connected to chat server@ port {self.port}')
            self.connected = True

        except socket.error as e:
            print(f'Failed to connect to chat server @ port {self.port}')
            sys.exit(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())
