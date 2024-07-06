import socket

SERVER_ADD = '127.0.0.1'
SERVER_PORT = 21371
CLIENT_ADD = '127.0.0.1'
CLIENT_PORT = 21372

TRANSPORT_PROT = socket.SOCK_DGRAM # UDP
IP_FAM = socket.AF_INET # IPv4

serverSocket = socket.socket(family=IP_FAM, type=TRANSPORT_PROT)
serverSocket.bind((SERVER_ADD, SERVER_PORT))

while True:
    recv_data, address = serverSocket.recvfrom(1024)
    print(recv_data.decode())
    send_data = input(">")
    send_data = send_data.encode()
    serverSocket.sendto(send_data, (CLIENT_ADD, CLIENT_PORT))