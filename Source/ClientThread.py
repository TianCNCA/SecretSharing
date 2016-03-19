import threading
from Codes import *


class ClientThread(threading.Thread):
    def __init__(self, connection, cmd):
        threading.Thread.__init__(self)
        self.connection = connection
        self.cmd = cmd
        self.secretPart = None


    def run(self):
        try:
            if self.cmd == "s":
                self.sendToClients()
            elif self.cmd == "g":
                self.recvSecretFromClients()
        except:
            print "Lost connection..."


    def sendToClients(self):
        lenSending = len(self.secret)
        protocolTx = str(SEND_SECRET) + SEPERATOR
        msg = protocolTx + self.secret
        self.connection.sendall(msg)


    def recvSecretFromClients(self):
        self.connection.send(str(GET_SECRET))
        data = self.connection.recv(SOCKET_SIZE)
        self.secretPart = data
        print "Secret Recieved: {0}".format(self.secretPart)


    def hasSecretPart(self):
        return not self.secretPart == None
