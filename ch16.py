#!/usr/bin/env python3
# Script:                       Create automated script to brute force attack using wordlist
# Author:                       Yue Moua
# Date of latest revision:      1/29/2024
# Purpose:                      Challenge 16

import time

def offensive_mode(word_list_path):
    try:
        with open(word_list_path, 'r') as file:
            for word in file:
                word = word.strip()  # Remove leading and trailing whitespaces
                time.sleep(1)  # Add a delay of 1 second between words
                print(word)
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
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognized")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            word_list_path = input("Enter the path of the word list file: ")
            offensive_mode(word_list_path)
        elif choice == '2':
            user_input = input("Enter the string to search: ")
            word_list_path = input("Enter the path of the word list file: ")
            defensive_mode(user_input, word_list_path)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

# REF
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/DEMO.md
# https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# https://chat.openai.com/share/6c33b744-080b-4ad2-b3dc-113539bd7a57