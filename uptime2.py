#!/usr/bin/env python3

# Script:                       Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or downs
# Author:                       Yue Moua
# Date of latest revision:      1/10/2024
# Purpose:                      Challenge 03

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import sys
import time
import datetime

def send_email(sender_email, sender_password, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def check_host_status(host):
    try:
        subprocess.run(["ping", "-c", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "up"
    except subprocess.CalledProcessError:
        return "down"

def main():
    sender_email = input("Enter your email address: ")
    if not sender_email:
        sender_email = 'ymoua27@gmail.com'  # Replace with your Gmail address
    sender_password = input("Enter your email password: ") #jlfj iljs gugv caot
    receiver_email = input("Enter administrator email address: ")
    host_to_monitor = input("Enter the host to monitor (e.g., 8.8.8.8): ")

    previous_status = check_host_status(host_to_monitor)

    try:
        while True:
            current_status = check_host_status(host_to_monitor)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            if current_status != previous_status:
                subject = f"Host Status Change - {host_to_monitor}"
                body = f"Host status changed at {timestamp}.\nPrevious Status: {previous_status}\nCurrent Status: {current_status}"

                send_email(sender_email, sender_password, receiver_email, subject, body)

                previous_status = current_status

            print(f"{timestamp} Network {'Active' if current_status == 'up' else 'Inactive'} to {host_to_monitor}")

            time.sleep(2)  # Sleep for two seconds before sending the next ICMP packet

    except KeyboardInterrupt:
        print("\nExiting the script")

if __name__ == "__main__":
    main()


# REF: 
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/DEMO.md
# https://chat.openai.com/share/5a68588d-c089-4f02-9b7c-e1b2641f44f1
# https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151



