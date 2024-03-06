#!/usr/bin/env python3
# Script:                       Create a port scanner
# Author:                       Yue Moua
# Date of latest revision:      3/6/2024
# Purpose:                      Challenge 43

#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5 # setting a timeout value of 5 seconds
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        result = sockmod.connect_ex((hostip, portno))
        if result == 0:
            print(f"Port {portno} is open")
        else:
            print(f"Port {portno} is closed")
        sockmod.close()
    except socket.error as e:
        print(f"Error: {e}")

portScanner(portno)

# REF:
# https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html
# https://chat.openai.com/share/66d26fe0-cdb1-4e78-95fe-24a4e0da3c7e