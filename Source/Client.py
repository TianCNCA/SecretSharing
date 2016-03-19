import socket
import sys
from Codes import *
import time

serverURL = ""
port = 0
secret = ""


def init():
    global serverURL, port

    if len(sys.argv) == 1:
        serverURL = 'localhost'
        port = 5252
    elif not len(sys.argv) == 3:
        raise "Arguments are: [host] [port], leave as blank for localhost"
    elif len(sys.argv) == 3:
        serverURL = sys.argv[1]
        port = int(sys.argv[2])
    print "Host: {0} Port: {1}".format(serverURL, port)


def connectToSever():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Connecting..."
    serverAddress = (serverURL, port)
    notConnected = True

    while notConnected:
        try:
            clientSocket.connect(serverAddress)
            notConnected = False
        except socket.error as msg:
            print "No connection to: {0}".format(serverAddress)
            time.sleep(2)

    print "Connected!"

    return clientSocket
# end connectToSever


def handleData(data, clientSocket):
    global secret

    if len(data) > 0:
        print "Data Received: " + str(data)

        if int(data[0]) == SEND_SECRET:
            print "Aquiring Secret"
            tmp = data.split("::")
            secret = tmp[1]
            print "Secret is: {0}".format(secret)
        elif int(data[0]) == GET_SECRET:
            print "Sending My Secret: {0}".format(secret)
            if secret != "":
                clientSocket.sendall(secret)
                print "Sent"
            else:
                print "Secret is null"
                clientSocket.sendall("I have no secret")
        elif int(data[0]) == STOP_RECEIVING:
            print "Ending Client"
            clientSocket.close()
            sys.exit()
        else:
            clientSocket.sendall("Unknown Command")
# end handleData


def main():
    clientSocket = connectToSever()
    print "Waiting for Instruction"

    while True:
        time.sleep(2)
        print "Listening..."
        data = clientSocket.recv(SOCKET_SIZE)
        handleData(data, clientSocket)
    # end while

    print "Closing Client Socket"
    clientSocket.close()
# end main


init()
main()
