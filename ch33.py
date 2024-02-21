#!/usr/bin/env python3

# Script:                       Create Signature-based Malware Detection part 3
# Author:                       Yue Moua
# Date of latest revision:      2/22/2024
# Purpose:                      Challenge 33

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os
import hashlib
import time

def search_files(directory):
    scanned_files = 0
    positives_detected = 0
    total_files_scanned = 0
    
    # Retrieve API key from environment variable
    apikey = os.getenv('API_KEY_VIRUSTOTAL')

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

                # Construct the shell command to submit hash to VirusTotal
                query = f'python3 virustotal-search.py -k {apikey} -m {md5_hash}'

                # Execute the shell command
                output = os.popen(query).read()

                # Parse the output to extract number of positives and total files scanned
                for line in output.split('\n'):
                    if 'Positives' in line:
                        positives_detected += int(line.split(':')[1].strip())
                    elif 'Total Files Scanned' in line:
                        total_files_scanned += int(line.split(':')[1].strip())
            except Exception as e:
                print(f"Error scanning file: {file_path} - {e}")
    return scanned_files, positives_detected, total_files_scanned

def main():
    directory = input("Enter the directory to search in: ")

    if not os.path.exists(directory):
        print("Error: Directory not found.")
        return

    print("\nScanning files...\n")
    scanned_files, positives_detected, total_files_scanned = search_files(directory)
    
    print(f"\nScanned {scanned_files} files.")
    print(f"Positives detected: {positives_detected}")
    print(f"Total files scanned on VirusTotal: {total_files_scanned}")

if __name__ == "__main__":
    main()


# REF: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-33/challenges/DEMO.md
# https://github.com/eduardxyz/virustotal-search/blob/master/virustotal-search.py
# https://chat.openai.com/share/85e70743-4278-492a-b56f-df1967f963fc