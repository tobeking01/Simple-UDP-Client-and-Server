#Student name: Tobechi Onwenu
# star-id: 15083313 

import socket       # For socket
import sys	    # For passing arguments
import hashlib      # For calculating checksum
import datetime     # For getting timestamp

def main(argv):
    server_ip = "127.0.0.1"
    port_num = sys.argv[1]
    # Create to the UDP server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Assign the IP address and port number to socket
    server_socket.bind((server_ip, int(port_num)))

    print("Listening on port ", port_num)
    print("Waiting...\n")

    # Listen for the incoming
    while True:
        # Receive to the client packet along with the address its coming from
        message, address = server_socket.recvfrom(1024)  # Receive the messages
        # get timestamp for received message
        timestamp = str(datetime.datetime.now())
        print("*** new message ***")
        print("Received time:", timestamp)
        #  receive the checksum from the client
        checksum_received, address = server_socket.recvfrom(1024)  # Receive the checksum
        #  print client message
        print("Received message:")
        print(message.decode())
        #  print client checksum
        print("Received checksum:", checksum_received.decode())

        # calculate to the checksum in server for comparing to the received checksum
        checksum_server = hashlib.md5(message).hexdigest()
        #  print server checksum
        print("Calculated checksum:", checksum_server)

        # check if checksum for client and server is a match
        if (checksum_server == checksum_received.decode()):
            #  send timestamp to client
            server_socket.sendto(timestamp.encode(), address)
        else:
            print("[ERROR] Checksum does not match!")
            server_socket.sendto("0".encode(), address)

        print()  # For extra newline

if __name__ == "__main__":
   main(sys.argv)

