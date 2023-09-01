#!/usr/bin/python3
"""
Script that takes in a letter, sends a POST request to a specified
URL with the letter as a parameter, and handles the response
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    res = requests.post(url, data=q)
    try:
        body = res.json()
        if len(body) == 0:
            print("No result")
        else:
            print("[{}] {}".format(body["id"], body["name"]))
    except ValueError:
        print("Not a valid JSON")
