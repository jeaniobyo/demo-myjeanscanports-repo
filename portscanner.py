#!/usr/bin/env python 

from pyfiglet import Figlet 
import sys
import socket 
from datetime import datetime


F = Figlet(font='slant')
print(F.renderText("PORT SCANNER"))

Today = datetime.now()
print("Scanning started at:", Today)

print("-" * 70)
host = socket.gethostbyaddr()
def new_func(host):
        for port in range(1,655335):
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect((host, port))
        if result == 0:
            print("Port is open")
        else:
            print()
        s.close("port is closed")

new_func(host)


