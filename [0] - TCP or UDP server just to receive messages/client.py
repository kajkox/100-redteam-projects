from socket import *
from socketserver import *

def createClientSocket() -> socket:
    print("[CLIENT] Creating socket object...")
    addres_fam = AF_INET
    transport_prot = SOCK_STREAM    # can implement UDP in the future
    newSocketObject = socket(family=addres_fam, type=transport_prot)
    print("[CLIENT] Socket object created successfully!")
    return newSocketObject

def bindToLocalClientSocket(local_ipv4_add: str, local_port: int, socketObject: socket = createClientSocket()) -> socket:
    print("[CLINET] Binding to local socket...")
    socket_add = (local_ipv4_add, local_port)
    socketObject.bind(socket_add)
    print(f"[CLIENT] Socket bound succesfully to {local_ipv4_add}:{local_port}")
    return socketObject

def requestConnectionToServerSocket(remote_ipv4_add: str, remote_port: int, boundSocketObject : socket):
    print("[CLIENT] Attempting connection...")
    server_socket_add = (remote_ipv4_add, remote_port)
    boundSocketObject.connect(server_socket_add)
    print("[CLIENT] Connected!")
    