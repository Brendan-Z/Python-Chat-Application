import select
import socket
import sys
import signal
import ssl

SERVER_HOST = 'localhost'


class Server(object):
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.allClient = {}
        self.groups = 0
        self.groupOwners = {}
        self.clientSockets = {}
        self.outputs = []  # list output sockets
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self.context.load_cert_chain(certfile="cert.pem", keyfile="cert.pem")
        self.context.load_verify_locations('cert.pem')
        self.context.set_ciphers('AES128-SHA')

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        self.server.listen(backlog)
        self.server = self.context.wrap_socket(self.server, server_side=True)

        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

        print(
            f'Server (IP Address: {SERVER_HOST}) listening to port: {port} ...')

    def sighandler(self, signum, frame):
        """ Clean up client outputs"""
        print('Shutting down server...')

        # Close existing client sockets
        for output in self.outputs:
            output.close()

        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        # inputs = [self.server, sys.stdin]
        inputs = [self.server]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional = select.select(
                    inputs, self.outputs, [])
            except select.error as e:
                break

            for sock in readable:
                sys.stdout.flush()
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print(
                        f'Chat server: got connection {client.fileno()} from {address}')
                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]

                    # Compute client name and send back
                    self.clients += 1
                    send(client, f'CLIENT: {str(address)}')
                    inputs.append(client)

                    self.clientmap[client] = (address, cname)
                    self.allClient[(address[0], address[1], cname)] = []
                    self.groupOwners[(address[0], address[1], cname)] = []
                    self.clientSockets[(
                        address[0], address[1], cname)] = client
                    self.outputs.append(client)

                else:
                    # handle all other sockets
                    try:
                        data = receive(sock)
                        if data:

                            if type(data) == int:
                                if (data == 2):
                                    send(
                                        sock, [self.allClient, self.groupOwners])
                                if (data == 3):
                                    self.groups = self.groups + 1
                                    clientInfo = self.clientmap[sock]
                                    self.allClient[(clientInfo[0][0], clientInfo[0][1], clientInfo[1])].append(
                                        self.groups)
                                    self.groupOwners[(clientInfo[0][0], clientInfo[0][1], clientInfo[1])].append(
                                        self.groups)
                            if type(data) == list:
                                clientInfo = self.clientmap[sock]
                                if data[0] == 0:
                                    if data[2] == (clientInfo[0][0], clientInfo[0][1], clientInfo[1]):
                                        send(self.clientSockets[data[1]], data)
                                if data[0] == 1:
                                    if (data[1] == data[2]):
                                        send(sock, data)
                                    else:
                                        for (ip, port, name), clientData in self.allClient.items():
                                            if data[1] in clientData:
                                                if data[2] != (ip, port, name):
                                                    clientToSendTo = self.clientSockets[(
                                                        ip, port, name)]
                                                    send(clientToSendTo, data)
                                if data[0] == 4:
                                    self.allClient[data[1]].append(data[2])
                        else:
                            print(f'Chat server: {sock.fileno()} hung up')
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            clientInfo = self.clientmap[sock]
                            keyToRemove = (
                                clientInfo[0][0], clientInfo[0][1], clientInfo[1])
                            self.clientmap.pop(sock)
                            self.allClient.pop(keyToRemove)
                            self.clientSockets.pop(keyToRemove)
                    except socket.error as e:
                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)
                        self.clients -= 1
                        clientInfo = self.clientmap[sock]
                        keyToRemove = (
                            clientInfo[0][0], clientInfo[0][1], clientInfo[1])
                        self.clientmap.pop(sock)
                        self.allClient.pop(keyToRemove)
                        self.clientSockets.pop(keyToRemove)

        self.server.close()


if __name__ == "__main__":
    host = "localhost"
    port = 5555
    chat_server = Server(host, port)
