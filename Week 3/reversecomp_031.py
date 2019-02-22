#!/usr/bin/env python

import sys

def reverse(words):
    five = {i.lower(): True for i in words if len(i) >= 5}
    words = [i for i in words if i.lower()[::-1] in five]
    print(words)
    return words

def main():
    words = [word.strip() for word in sys.stdin]
    reverse(words)

if __name__ == '__main__':
    main()
