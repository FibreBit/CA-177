#!/usr/bin env python

import sys

filename = sys.argv[1]

def main():
    with open(filename, 'r') as f:
        words = f.read().strip().split()

    for line in sys.stdin:
        line = line.strip()
        for i in range(len(words)):
            if words[i] in line:
                line = line.replace(words[i], "@" * len(words[i]))
        print(line)

if __name__ == '__main__':
    main()
