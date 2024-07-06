import socket

CLIENT_ADD = '127.0.0.1'
CLIENT_PORT = 21372
SERVER_ADD = '127.0.0.1'
SERVER_PORT = 21371

TRANPORT_PROT = socket.SOCK_DGRAM # UDP
IP_FAMILY = socket.AF_INET # IPv4

clientSocket = socket.socket(family=IP_FAMILY, type=TRANPORT_PROT)
clientSocket.bind((CLIENT_ADD, CLIENT_PORT))
print(f"[CLIENT] Bound succesfully to {(CLIENT_ADD, CLIENT_PORT)}")

while True:
    send_data = input(">")
    if send_data == "close":
        print(f"Connection with {(SERVER_ADD, SERVER_PORT)} closed by localhost!")
        break

    send_data = send_data.encode()
    clientSocket.sendto(send_data, (SERVER_ADD, SERVER_PORT))
    recv_data, address = clientSocket.recvfrom(1024)
    if recv_data == "close":
        print(f"Connection with {address} closed by server!")
        break

    print(recv_data.decode())
