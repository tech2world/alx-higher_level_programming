#!/bin/bash
# send a POST request to a URL and display body of the response

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
