#!/usr/bin/env python 

#This is Network Port Scanner.

from pyfiglet import Figlet #This code will import figlet from pyfiglet library.
import sys #This will import sys module,and its fuction such as sys.version, sys.executable etc.
import socket #This will import the socket library and its objects such as AF_NET and many more.
from datetime import datetime #This will import the datetime modules and with it classes such as time and date. 


F = Figlet(font='thick')  #The code to design a fancy text display.
print(F.renderText("PORT SCANNER")) #The code to display the fanncy text named port scanner.

Today = datetime.now() #The code show the current time and date.
print("Scanning Host IP Target:", "10.10.90.16")    #This code will show the IP address of the target host I am scanning on the top.
print("Scanning started at:", Today)                #This code will show the time and date the scanning took place.

print("-" * 70) #This code will show the bottom dots border line between scanning time and scanning ports.

for port in range(80,443): #This code will show the ranges of the ports, will be scanning.
    n = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This code show I be scanning IPV4 and with the TCP connections.
    result = n.connect_ex(("10.10.90.16", port)) #This code focus on which host IP address will be scanning plus the port variable.

    if result == 0:    
        print("port: " + str(port) + " is open") # I got this code from (Herbertech on youtube under 'build a basic port scanner in python') This code will display port number plus statement saying the port is open.
    else:
        print("port: " + str(port) + " is closed") # I got this code from(Herbertech on youtube under "build a basic port scanner in python") This code will display port number plus statement saying the port is closed.
    n.close() #The code will close the socket. 

print(sys.version) #The code will display version of the python I am running.