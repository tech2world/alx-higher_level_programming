#!/usr/bin/python3
"""display value of variable X-Requests_id response header"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Requests-Id"))
