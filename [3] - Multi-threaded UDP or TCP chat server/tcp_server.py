import threading
import socket
# so basically the main idea is to create a function that handles two clients, one receiving one sending
# the client will send the data to the server, the server will see where the data needs to be sent, and using a thread it sends it to a proper destination
# will it work on tcp? sure why not
# the first client will establish a connection with the server, the server stores the data temporarily, and "switches" to being a client
# now, the receivinig client will need to be already set up, maybe have a function that implements that? could be also called
# so, the server will then send the data to the end, although it would be easier to do on udp, but i think i will be able to handle it
# we will see
# 

# constants
TRANPORT_PROT = socket.SOCK_STREAM
ADDRESS_FAM = socket.AF_INET
SERVER_IP = '127.0.0.1'
SERVER_ADD = 27310

