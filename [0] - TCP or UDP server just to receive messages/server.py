import socket

def setupServer():
    try:
        HOST_ADD = "127.0.0.1"
        HOST_PORT = 65432

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST_ADD, HOST_PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    connection.sendall(data)
    except KeyboardInterrupt:
        return 0
    
setupServer()