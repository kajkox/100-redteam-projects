### server side

import socket, threading, time, logging

# NOTE
# because threads in python by defauly don't return the values of the functions they run
# i changed the functionality a little bit
# its pretty intuitive but it basically just stores the return value of the target function in _result and returns it by calling get_result()

class ThreadReturning(threading.Thread):
    def __init__(self, target, args=()):
        super(ThreadReturning, self).__init__()
        self.target = target
        self.args = args
        self._result = None

    def run(self):
        self._result = self.target(*self.args)

    def get_result(self):
        return self._result


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

# creating a socket object and binding

logger.debug(f"Creating a socket at with {(ADD_FAM, S_TYPE)}")

s_obj = socket.socket(ADD_FAM, S_TYPE)

logger.debug(f"Socket created succesfully!")
logger.debug(f"Binding to {(SERVER_IP, SERVER_PORT)}")

s_obj.bind((SERVER_IP, SERVER_PORT))

logger.debug(f"Socket bound succesfully!")

# function that searches the contact book and returns the name of the client
def friend_req_ip(client_ip: str, client_port: int) -> None | str:
    
    logger.info(f"Searching for {(client_ip, client_port)} in contact_book...")
    # iterating over the contact book
    for client in contact_book.keys():
        
        # client found in the servers contact book
        if contact_book[client] == (client_ip, client_port):
            logger.info(f"Client {client} found!\nReturning.")
            return client
        
    # client is not found
    logger.info(f"Client not found!\nReturning")
    return None

# function that handles the threading and error values
def handle_friend_req_ip(received_message: str) -> str | IndexError:
    
    logger.info("Handling the friend request...")
    # parsing the message to separate the ip and port
    logger.debug("Parsing the received message...")
    ip = received_message.split(',')[0]
    port = int(received_message.split(',')[-1])
    logger.debug(f"IP: {ip}")
    logger.debug(f"PORT: {port}")

    # creating the thread
    logger.debug(f"Creating thread...")
    arguments = (ip, port)
    logger.debug(f"Using args: {arguments}")
    thread = ThreadReturning(target=friend_req_ip, args=arguments)
    logger.debug(f"Successfully created thread at target function friend_req_ip")

    # starting the thread
    logger.debug("Starting thread...")
    thread.start()
    logger.debug("Thread started.")

    # waiting for it to finish
    logger.debug("Waiting for thread to finish...")
    thread.join()
    logger.debug("Thread finished")

    # getting the result of the thread
    logger.debug("Geting return value...")
    return_val = thread.get_result()
    logger.debug(f"Returned value: {return_val}")

    # checking the return value
    if return_val == None:
        logger.info("Return value is None, raising Error...")
        raise IndexError
    
    else:
        logger.info(f"Returning value isn't None, returning...")
        return return_val
    
# multipurpose function that will use threading to send messages to clients    
def send_to_client(client_ip: str, client_port: int, message_to_client:str) -> None:

    logger.info("Sending message to client...")

    # encoding 
    logger.debug("Encoding message...")
    message_to_client = message_to_client.encode()
    logger.debug(f"Message encoded succesfully: {message_to_client}")

    # sending
    logger.debug(f"Sending message to {(client_ip, client_port)}...")
    s_obj.sendto(message_to_client, (client_ip, client_port))
    logger.info(f"Message sent succesfully!")
    

# main loop
def main():
    
    # can stop with ctrl+c
    try:
        while True:

            logger.info("Starting main loop.")
            logger.debug("Waiting for message...")

            # receving a message from a client, decoding
            encd_messagge, client_add = s_obj.recvfrom(1024)
            logger.debug(f"Message received from {client_add}")
            logger.debug("Decoding...")
            message = encd_messagge.decode()
            logger.debug(f"Message decoded: {message}")

            # parsing message
            logger.debug("Parsing message...")
            parsed_message = message.split(sep="[TYPE]:")
            logger.debug(f"Parsed message: {parsed_message}")

            request = parsed_message[-1]
            data = parsed_message[0]
            logger.debug(f"Request {request}")
            logger.debug(f"Data: {data}")
            logger.info("Checking request type.")
        # checking the request type
            if request == FR_ADD_IP:
                logger.info("The request is adding a friend by ip:port.")
                
                # handling the threading
                try:
                    # getting the name of the client
                    friend_name = handle_friend_req_ip(received_message=data)

                    # crafting the message
                    respond_message = ""
                    respond_message += friend_name
                    respond_message += "[TYPE]:"
                    respond_message += FR_ADD_IP

                    # preparing args
                    ip = client_add[0]
                    port = client_add[1]

                    # creating the thread
                    thread = threading.Thread(target=send_to_client, args=(ip, port, respond_message))

                    # starting the thread
                    thread.start()

                    # waiting for it to finish
                    thread.join()

                # the server couldn't find the name of the client
                except IndexError:

                    # creating the message
                    respond_message = ""
                    respond_message += "ERROR[TYPE]:"
                    respond_message += ERR_FR_ADD_IP

                    # sending the response
                    
                    # creating the thread
                    thread = threading.Thread(target=send_to_client, args=(client_add, respond_message))

                    # runnig the thread
                    thread.start()

                    # wait for it to finish
                    thread.join()

            elif request == FR_ADD_NM:
                # same as above
                # -----
                pass

            else:

                # unexpected request, sending error message
                pass
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
