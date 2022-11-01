#!/usr/bin/env python

import socket 
from datetime import date

Today = date.today()
print(Today)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 80
c.connect((host, port))
c.recv(80)
c.close 