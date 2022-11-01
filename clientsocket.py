#!/usr/bin/env python

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 443
s.connect(('', port))
print(s.recv(80))
s.close()