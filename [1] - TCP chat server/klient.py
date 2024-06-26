import socket

TRANSPORT_PROT = socket.SOCK_STREAM # TCP
ADDRESS_FAM = socket.AF_INET    # IPv4
IP_ADD = '127.0.0.1'
PORT = 23985
socketObject = socket.socket(family=ADDRESS_FAM, type=TRANSPORT_PROT)

socketObject.connect((IP_ADD, PORT))
print(f"Connection with {IP_ADD}:{PORT} successful!\n")
print("Type 'close' to end connection")
while True:
    print(f"Received: {socketObject.recv(1024).decode()}")
    data = input("> ")
    if data == "close":
        socketObject.close()
        print("Connection closed!")
        break
    else:

        data = data.encode()
        socketObject.sendall(data)
