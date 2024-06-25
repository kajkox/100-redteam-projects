import socket

def connect(ipv4_add: str = "", port: int = 42069):
    add = (ipv4_add, port)
    return socket.create_connection(add)