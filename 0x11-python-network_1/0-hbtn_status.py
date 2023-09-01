#!/usr/bin/python3
"""
a script that fetches https://alx-intranet.hbtn.io/status
use urllib packages
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        text = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(text)))
        print('\t- content: {}'.format(text))
        print('\t- utf8 content: {}'.format(text.decode('utf-8')))
