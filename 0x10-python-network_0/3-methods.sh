#!/bin/bash
# display all allowed HTTP methods

curl -sI "$1" | awk '/^Allow:/ {print substr($0, 8)}'
