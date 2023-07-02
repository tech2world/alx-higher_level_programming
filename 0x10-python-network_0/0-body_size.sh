#!/bin/bash
# send a request to a url and display size of the body response
curl -s "$1" | wc -c
