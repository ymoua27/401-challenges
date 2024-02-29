#!/usr/bin/env python3

# Author:      Yue Moua
# Description: TODO: Create XSS vulnerability detection  
# Date:        TODO: 2/28/24
# Modified by: TODO: Yue MOua

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: It gets the HTML contents of a web page which will parse it using BeautifulSoup. It also extracts all the <form> elements from it ###
### This is useful for the script since we want to test a web page###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: It parses an HTML <form> element and extract the action URL, method, and input fields ###
### We want to be able to view characteristics of the HTML forms, so we can identify vulnerabilities###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: It constructs the form data based on the input fields, determines the form submission method (POST or GET), and sends the appropriate HTTP request to submit the form data to the target URL###
### This will allow us to interact with the web forms and inject payloads for testing ###
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Identifies XSS vulnerabilities ###
### This is what we want to test for in web application. It automates it for us###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"  # Inserted JavaScript code here
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Provides a way to include script execution logic that only runs when the script is executed directly ###
### It allows use to run a specific part of the code when we use the script ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

# False
# Enter a URL to test for XSS:http://juiceshop.local:3008
# [+] Detected 0 forms on http://juiceshop.local:3008.
# False

# I couldn't get a positive detection
