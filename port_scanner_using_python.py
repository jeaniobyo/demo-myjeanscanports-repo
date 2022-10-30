import socket #This is used to import the socket from the library.
 #The (j) represent the socket letter which i am going to use.
 # I use (AF_INET) as socket family for ipv4. 
 #(SOCK_STREAM) is for TCP traffic, while (SOCK_DGRAM) is for udp traffic.
j = socket.socket (socket.AF_INET, socket.SOCK_STREAM, socket.SOCK_DGRAM)

