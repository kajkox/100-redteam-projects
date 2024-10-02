import socket

# setting up constants for easier readability
TRANSPORT_PROT = socket.SOCK_STREAM # TCP
ADDRESS_FAM = socket.AF_INET    # IPv4
IP_ADD = '127.0.0.1'
PORT = 23985

# creating and connecting, requires server.py first
socketObject = socket.socket(family=ADDRESS_FAM, type=TRANSPORT_PROT)
socketObject.connect((IP_ADD, PORT))

print(f"Connection with {IP_ADD}:{PORT} successful!\n")
print("Type 'close' to close connection")

# runs until one side desides to disconnect
while True:
    data = input(">")
    if data == "close":
        socketObject.close()
        print(f"Connetion with {(IP_ADD, PORT)} closed!")
        break
    else:
        data = data.encode()
        socketObject.send(data)
        print(f"Received: {socketObject.recv(1024).decode()}")
