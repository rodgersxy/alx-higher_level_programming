#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(data) as res:
            print(res.read().decode('UTF-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
