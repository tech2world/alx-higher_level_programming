#!/usr/bin/python3

if __name__ == "__main__":
    """Print addition of args"""
    import sys
    add = 0
    for s in range(len(sys.argv) - 1):
        add += int(s)
    print("{:d}".format(add))