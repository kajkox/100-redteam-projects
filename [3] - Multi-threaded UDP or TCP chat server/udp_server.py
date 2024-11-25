### server side

import socket, threading

## CONSTANTS

# these constants make creating socket objects easier
from config import SERVER_PORT, SERVER_IP, ADD_FAM, S_TYPE

# these define the types of messages sent
from config import FR_ADD_IP, FR_ADD_NM

# error messages
from config import ERR_FR_ADD_IP, ERR_FR_ADD_NM, OK

# creating a socket object and binding
s_obj = socket.socket(ADD_FAM, S_TYPE)
s_obj.bind((SERVER_IP, SERVER_PORT))

# main loop
while True:

    # receving a message from a client, decoding
    encd_messagge, client_add = s_obj.recvfrom(1024)
    message = encd_messagge.decode()

    # parsing message
    parsed_message = message.split("[TYPE]:")
    request = parsed_message[-1]
    data = parsed_message[0]
    print(f"{client_add}\n{data}\n{request}")
