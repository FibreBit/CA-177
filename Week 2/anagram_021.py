#!/usr/bin/env python

import sys

def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for c in word1:
        if c in word2:
            word2 = word2.replace(c, '', 1)
    if len(word2) == 0:
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        words = line.split()
        word1 = words[0]
        word2 = words[1]
        print(anagram(word1, word2))

if __name__ == '__main__':
    main()
