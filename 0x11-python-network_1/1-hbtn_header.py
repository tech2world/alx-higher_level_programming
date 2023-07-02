#!/usr/bin/python3
"""Displays the X-Request-ID Header of a given URL
Usuage: ./1-hbtn_header.py <URL>
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
