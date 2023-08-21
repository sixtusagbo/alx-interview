#!/usr/bin/python3
"""Log parser"""
import sys


def parse_lines(lines):
    """Parse some lines from stdin"""
    print("Lines: ", len(lines))
    print("200")


def extract_lines():
    """Read a given number of lines from standard input"""
    lines = []
    try:
        count = 1
        while True:
            line = sys.stdin.readline().rstrip()
            lines.append(line)
            print(line, flush=True)
            if count == 10:
                parse_lines(lines)
                count = 0
            count += 1
    except KeyboardInterrupt:
        parse_lines(lines)


if __name__ == "__main__":
    extract_lines()
