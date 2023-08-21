#!/usr/bin/python3
"""Log parser"""
import sys
from typing import List


def parse_lines(lines: List[str]):
    """Parse some lines from stdin"""
    if not lines:
        return
    file_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    for log in lines:
        line = log.split(" ")
        file_size += int(line[8])
        try:
            status_code = int(line[7])
        except ValueError:
            status_code = None
        if status_code:
            status_codes_count[status_code] += 1
    print("File size: {}".format(file_size))
    for key, value in status_codes_count.items():
        if value != 0:
            print("{}: {}".format(key, value))


def extract_lines():
    """Read a given number of lines from standard input"""
    lines = []
    try:
        count = 1
        while True:
            line = sys.stdin.readline().rstrip()
            if not line.strip():
                continue
            lines.append(line)
            if count == 10:
                parse_lines(lines)
                count = 0
            count += 1
    except KeyboardInterrupt:
        parse_lines(lines)


if __name__ == "__main__":
    extract_lines()
