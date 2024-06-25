import socket

def createServerSocket() -> socket.socket:
    socketObject = socket.socket(family=socket.AF_INET, proto=socket.SOCK_STREAM)
    return socketObject

def initializeServerSocket(ipv4_add: str, port: int):
    add = (ipv4_add, port)
    serverSocket = createServerSocket()
    serverSocket.bind(add)
    
    