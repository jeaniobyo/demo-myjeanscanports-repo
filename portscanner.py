#!/usr/bin/env python 

from pyfiglet import Figlet 
import sys
import socket 
from datetime import datetime


F = Figlet(font='slant')
print(F.renderText("PORT SCANNER"))

Today = datetime.now()
print("Scanning started at:", Today)

print("-" * 50)
Host = socket.gethostbyname_ex()
for port in range(1,655335):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((Host, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

print(sys.copyright)
sys.exit()
