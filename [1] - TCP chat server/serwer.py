import socket

TRANSPORT_PROT = socket.SOCK_STREAM # TCP
ADDRESS_FAM = socket.AF_INET    # IPv4
IP_ADD = '127.0.0.1'
PORT = 23985
socketObject = socket.socket(family=ADDRESS_FAM, type=TRANSPORT_PROT)

socketObject.bind((IP_ADD, PORT))
socketObject.listen()
connection, address = socketObject.accept()
print(f"Connection accepted from {address}")
while True:
    data = input("> ")
    if data == "close":
        connection.close()
        print("Connection closed!")
        break
    else:
    print(f"Received: {connection.recv(1024).decode()}")
        data = data.encode()
        connection.sendall(data)