#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and display the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code < 400:
        print(r.content.decode('utf-8'))
    else:
        print('Error code:', r.status_code)
