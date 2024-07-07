import socket
# In UDP two socket objects need to be bound, but they do not need to establish a 3-way handshake to operate
# both the client and server side contain these values
CLIENT_ADD = '127.0.0.1'
CLIENT_PORT = 21372
SERVER_ADD = '127.0.0.1'
SERVER_PORT = 21371

TRANPORT_PROT = socket.SOCK_DGRAM # UDP
IP_FAMILY = socket.AF_INET # IPv4

# creating and binding
clientSocket = socket.socket(family=IP_FAMILY, type=TRANPORT_PROT)
clientSocket.bind((CLIENT_ADD, CLIENT_PORT))
print(f"[CLIENT] Bound succesfully to {(CLIENT_ADD, CLIENT_PORT)}")

# main loop
while True:
    send_data = input(">")  # capturing data
    if send_data == "close":    # break case
        print(f"Connection with {(SERVER_ADD, SERVER_PORT)} closed by localhost!")
        send_data = send_data.encode()
        clientSocket.sendto(send_data, (SERVER_ADD, SERVER_PORT))
        clientSocket.close()
        break

    send_data = send_data.encode()  # encoding
    clientSocket.sendto(send_data, (SERVER_ADD, SERVER_PORT))   # sending to the client_ip, server_ip tuple (socket)
    recv_data, address = clientSocket.recvfrom(1024)    # recvfrom method returns data and the address
    if recv_data.decode() == "close":    # second break case
        print(f"Connection with {address} closed by server!")
        clientSocket.close()
        break

    print(recv_data.decode())   # decoded data is printed
