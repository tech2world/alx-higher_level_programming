#!/usr/bin/python3
"""send request to a given URL and display the res;onse body
Usage: ./3-error_code.py <URL>
    -Handles http errors
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
