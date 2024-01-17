#!/usr/bin/env python3

# Script:                       Create File Encryption Script 2
# Author:                       Yue Moua
# Date of latest revision:      1/17/2024
# Purpose:                      Challenge 07

from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key", "rb").read()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_string(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    print("Encrypted Text:", encrypted_text.decode())

def decrypt_string(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(encrypted_text.encode())
    print("Decrypted Text:", decrypted_text.decode())

def encrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, key)
    print("Folder encrypted successfully.")

def decrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, key)
    print("Folder decrypted successfully.")

def main():
    key = None

    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n"))

    if mode == 1 or mode == 2:
        file_path = input("Enter the file path: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        else:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        text = input("Enter the text: ")
        if mode == 3:
            encrypt_string(text, key)
        else:
            decrypt_string(text, key)
    elif mode == 5 or mode == 6:
        folder_path = input("Enter the folder path: ")
        if mode == 5:
            encrypt_folder(folder_path, key)
        else:
            decrypt_folder(folder_path, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()


# Ref:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-07/challenges/DEMO.md
# https://chat.openai.com/share/e4cfa291-37ee-4e26-ae38-836768fa6041
# https://github.com/ymoua27/401-challenges/blob/main/encrypt.py