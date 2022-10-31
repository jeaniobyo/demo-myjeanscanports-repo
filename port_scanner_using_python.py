import socket  #Create a socket 
j = socket.socket (socket.AF_INET, socket.SOCK_STREAM, socket.SOCK_DGRAM)  #Containing socket value present, family and connetion type.
print("socket created successfully")
j.bind(("10.10.64.115",80))  #Associate with ip address and port number of the server socket can use. This is server socket.
j.listen(1)                   #This show number of the clients I want the server to listen, and don't allow connections of the client that is out of server listening scope.
print("waiting for connetions response") #This will print something on the screen.
while True:     #I want the connection to continueing in the loop format.
    c, addr = j.accept()    #The server will accept the client socket and it ip address.
    print("connected with", addr)  #To check the connection will work.

    c.send("Welcome to Jean port scanner") #This will send welcome note to the client.

    c.close() #This will close the connection.







