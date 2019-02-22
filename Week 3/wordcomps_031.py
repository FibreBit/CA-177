#!/usr/bin/env python

import sys

def dictionary():
    words = []
    for line in sys.stdin:
        line = line.split()
        for i in line:
            words.append(i)
    return words


def most(words):
    most = 0
    for i in words:
        if i.count("e") > most:
            most = i.count("e")
    return [w for w in words if w.count("e") == most]


def comp(words):
    print("Words containing 17 letters: " + str([i for i in words if len(i) == 17]))
    print("Words containing 18+ letters: " + str([i for i in words if 17 < len(i)]))
    print("Shortest word containing all vowels: {}".format(min([i for i in words if all(c in i for c in list("aeiou"))], key=len)))
    print("Words with 4 a's: {}".format([i for i in words if i.lower().count("a") == 4]))
    print("Words with 2+ q's: {}".format([i for i in words if i.lower().count("q") > 1]))
    print("Words containing cie: {}".format([i for i in words if 'cie' in i]))
    print("Anagrams of angle: {}".format([i for i in words if all(c.lower() in i.lower() for c in list("angle")) and len(i) == 5 and i != "angle"]))
    print("Words ending in iary: {}".format(len([i for i in words if i.endswith('iary')])))
    print("Words with most e's: {}".format(most(words)))

def main():
    words = dictionary()
    comp(words)


if __name__ == '__main__':
    main()
