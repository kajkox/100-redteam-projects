### server side

import socket, threading

## CONSTANTS

# these constants make creating socket objects easier
from config import SERVER_PORT, SERVER_IP, ADD_FAM, S_TYPE

# these define the types of messages sent
from config import FR_ADD_IP, FR_ADD_NM

# error messages
from config import ERR_FR_ADD_IP, ERR_FR_ADD_NM, OK

## GLOBAL VARIABLES

# this will be filled when a user 'registers', but for now i will just insert the data manually
contact_book = {
    "client1" : ("127.0.0.1", 34568),
    "client2" : ("127.0.0.1", 34569)
}

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

    # checking the request type
    if request == FR_ADD_IP:
        # create a new thread and run the proper function
        # -----
        pass

    elif request == FR_ADD_NM:
        # same as above
        # -----
        pass

    else:

        # unexpected request, sending error message
