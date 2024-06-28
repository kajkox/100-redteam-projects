import socket

TRANSPORT_PROT = socket.SOCK_DGRAM
ADDRESS_FAM = socket.AF_INET
IP_ADD = '127.0.0.1'
PORT = 21372

socketObject = socket.socket(family=ADDRESS_FAM, type=TRANSPORT_PROT)
