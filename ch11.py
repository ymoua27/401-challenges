#!/usr/bin/env python3
# Script:                       Create TCP Port Range Scanner that test if a TCP port is open or closed
# Author:                       Yue Moua
# Date of latest revision:      1/22/2024
# Purpose:                      Challenge 11

# Run this with sudo

from scapy.all import *

def tcp_scan(target, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        # Crafting TCP SYN packet
        ip_packet = IP(dst=target)
        tcp_packet = TCP(dport=port, flags="S")

        # Sending the packet and receiving the response
        response = sr1(ip_packet/tcp_packet, timeout=1, verbose=0)

        if response is not None:
            # Checking TCP flags in the response
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                # Open port
                send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)
                print(f"Port {port} is open.")
            elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                # Closed port
                print(f"Port {port} is closed.")
            else:
                # Filtered port
                print(f"Port {port} is filtered and silently dropped.")
        else:
            # No response
            print(f"Port {port} could not be reached.")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the target IP address
    port_range_to_scan = (1, 100)  # Replace with the desired port range

    tcp_scan(target_ip, port_range_to_scan)


#Ref: 
# https://scapy.readthedocs.io/en/latest/extending.html
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md
# https://chat.openai.com/share/b1e45063-0d43-45a6-b1a3-19bce86832cb