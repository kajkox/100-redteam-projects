import socket

HOST_ADD = "127.0.0.1"  #
HOST_PORT = 65432   # constants on where to bind the socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # socket.socket returns a socket object that supports context manager, so using with keyword
    s.bind((HOST_ADD, HOST_PORT))   # binding the socket object to addres, port tuple
    s.listen()  # listening for connections
    connection, address = s.accept()    # accept method of the socket object returns two objects, one for the connection, one for the address
    with connection:    # also supports context manager, so using with
        print(f"Connected by {address}!")   # printing the client address
        while True: # while loop, here reduntant because the client disconnects after receiving the message
            data = connection.recv(1024)    # receiving the message from the client with 1024 buffer size
            if not data:    # break case, if the data sent is empty => "b''"
                break
            connection.sendall(data)    # sending back the message from the client