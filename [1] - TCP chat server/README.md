# 02.10.2024
In this case the client server relation is more permament, because it doesn't automatically close after sending one message back and forth.
First, the server-side socket object is bound to a socket, that then listens for any incoming connections
Then, the client-side socket object connects to the serverm the server accepts, and a TCP connection is established

I then decided to implement a permament while True loop that breaks only when one side writes 'close' to the other one.
This creates a realistic chat server scenario which im pretty proud of :)