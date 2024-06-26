import socket

HOST_ADD = "127.0.0.1"  # 
HOST_PORT = 65432   # constants where to connect
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # creating a socket object compliant with the context manager
    s.connect((HOST_ADD, HOST_PORT))    # connecting to the socket, with the addres, port tuple
    s.sendall(b"Hello, world")  # sending the message in byte format
    data = s.recv(1024) # receiving the data from the client with 1024 buffer size

    print(f"Received {data}!")  # printing the message