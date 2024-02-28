#!/usr/bin/env python3
# Script:                       Create cookie script
# Author:                       Yue Moua
# Date of latest revision:      2/27/2024
# Purpose:                      Challenge 37

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print("Cookie:", cookie)

# Send the cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
with open("response_content.html", "w") as html_file:
    html_file.write(response_with_cookie.text)

# Open the HTML file with Firefox
webbrowser.open("response_content.html")

# REF:
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-37/challenges/DEMO.md
# https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/
# https://chat.openai.com/share/664080ce-89f6-4058-8b39-f8b8ed9b2570