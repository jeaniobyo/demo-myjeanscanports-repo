#The server socket side. 

import socket 
host_ip = "10.10.64.115"
port_number = 9999
s = socket.socket()
print("Socket created sucessfully")
s.bind = (host_ip , port_number)   #The server listening to the specific ip address and port.
print("The server is waiting for bound")
s.listen(1)
print("The server is listening for conections")
while True:
    c, host_ip = s.accept()
    print("The folloing host is connection", host_ip)

    c.send("Welcome to Jean Server") #The server send to client a connetion message.
    c.close 


#The Cleint socket side.