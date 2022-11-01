#!/usr/bin/env python 

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 443
s.bind (("", port))
print("connections completed successfully")
s.listen(3)
print("listening for client connections")
while True:
    c, addr = s.accept()
    print("connected successfully with", addr)
    c.send("Welcome to Jean Server!!!!!!")
    c.close()
