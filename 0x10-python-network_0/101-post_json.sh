#!/bin/bash
# send a jSON POST request and display body of the response
curl -sH "Content-Type: application/json" -d @"$2" -X POST "$1"
