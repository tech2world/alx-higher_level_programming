#!/bin/bash
# take a URL as argument and display the status code of the response

curl -s -o /dev/null -w "%{http_code}" "$1"
