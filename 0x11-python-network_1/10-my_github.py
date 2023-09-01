#!/usr/bin/python3
"""
Script to display GitHub user ID using Basic Authentication
"""

from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    response = get(url, auth=HTTPBasicAuth(username, token))

    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print(None)
