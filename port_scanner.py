#!/usr/bin/env python 

from email.headerregistry import Address
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1245
s.bind ((host,port))
s.listen(5)
socketclient,address=s.accept()
print("connected recieved from other terminal",address)
message=socketclient.recv(1024)
message=message.decode("utf-8")
print(message)
s.close()