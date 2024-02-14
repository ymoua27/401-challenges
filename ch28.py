#!/usr/bin/env python3
# Script:                       Create logging script pt3 
# Author:                       Yue Moua
# Date of latest revision:      2/14/2024
# Purpose:                      Challenge 28

import logging
from logging import FileHandler
from logging import StreamHandler
from scapy.all import *

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler and set level to INFO
file_handler = FileHandler('tcp_scan.log')
file_handler.setLevel(logging.INFO)

# Create console handler and set level to INFO
console_handler = StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def tcp_scan(target, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        try:
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
                    logging.info(f"Port {port} is open.")
                elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                    # Closed port
                    logging.info(f"Port {port} is closed.")
                else:
                    # Filtered port
                    logging.warning(f"Port {port} is filtered and silently dropped.")
            else:
                # No response
                logging.error(f"Port {port} could not be reached.")
        except Exception as e:
            # Log any exceptions that occur during scanning
            logging.error(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the target IP address
    port_range_to_scan = (1, 100)  # Replace with the desired port range

    tcp_scan(target_ip, port_range_to_scan)


# Ref:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-28/challenges/DEMO.md
# https://realpython.com/python-logging/#using-handlers
# https://chat.openai.com/share/8e62c777-e1da-4cc0-a47c-6d378a5028a2