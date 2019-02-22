#!/usr/bin/env python

import sys

def replace(number):
    if number % 3 == 0:
        return "X"
    else:
        return number

def prime(number):
    f = True
    a = range(2, number)
    for x in a:
        if number % x == 0:
            f = False
    if f is True:
        return number

def comps(number):
    b = []
    print("Multiples of 3: " + str([i for i in range(1, number + 1) if i % 3 == 0]))
    print("Multiples of 3 squared: " + str([i ** 2 for i in range(1, number + 1) if i % 3 == 0]))
    print("Multiples of 4 doubled: " + str([i * 2 for i in range(1, number + 1) if i % 4 == 0]))
    print("Multiples of 3 or 4: " + str([i for i in range(1, number + 1) if i % 3 == 0 or i % 4 == 0]))
    print("Multiples of 3 and 4: " + str([i for i in range(1, number + 1) if i % 3 == 0 and i % 4 == 0]))
    print("Multiples of 3 replaced: " + str([replace(i) for i in range(1, number + 1)]))
    a = [prime(i) for i in range(1, number + 1)]
    for x in a:
        if x is not None and x != 1:
            b.append(x)
    print("Primes: " + str(b))

def main():
    number = int(sys.argv[1])
    comps(number)

if __name__ == '__main__':
    main()
