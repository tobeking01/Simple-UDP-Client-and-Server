# Simple-UDP-Client-and-Server
Write a simple UDP client and server program and a communication protocol using C or python3 in which the client will send a message or a file to the server. Then, the server will reply with the timestamp when it receives the message. The client needs to compute the round-trip-time (RTT) of the sent messages. 


Problem:
The message:

A string or a file.
The client program takes:

The hostname or the IP address of the server is in (argument 1).
The port number on the server is in (argument 2).
The text/file to send is in (argument 3). 
The client program name should be client_simple_udp.py or .c
client_simple_udp <server_ip> <port_num> <"Test text"|test_file.txt>
E.g.,
python3 client_simple_udp.py <server_ip> <port_num> <"Test text"> 
python3 client_simple_udp.py <server_ip> <port_num> <test_file.txt>
The server takes:

The port number to listen in (argument 1).
The server program name must be server_simple_udp.py or .c
E.g.,
./server_simple_udp <port_num>
python3 server_simple_udp.py <port_num>
 

Protocol Description
The client creates a checksum of the message.
The client sends both the message and the checksum to the server. 
The server receives the message as well as the checksum. It first records the local timestamp when it received the message. The server then prints the date and time, the message, and the received checksum to the screen. Then it calculates the checksum of the received message, prints it, and compares it with the received checksum. If the checksum matches, the server sends the timestamp back to the client. If the checksum does not match, the server reports an error message and acknowledges the client (e.g., value 0). 
The client receives the response message from the server. If the message is a valid timestamp, print the date and time; otherwise, report an error message (e.g., print "message failed!"). It also calculates and prints the round-trip-time (RTT), in microseconds, from when it sent the message to when it received the response.
