#!/usr/bin/env python3
# Script:                       Create to prompt user choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
# Author:                       Yue Moua
# Date of latest revision:      1/23/2024
# Purpose:                      Challenge 12

import ipaddress
from scapy.all import ICMP, IP, sr1

def icmp_ping_sweep(network):
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(network, strict=False).hosts()]
    hosts_count = 0

    for host in ip_list:
        # Exclude network address and broadcast address
        if ipaddress.IPv4Address(host) == ipaddress.IPv4Network(network, strict=False).network_address or \
           ipaddress.IPv4Address(host) == ipaddress.IPv4Network(network, strict=False).broadcast_address:
            continue

        print("Pinging", host, "- please wait...")
        response = sr1(
            IP(dst=host) / ICMP(),
            timeout=2,
            verbose=0
        )

        if response is None:
            # If no response, inform the user that the host is down or unresponsive
            print(f"Host {host} is down or unresponsive.")
        elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
            # If ICMP type is 3 and ICMP code is blocking traffic, inform the user
            print(f"Host {host} is actively blocking ICMP traffic.")
        else:
            # Otherwise, inform the user that the host is responding
            print(f"Host {host} is responding.")
            hosts_count += 1

    # Count and inform the user about the number of online hosts
    print(f"\n{hosts_count} hosts are online.")

def tcp_port_range_scanner(network):
    # Implement TCP Port Range Scanner code from yesterday's feature set
    pass

def main():
    print("Network Security Tool Menu:")
    print("1. ICMP Ping Sweep")
    print("2. TCP Port Range Scanner")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        network = input("Enter the network address (CIDR format, e.g., '10.0.2.0/24'): ")
        icmp_ping_sweep(network)
    elif choice == "2":
        network = input("Enter the network address (CIDR format, e.g., '10.0.2.0/24'): ")
        tcp_port_range_scanner(network)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()


# Ref:
# https://web.archive.org/web/20180826164313/https://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md
# https://chat.openai.com/share/e108f370-4137-4a6c-b1d9-880ecd755b32

