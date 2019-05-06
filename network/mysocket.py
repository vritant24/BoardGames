import socket
import sys

MAX_LENGTH = 4096

# returns socket    
def createTCPSocket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except socket.err as err:
        raise err

def bindSocketToPortandListen(sock, port):
    sock.bind(('', port))
    sock.listen()

# returns (client, address)
def acceptConnections(sock):
    return sock.accept()

def connectToServer(sock, ip, port):
    sock.connect((ip, port))

def closeSocket(sock):
    sock.close()

