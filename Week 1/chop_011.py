#!/usr/bin/env python

import sys

def chop(s):
    return s[1:-1]

def main():
    for line in sys.stdin:
        chopped = chop(line.strip())
        if len(chopped) > 0:
            print(chopped)


if __name__ == '__main__':
    main()
