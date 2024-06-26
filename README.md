My personal attempt at completing "100-redteam-projects", while learning something along the way:)
Also here will be my personal thoughts and what i have learned throughout the way.
Future me, keep it up

a socket is an ip address + port, usually. socket objects on the server side should be bound -> start listening -> accept connection
the accept method returns a connection socket object, which is different from the original socket and should be used to receive or send messages, and address is the address of the client
client side socket objects just have to be created and connect to the server accepting socket object, and can also send and receive messages, among other things
