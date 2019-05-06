from mysocket import *

SERVER_IP = "127.0.0.1" #currently localhost
PORT = 7766

def runClient():
    sock = createTCPSocket()
    connectToServer(sock, SERVER_IP, PORT)
    sock.send(b"Hello") #has to b sent in binary
    print(sock.recv(1024))
    closeSocket(sock)

runClient()