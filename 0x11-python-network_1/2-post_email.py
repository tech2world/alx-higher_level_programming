#!/usr/bin/python3
"""Send a POST request to a given URL with an emaill address
Usauge: ./2-post_email.py <uRL> <email>
    - Display body of the response.
"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
