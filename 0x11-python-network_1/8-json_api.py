#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_data = r.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
