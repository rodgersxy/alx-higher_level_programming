#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    email = {'email': argv[2]}
    url = argv[1]

    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')

    request = urllib.request.Request(url, email)

    with urllib.request.urlopen(request) as res:
        res = res.read()
        res = res.decode('utf-8')
        print(res)
