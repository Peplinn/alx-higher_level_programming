#!/usr/bin/python3
""" fetch https://alx-intrant.hbtn.io/status using urllib """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('utf-8'))
