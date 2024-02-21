#!/usr/bin/env python3

# Script:                       Create Signature-based Malware Detection part 2
# Author:                       Yue Moua
# Date of latest revision:      2/20/2024
# Purpose:                      Challenge 32

import os
import hashlib
import time

def search_files(directory):
    scanned_files = 0
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                file_size = os.path.getsize(file_path)
                with open(file_path, "rb") as f:
                    data = f.read()
                    md5_hash = hashlib.md5(data).hexdigest()
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
                print(f"Timestamp: {timestamp}, File: {file_name}, Size: {file_size} bytes, Path: {file_path}, MD5 Hash: {md5_hash}")
                scanned_files += 1
            except Exception as e:
                print(f"Error scanning file: {file_path} - {e}")
    return scanned_files

def main():
    directory = input("Enter the directory to search in: ")

    if not os.path.exists(directory):
        print("Error: Directory not found.")
        return

    print("\nScanning files...\n")
    scanned_files = search_files(directory)
    
    print(f"\nScanned {scanned_files} files.")

if __name__ == "__main__":
    main()


# REF
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-32/challenges/DEMO.md
# https://chat.openai.com/share/176700ef-faf8-455b-aee6-82a4f1151781
# https://docs.python.org/3/library/hashlib.html
# https://www.programiz.com/python-programming/examples/hash-file