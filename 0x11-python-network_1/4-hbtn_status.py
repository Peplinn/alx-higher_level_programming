#!/usr/bin/python3
"""
fetch https://alx-intrant.hbtn.io/status using requests
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    html = r.content.decode('utf-8')
    print('Body response:')
    print('\t- type:', type(html))
    print('\t- content:', html)
