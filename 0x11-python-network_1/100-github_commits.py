#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    for commit in r.json()[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
