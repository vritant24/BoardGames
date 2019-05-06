from mysocket import *

PORT = 7766

def initServer():
    sock = createTCPSocket()
    bindSocketToPortandListen(sock, PORT)

    while(True):
        (client, addr) = acceptConnections(sock)
        (client_ip, port) = addr
        print(client_ip)
        break;

    closeSocket(sock)



initServer()
