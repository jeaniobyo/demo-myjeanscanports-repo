#!/usr/bin/env python

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1245
s.connect((host,port))
message = "This is hi from client"
s.send(message.encode("utf-8"))

s.close()