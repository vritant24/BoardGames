from mysocket import *

PORT = 7766

def initServer():
    sock = createTCPSocket()
    bindSocketToPortandListen(sock, PORT)

    while(True):
        (client, addr) = acceptConnections(sock)
        (client_ip, port) = addr
        print(client_ip)
        print(client.recv(1024))
        break;

    closeSocket(sock)



initServer()
