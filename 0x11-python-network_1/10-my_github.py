#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    if r.status_code < 400:
        print(r.json()['id'])
    else:
        print("None")
