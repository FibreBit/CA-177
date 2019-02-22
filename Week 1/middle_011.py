#!/usr/bin/env python

import sys

def middle(word):
    if len(word) % 2 != 0:
        return word[int(len(word) / 2)]
    else:
        return 'No middle character!'

def main():
    for line in sys.stdin:
        word = middle(line.strip())
        print(word)


if __name__ == '__main__':
    main()
