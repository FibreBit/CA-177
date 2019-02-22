#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        words = line.lower().strip().split()
        new = ""
        i = 0
        while i < len(words):
            new = new + words[i][:-1].lower() + words[i][-1].upper()
            if i < len(words) - 1:
                new = new + " "
            i = i + 1
        print(new)

if __name__ == '__main__':
    main()
