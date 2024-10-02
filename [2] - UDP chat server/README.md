# 02.10.2024
learned the difference between udp and tcp, makes a lot of sense
the differnece is because there is no three way handshake present there is no need to listen, the client and server just send packets at eachother hoping that one of them makes it, which i think is pretty funny
also i implemented something pretty cool, which is that when one side sends the 'close' command the message is still sent to the other side, which reads it and also closes itself, which was fun to implement and makes more sense