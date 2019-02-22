#!/usr/bin/env python

import sys

def main():
    qnou = []
    for line in sys.stdin:
        words = line.lower().strip()
        if "qu" in words:
            words = words.replace("qu", "")
        if "q" in words:
            qnou.append(line.strip())

    print("Words with q but no u:", qnou)

if __name__ == '__main__':
    main()
