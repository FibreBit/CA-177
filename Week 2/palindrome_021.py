#!/usr/bin/env python

import sys

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        words = line.lower().strip()
        for c in words:
            if not c.isalnum():
                words = words.replace(c, '', 1)
        print(palindrome(words))

if __name__ == '__main__':
    main()
