#!/usr/bin/env python3

# Script:                       Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or downs
# Author:                       Yue Moua
# Date of latest revision:      1/9/2024
# Purpose:                      Challenge 02

import time
from ping3 import ping, verbose_ping

def check_host_status(destination_ip):
    while True:
        try:
            response_time = ping(destination_ip)
            if response_time is not None:
                status = "Network Active"
            else:
                status = "Network Inactive"

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"{timestamp} {status} to {destination_ip}")

            time.sleep(2)  

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    target_ip = "8.8.8.8"  
    check_host_status(target_ip)

# REF
# https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-02/challenges
# https://www.cybrary.it/blog/ping-using-python-script
# https://web.archive.org/web/20190814203701/https://www.ictshore.com/python/python-ping-tutorial/
# https://chat.openai.com/share/9e7a718c-d249-43ae-ac65-20112f19417d

