#!/usr/bin/python3
"""send post request to a URL with a given email
Usuage: ./6-post_email.py <URL> <email>
    - display the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    mail = {"email": argv[2]}

    req = requests.post(url, data=mail)
    print(req.text)
