#!/usr/bin/env python3
# Script:                       Create web application fingerprinting script
# Author:                       Yue Moua
# Date of latest revision:      2/26/2024
# Purpose:                      Challenge 36

import socket
import subprocess

def netcat_banner_grabbing(host, port):
    try:
        nc_cmd = f"nc -v {host} {port}"
        result = subprocess.check_output(nc_cmd, shell=True, stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing netcat:", e.output.decode())

def telnet_banner_grabbing(host, port):
    try:
        tn_cmd = f"telnet {host} {port}"
        result = subprocess.check_output(tn_cmd, shell=True, stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing telnet:", e.output.decode())

def nmap_banner_grabbing(host):
    try:
        nmap_cmd = f"nmap -Pn -sV --script=banner {host}"
        result = subprocess.check_output(nmap_cmd, shell=True, stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing nmap:", e.output.decode())

def main():
    # Prompt the user to input URL or IP address
    target_host = input("Enter the target URL or IP address: ")
    # Prompt the user to input port number
    target_port = input("Enter the target port number: ")

    print("\n--- Netcat Banner Grabbing ---")
    netcat_banner_grabbing(target_host, target_port)

    print("\n--- Telnet Banner Grabbing ---")
    telnet_banner_grabbing(target_host, target_port)

    print("\n--- Nmap Banner Grabbing ---")
    nmap_banner_grabbing(target_host)

if __name__ == "__main__":
    main()


# REF:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-36/challenges/DEMO.md
# https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
# https://chat.openai.com/share/8a6b1641-fea6-4557-82fa-1619220939bb
