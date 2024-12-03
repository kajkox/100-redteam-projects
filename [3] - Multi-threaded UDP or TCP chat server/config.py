### this file contains constants that are used throughout the project
import socket

# socket constants
SERVER_IP = '127.0.0.1'
SERVER_PORT = 34567
ADD_FAM = socket.AF_INET
S_TYPE = socket.SOCK_DGRAM

# message constants
FR_ADD_IP = "FIP"
FR_ADD_NM = "FNM"
OK = "OK"
# error constants
ERR_FR_ADD_IP = "EFIP"
ERR_FR_ADD_NM = "EFNM"

## the format below specifies the type and message that is being sent by the client/user
# the request type is specified in the end, and is seperated by a special character combination to ensure that the user doesn't accidentally mess up
# the syntax is
    # <message/data>[TYPE]:<type>
    # the server then parses this data and uses the appropriate function depending on the <type>
    # also the client parses the answer and know when to raise a error or include the data