#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        words = line.lower().split()
        a = words[0]
        b = words[1]
        if a in b:
            print( True )
        else:
            print( False )

if __name__ == '__main__':
    main()
