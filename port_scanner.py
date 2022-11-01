#!/usr/bin/env python 

import socket
from datetime import date 
import sys

Today = date.today()
print(Today)

j=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 80
j.bind ((host, port))
print("connections completed successfully")
j.listen(3)
print("listening for client connections")
while True:
    c, addr = j.accept()
    print("connected successfully with", addr)
    c.send("Welcome to Jean Server!!!!!!")
    c.close
