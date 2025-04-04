import socket

# setting up some constants for easier readability
TRANSPORT_PROT = socket.SOCK_STREAM # TCP
ADDRESS_FAM = socket.AF_INET    # IPv4
IP_ADD = '127.0.0.1'
PORT = 23985

# has to be done first, otherwise the client won't connect
socketObject = socket.socket(family=ADDRESS_FAM, type=TRANSPORT_PROT)
socketObject.bind((IP_ADD, PORT))
socketObject.listen()

connection, address = socketObject.accept()
print(f"Connection accepted from {address}")
print("Input 'close' to close connection.")

# runs until one side desides to disconnect
while True:
    print(f"Received: {connection.recv(1024).decode()}")
    data = input(">")
    if data == "close":
        print(f"Connection with {address} closed!")
        connection.close()
        break
    else:
        data = data.encode()
        connection.send(data)
