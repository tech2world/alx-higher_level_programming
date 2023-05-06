#!/usr/bin/python3

if __name__ == "__main__":
    """Print addition of args"""
    import sys

    count = sys.argv
    add = 0
    for s in range(len(count) - 1):
        add += int(s)
    print("{:d}".format(add))
    # print(count)
