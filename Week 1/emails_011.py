#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split(".")
    second = ""
    for c in line[1]:
        if c.isalpha() is True:
            second = second + c

    name = line[0].capitalize() + " " + second[:-4].capitalize()
    
    print(name)
