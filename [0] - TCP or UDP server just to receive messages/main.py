from server import *
from client import *

def initializeConnection(server_ipv4_add, server_port, client_ipv4_add, client_port):
    clientSocket = createClientSocket()
    boundClientSocket = bindToLocalClientSocket(local_ipv4_add=client_ipv4_add, local_port=client_port, socketObject=clientSocket)
    serverSocket = createServerSocket()
    boundServerSocket = bindToLocalServerSocket(local_ipv4_add=server_ipv4_add, local_port=server_port, socketObject=serverSocket)
    startListening(remote_ipv4_add=client_ipv4_add, remote_port=client_port, boundSocketObject=boundServerSocket)
    requestConnectionToServerSocket(remote_ipv4_add=server_ipv4_add, remote_port=server_port, boundSocketObject=boundClientSocket)


def main():
    IP_ADD = '127.0.0.1'    # TODO muszą być dwa różne sockety
    PORT = 42069
    initializeConnection(server_ipv4_add=IP_ADD, server_port=PORT, client_ipv4_add=IP_ADD, client_port=PORT)
    return 0

if __name__ == "__main__":
    main()