#!/usr/bin/env python3
# Script:                       Create a script to combine port and ping, delete menu, prompt user for ip to target, move poprt scan to its own function, call the port scan function
# Author:                       Yue Moua
# Date of latest revision:      1/24/2024
# Purpose:                      Challenge 13

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

def icmp_ping_sweep(host):
    print("Pinging", host, "- please wait...")
    response = sr1(
        IP(dst=host) / ICMP(),
        timeout=2,
        verbose=0
    )

    if response is None:
        # If no response, inform the user that the host is down or unresponsive
        print(f"Host {host} is down or unresponsive.")
        return False
    elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
        # If ICMP type is 3 and ICMP code is blocking traffic, inform the user
        print(f"Host {host} is actively blocking ICMP traffic.")
        return False
    else:
        # Otherwise, inform the user that the host is responding
        print(f"Host {host} is responding.")
        return True

def tcp_port_range_scanner(host):
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = []

    print(f"Scanning ports {start_port}-{end_port} on {host}...")

    for port in range(start_port, end_port + 1):
        response = sr1(
            IP(dst=host) / TCP(dport=port, flags="S"),
            timeout=1,
            verbose=0
        )

        if response is not None and response.haslayer(TCP) and response[TCP].flags == 18:
            # If the TCP flag is SYN-ACK, consider the port open
            open_ports.append(port)

    if open_ports:
        print(f"Open ports on {host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {host}.")

def main():
    print("Network Security Tool Menu:")
    
    target_ip = input("Enter the target IP address: ")

    if icmp_ping_sweep(target_ip):
        tcp_port_range_scanner(target_ip)

if __name__ == "__main__":
    main()

#Ref:
# https://chat.openai.com/share/8baa2dc5-8638-4d56-90e0-325b8e434bb9 