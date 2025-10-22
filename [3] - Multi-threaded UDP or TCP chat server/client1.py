import socket
from macros.py import *

# macros
SERVER_IP = "127.0.0.1"
SERVER_PORT = 54321

CLIENT_IP = "127.0.0.1"
CLIENT_PORT =

IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

# creating
socket_obj = socket.socket(IPv4, TCP)

# binding
socket_obj.bind()
