# My personal attempt at completing "100-redteam-projects", while learning something along the way:)
Also here will be my personal thoughts and what i have learned throughout the way. Kind of like my personal notes.
Future me, keep it up

a socket is an ip address + port, usually. socket objects on the server side should be bound -> start listening -> accept connection 
the accept method returns a connection socket object, which is different from the original socket and should be used to receive or send messages, and address is the address of the client
client side socket objects just have to be created and connect to the server accepting socket object, and can also send and receive messages, among other things

# NOTE, starting to add dates 
# 07.07.2024
the earlier comment is almost correct, but it only contains information about the TCP connection (socket.SOCK_STREAM), in UPD (socket.SOCK_DGRAM) both the client/s need to be bound to sockets (each one to a different obv.) after binding the socketObject.recvfrom(1024) method also returns two objects, one for the received data, the second for the address of the client. because no 3WHS is established there is no object for the connection like in TCP, instead the program i have written just stops the while loop, with it the recv_from method. sending data is also pretty easy, after encoding we use the socketObject.sendto(data, (socket_tuple)) method, which is pretty clear in itself.
# 02.10.2024
After a *short* break i decided to return to this project of mine, partly because my spring break is over and im back at uni so im more tuned into programming. We will see what i can do.

