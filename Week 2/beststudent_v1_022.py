#!/usr/bin/env python

import sys

def main():
    filename = sys.argv[1]
    total = 0
    try:
        with open(filename, "r") as f:
            for data in f:
                data = data.split()
                if int(data[0]) > total:
                    total = int(data[0])
                    sname = " ".join((data[1:]))
        print('Best student:', sname)
        print('Best mark:', total)
    except:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()
