First proper attempt at creating something from the list, was actually pretty good at teaching something about sockets.

# 02.10.2024
To work, first run server.py and then client.py
First the server listens for a connection from the client, accepts it receives data from the client until he sends an empty message
In this particular case, becuase the client doesn't have a loop or a break condition, the client disconnects after receiving a message back from the server