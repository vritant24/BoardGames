from mysocket import *

SERVER_IP = "127.0.0.1" #currently localhost
PORT = 7766

def runClient():
    sock = createTCPSocket()
    connectToServer(sock, SERVER_IP, PORT)
    sock.send(b"HI") #has to b sent in binary
    closeSocket(sock)

runClient()