#!/usr/bin/env python

import sys

def main():
    total = 0
    for line in sys.stdin:
        words = line.strip().split()
        total = total + int(len(words))
    print(total)

if __name__ == '__main__':
    main()
