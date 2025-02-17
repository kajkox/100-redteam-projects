### client file, if new clients need to be implemented just increment the port number

import socket, logging

## CONSTANTS

# client constants
CLIENT_IP = '127.0.0.1'
CLIENT_PORT = 34568

# these constants make creating socket objects easier
from config import SERVER_PORT, SERVER_IP, ADD_FAM, S_TYPE

# these define the types of messages sent
from config import FR_ADD_IP, FR_ADD_NM

# error messages
from config import ERR_FR_ADD_IP, ERR_FR_ADD_NM, OK

# TODO 
# add friend by ip - DONE
# add friend by name - DONE
# displaying contact book - DONE
# actually sending messages
# server responses - DONE (debugging)
# implementing threading - DONE (debugging)
# finish writing debug info !!!!!

# main menu prompt
MAIN_MENU: str = """
---Welcome to my UDP chat server---
Please select an option from the menu below:
    [0] - exit
    [1] - add a friend by name
    [2] - add a friend by ip:port 
    [3] - display contact book
Your choice: """


## GLOBAL VARIABLES

# changing this to false will display less info
is_debug = True

# logger function, default level is just info
def configure_logger(verbose = False):

    # setting the logging level
    if verbose:
        level = logging.DEBUG
    else:
        logging.INFO
    
    # configurating the display message
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

# creating the logger
logger = configure_logger(is_debug)
logger.debug("Logger configured properly!")

# contant book (might implement it in a file)
contact_book = {

}

logger.debug(f"Creating socket object with {(ADD_FAM, S_TYPE)}.")
s_obj = socket.socket(family=ADD_FAM, type=S_TYPE)
logger.debug(f"Binding to {(CLIENT_IP, CLIENT_PORT)}...")
s_obj.bind((CLIENT_IP, CLIENT_PORT))
logger.debug(f"Socket bound successfully")

# multipurpose function that handles sending requests to the server
def send_server_request(sending_request: str) -> str:

    logger.info("Sending server request...")
    # encoding
    logger.debug(f"Encoding message: {sending_request}")
    sending_request = sending_request.encode()
    logger.debug("Message succesfully encoded!")

    # sending message
    logger.debug(f"Sending the message to the server address: {(SERVER_IP, SERVER_PORT)}...")
    s_obj.sendto(sending_request, (SERVER_IP, SERVER_PORT))
    logger.debug("Message sent.")
    logger.debug("Waiting for response...")
    response = s_obj.recv(1024).decode()
    logger.info("Server responded")
    return response

# function that displays the contact book
def show_contact() -> None | IndexError:
    
    logger.info("Displaying contact book")
    # checking if contact_book is empty
    logger.debug("Checking if contact book is empty...")
    if len(contact_book) == 0:
        raise IndexError

    # index for displaying contact info
    index: int = 0
    for friend in contact_book.keys():

        # incrementing
        index += 1
        print(f"({index}) {friend} : {contact_book[friend]}")
    logger.debug("Iterated over every object in contact book, returning...")
    
    return None


# function that adds friend by name to the contact book
# the function sends data to the server with some metadata to interpret what type of request it is
# the same method is used in ip_add()
def name_add(friend_name: str) -> None | SyntaxError | NameError | ValueError:


    # checking if name is already in contact book
    if friend_name in contact_book.keys():
        raise NameError

    # crafting the message
    message = ""
    message += friend_name
    message += FR_ADD_NM


    # sending the message and waiting for response
    response = send_server_request(sending_request=message)

    # parsing data, comparing response
    parsed_response: list[str] = response.split("[TYPE]:")

    # couldn't implement match case because of "Irrefutable pattern is allowed only for the last case statement", see: https://stackoverflow.com/questions/69854421/python-match-case-using-global-variables-in-the-cases-solvable-by-use-of-classe
    # will just do a classic if else comparison

    # the server responded with an error
    if parsed_response[-1] == ERR_FR_ADD_NM:
        raise SyntaxError
        
    # the server responded properly with a (ip, port) response tuple
    elif parsed_response[-1] == OK:
        # extracting the ip and port from message
        friend_ip = parsed_response[0].split(',')[0]
        friend_port = int(parsed_response[0].split(',')[1])

        # adding to contact book
        contact_book[friend_name] = (friend_ip, friend_port)
        return None
        
        # unexpected or no response
    else:
        raise ValueError



# funtction that adds friend by ip, port pair to contact book
def ip_add(friend_ip: str, friend_port: int) -> None | SyntaxError | NameError | ValueError:

    # checking if name is already in contact book
    if (friend_ip, friend_port) in contact_book.values():
        raise NameError

    # crafting the message
    message: str = ""
    message += friend_ip + ',' + str(friend_port)
    message += "[TYPE]:" + FR_ADD_IP

    # sending the message and waiting for response
    # client will continuesly send until all data is sent
    response = send_server_request(sending_request=message)

    # parsing data, comparing response
    parsed_response: list[str] = response.split("[TYPE]:")

    # couldn't implement match case because of "Irrefutable pattern is allowed only for the last case statement", see: https://stackoverflow.com/questions/69854421/python-match-case-using-global-variables-in-the-cases-solvable-by-use-of-classe
    # will just do a classic if else comparison

    # the server responded with an error
    if parsed_response[-1] == ERR_FR_ADD_IP:
        raise SyntaxError
        
    # the server responded properly with a name of the friend
    elif parsed_response[-1] == OK:
        friend_name = parsed_response[0]

        # adding to contanct book
        contact_book[friend_name] = (friend_ip, friend_port)
        return None
        
    # unexpected or no response
    else:
        raise ValueError


# main menu loop
def main() -> int:

    # can stop with ctrl_c
    try:

        while True:
            print(f"{MAIN_MENU}")

            # catching wrong input
            try:
                choice = int(input())
            except ValueError:
                print("Please input a number.")

            # menu selection
            match choice:

                # exiting
                case 0:
                    return 0

                # adding friend by name
                case 1:
                    print(f"Please input the name of the friend you want to add: ")
                    name = input()

                    # catching error from function
                    try:

                        # adding friend
                        name_add(name)
                    
                    # server couldn't add friend
                    except SyntaxError:
                        print("[ERROR] Friend not found, make sure you typed the name correctly.")

                    # friend already in contact book
                    except NameError:
                        print(f"[ERROR] Friend is already in your contact book.")

                    # unexpected or no response from server
                    except ValueError:
                        print(f"[ERROR] The server didn't respond properly, make sure your connection is stable.")


                # adding friend by ip
                case 2:
                    print(f"Please input your friend's ip: ")
                    ip = input()
                    print(f"Please input the port: ")

                    # catching wrong input
                    try:
                        port = int(input())
                    except ValueError:
                        print("[ERROR] Please input the port as a number.")

                    # catching error from function
                    try:

                        # adding friend
                        ip_add(ip, port)

                    # server couldn't add friend
                    except SyntaxError:
                        print(f"[ERROR] Friend not found, make sure you typed the ip and port correctly.")

                    # friend already in contact book
                    except NameError:
                        print(f"[ERROR]: Friend is already in your contact book.")

                    # unexpected or no response from server
                    except ValueError:
                        print(f"[ERROR] The server didn't respond properly, make sure your connection is stable")

                # displaying contact book
                case 3:
                    
                    # catching error from function
                    try:
                        show_contact()

                    # contact book is empty
                    except IndexError:
                        print(f"You currently have no contacts!")

                case _:
                    print(f"Option not found, make sure you typed the option correctly")
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()