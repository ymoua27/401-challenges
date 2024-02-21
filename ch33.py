#!/usr/bin/env python3

# Script:                       Create Signature-based Malware Detection part 3
# Author:                       Yue Moua
# Date of latest revision:      2/22/2024
# Purpose:                      Challenge 33

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os

apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = 'a7a497cdd83580bf105638187bdccc01' # Set your hash here. 

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

os.system(query)

# REF: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-33/challenges/DEMO.md
# https://github.com/eduardxyz/virustotal-search/blob/master/virustotal-search.py