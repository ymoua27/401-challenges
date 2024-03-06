#!/usr/bin/env python3
# Script:                       Create atack tools part 2
# Author:                       Yue Moua
# Date of latest revision:      3/5/2024
# Purpose:                      Challenge 42

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")

print("You have selected option: ", resp)

port_range = input("Enter port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, arguments='-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, arguments='-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, arguments='-v -sS -sU -sV -O -A -T4')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
elif int(resp) >= 4:
    print("Please enter a valid option")


# REF:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md
# https://chat.openai.com/share/fd19211a-e4b9-46b0-a80f-efa8449148c6
