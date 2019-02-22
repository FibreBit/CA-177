#!/usr/bin/env python

import sys

filename = sys.argv[1]

def add_dic():
    d = {}
    with open(filename, 'r') as f:
        for data in f:
            data = data.split()
            d[data[0]] = data[1]
        return d

def main():
    for line in sys.stdin:
        line = line.split()
        d = add_dic()
        if line[0] in d:
            print("Name: {}".format(line[0]))
            print("Phone: {}".format(d[line[0]]))
        else:
            print("Name: {}".format(line[0]))
            print("No such contact")

if __name__ == '__main__':
    main()
