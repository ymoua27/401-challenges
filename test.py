
#!/usr/bin/env python3

# Script:                       Create Signature-based Malware Detection part 1
# Author:                       Yue Moua
# Date of latest revision:      2/20/2024
# Purpose:                      Challenge 31


import os

def search_file(file_name, directory):
    hits = 0
    searched_files = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                print(f"Found: {file} at {os.path.join(root, file)}")
            searched_files += 1
    return searched_files, hits

def main():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if not os.path.exists(directory):
        print("Directory not found.")
        return

    searched_files, hits = search_file(file_name, directory)
    
    print(f"\nSearched {searched_files} files. Found {hits} hits.")

if __name__ == "__main__":
    main()

# REF
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-31/challenges/DEMO.md
# https://chat.openai.com/share/176700ef-faf8-455b-aee6-82a4f1151781
# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/