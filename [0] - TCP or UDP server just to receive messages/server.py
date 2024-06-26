import socket

HOST_ADD = "127.0.0.1"  #
HOST_PORT = 65432   # constants on where to bind the socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # 
    s.bind((HOST_ADD, HOST_PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}!")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)