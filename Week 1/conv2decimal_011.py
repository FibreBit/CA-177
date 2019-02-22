#!/usr/bin/env python

import sys

def converter(number, base):
    number = number[::-1]
    total = 0
    i = 0
    while i < len(number):
        total = total + ((base ** i) * int(number[i]))
        i += 1
    return total

def main():
    for line in sys.stdin:
        line = line.strip().split()
        number = line[0]
        base = int(line[1])
        print(converter(number, base))

if __name__ == "__main__":
    main()
