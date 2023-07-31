#Student name: Tobechi Onwenu
# star-id: 15083313 



import socket 	# For socket
import sys      # For passing arguments
import hashlib  # For calculating checksum
import time	    # For calculating RTT

def main(argv):
    # Get the server ip, port number and message from argument
    server_ip, port_num, message = sys.argv[1:]
    # Used to measuring the RTT, and do the checksum calculation,
    # send that checksum, and receive a reply from the server.
    server_info = (server_ip, int(port_num))

    # Create the UDP server socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #  start timer for RTT
    start_time = time.time()

    # Create md5 checksum
    # Check if message passed is text or filename of text
    if message[-4:] == ".txt":
        # Do file content checksum
        text_content = open(message,'rb').read()  # 'rb' read as binary [hashlib requires a binary format]
        checksum = hashlib.md5(text_content).hexdigest()  # start the checksum calculation
        client_socket.sendto(text_content, server_info)  # send the file contest as a message
    else:
        checksum = hashlib.md5(message.encode()).hexdigest()  # encode() text for sending and calculate checksum
        client_socket.sendto(message.encode(), server_info)  # send the text message

    client_socket.sendto(checksum.encode(), server_info)  # send the checksum calculated

    print("checksum sent: ", checksum)
    # Get the server's reply
    server_msg, server_address = client_socket.recvfrom(1024)
    #  end timer for RTT
    end_time = time.time()

    # check empty message from server
    if (server_msg.decode() == "0"):
        print("message failed!")
    else:
        print("server has successfully received the message at ", server_msg.decode())

    #  calculate final RTT
    rtt = ((end_time - start_time) * 1000)

    print("RTT: %.3f ms\n" % rtt)

if __name__ == "__main__":
   main(sys.argv)
