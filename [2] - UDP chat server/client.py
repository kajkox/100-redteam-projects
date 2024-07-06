import socket

CLIENT_ADD = '127.0.0.1'
CLIENT_PORT = 21372
SERVER_ADD = '127.0.0.1'
SERVER_PORT = 21371

TRANPORT_PROT = socket.SOCK_DGRAM
IP_FAMILY = socket.AF_INET

clientSocket = socket.socket(family=IP_FAMILY, type=TRANPORT_PROT)
clientSocket.bind((CLIENT_ADD, CLIENT_PORT))

while True:
    send_data = input(">")
    send_data = send_data.encode()
    clientSocket.sendto(send_data, (SERVER_ADD, SERVER_PORT))
    data, address = clientSocket.recvfrom(1024)
    print(data.decode())
