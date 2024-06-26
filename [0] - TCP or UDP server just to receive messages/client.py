import socket

HOST_ADD = "127.0.0.1"
HOST_PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_ADD, HOST_PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

    print(f"Received {data}!")