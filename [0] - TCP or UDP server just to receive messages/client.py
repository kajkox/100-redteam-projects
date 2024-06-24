from socket import *
from socketserver import *

def createSocket():
    print("[CLIENT] Creating socket object...")
    addres_fam = AF_INET
    transport_prot = SOCK_STREAM    
    newSocketObject = socket(family=addres_fam, type=transport_prot)
    print("[CLIENT] Socket object created successfully!")
    return newSocketObject

def bindToLocalSocket(local_ipv4_add: str, local_port: int, socketObject: socket = createSocket()) -> socket:
    print("[CLINET] Binding to local socket...")
    socketAdress = (local_ipv4_add, local_port)
    socketObject.bind(socketAdress)
    print(f"[CLIENT] Socket bound succesfully to {local_ipv4_add}:{local_port}")
    return socketObject

def requestConnection(remote_ipv4_add: str, remote_port: int, local_socket_object : socket):
    local_socket_object.connect((remote_ipv4_add, remote_port))
    