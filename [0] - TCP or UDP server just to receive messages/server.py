from socket import *
from socketserver import *

def createServerSocket() -> socket:
    print("[SERVER] Creating socket object...")
    addres_fam = AF_INET
    transport_prot = SOCK_STREAM    # can implement UDP in the future
    newSocketObject = socket(family=addres_fam, type=transport_prot)
    print("[SERVER] Socket object created succesfully!")
    return newSocketObject

def bindToLocalServerSocket(local_ipv4_add: str, local_port: int, socketObject: socket = createServerSocket()) -> socket:
    print("[SERVER] Binding to local socket")
    socket_add = (local_ipv4_add, local_port)
    socketObject.bind(socket_add)
    return socketObject
    

def startListening(remote_ipv4_add: str, remote_port: int, boundSocketObject: socket):
    boundSocketObject.